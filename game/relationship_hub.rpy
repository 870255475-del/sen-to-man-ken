# 存档内的相处记录。分数不参与主线关系答复或结局判断。
default affection_points = {}
default affection_events = {}
default affection_special_seen = []
default affection_last_change = ''
default affection_special_active = False

init -2 python:
    import copy as affection_copy
    import re as affection_re

    AFFECTION_ROLES = ('deepseek','gpt','claude','grok','minimax','kimi',
        'gemini','qwen','glm','opencode','zcode')
    AFFECTION_SPECIALS = (
        dict(id='ds_stream', role='deepseek', title='水里那块石头',
            label='ds_stream_detour', chapters=2, points=20, love=False,
            cgs=('fan_deepseek_01',),
            note='浅水同行；可以牵手，也可以沿岸陪她走。'),
        dict(id='ds_outerwear', role='deepseek', title='外带又打结了',
            label='ds_optional_outerwear', chapters=7, points=70, love=False,
            cgs=('ds_outerwear_worn','ds_outerwear','ds_outerwear_turn'),
            note='完整女仆裙与外衣；帮忙解外带或让她自己整理。'),
        dict(id='ds_hug', role='deepseek', title='这一步轮到我',
            label='ds_optional_hug', chapters=8, points=80, love=True,
            cgs=('ds_hug_pov',),
            note='恋人答复后，她先询问；可以轻抱，也可以坐近说话。'),
    )
    # 恢复剧情、分数日志和呈现字段；不复原已见特殊事件、persistent 或阅读/音量偏好。
    AFFECTION_STATE_KEYS = tuple(dict.fromkeys(tuple(key for key in ENDING_STATE_KEYS
        if key not in ('affection_special_seen','affection_last_change','affection_special_active')) + (
        'main_cg','main_portrait_mode','main_current_label','main_common_cursor',
        'main_ds_cursor','side_cursor','side_route','opening_cursor','opening_role','opening_route',
        'ds_stream_detail','secret_run_key','bad_run_key','secret_exploration',
        'ending_requested','_history_list','_last_say_what','_last_say_who',
        '_last_say_kwargs','_window','_window_auto','_window_subtitle',
        '_side_image_attributes','_side_image_attributes_reset','_menu','suppress_overlay')))

    def affection_value(role):
        values = getattr(store, 'affection_points', {}) or {}
        return max(0, min(100, int(values.get(role, 0))))

    def affection_reset():
        store.affection_points = {}
        store.affection_events = {}
        store.affection_special_seen = []
        store.affection_last_change = ''
        store.affection_special_active = False

    def affection_blocked_context():
        return bool(getattr(store, 'main_menu', False)
            or getattr(store, '_in_replay', None)
            or getattr(store, 'town_preview_mode', False)
            or (getattr(store, 'town_recall', False) and str(getattr(store, 'chapter', '')).startswith('自由日'))
            or getattr(store, 'secret_run_key', '')
            or getattr(store, 'bad_run_key', '')
            or getattr(store, 'secret_exploration', False)
            or getattr(store, 'affection_special_active', False))

    def affection_record(role, key, points):
        events = dict(getattr(store, 'affection_events', {}) or {})
        event_id = role + '|' + key
        if event_id in events:
            return 0
        before = affection_value(role)
        after = min(100, before + points)
        values = dict(getattr(store, 'affection_points', {}) or {})
        values[role] = after
        events[event_id] = after - before
        store.affection_points = values
        store.affection_events = events
        if after > before:
            message = TOWN_ROLE_NAMES[role] + ' 好感度 +' + str(after-before) + '（' + str(after) + '/100）'
            store.affection_last_change = message
            renpy.notify(message)
        return after - before

    def affection_award(role, chapter_key):
        """在真实章节 return 后且 main_last_chapter 写入后调用；每章只记一次。"""
        if role not in AFFECTION_ROLES or affection_blocked_context():
            return 0
        prefix = 'ds' if role == 'deepseek' else role
        if not affection_re.fullmatch(affection_re.escape(prefix) + r'_ch0[1-8]', str(chapter_key)):
            return 0
        if (getattr(store, 'main_last_chapter', '') != chapter_key
                or not renpy.has_label(chapter_key)):
            return 0
        return affection_record(role, chapter_key, 10)

    def affection_award_town(role, flag):
        """town_mark 完成后接入；真实地图小事每个 flag 只记一次。"""
        if role not in AFFECTION_ROLES or affection_blocked_context():
            return 0
        if (getattr(store, 'town_current_role', '') != role
                or not isinstance(flag, str) or not flag
                or not (getattr(store, 'town_event_flags', {}) or {}).get(flag, False)):
            return 0
        return affection_record(role, 'town:' + flag, 2)

    def affection_completed(role, number):
        prefix = 'ds' if role == 'deepseek' else role
        events = getattr(store, 'affection_events', {}) or {}
        return role + '|' + prefix + '_ch%02d' % number in events

    def opening_relationship_answer(role):
        # Chapter7 is an explicit answer, not an eight-chapter route ending.
        if role not in ('claude','kimi'):
            return ''
        field = 'claude7_answer' if role == 'claude' else 'kimi7_response'
        answer = getattr(store, field, '')
        answered_run = getattr(store, field+'_run_id', None)
        completed_run = getattr(store, role+'7_completed_run_id', None)
        current_run = getattr(store, 'ending_route_run_id', '')
        if (answer not in ('love','wait','friend') or completed_run is None
                or getattr(store, 'ending_route_run_role', '') != role
                or answered_run != completed_run or completed_run != current_run
                or getattr(store, 'main_last_chapter', '') != role+'_ch07'):
            return ''
        if current_run and 7 not in (getattr(store, 'ending_route_run_chapters', []) or []):
            return ''
        return answer

    def affection_relationship(role):
        answer = (getattr(store, 'ds_ending', '') if role == 'deepseek'
            else getattr(store, role + '_ending', '') if role in ('gpt','grok')
            else completed_opening_relationship_answer(role) or opening_relationship_answer(role))
        return {'love':'恋人 · 已明确答复','wait':'等待 · 已明确答复',
            'friend':'友人 · 已明确答复'}.get(answer, '关系答复尚未确定')

    def affection_special_by_id(key):
        return next((item for item in AFFECTION_SPECIALS if item['id'] == key), None)

    def affection_special_ready(item):
        if not item or not renpy.has_label(item['label']):
            return False
        if any(not affection_completed(item['role'], n) for n in range(1, item['chapters']+1)):
            return False
        if affection_value(item['role']) < item['points']:
            return False
        if item['love'] and (getattr(store, 'ds_reply', '') != 'love'
                or getattr(store, 'ds_ending', '') != 'love'):
            return False
        return True

    def affection_special_hint(item):
        if not item or not renpy.has_label(item['label']):
            return '这一段尚未接入。'
        missing = [str(n) for n in range(1,item['chapters']+1)
            if not affection_completed(item['role'], n)]
        requirements = []
        if missing:
            requirements.append('本存档读完 DeepSeek 第' + '、'.join(missing) + '章')
        if affection_value(item['role']) < item['points']:
            requirements.append('好感度达到 ' + str(item['points']) + '（当前 ' + str(affection_value(item['role'])) + '）')
        if item['love'] and (getattr(store, 'ds_reply', '') != 'love'
                or getattr(store, 'ds_ending', '') != 'love'):
            requirements.append('主线当面答复成为恋人并完成第八章')
        if requirements:
            return '需要：' + '；'.join(requirements) + '。'
        if getattr(store, 'main_menu', False):
            return '已满足条件；先读取这个存档，从故事中的好感页面回看。'
        if affection_blocked_context():
            return '请先回到普通主线；地图预览、回忆与IF中不开放特殊回看。'
        return '已开放 · 回看结束返回此页，Esc继续原故事。'

    def affection_special_can_enter(item):
        return affection_special_ready(item) and not affection_blocked_context()

    def affection_special_cg_status(item):
        count = sum(1 for key in item['cgs'] if original_cg_unlocked(original_cg_by_id(key)))
        return '已见CG ' + str(count) + '/' + str(len(item['cgs'])) + ' · 只记录实际展示的版本'

    def affection_prepare_context():
        renpy.context_dynamic(*(AFFECTION_STATE_KEYS + ('affection_special_active','affection_context_item')))
        # 复制可防 ds_romance_style 原地修改连带污染父存档 dynamic 备份。
        for name in AFFECTION_STATE_KEYS:
            if hasattr(store,name):
                setattr(store,name,affection_copy.deepcopy(getattr(store,name)))
        # A story invoked from a menu inherits its Context.info flags.
        # Reset only this child, so ShowMenu opens a real nested settings menu.
        renpy.context()._menu = False
        renpy.context()._main_menu = False
        store._menu = False
        store.suppress_overlay = False
        store.affection_special_active = True
        store.quick_menu = False
        store.main_cg = None

    def affection_play_special(key):
        # Function 必须返回 None，避免关闭父菜单或把值送进当前故事的 call screen。
        item = affection_special_by_id(key)
        if not affection_special_can_enter(item):
            if item:
                renpy.notify(affection_special_hint(item))
            return
        snapshot = {name:affection_copy.deepcopy(getattr(store,name))
            for name in AFFECTION_STATE_KEYS if hasattr(store,name)}
        missing = [name for name in AFFECTION_STATE_KEYS if not hasattr(store,name)]
        music = (list(renpy.music.get_loop(channel='music') or []), renpy.music.get_pause(channel='music'))
        previous_active = store.affection_special_active
        finished = False
        try:
            finished = renpy.call_in_new_context('affection_special_context', key)
        finally:
            for name, value in snapshot.items():
                setattr(store, name, affection_copy.deepcopy(value))
            for name in missing:
                if hasattr(store,name):
                    delattr(store,name)
            store.affection_special_active = previous_active
            # get_playing can still be the outgoing track during a fade. The
            # public get_loop API preserves the parent's actual queued loop.
            tracks, paused = music
            if list(renpy.music.get_loop(channel='music') or []) != tracks or paused:
                if tracks:
                    renpy.music.play(tracks, channel='music', loop=True,
                        fadeout=0 if paused else 0.7, fadein=0 if paused else 0.7)
                else:
                    renpy.music.stop(channel='music', fadeout=0 if paused else 0.7)
            if paused:
                renpy.music.pump()
            renpy.music.set_pause(paused, channel='music')
        if finished:
            seen = list(getattr(store, 'affection_special_seen', []) or [])
            if key not in seen:
                store.affection_special_seen = seen + [key]
            renpy.save_persistent()
        return

label affection_special_context(key):
    # 独立上下文的 scene list 由引擎恢复；状态恢复在父函数 finally 完成。
    # 新上下文存读档指向父故事：冻结将会变动的字段为 context dynamic，
    # 使 Ren'Py 保存父上下文时取父值。阅读设置、persistent CG 标记不在其中。
    $ affection_prepare_context()
    $ affection_context_item = affection_special_by_id(key)
    if not affection_special_ready(affection_context_item):
        return False
    call expression affection_context_item['label']
    return True

screen relationship_hub():
    tag menu
    default selected_affection_role = 'deepseek'
    $ role_name = TOWN_ROLE_NAMES[selected_affection_role]
    $ score = affection_value(selected_affection_role)
    $ special_items = [item for item in AFFECTION_SPECIALS if item['role'] == selected_affection_role]
    use game_menu('好感度 / 与她相处'):
        hbox:
            spacing 18
            vbox:
                xsize 214
                spacing 7
                text '本存档 · 十一位角色' style 'tok_ui_note' size 18 color TOK_UI_MUTED xmaximum 214
                viewport:
                    id 'affection_role_scroll'
                    xsize 214
                    ysize 346
                    mousewheel True
                    draggable True
                    pagekeys False
                    arrowkeys False
                    vbox:
                        spacing 6
                        for role in AFFECTION_ROLES:
                            textbutton (TOWN_ROLE_NAMES[role]+'  '+str(affection_value(role))+'/100'):
                                id ('affection_role_'+role)
                                action SetScreenVariable('selected_affection_role',role)
                                selected selected_affection_role == role
                                style 'tok_ui_button'
                                xsize 214
                                yminimum 44
                                padding (10,9)
                                text_size 18
                                text_xmaximum 194
                hbox:
                    spacing 8
                    textbutton '上翻' id 'affection_roles_previous' style 'tok_ui_button' action Scroll('affection_role_scroll','vertical decrease','page',delay=(0 if persistent.reduce_motion else 0.12)) xsize 103 ysize 44 padding (10,8) text_size 17
                    textbutton '下翻' id 'affection_roles_next' style 'tok_ui_button' action Scroll('affection_role_scroll','vertical increase','page',delay=(0 if persistent.reduce_motion else 0.12)) xsize 103 ysize 44 padding (10,8) text_size 17
                text '读完章节 +10\n地图小事 +2\n同一件事只记一次' style 'tok_ui_note' size 16 color TOK_UI_MUTED xmaximum 214
            viewport:
                id 'affection_special_scroll'
                xsize 696
                ysize 530
                mousewheel True
                draggable True
                pagekeys True
                arrowkeys False
                vbox:
                    xsize 680
                    spacing 12
                    text (role_name+' · 好感度 '+str(score)+'/100') id 'affection_score' style 'tok_ui_heading' size 27 color TOK_UI_INK xmaximum 680
                    bar value StaticValue(score,100) id 'affection_bar' xsize 680 ysize 18 left_bar Solid(TOK_UI_ACCENT) right_bar Solid('#EFDFE7') thumb None
                    text affection_relationship(selected_affection_role) id 'affection_relationship' style 'tok_ui_body' size 20 color TOK_UI_INK xmaximum 680
                    text '好感度记录相处熟悉；恋人、等待或友人的答复始终优先。拒绝恋爱不会扣分。' style 'tok_ui_note' size 18 color TOK_UI_MUTED xmaximum 680 line_spacing 4
                    if affection_last_change:
                        text affection_last_change style 'tok_ui_note' size 17 color TOK_UI_ACCENT_TEXT xmaximum 680
                    text '特殊CG事件 / 自愿互动' style 'tok_ui_heading' size 22 color TOK_UI_INK xmaximum 680
                    if not special_items:
                        text '这位角色的特殊事件还在制作。已接入的章节仍会记录本存档好感度。' style 'tok_ui_note' size 19 color TOK_UI_MUTED xmaximum 670
                    for item in special_items:
                        frame:
                            style 'tok_ui_panel'
                            xsize 680
                            padding (14,14)
                            background SoftPanel(TOK_UI_PAPER,TOK_UI_EDGE,12)
                            vbox:
                                spacing 9
                                text item['title'] style 'tok_ui_heading' size 23 color TOK_UI_INK xmaximum 650 line_spacing 4
                                text item['note'] style 'tok_ui_body' size 17 color TOK_UI_INK xmaximum 650 line_spacing 4
                                text affection_special_hint(item) id ('affection_hint_'+item['id']) style 'tok_ui_note' size 17 color TOK_UI_MUTED xmaximum 650
                                text affection_special_cg_status(item) style 'tok_ui_note' size 16 color TOK_UI_MUTED xmaximum 650
                                textbutton ('再次回看' if item['id'] in affection_special_seen else '进入这一段'):
                                    id ('affection_special_'+item['id'])
                                    action Function(affection_play_special,item['id'])
                                    sensitive affection_special_can_enter(item)
                                    style 'tok_ui_button'
                                    text_size 18
                                    yminimum 44
                                    padding (14,9)
                    textbutton '查看已见CG与动作差分' id 'affection_gallery' action ShowMenu('original_cg_gallery') style 'tok_ui_button' text_size 19 yminimum 44 padding (14,9) text_xmaximum 650
