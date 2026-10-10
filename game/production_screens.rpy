default persistent.rice_cg_seen = False

screen route_overview():
    tag menu
    default selected_route = 'common'
    $ chapters = LONG_COMMON if selected_route == 'common' else ai_profile(selected_route)['chapters']
    $ quick_chapter_limit = 7 if selected_route == 'common' else 8 if selected_route in ('deepseek','gpt','grok') else OPENING_CHAPTER_LIMITS.get(selected_route, 0)
    $ route_columns_height = 530 if main_menu else 496
    use game_menu('故事目录 / 与她相处'):
        vbox:
            spacing 10
            if not main_menu:
                text '切换章节请返回标题；Esc继续当前故事。可先保存进度。' style 'tok_ui_note' size 18 color TOK_UI_MUTED xmaximum 920
            hbox:
                spacing 18
                viewport:
                    xsize 174
                    ysize route_columns_height
                    mousewheel True
                    draggable True
                    pagekeys True
                    arrowkeys False
                    vbox:
                        spacing 6
                        textbutton '共通篇' action SetScreenVariable('selected_route','common') selected selected_route == 'common' style 'tok_ui_button' xsize 166 yminimum 44 padding (12,9) text_size 19 text_xmaximum 142
                        for r in LONG_ROUTES:
                            textbutton r['name'] action SetScreenVariable('selected_route',r['id']) selected selected_route == r['id'] style 'tok_ui_button' xsize 166 yminimum 44 padding (12,9) text_size 19 text_xmaximum 142
                vbox:
                    xsize 726
                    spacing 8
                    hbox:
                        xsize 726
                        ysize 44
                        spacing 8
                        if quick_chapter_limit:
                            text '章节直达' style 'tok_ui_note' size 18 color TOK_UI_MUTED xsize 104 yalign 0.5
                            for quick_ch in chapters:
                                if 1 <= quick_ch['number'] <= quick_chapter_limit:
                                    if selected_route == 'common':
                                        $ quick_read_label = ('common_ch%02d' % quick_ch['number']) + ('' if quick_ch['number'] <= 2 else '_play')
                                    elif selected_route == 'deepseek':
                                        $ quick_read_label = 'ds_ch%02d_play' % quick_ch['number']
                                    else:
                                        $ quick_read_label = selected_route+'_ch%02d_play' % quick_ch['number']
                                    textbutton str(quick_ch['number']) id ('quick_read_'+quick_ch['id']) action Start(quick_read_label) style 'tok_ui_button' xsize 56 ysize 44 padding (8,4) text_size 20 text_xalign 0.5 text_yalign 0.5 sensitive main_menu
                        else:
                            text '正文制作中 · 暂无章节入口' style 'tok_ui_note' size 18 color TOK_UI_MUTED yalign 0.5
                    viewport:
                        id 'route_chapter_scroll'
                        arrowkeys False
                        pagekeys True
                        xsize 726
                        ysize (route_columns_height - 52)
                        mousewheel True
                        draggable True
                        vbox:
                            xsize 700
                            spacing 14
                            if selected_route == 'common':
                                text '共通篇 / 花灯亮起之前' style 'tok_ui_heading' size 28 color TOK_UI_INK xmaximum 700
                                text '七章已开放。读完共通篇后，选择想继续认识的她。' style 'tok_ui_note' size 19 xmaximum 700 color TOK_UI_MUTED
                            else:
                                $ route = ai_profile(selected_route)
                                text (route['name']+' / '+route['title']) style 'tok_ui_heading' size 28 color TOK_UI_INK xmaximum 700
                                text route['seed'] style 'tok_ui_body' size 20 color TOK_UI_INK xmaximum 700 line_spacing 4
                                text ('八章已开放 · 恋人、等待与友人三种结局' if selected_route in ('deepseek','gpt','grok','claude','kimi') else '已开放 '+str(OPENING_CHAPTER_LIMITS[selected_route])+' / 8 章 · 后续剧情及结局制作中' if selected_route in OPENING_CHAPTER_LIMITS else '角色篇制作中 · 暂无可进入的章节') style 'tok_ui_note' size 19 color TOK_UI_MUTED xmaximum 700
                                if selected_route in ROUTE_FOLLOWUP_DESIGNS:
                                    textbutton '后续路线设计 / 关系与结局' id 'route_followup_open' action ShowMenu('route_followup',role=selected_route) style 'tok_ui_button' yminimum 44 padding (16,9) text_size 20 text_xmaximum 650
                            for ch in chapters:
                                frame:
                                    style 'tok_ui_panel'
                                    background SoftPanel(TOK_UI_PAPER,TOK_UI_EDGE,12)
                                    xsize 700
                                    padding (18,16)
                                    vbox:
                                        spacing 10
                                        text ('第'+str(ch['number'])+'章  '+ch['title']) style 'tok_ui_heading' size 23 color TOK_UI_INK xmaximum 660 line_spacing 4
                                        text ch['outline'] style 'tok_ui_body' size 19 color TOK_UI_INK xmaximum 660 line_spacing 5
                                        text ('可阅读' if ch['number'] <= quick_chapter_limit else '后续制作中') id ('chapter_readability_'+ch['id']) style 'tok_ui_note' size 16 color TOK_UI_MUTED
                                        if selected_route == 'common':
                                            textbutton '从本章开始' id ('read_'+ch['id']) action Start(('common_ch%02d' % ch['number']) + ('' if ch['number'] <= 2 else '_play')) style 'tok_ui_button' yminimum 44 padding (14,9) text_size 18 sensitive main_menu
                                        elif selected_route == 'deepseek':
                                            textbutton '从本章开始' id ('read_'+ch['id']) action Start('ds_ch%02d_play' % ch['number']) style 'tok_ui_button' yminimum 44 padding (14,9) text_size 18 sensitive main_menu
                                        elif selected_route in ('gpt','grok') and ch['number'] <= 8:
                                            textbutton '从本章开始' id ('read_'+ch['id']) action Start(selected_route+'_ch%02d_play' % ch['number']) style 'tok_ui_button' yminimum 44 padding (14,9) text_size 18 sensitive main_menu
                                        elif selected_route in OPENING_CHAPTER_LIMITS and ch['number'] <= OPENING_CHAPTER_LIMITS[selected_route]:
                                            textbutton '从本章开始' id ('read_'+ch['id']) action Start(selected_route+'_ch%02d_play' % ch['number']) style 'tok_ui_button' yminimum 44 padding (14,9) text_size 18 sensitive main_menu

screen production_gallery():
    tag menu
    default selected_art = 'deepseek'
    use game_menu('原创素材 / 动作与神态'):
        hbox:
            spacing 18
            viewport:
                xsize 188
                ysize 530
                mousewheel True
                draggable True
                pagekeys True
                arrowkeys False
                vbox:
                    spacing 6
                    text '11角色 · 动作与神态' style 'tok_ui_note' size 16 color TOK_UI_MUTED xmaximum 177
                    for r in LONG_ROUTES:
                        textbutton r['name'] action SetScreenVariable('selected_art',r['id']) selected selected_art == r['id'] style 'tok_ui_button' xsize 177 yminimum 44 text_size 18 padding (10,9) text_xmaximum 157
                    textbutton 'DeepSeek / 白饭' action SetScreenVariable('selected_art','rice_pose') selected selected_art == 'rice_pose' style 'tok_ui_button' xsize 177 yminimum 44 text_size 18 padding (10,9) text_xmaximum 157
                    textbutton '偷饭CG' action SetScreenVariable('selected_art','rice_cg') selected selected_art == 'rice_cg' style 'tok_ui_button' xsize 177 yminimum 44 text_size 18 padding (10,9) text_xmaximum 157
                    for expression_id, expression_name in (('shy','害羞'),('determined','认真'),('annoyed','小恼'),('sleepy','困倦'),('happy','开怀')):
                        textbutton ('大肥鱼 / '+expression_name) action SetScreenVariable('selected_art','ds_'+expression_id) selected selected_art == 'ds_'+expression_id style 'tok_ui_button' xsize 177 yminimum 44 text_size 18 padding (10,9) text_xmaximum 157
                    for pose_id, pose_name in (('offer_rice','羞涩递饭'),('fix_lamp','认真修灯'),('shy_wave','羞涩挥手'),('summer','夏裙递点心'),('yukata','浴衣理衣带')):
                        textbutton ('大肥鱼 / '+pose_name) id ('art_ds_'+pose_id) action SetScreenVariable('selected_art','ds_'+pose_id) selected selected_art == 'ds_'+pose_id style 'tok_ui_button' xsize 177 yminimum 44 text_size 18 padding (10,9) text_xmaximum 157
                    textbutton 'MiniMax / 持机' id 'art_minimax_camera_shy' action SetScreenVariable('selected_art','minimax_camera_shy') selected selected_art == 'minimax_camera_shy' style 'tok_ui_button' xsize 177 yminimum 44 text_size 18 padding (10,9) text_xmaximum 157
            viewport:
                xsize 714
                ysize 530
                mousewheel True
                draggable True
                pagekeys True
                arrowkeys False
                vbox:
                    xsize 690
                    spacing 12
                    if selected_art == 'rice_cg':
                        text '偷吃白饭被抓包 / CG制作预览' style 'tok_ui_heading' size 25 color TOK_UI_INK xmaximum 690
                        add Transform('images/original/rice_break.png',xysize=(690,388),fit='contain')
                        text ('已在原创序章解锁' if persistent.rice_cg_seen else '在原创序章中经历此场景后解锁') style 'tok_ui_note' size 19 color TOK_UI_MUTED xmaximum 690
                    else:
                        $ display_role = 'deepseek' if (selected_art.startswith('ds_') or selected_art == 'rice_pose') else 'minimax' if selected_art == 'minimax_camera_shy' else selected_art
                        $ display_pose = selected_art[3:] if selected_art.startswith('ds_') else 'rice' if selected_art == 'rice_pose' else 'camera_shy' if selected_art == 'minimax_camera_shy' else 'neutral'
                        text (ai_profile(display_role)['name']+' / '+('动作与神态' if selected_art.startswith('ds_') else '捧饭姿态' if selected_art == 'rice_pose' else '持机害羞 / 动作与神态' if selected_art == 'minimax_camera_shy' else '基础立绘')) style 'tok_ui_heading' size 25 color TOK_UI_INK xmaximum 690
                        frame:
                            style 'tok_ui_panel'
                            background SoftPanel(TOK_UI_PAPER,TOK_UI_EDGE,12)
                            xsize 690
                            ysize 405
                            padding (5,5)
                            add Transform(sprite_file(display_role,display_pose),xysize=(680,395),fit='contain') xalign 0.5
                        text '表情配合身体动作，夏裙与浴衣各有独立姿态。旧动作继续保留。' style 'tok_ui_note' size 17 color TOK_UI_MUTED xmaximum 690 line_spacing 4
