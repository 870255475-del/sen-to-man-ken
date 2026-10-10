# Chapter-bound AI dialogue; only explicit player continuation returns to authored runner.
init -1 python:
    import mainline_agent as mla
    import mainline_agent_runtime as mlrt
    import json as mla_json
    import re as mla_re
    with renpy.file('story_data/mainline_agent_personas.json') as mla_file:
        MAINLINE_AGENT_PERSONAS = mla_json.load(mla_file)['personas']

    MAINLINE_AGENT_AUTHORED_LIMITS = {'deepseek':8,'gpt':8,'grok':8,'claude':8,'kimi':8}
    MLA_ACTION_TEXT = {'share_thought':'我想说说刚才的想法。','plan_next':'一起商量下一步。'}
    MLA_PLAN_NEXT_SENTENCE = mla_re.compile(r'(?:一起商量下一步|我想商量下一步|我来商量下一步|我想继续下一章|我愿意继续下一章|我同意继续下一章)[。！!]?')

    def mla_ui_eligible(state,text,action=None):
        eligible=mla.candidates(state,text,action)
        if eligible==['plan_next'] and (not isinstance(text,str) or MLA_PLAN_NEXT_SENTENCE.fullmatch(text.strip()) is None):
            return []
        return eligible

    def mla_scroll_bottom(adjustment):
        adjustment.change(adjustment.range)

    def mla_message_name(index,name):
        return '你' if mlrt.session.messages[index]['role']=='user' else name

    def mla_message_text(index):
        return safe_ai_text(mlrt.session.messages[index]['content'])

    def mla_context_summary(title,choices):
        lines=['章题：'+title]
        lines.extend(key+' = '+mla_json.dumps(value,ensure_ascii=False) for key,value in sorted(choices.items()))
        summary='\n'.join(lines)
        while True:
            cleaned=mla.clean_text(summary)
            if cleaned==summary:
                return summary
            summary=cleaned

    def mla_context(role, number):
        prefix='ds' if role=='deepseek' else role
        label=prefix+'_ch%02d'%number
        next_label=prefix+'_ch%02d'%(number+1)
        route=next((r for r in LONG_ROUTES if r['id']==role),None)
        title=route['chapters'][number-1]['title'] if route and 1<=number<=8 else ''
        choices={}
        for key,value in vars(store).items():
            if key.startswith(prefix+str(number)+'_') and not key.endswith(('_run_id','_complete','_seen')) and type(value) in (str,int,bool):
                choices[key]=value[:100] if isinstance(value,str) else value
        relation='unknown'
        if number>=7 and 7 in ending_route_run_chapters:
            if role=='deepseek': relation=ds_reply
            elif role=='gpt': relation=gpt7_reply
            elif role=='grok': relation=grok7_answer
            elif role in ('claude','kimi'): relation=opening_relationship_answer(role) or 'unknown'
        blocked=bool(secret_run_key or bad_run_key or secret_exploration or affection_special_active or ds_tipsy_active or getattr(store,'character_event_active',False) or getattr(store,'town_preview_mode',False))
        return dict(role=role,run_id=ending_route_run_id,chapter=number,
            current_label=main_last_chapter,visited=list(ending_route_run_chapters),
            next_label=next_label,next_label_exists=bool(number+1<=MAINLINE_AGENT_AUTHORED_LIMITS.get(role,0) and renpy.has_label(next_label)),
            main_menu=bool(main_menu or getattr(renpy.context(),'_main_menu',False)),replay=bool(getattr(store,'_in_replay',False)),
            blocked=blocked or ending_route_run_role!=role or main_last_chapter!=label,
            relationship=relation,relationship_source=ending_route_run_id if relation!='unknown' else '',
            summary=mla_context_summary(title,choices))

    def mla_ready(role, number):
        return type(number) is int and role in MAINLINE_AGENT_PERSONAS and mla.validate_context(mla_context(role,number))

    def mla_bind(role,number):
        renpy.hide_screen('notify')
        mlrt.invalidate()
        s=mlrt.session
        s.context=mla_context(role,number)
        s.state=mla.new_state(s.context)
        s.messages=[]
        s.busy=False
        s.active=True
        s.status='已绑定当前章节。开场不发请求；也可以返回原章间菜单。'

    def mla_current():
        s=mlrt.session
        return mla_context(s.context['role'],s.context['chapter']) if s.context else {}

    def mla_submit(text,action=None):
        s=mlrt.session
        if not s.active or s.busy:
            return
        context=mla_current()
        if not mla.validate_context(context) or context!=s.context:
            mlrt.invalidate()
            renpy.restart_interaction()
            return
        try:
            eligible=mla_ui_eligible(s.state,text,action)
            prompt=mla.system_prompt(MAINLINE_AGENT_PERSONAS[context['role']],context,s.state,eligible)
            ai_bridge.make_payload(ai_bridge.session.model,prompt,s.messages,text,ai_bridge.session.max_tokens)
            token=mla.make_token(context,s.state,s.generation)
            bridge_generation=ai_bridge.claim_request()
        except (ai_bridge.BridgeError,ValueError,TypeError) as exc:
            s.status=str(exc)
            renpy.restart_interaction()
            return
        s.busy=True
        s.status='她正在回答……'
        snapshot=(ai_bridge.session.base_url,ai_bridge.session.model,ai_bridge.session.api_key,prompt,list(s.messages),text,ai_bridge.session.max_tokens)
        def worker():
            try:
                answer=ai_bridge.send_chat(*snapshot);problem=None
            except ai_bridge.BridgeError as exc:
                answer=None;problem=str(exc)
            except Exception:
                answer=None;problem='请求未完成；没有自动重试。'
            renpy.invoke_in_main_thread(mla_finish,token,bridge_generation,text,eligible,answer,problem)
        renpy.invoke_in_thread(worker)
        renpy.restart_interaction()

    def mla_finish(token,bridge_generation,text,eligible,answer,problem):
        ai_bridge.release_request()
        s=mlrt.session
        s.busy=False
        if not s.active or bridge_generation!=ai_bridge.session.generation or not mla.response_is_current(token,mla_current(),s.state,s.generation):
            s.status='存档、场景或联机状态已变化；旧回答没有写回。'
        elif problem:
            s.status=problem
        else:
            try:
                answer=mla.normalize_response(answer)
            except (ValueError,TypeError):
                s.status='回答格式不符合角色对白要求；主线没有推进。'
                renpy.restart_interaction()
                return
            s.messages.extend([dict(role='user',content=text),dict(role='assistant',content=answer['reply'])])
            s.messages=s.messages[-24:]
            s.state,fact=mla.apply_proposal(s.state,answer.get('event'),eligible)
            s.status='你可以确认继续下一章。' if mla.can_return_next(mla_current(),s.state) else '这一句已收到。' if not fact else '这一件小事记下了。'
        renpy.restart_interaction()

    def mla_request_next():
        s=mlrt.session
        return bool(s.active and not s.busy and mla.can_return_next(mla_current(),s.state))

label mainline_agent_after_chapter(role, number):
    if not mla_ready(role,number):
        return 'back'
    $ mla_bind(role,number)
    call screen mainline_agent_chat
    $ mla_result = 'next' if _return == 'next' and mla_request_next() else 'back'
    $ mlrt.invalidate()
    return mla_result

label mainline_finish_with_agent(role, arc, number, title, next_title):
    while True:
        call screen main_chapter_finish(arc,number,title,next_title,agent_role=role)
        if _return == 'agent':
            call mainline_agent_after_chapter(role,number)
            if _return == 'next':
                return 'next'
        else:
            return _return

label after_load:
    $ mlrt.invalidate()
    return

screen mainline_agent_chat():
    modal True
    $ s=mlrt.session
    if not s.active or not s.context or not s.state:
        timer 0.01 action Return('back')
    else:
        $ name=MAINLINE_AGENT_PERSONAS[s.context['role']]['display_name']
        default chat_input=FieldInputValue(mlrt.session,'draft',default=False)
        default scroll_adjustment=ui.adjustment()
        default scroll_seen_count=-1
        if scroll_seen_count != len(s.messages):
            timer 0.01 action [SetScreenVariable('scroll_seen_count',len(s.messages)),Function(mla_scroll_bottom,scroll_adjustment)]
        add Solid('#241c32b8')
        frame:
            align (0.5,0.5)
            xsize 1030
            ysize 625
            background SoftPanel(TOK_UI_PAPER+'f5',TOK_UI_EDGE,16)
            padding (30,22)
            vbox:
                spacing 12
                text (name+' · 主线章间对话') style 'tok_ui_heading' size 28
                text '当前章后的小事会随对话推进；下一章由你确认继续。' style 'tok_ui_note' size 18
                hbox:
                    spacing 18
                    add Transform(sprite_file(s.context['role'],'neutral'),xysize=(188,295),fit='contain')
                    viewport:
                        id 'mla_messages'
                        ysize 295
                        xsize 756
                        yadjustment scroll_adjustment
                        mousewheel True
                        draggable True
                        pagekeys True
                        yinitial 1.0
                        vbox:
                            spacing 12
                            if not s.messages:
                                text '想跟她说什么？从刚刚发生的事聊起吧。' size 21 color TOK_UI_INK
                            for message_index in range(len(mlrt.session.messages)):
                                text mla_message_name(message_index,name) size 17 color TOK_UI_ACCENT_TEXT
                                text mla_message_text(message_index) substitute False size 23 color TOK_UI_INK xmaximum 728
                hbox:
                    spacing 12
                    for node in mla.available(s.state):
                        textbutton node['label'] id ('mla_action_'+node['event']) action Function(mla_submit,MLA_ACTION_TEXT[node['event']],node['event']) sensitive s.active and ai_bridge.session.enabled and not s.busy xsize 460 ysize 44 text_size 20
                button:
                    id 'mla_input_field'
                    action chat_input.Toggle()
                    xsize 960
                    ysize 48
                    padding (14,8)
                    input id 'mla_input' value chat_input length 800 pixel_width 928 copypaste True size 22
                hbox:
                    spacing 12
                    textbutton '发送' id 'mla_send' action [Function(mla_submit,s.draft),SetField(mlrt.session,'draft','')] sensitive s.active and ai_bridge.session.enabled and not s.busy xsize 110 text_size 21
                    textbutton '接口设置' id 'mla_settings' action ShowMenu('ai_settings') xsize 145 text_size 21
                    textbutton '继续下一章' id 'mla_next' action Return('next') sensitive mla_request_next() xsize 195 text_size 21
                    textbutton '返回章间菜单' id 'mla_back' action Return('back') xsize 195 text_size 21
                text safe_ai_text(s.status) substitute False style 'tok_ui_note' size 17 xmaximum 952

