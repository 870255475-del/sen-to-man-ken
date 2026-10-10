# v0.15 core UI candidate. Story actions, IDs and choice measurement stay intact.
init -5:
    style default:
        font "fonts/SourceHanSansCN-Regular.otf"
        size 25
        color TOK_UI_INK
        language "unicode"
    style button:
        background SoftPanel(TOK_UI_PAPER, TOK_UI_EDGE, 10)
        hover_background SoftPanel('#F8E3ED', TOK_UI_ACCENT, 10)
        selected_background SoftPanel('#EFD5E1', TOK_UI_ACCENT, 10)
        activate_background SoftPanel('#E8C4D5', '#854360', 10)
        insensitive_background SoftPanel('#F1EBED', '#DDD1D7', 10)
        padding (18, 6)
    style button_text:
        color TOK_UI_INK
        hover_color '#73334F'
        selected_color '#73334F'
        activate_color '#602640'
        insensitive_color '#93848E'
        size 24
    style title_menu_button is button:
        yminimum 42
        padding (14, 6)
    style title_menu_button_text is button_text:
        size 21
    style navigation_button is button:
        yminimum 40
    style navigation_button_text is button_text:
        font 'fonts/SourceHanSansCN-Regular.otf'
        size 18
    style navigation_vbar is vbar:
        top_bar Solid('#F0E2E8')
        bottom_bar Solid('#F0E2E8')
        thumb Solid(TOK_UI_ACCENT)
    style bar:
        ysize 24
        left_bar Solid(TOK_UI_ACCENT)
        right_bar Solid('#E7D7DF')
        thumb Solid('#7D435F')
        thumb_offset 5
        thumb_shadow None
    style vbar:
        xsize 7
        ysize None
        top_bar Solid('#F0E2E8')
        bottom_bar Solid('#F0E2E8')
        thumb Solid(TOK_UI_ACCENT)
        thumb_shadow None
    style core_quick_button is button:
        background None
        hover_background SoftPanel('#F4DCE7', TOK_UI_ACCENT, 7)
        selected_background SoftPanel('#EFD1E0', TOK_UI_ACCENT, 7)
        padding (13, 8)
        yminimum 38
    style core_quick_button_text is button_text:
        size 17
    style core_page_button is button:
        xminimum 44
        yminimum 40
        padding (12, 7)
    style core_page_button_text is button_text:
        size 18

screen say(who, what):
    $ speaking_role = speech_role(who)
    $ portrait_visible = bool(speaking_role) and not hide_speaker_portrait
    $ compact_cg_dialogue = bool(hide_speaker_portrait and main_cg and "\n" not in what and ((main_cg.get("id") in ("kimi_private_map", "kimi_private_map_offer") and len(what) <= 32) or ((main_cg.get("id") in ("ds_tipsy_wait", "ds_tipsy_pounce", "claude_river_confess", "claude_river_relax", "kimi_moon_offer", "kimi_moon_lean") or main_cg.get("compact_dialogue", False) or main_cg.get("id", "").startswith("opening_") or (main_cg.get("id", "").startswith("fan_") and main_cg.get("id", "").endswith(("_swim", "_mishap", "_kiss")))) and len(what) <= 36)))
    window:
        id "window"
        background SoftPanel(TOK_UI_PAPER+'df', TOK_UI_PAPER+'df', 16)
        xpos 0
        ypos (590 if compact_cg_dialogue else 514)
        xsize 1280
        ysize (130 if compact_cg_dialogue else 206)
        padding (290 if portrait_visible else 74, 12 if compact_cg_dialogue else 18, 44, 35 if compact_cg_dialogue else 41)
        fixed:
            if who:
                text who id "who" ypos 0 size 26 font "fonts/SourceHanSerifCN-SemiBold.otf" color TOK_UI_ACCENT outlines [(1, TOK_UI_INK, 0, 0)]
            text what id "what" ypos ((34 if who else 15) if compact_cg_dialogue else (43 if who else 21)) size 28 color TOK_UI_INK line_spacing 5 xmaximum (938 if portrait_visible else 1162)
    if portrait_visible:
        # 肖像位于背景带之上；不遮正文，也不显示男主立绘。
        add speaker_portrait(speaking_role) xpos 16 ypos 496
    $ chapter_ribbon_width = max(425, min(1216, 64 + len(chapter) * 18))
    frame:
        id "chapter_ribbon"
        xpos 0
        ypos 22
        xsize chapter_ribbon_width
        ysize 43
        background SoftPanel(TOK_UI_PAPER+'ed', TOK_UI_EDGE, 8)
        padding (24, 6, 30, 6)
        text chapter id "chapter_title" size 18 color TOK_UI_INK xmaximum (chapter_ribbon_width - 54) layout "nobreak"

# Choice-only states: focus and held press redraw only on input changes.
style choice_card is button:
    xsize 866
    yminimum 72
    padding (24, 15)
    background SoftPanel(TOK_UI_PAPER, TOK_UI_EDGE, 11)
    hover_background SoftPanel('#F8E0ED', TOK_UI_ACCENT, 11)
    activate_background SoftPanel('#EABBD3', '#6E3056', 11)
    insensitive_background SoftPanel('#F1EBED', '#D6C6D0', 11)
style choice_card_text is button_text:
    font 'fonts/SourceHanSansCN-Regular.otf'
    size 24
    color TOK_UI_INK
    hover_color '#76254F'
    activate_color '#4F1D3E'
    insensitive_color '#817380'
    xalign 0.5
    text_align 0.5
    xmaximum 818
    line_spacing 5
    layout 'greedy'
style choice_scrollbar is vbar:
    xsize 6
    top_bar Solid('#EFDEE6')
    bottom_bar Solid('#EFDEE6')
    thumb Solid(TOK_UI_ACCENT)
    thumb_shadow None

screen choice(items):
    modal True
    default choice_scroll_adjustment = ui.adjustment()
    default choice_particles = ChoiceSparkles(14)
    $ choice_view_height = choice_viewport_height(items)
    add Solid('#49384F70')
    if renpy.showing('bg shrine'):
        add Solid(TOK_UI_PAPER) ysize 85
    add Solid(TOK_UI_PAPER) ypos 650 ysize 70
    frame:
        xalign 0.5
        yalign 0.39
        xsize 940
        padding (24,22)
        background SoftPanel(TOK_UI_PAPER+'f5', TOK_UI_EDGE, 14)
        fixed:
            xsize 892
            ysize (choice_view_height+94)
            if not persistent.reduce_motion:
                add choice_particles id 'choice_particles' xsize 892 ysize (choice_view_height+94)
            vbox:
                xsize 892
                spacing 10
                text '你想如何回应？' font 'fonts/SourceHanSerifCN-SemiBold.otf' size 30 color TOK_UI_INK xalign 0.5
                text '↑↓ 选择 · Enter 确认 · 长选项可滚动' size 18 color TOK_UI_MUTED xalign 0.5
                hbox:
                    spacing 10
                    viewport:
                        id 'choice_scroll'
                        xsize 876
                        ysize choice_view_height
                        yadjustment choice_scroll_adjustment
                        mousewheel True
                        draggable True
                        arrowkeys False
                        pagekeys True
                        vbox:
                            spacing 10
                            for choice_index, item in enumerate(items):
                                add ChoiceOptionButton(item.caption, item.action) id ('choice_item_'+str(choice_index))
                    if len(items) > 2 or choice_scroll_adjustment.range > 0:
                        vbar style 'choice_scrollbar' adjustment choice_scroll_adjustment ysize choice_view_height

screen quick_menu():
    zorder 100
    if quick_menu and not main_menu and (renpy.get_screen("say") or renpy.get_screen("choice")):
        frame:
            xalign 0.97
            yalign 0.987
            background SoftPanel(TOK_UI_PAPER+'f5', TOK_UI_EDGE, 10)
            padding (6, 3)
            hbox:
                spacing 2
                for title, action in [("回退", Rollback()), ("回看", ShowMenu("history")), ("快进", Skip()), ("自动", StoryAutoToggle()), ("存档", ShowMenu("save")), ("读档", ShowMenu("load")), ("好感", ShowMenu("relationship_hub")), ("设置", ShowMenu("preferences"))]:
                    textbutton title style 'core_quick_button' id ('quick_auto' if title == '自动' else 'quick_' + title) action action

screen main_menu():
    tag menu
    add "bg moon"
    add SoftPanel(TOK_UI_PAPER+'ee', TOK_UI_EDGE, 0) xsize 446
    add Solid(TOK_UI_EDGE) xpos 446 xsize 2
    add Solid(TOK_UI_ACCENT) xpos 48 ypos 28 xsize 45 ysize 2
    text "令樱镇 / 回声祭" xpos 48 ypos 38 size 17 color TOK_UI_MUTED
    text "千{size=42}{color=#7B4D95}to{/color}{/size}万{size=42}{color=#A23D6C}ken{/color}{/size}" xpos 44 ypos 62 size 60 color TOK_UI_INK font "fonts/SourceHanSerifCN-SemiBold.otf"
    text "蓝色大肥鱼的恋爱请求" xpos 48 ypos 148 size 21 color TOK_UI_MUTED
    vbox:
        style_prefix 'title_menu'
        xpos 48
        ypos 187
        spacing 6
        textbutton "开始故事" id "start_button" action Start() xsize 348 ysize 60 text_size 28 background SoftPanel(TOK_UI_ACCENT, '#CD8EA9', 12) hover_background SoftPanel('#954664', '#F0BACF', 12) text_color '#FFF8FB' text_hover_color '#FFFFFF' activate_background SoftPanel('#854360', TOK_UI_EDGE, 12) text_activate_color '#FFFFFF'
        hbox:
            spacing 12
            textbutton "继续阅读" action Continue() xsize 168 ysize 42 text_size 21
            textbutton "读取存档" action ShowMenu("load") xsize 168 ysize 42 text_size 21
        text "今晚，先借一碗饭。" font "fonts/SourceHanSerifCN-SemiBold.otf" size 23 color TOK_UI_ACCENT
        textbutton "DeepSeek前日谈" id "prequel_button" action Start("deepseek_prequel") xsize 348 ysize 42 padding (14, 7) text_size 21
        hbox:
            spacing 12
            textbutton "故事目录" action ShowMenu("route_overview") xsize 168 ysize 42 text_size 20
            textbutton "自由对话" action ShowMenu("ai_chat") xsize 168 ysize 42 text_size 20
        hbox:
            spacing 12
            textbutton "原创素材" action ShowMenu("production_gallery") xsize 168 ysize 42 padding (14, 7) text_size 20
            textbutton "配乐鉴赏" id "nav_music_room" action ShowMenu("music_room") xsize 168 ysize 42 padding (14, 7) text_size 20
        hbox:
            spacing 12
            textbutton "后日谈与IF" id "nav_afterstories" action ShowMenu("afterstories") xsize 168 ysize 42 padding (14, 7) text_size 20
            textbutton "CG鉴赏" action ShowMenu("original_cg_gallery") xsize 168 ysize 42 padding (14, 7) text_size 20
        hbox:
            spacing 12
            textbutton "逛逛令樱镇" id "town_preview" action Start('open_town_preview') xsize 168 ysize 42 padding (10, 7) text_size 20
            textbutton "泳装·乌龙·轻吻" id "title_character_events" action ShowMenu('character_event_archive') xsize 168 ysize 42 padding (10, 7) text_size 17
        text (config.version + " · 原创故事制作中") size 15 color TOK_UI_MUTED
    frame:
        id 'r18_marker'
        xpos 977
        ypos 82
        xsize 261
        background SoftPanel(TOK_UI_PAPER+'ed', TOK_UI_EDGE, 10)
        padding (17, 10)
        vbox:
            spacing 2
            text 'R18 · 成人限定' size 25 color '#98315F' font 'fonts/SourceHanSerifCN-SemiBold.otf'
            text '仅限18岁以上' size 17 color TOK_UI_MUTED
    use ui_whale_pet(1107,422,134)
    textbutton "退出游戏" action Quit(confirm=True) xpos 1100 ypos 16 xsize 142 ysize 42 text_size 18
    frame:
        yalign 1.0
        xfill True
        ysize 111
        background SoftPanel(TOK_UI_PAPER+'f5', TOK_UI_EDGE, 0)
        padding (52, 12)
        vbox:
            spacing 10
            text "探索令樱镇 / 花灯下的故事与回忆" size 16 color TOK_UI_MUTED
            hbox:
                spacing 10
                for title, target in [("世界树", "world_tree"), ("剧情树", "story_tree"), ("好感与邀约", "relationship_hub"), ("素材画廊", "gallery"), ("片头 OP", "op_player"), ("结局收藏", "endings"), ("阅读设置", "preferences")]:
                    textbutton title style 'title_menu_button' action ShowMenu(target) xsize 156 ysize 50 text_size 21 padding (12, 10)

screen navigation():
    default nav_scroll = ui.adjustment()
    viewport:
        xpos 28
        ypos 139
        xsize 219
        ysize 484
        yadjustment nav_scroll
        mousewheel True
        draggable True
        arrowkeys False
        pagekeys True
        vbox:
            style_prefix 'navigation'
            spacing 5
            text "故事与阅读" size 15 color TOK_UI_MUTED
            if not main_menu:
                textbutton "回到故事" action Return() xsize 203 ysize 40 text_size 18 padding (13, 6)
                textbutton "保存进度" action ShowMenu("save") xsize 203 ysize 40 text_size 18 padding (13, 6)
            textbutton "读取存档" action ShowMenu("load") xsize 203 ysize 40 text_size 18 padding (13, 6)
            textbutton "阅读设置" action ShowMenu("preferences") xsize 203 ysize 40 text_size 18 padding (13, 6)
            textbutton "好感与特殊CG" id "nav_relationship" action ShowMenu("relationship_hub") xsize 203 ysize 40 text_size 18 padding (13, 6)
            textbutton "故事目录" action ShowMenu("route_overview") xsize 203 ysize 40 text_size 18 padding (13, 6)
            textbutton "原创素材" action ShowMenu("production_gallery") xsize 203 ysize 40 text_size 18 padding (13, 6)
            textbutton "配乐鉴赏" id "nav_music_room" action ShowMenu("music_room") xsize 203 ysize 40 text_size 18 padding (13, 6)
            textbutton "后日谈与IF" id "nav_afterstories" action ShowMenu("afterstories") xsize 203 ysize 40 text_size 18 padding (13, 6)
            textbutton "CG鉴赏" action ShowMenu("original_cg_gallery") xsize 203 ysize 40 text_size 18 padding (13, 6)
            textbutton "自由对话" action ShowMenu("ai_chat") xsize 203 ysize 40 text_size 18 padding (13, 6)
            textbutton "联机设置" action ShowMenu("ai_settings") xsize 203 ysize 40 text_size 18 padding (13, 6)
            null height 8
            text "令樱镇资料" size 15 color TOK_UI_MUTED
            for title, target in [("世界树", "world_tree"), ("剧情树", "story_tree"), ("角色图鉴", "character_book"), ("素材画廊", "gallery"), ("结局收藏", "endings")]:
                textbutton title action ShowMenu(target) xsize 203 ysize 40 text_size 18 padding (13, 6)
            if not main_menu:
                textbutton "对话回看" action ShowMenu("history") xsize 203 ysize 40 text_size 18 padding (13, 6)
            textbutton "游戏说明" action ShowMenu("about") xsize 203 ysize 40 text_size 18 padding (13, 6)
    vbar style 'navigation_vbar' adjustment nav_scroll xpos 241 ypos 139 xsize 5 ysize 484
    text '滚动查看全部菜单' xpos 36 ypos 626 size 12 color TOK_UI_MUTED
    if main_menu:
        textbutton "返回标题" style 'navigation_button' action Return() xpos 28 ypos 645 xsize 207 ysize 43 text_size 21
    else:
        textbutton "返回标题" style 'navigation_button' action MainMenu() xpos 28 ypos 645 xsize 207 ysize 43 text_size 21

screen game_menu(title):
    add "bg moon"
    add Solid(TOK_UI_PAPER+'e4')
    add SoftPanel('#FFFBF8ee', TOK_UI_EDGE+'b0', 12) xsize 257
    add Solid(TOK_UI_EDGE) xpos 257 xsize 1
    text "千to万ken" xpos 35 ypos 40 size 28 font "fonts/SourceHanSerifCN-SemiBold.otf" color TOK_UI_INK
    text 'R18 · 仅限18岁以上' id 'menu_r18_marker' xpos 35 ypos 87 size 15 color '#98315F'
    use ui_whale_pet(183,71,64)
    text title at tok_ui_enter xpos 286 ypos 48 size 33 font "fonts/SourceHanSerifCN-SemiBold.otf" color TOK_UI_INK xmaximum 925
    add Solid(TOK_UI_EDGE) xpos 284 ypos 111 xsize 925 ysize 2
    use navigation
    frame:
        background None
        xpos 280
        ypos 136
        at tok_ui_enter
        xsize 940
        ysize 540
        padding (0, 0)
        transclude
    if main_menu:
        key "game_menu" action Return()
    else:
        key "game_menu" action Return()

screen save():
    tag menu
    use file_slots("保存进度")

screen load():
    tag menu
    use file_slots("读取存档")

screen file_slots(title):
    default file_scroll_adjustment = ui.adjustment()
    use game_menu(title):
        vbox:
            spacing 8
            text ('选择空位保存；选择已有档位会覆盖，并先确认。' if title == '保存进度' else '选择已有档位读取；空档位不可读取。') size 17 color TOK_UI_MUTED
            hbox:
                spacing 12
                viewport:
                    xsize 900
                    ysize 458
                    yadjustment file_scroll_adjustment
                    mousewheel True
                    draggable True
                    arrowkeys False
                    pagekeys True
                    grid 3 2:
                        spacing 10
                        for slot in range(1, 7):
                            button:
                                id ('file_slot_'+str(slot))
                                xsize 285
                                ysize 224
                                padding (12, 10)
                                action FileAction(slot)
                                vbox:
                                    spacing 3
                                    fixed:
                                        xsize 260
                                        ysize 128
                                        add Solid('#E9DFE4') xysize (260, 128)
                                        add Transform(FileScreenshot(slot), xysize=(260, 128), fit='contain') xalign 0.5 yalign 0.5
                                    text FileTime(slot, format="%Y-%m-%d %H:%M", empty="空存档位") size 16 color TOK_UI_INK
                                    text FileSaveName(slot) size 14 color TOK_UI_MUTED xmaximum 260
                                key "save_delete" action FileDelete(slot)
                vbar adjustment file_scroll_adjustment ysize 458
            hbox:
                spacing 6
                textbutton "自动" style 'core_page_button' action FilePage("auto")
                textbutton "快存" style 'core_page_button' action FilePage("quick")
                for page in range(1, 6):
                    textbutton str(page) style 'core_page_button' action FilePage(page)

screen preferences():
    tag menu
    use game_menu("阅读设置"):
        vbox:
            spacing 12
            text "显示方式" font 'fonts/SourceHanSerifCN-SemiBold.otf' size 24 color TOK_UI_INK
            hbox:
                spacing 12
                textbutton "窗口" action Preference("display", "window") text_size 22 ysize 44 padding (16, 5)
                textbutton "全屏" action Preference("display", "fullscreen") text_size 22 ysize 44 padding (16, 5)
                textbutton "减少画面移动" action ToggleField(persistent,"reduce_motion") selected persistent.reduce_motion text_size 20 ysize 44
                textbutton "CG轻动效" id 'preferences_cg_motion' action ToggleField(persistent,'cg_motion_enabled') selected persistent.cg_motion_enabled text_size 20 ysize 44
            hbox:
                spacing 25
                frame:
                    background SoftPanel('#FFFCFA', TOK_UI_EDGE, 13)
                    xsize 440
                    ysize 220
                    padding (25, 18)
                    vbox:
                        spacing 10
                        text "文字速度" font "fonts/SourceHanSerifCN-SemiBold.otf" size 26 color TOK_UI_INK
                        bar style "bar" value Preference("text speed") xsize 390 ysize 28
                        text "自动阅读间隔" size 22 color TOK_UI_INK
                        bar style "bar" value Preference("auto-forward time") xsize 390 ysize 28
                frame:
                    background SoftPanel('#FFFCFA', TOK_UI_EDGE, 13)
                    xsize 440
                    ysize 220
                    padding (25, 18)
                    vbox:
                        spacing 10
                        text "音乐音量" font "fonts/SourceHanSerifCN-SemiBold.otf" size 26 color TOK_UI_INK
                        bar style "bar" value Preference("music volume") xsize 390 ysize 28
                        textbutton "静音 / 恢复音乐" id "preferences_music_mute" action Preference("music mute", "toggle") text_size 21 ysize 42 padding (16, 5)
            textbutton "打开配乐鉴赏 / 查看署名" id "preferences_music_room" action ShowMenu("music_room") text_size 21 ysize 42 padding (16, 5)
            textbutton '键位与阅读帮助 / F1' id 'preferences_help' action ShowMenu('help') text_size 21 ysize 42 padding (16, 5)
            text "快进默认仅跳过读过的文字；遇到选项时会停下。" size 19 color TOK_UI_MUTED xmaximum 905

screen history():
    tag menu
    default history_scroll_adjustment = ui.adjustment()
    use game_menu("对话回看"):
        hbox:
            spacing 12
            viewport:
                id 'history_scroll'
                xsize 912
                ysize 530
                yadjustment history_scroll_adjustment
                arrowkeys False
                pagekeys True
                mousewheel True
                draggable True
                yinitial 1.0
                vbox:
                    spacing 14
                    if not _history_list:
                        text "还没有读过的对话。" color TOK_UI_MUTED
                    for h in _history_list:
                        frame:
                            background SoftPanel('#FFFCFA', TOK_UI_EDGE, 10)
                            xsize 900
                            padding (18, 14)
                            vbox:
                                spacing 7
                                if h.who:
                                    text h.who size 21 color TOK_UI_ACCENT
                                text h.what size 24 color TOK_UI_INK line_spacing 5 xmaximum 864 substitute False
            vbar adjustment history_scroll_adjustment ysize 530

screen cg_view(path, title):
    modal True
    zorder 200
    add Solid("#000000")
    add Transform(path, xysize=(1280, 720), fit="contain") xalign 0.5 yalign 0.5
    frame:
        background SoftPanel(TOK_UI_PAPER+'f5', TOK_UI_EDGE, 0)
        yalign 1.0
        xfill True
        padding (25, 12)
        hbox:
            spacing 24
            text title yalign 0.5 size 24 color TOK_UI_INK xmaximum 970
            textbutton "返回鉴赏" action Hide("cg_view") text_size 21 ysize 44 padding (16, 6)
    key "game_menu" action Hide("cg_view")

screen endings():
    tag menu
    default endings_scroll_adjustment = ui.adjustment()
    use game_menu("结局收藏"):
        hbox:
            spacing 12
            viewport:
                id 'endings_scroll'
                xsize 912
                ysize 530
                yadjustment endings_scroll_adjustment
                arrowkeys False
                pagekeys True
                mousewheel True
                draggable True
                vbox:
                    spacing 15
                    text 'DeepSeek主线 · 八章之后' size 27 color TOK_UI_ACCENT
                    for key in ('love','wait','friend'):
                        $ opened = bool(getattr(persistent, 'main_ds_'+key, False))
                        frame:
                            background SoftPanel('#FFFCFA', TOK_UI_EDGE, 10)
                            xsize 890
                            padding (22,16)
                            vbox:
                                spacing 7
                                text (DS_ENDINGS[key][0] if opened else '尚未发现的主线结局') size 26 color TOK_UI_INK
                                text (DS_ENDINGS[key][1]+' · 已收藏' if opened else '在第七章认真回答她，再一起走完第八章。') size 19 color TOK_UI_MUTED xmaximum 846
                    textbutton '婚礼、家庭与独立IF' id 'endings_afterstories' action ShowMenu('afterstories') text_size 22 ysize 44 padding (16, 5)
                    for role in ('gpt','grok','claude','kimi'):
                        text (SIDE_ROLE_NAMES[role]+'主线 · 八章之后') size 27 color TOK_UI_ACCENT
                        for key in ('love','wait','friend'):
                            $ opened=bool(getattr(persistent,'main_'+role+'_'+key,False))
                            frame:
                                background SoftPanel('#FFFCFA', TOK_UI_EDGE, 10)
                                xsize 890
                                padding (22,16)
                                vbox:
                                    spacing 7
                                    text (SIDE_ENDINGS[role][key][0] if opened else '尚未发现的主线结局') size 26 color TOK_UI_INK
                                    text (SIDE_ENDINGS[role][key][1]+' · 已收藏' if opened else '亲自回答她，再一起读完第八章。') size 19 color TOK_UI_MUTED xmaximum 846
                    if not main_menu:
                        text '独立IF从标题进入；Esc返回当前对白，存档页可保存进度。' size 18 color TOK_UI_MUTED xmaximum 890
                    text '前日谈 · 旧三结局' size 25 color TOK_UI_ACCENT
                    for key, title in [('love','花灯有回音'),('wait','答案还在路上'),('friend','鲸鱼的好朋友')]:
                        $ opened = getattr(persistent, 'end_'+key)
                        text (title if opened else '尚未发现的前日谈结局') size 21 color TOK_UI_INK
                    text '主线与前日谈分别收藏。可以在重要选择前存档，回来读另一种回应。' size 18 color TOK_UI_MUTED xmaximum 890
                    text '独立IF · 没有等到的那碗饭' size 25 color TOK_UI_ACCENT
                    text '暴雨中的另一种走向，包含人物死亡与血迹。与主线三种结局分开。' size 18 color TOK_UI_MUTED xmaximum 890
                    hbox:
                        spacing 14
                        textbutton '阅读独立IF' id 'tragedy_read' action Start('optional_tragedy') text_size 21 sensitive main_menu ysize 44 padding (16, 6)
                        textbutton '查看IF画面' id 'tragedy_cg_open' action Show('optional_tragedy_cg_view') sensitive persistent.cg_ds_tragedy text_size 21 ysize 44 padding (16, 6)
            vbar adjustment endings_scroll_adjustment ysize 530

screen ending_card():
    modal True
    add Solid('#49384FAF')
    frame:
        xalign 0.5
        yalign 0.5
        xsize 960
        background SoftPanel(TOK_UI_PAPER, TOK_UI_EDGE, 16)
        padding (44, 34)
        vbox:
            xsize 872
            spacing 20
            text "DeepSeek 线  /  结局" size 23 color TOK_UI_MUTED xalign 0.5
            text ending_name size 48 color TOK_UI_INK xalign 0.5 text_align 0.5 xmaximum 872
            text ending_note size 25 color TOK_UI_MUTED xalign 0.5 text_align 0.5 xmaximum 872
            null height 8
            textbutton "回到标题" action Return() xalign 0.5 xsize 220 ysize 48

screen about():
    tag menu
    use game_menu("游戏说明"):
        viewport:
            mousewheel True
            draggable True
            arrowkeys False
            pagekeys True
            xsize 920
            ysize 530
            vbox:
                xsize 900
                spacing 22
                text 'R18 · 仅限18岁以上 / 全员成年' size 23 color '#98315F'
                text "千to万ken  /  蓝色大肥鱼的恋爱请求" size 28 color TOK_UI_ACCENT
                text "原创AI娘恋爱喜剧制作版，共通七章与DeepSeek八章已接入。\nGPT、Grok各八章和独立三结局可读；其余个人篇制作中。\n主线三种结局、小镇地图、旧前日谈、CG与OP均可回看。" size 24 color TOK_UI_INK xmaximum 900
                text "其余八条个人线已有后续设计，正文仍在制作。首次通关5–6小时是目标，尚未完成玩家计时。\n角色均为成年人，没有男主立绘。" size 22 color TOK_UI_MUTED xmaximum 900
                text "左键、回车或空格继续对话。滚轮向上回退。\nEsc打开菜单；F切换全屏。点击下方按钮可回看、存档或自动阅读。" size 22 color TOK_UI_INK xmaximum 900
                text "版本 [config.version]" size 20 color TOK_UI_MUTED

screen confirm(message, yes_action, no_action):
    modal True
    zorder 300
    $ confirm_message_height = min(300, max(54, int(Text(message, font='fonts/SourceHanSansCN-Regular.otf', size=26, line_spacing=6).size(652,720,0,0)[1])+4))
    add Solid('#49384FAF')
    frame:
        xalign 0.5
        yalign 0.5
        xsize 740
        background SoftPanel(TOK_UI_PAPER, TOK_UI_EDGE, 14)
        padding (44, 32)
        vbox:
            spacing 24
            viewport:
                xsize 652
                ysize confirm_message_height
                mousewheel True
                pagekeys True
                arrowkeys False
                text message size 26 color TOK_UI_INK line_spacing 6 xmaximum 652 text_align 0.5 xalign 0.5
            hbox:
                xalign 0.5
                spacing 22
                textbutton "确定" id "confirm_yes" action yes_action xsize 180 ysize 48
                textbutton "取消" id "confirm_no" action no_action xsize 180 ysize 48
    key "game_menu" action no_action

screen notify(message):
    zorder 400
    frame:
        xpos 30
        ypos 75
        xmaximum 900
        background SoftPanel(TOK_UI_PAPER+'f5', TOK_UI_EDGE, 10)
        padding (20, 12)
        text message size 21 color TOK_UI_INK xmaximum 860
    timer 3.0 action Hide("notify")

screen skip_indicator():
    zorder 150
    frame:
        xpos 1090
        ypos 24
        xsize 158
        background SoftPanel(TOK_UI_PAPER+'ed', TOK_UI_EDGE, 10)
        padding (14, 9)
        text "快进中" size 20 color TOK_UI_ACCENT_TEXT

translate None strings:
    old "Are you sure you want to quit?"
    new "确定退出游戏吗？"
    old "Are you sure you want to return to the main menu?\nThis will lose unsaved progress."
    new "确定返回标题吗？未保存的进度会丢失。"
    old "Are you sure you want to overwrite your save?"
    new "确定覆盖这个存档吗？"
    old "Are you sure you want to load this save?\nUnsaved progress will be lost."
    new "确定读取这个存档吗？当前未保存的进度会丢失。"
    old "Are you sure you want to delete this save?"
    new "确定删除这个存档吗？"
