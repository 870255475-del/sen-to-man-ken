# v0.9 候选：八角色后续路线设计浏览；未复制入当前 game，未 native 验证。
# 合入：route_followups.json 放 game/ 根目录，本文件放 game/。
# 现有 route_overview 入口可用 ShowMenu('route_followup', role=selected_route)。
# 只展示设计；关系按钮仅改 screen 局部变量，不开始章节、不修改关系/周目/图库。

init -2 python:
    import json as route_followup_json

    ROUTE_FOLLOWUP_DESIGNS = {}
    if renpy.loadable('story_data/route_followups.json'):
        try:
            with renpy.file('story_data/route_followups.json') as route_followup_file:
                route_followup_payload = route_followup_json.load(route_followup_file)
            if route_followup_payload.get('schema_version') == 1:
                ROUTE_FOLLOWUP_DESIGNS = {
                    route_followup_item['id']: route_followup_item
                    for route_followup_item in route_followup_payload.get('roles', [])
                }
        except (ValueError, KeyError, TypeError, AttributeError):
            ROUTE_FOLLOWUP_DESIGNS = {}

    def route_followup_design(role):
        return ROUTE_FOLLOWUP_DESIGNS.get(role)


screen route_followup_design_card(caption, body):
    frame:
        style 'tok_ui_panel'
        background SoftPanel(TOK_UI_PAPER,TOK_UI_EDGE,12)
        xsize 878
        padding (18,16)
        vbox:
            spacing 9
            text caption style 'tok_ui_heading' size 22 color TOK_UI_INK xmaximum 838 line_spacing 4 substitute False
            text body style 'tok_ui_body' size 19 color TOK_UI_INK xmaximum 838 line_spacing 5 substitute False

screen route_followup(role):
    tag menu
    default followup_relation = 'love'
    $ followup_item = route_followup_design(role)
    $ followup_title = ((followup_item['name'] + ' / 后续路线设计') if followup_item else '后续路线设计')

    use game_menu(followup_title):
        vbox:
            spacing 10
            text '设计索引／后续仍待正文与验收，已开放章以故事目录为准。三种关系均保留后续计划。' style 'tok_ui_note' size 17 color TOK_UI_MUTED xmaximum 920

            if followup_item:
                hbox:
                    spacing 10
                    for followup_key, followup_name in [('love','恋人后续'),('wait','等待后续'),('friend','友人后续')]:
                        textbutton followup_name:
                            id ('followup_relation_' + followup_key)
                            style 'tok_ui_button'
                            xsize 162
                            yminimum 44
                            padding (12,9)
                            text_size 18
                            selected followup_relation == followup_key
                            action SetScreenVariable('followup_relation',followup_key)

                viewport:
                    id 'route_followup_scroll'
                    xsize 925
                    ysize 392
                    mousewheel True
                    draggable True
                    pagekeys True
                    arrowkeys False
                    vbox:
                        xsize 884
                        spacing 14
                        text followup_item['route_title'] style 'tok_ui_heading' size 27 color TOK_UI_INK xmaximum 874 line_spacing 4 substitute False
                        use route_followup_design_card('她想过的私人日子',followup_item['private_wish'])
                        use route_followup_design_card('关系中的核心误区',followup_item['core_misconception'])

                        text '八章因果 / 设计索引，实际正文见故事目录' style 'tok_ui_heading' size 23 color TOK_UI_ACCENT xmaximum 874
                        for followup_chapter in followup_item['chapters']:
                            use route_followup_design_card('第'+str(followup_chapter['number'])+'章  '+followup_chapter['title'],followup_chapter['outline'])
                        use route_followup_design_card('道具与选择怎样延续',followup_item['continuity_rules'])

                        $ followup_ending = followup_item['endings'][followup_relation]
                        use route_followup_design_card(followup_ending['title']+'结局 / 设计',followup_ending['outline'])
                        use route_followup_design_card(followup_ending['title']+'后日谈 / 设计',followup_item['afterstory'][followup_relation])
                        if followup_relation == 'love':
                            use route_followup_design_card('自愿婚育后续 / 可不选择',followup_item['afterstory']['family_optional'])

                        use route_followup_design_card('遗憾 IF / 独立主动入口设计',followup_item['regret_if']['outline'])
                        use route_followup_design_card('坏 IF / 独立主动入口设计',followup_item['bad_if']['outline'])
                        text '拒绝恋爱、选择友人或退出，不会自动触发坏 IF。' style 'tok_ui_note' size 17 color TOK_UI_MUTED xmaximum 874
                        use route_followup_design_card('二周目额外事件 / 设计',followup_item['ng2']['outline'])
                        use route_followup_design_card('三周目额外事件 / 设计',followup_item['ng3']['outline'])

                        text '必要 CG / 计划，未生成或解锁' style 'tok_ui_heading' size 23 color TOK_UI_ACCENT xmaximum 874
                        for followup_cg in followup_item['cg_needs']:
                            use route_followup_design_card('第'+str(followup_cg['chapter_proposed'])+'章  '+followup_cg['title'],'动作 A：'+followup_cg['body_expression_variants'][0]+'\n动作 B：'+followup_cg['body_expression_variants'][1])
                        text '先写正文，再沿原句接入真实动作差分。短隐藏不抵完整路线；5–6小时仍未实测。' style 'tok_ui_note' size 17 color TOK_UI_MUTED xmaximum 874 line_spacing 5
            else:
                text '此角色的后续设计暂不可查看。请返回路线框架。' style 'tok_ui_body' size 21 color TOK_UI_INK xmaximum 880

            textbutton '返回路线框架':
                id 'route_followup_back'
                style 'tok_ui_button'
                yminimum 44
                padding (14,9)
                text_size 18
                action ShowMenu('route_overview')
