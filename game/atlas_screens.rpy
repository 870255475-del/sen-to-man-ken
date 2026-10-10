screen world_tree(initial_selected="root"):
    tag menu
    default selected = initial_selected
    default world_filter = "all"
    $ nodes = WORLD_NODES if world_filter == "all" else [n for n in WORLD_NODES if n['group'] == world_filter]
    $ item = next(n for n in WORLD_NODES if n['id'] == selected)
    use game_menu("世界树"):
        vbox:
            spacing 14
            hbox:
                spacing 7
                for name, group in [("全部", "all"), ("概览", "overview"), ("法则", "rules"), ("地点", "places"), ("人物", "characters"), ("主题", "conflict")]:
                    textbutton name style 'tok_ui_button' text_size 20 xsize 98 yminimum 44 padding (12,9) selected world_filter == group action [SetScreenVariable("world_filter", group), SetScreenVariable("selected", next(n['id'] for n in WORLD_NODES if group == 'all' or n['group'] == group))]
            hbox:
                spacing 20
                viewport:
                    id "world_list"
                    xsize 285
                    ysize 454
                    mousewheel True
                    draggable True
                    pagekeys True
                    arrowkeys False
                    vbox:
                        spacing 7
                        for n in nodes:
                            textbutton n['title']:
                                style 'tok_ui_button'
                                xsize 267
                                yminimum 44
                                text_size 19
                                text_xmaximum 243
                                padding (12,10)
                                selected selected == n['id']
                                action SetScreenVariable("selected", n['id'])
                frame:
                    style 'tok_ui_panel'
                    xsize 598
                    ysize 454
                    background SoftPanel(TOK_UI_PAPER,TOK_UI_EDGE,13)
                    padding (26,22)
                    viewport:
                        xsize 526
                        ysize 410
                        mousewheel True
                        draggable True
                        pagekeys True
                        arrowkeys False
                        vbox:
                            xsize 526
                            spacing 16
                            text item['title'] id 'world_detail_title' style 'tok_ui_heading' size 29 color TOK_UI_INK xmaximum 526 line_spacing 4
                            text item['status'] style 'tok_ui_note' size 17 color TOK_UI_ACCENT_TEXT xmaximum 526
                            text item['summary'] style 'tok_ui_body' size 22 color TOK_UI_INK line_spacing 6 xmaximum 526
                            add Solid(TOK_UI_EDGE) ysize 1 xsize 515
                            text item['detail'] style 'tok_ui_body' size 20 color TOK_UI_INK line_spacing 7 xmaximum 526

screen story_tree():
    tag menu
    default selected = "demo"
    default tree_mode = "demo"
    $ nodes = [n for n in PLOT_NODES if n['mode'] == tree_mode]
    $ item = next(n for n in PLOT_NODES if n['id'] == selected)
    $ next_nodes = [n for n in PLOT_NODES if any(e['from'] == selected and e['to'] == n['id'] for e in PLOT_EDGES)]
    use game_menu("剧情树"):
        vbox:
            spacing 12
            hbox:
                spacing 12
                textbutton "试玩篇 / 已可阅读" style 'tok_ui_button' text_size 20 yminimum 44 padding (16,9) selected tree_mode == "demo" action [SetScreenVariable("tree_mode", "demo"), SetScreenVariable("selected", "demo")]
                textbutton "长篇结构 / 原始规划" style 'tok_ui_button' text_size 20 yminimum 44 padding (16,9) selected tree_mode == "planned" action [SetScreenVariable("tree_mode", "planned"), SetScreenVariable("selected", "long")]
            text '本页为原始结构索引；实际开放章节请查看故事目录。' style 'tok_ui_note' size 16 color TOK_UI_MUTED xmaximum 920
            hbox:
                spacing 20
                viewport:
                    id "plot_list"
                    xsize 305
                    ysize 434
                    mousewheel True
                    draggable True
                    pagekeys True
                    arrowkeys False
                    vbox:
                        spacing 7
                        for n in nodes:
                            textbutton n['title']:
                                style 'tok_ui_button'
                                xsize 287
                                yminimum 44
                                text_size 19
                                text_xmaximum 263
                                selected selected == n['id']
                                padding (12,10)
                                action SetScreenVariable("selected", n['id'])
                frame:
                    style 'tok_ui_panel'
                    xsize 578
                    ysize 434
                    background SoftPanel(TOK_UI_PAPER,TOK_UI_EDGE,13)
                    padding (24,20)
                    viewport:
                        xsize 514
                        ysize 394
                        mousewheel True
                        draggable True
                        pagekeys True
                        arrowkeys False
                        vbox:
                            xsize 514
                            spacing 14
                            text item['title'] style 'tok_ui_heading' size 26 color TOK_UI_INK xmaximum 514 line_spacing 4
                            text item['status'] style 'tok_ui_note' size 17 color TOK_UI_ACCENT_TEXT xmaximum 514
                            text item['summary'] style 'tok_ui_body' size 21 color TOK_UI_INK xmaximum 514 line_spacing 6
                            text item['detail'] style 'tok_ui_body' size 20 color TOK_UI_INK xmaximum 514 line_spacing 6
                            if next_nodes:
                                text "后续节点" style 'tok_ui_note' size 17 color TOK_UI_MUTED
                                for n in next_nodes:
                                    textbutton n['title'] action SetScreenVariable("selected", n['id']) style 'tok_ui_button' text_size 18 xsize 508 yminimum 44 padding (14,9) text_xmaximum 480
                            if item['mode'] == 'demo':
                                textbutton "从试玩篇开头阅读" action Start() style 'tok_ui_button' text_size 20 xsize 508 yminimum 44 padding (14,9) sensitive main_menu
                            else:
                                text "结构节点不等于可阅读正文；开放章节以故事目录为准。" style 'tok_ui_note' size 17 color TOK_UI_MUTED xmaximum 514

screen character_book():
    tag menu
    default selected = "deepseek"
    $ character = next(c for c in CHARACTER_BOOK if c['id'] == selected)
    use game_menu("角色图鉴"):
        hbox:
            spacing 17
            viewport:
                id "character_list"
                xsize 159
                ysize 509
                mousewheel True
                draggable True
                pagekeys True
                arrowkeys False
                vbox:
                    spacing 6
                    for c in CHARACTER_BOOK:
                        textbutton c['name'] style 'tok_ui_button' text_size 19 xsize 143 yminimum 44 text_xmaximum 123 padding (10,10) selected selected == c['id'] action SetScreenVariable("selected", c['id'])
            frame:
                style 'tok_ui_panel'
                xsize 270
                ysize 508
                background SoftPanel(TOK_UI_PAPER,TOK_UI_EDGE,12)
                padding (10,10)
                add Transform(character['image'],xysize=(250,480),fit="contain") xalign 0.5 yalign 0.5
            vbox:
                spacing 10
                viewport:
                    xsize 446
                    ysize 425
                    mousewheel True
                    draggable True
                    pagekeys True
                    arrowkeys False
                    vbox:
                        xsize 425
                        spacing 10
                        text character['name'] id 'character_detail_name' style 'tok_ui_heading' size 36 color TOK_UI_INK xmaximum 425
                        text character['role'] id 'character_detail_role' style 'tok_ui_body' size 21 color TOK_UI_INK xmaximum 425 line_spacing 4
                        text "成年AI娘 / 30岁 / " + character['place'] style 'tok_ui_note' size 16 color TOK_UI_MUTED xmaximum 425
                        text character['tag'] style 'tok_ui_heading' size 22 color TOK_UI_ACCENT xmaximum 425
                        for label, key in [("她想要","desire"),("她担心","fear"),("相处的线索","bond")]:
                            vbox:
                                spacing 5
                                text label style 'tok_ui_note' size 17 color TOK_UI_ACCENT_TEXT
                                text character[key] style 'tok_ui_body' size 20 color TOK_UI_INK xmaximum 425 line_spacing 5
                        text character['status'] style 'tok_ui_note' size 17 color TOK_UI_MUTED xmaximum 425
                textbutton "在世界树中查看" action ShowMenu("world_tree",initial_selected="c_"+character['id']) style 'tok_ui_button' text_size 19 yminimum 44 padding (14,9)
                text "滚动查看完整资料" style 'tok_ui_note' size 14 color TOK_UI_MUTED

screen op_player():
    tag menu
    modal True
    on "show" action Function(renpy.music.set_pause,True,channel="music")
    on "hide" action Function(renpy.music.set_pause,False,channel="music")
    on "replace" action Function(renpy.music.set_pause,True,channel="music")
    on "replaced" action Function(renpy.music.set_pause,False,channel="music")
    add Solid("#000000")
    add Movie(play="video/opening.webm",size=(1280,720),loop=False)
    textbutton "跳过片头" action Return() style 'tok_ui_button' xpos 1100 ypos 26 xsize 150 yminimum 44 text_size 21 padding (12,9)
    timer 59.1 action Return()
    key "game_menu" action Return()

screen gallery(initial_category="story"):
    tag menu
    default category = initial_category
    default page = 0
    $ group = 'cg' if category in ['story','cg'] else category
    $ pool = group_assets(group)
    $ max_page = max(0,(len(pool)-1)//6)
    $ shown = pool[page*6:page*6+6]
    use game_menu("素材画廊"):
        vbox:
            spacing 10
            hbox:
                spacing 10
                for name, value in [("剧情回忆","story"),("现有CG","cg"),("OP静图","op"),("角色参考","portrait")]:
                    textbutton name style 'tok_ui_button' text_size 19 yminimum 44 padding (16,9) selected category == value action [SetScreenVariable("category",value),SetScreenVariable("page",0)]
            if category == "story":
                text "剧情回忆按阅读记录锁定；“现有CG”浏览本页登记素材。" style 'tok_ui_note' size 17 color TOK_UI_MUTED xmaximum 920
            else:
                text "本页显示已登记素材；点击缩略图查看大图。原有素材保留。" style 'tok_ui_note' size 17 color TOK_UI_MUTED xmaximum 920
            viewport:
                xsize 925
                ysize 390
                mousewheel True
                draggable True
                pagekeys True
                arrowkeys False
                grid 3 2:
                    spacing 13
                    for index in range(6):
                        if index < len(shown):
                            $ asset = shown[index]
                            $ opened = category != "story" or getattr(persistent,"cg_"+asset['unlock'])
                            button:
                                style 'tok_ui_button'
                                xsize 291
                                yminimum 196
                                padding (12,10)
                                sensitive opened
                                action (Show("cg_view",path=asset['image'],title=asset['title']) if opened else NullAction())
                                vbox:
                                    spacing 8
                                    fixed:
                                        xsize 266
                                        ysize 145
                                        if opened:
                                            if group == "portrait":
                                                add Solid(TOK_UI_PAPER)
                                                add Transform(asset['image'],xysize=(266,145),fit="contain") xalign 0.5 yalign 0.5
                                            else:
                                                add Solid(TOK_UI_PAPER)
                                                add Transform(asset['image'],xysize=(266,145),fit="contain") xalign 0.5 yalign 0.5
                                        else:
                                            add Solid("#EFE3E8")
                                            text "尚未解锁" style 'tok_ui_note' xalign 0.5 yalign 0.5 size 21 color TOK_UI_MUTED
                                    text (asset['title'] if opened else "未发现的回忆") style 'tok_ui_body' size 18 color TOK_UI_INK xmaximum 266 line_spacing 3
                        else:
                            null width 291 height 196
            hbox:
                spacing 16
                textbutton "上一页" action SetScreenVariable("page",page-1) sensitive page > 0 style 'tok_ui_button' text_size 19 yminimum 44 padding (16,9)
                text "第 {} / {} 页  /  共 {} 张".format(page+1,max_page+1,len(pool)) style 'tok_ui_note' size 18 yalign 0.5 color TOK_UI_MUTED
                textbutton "下一页" action SetScreenVariable("page",page+1) sensitive page < max_page style 'tok_ui_button' text_size 19 yminimum 44 padding (16,9)
