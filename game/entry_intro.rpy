# 原生图片片头。素材、音乐复用项目文件；没有网络或视频生成调用。
# splashscreen return 后由 Ren'Py 进入 main_menu。

transform entry_intro_reveal(delay_time=0.0, reduced=False):
    alpha (1.0 if reduced else 0.0)
    yoffset (0 if reduced else 14)
    pause (0.0 if reduced else delay_time)
    ease (0.0 if reduced else 0.42) alpha 1.0 yoffset 0

transform entry_intro_night(reduced=False):
    alpha (0.0 if reduced else 1.0)
    pause (0.0 if reduced else 0.25)
    ease (0.0 if reduced else 1.35) alpha 0.0

transform entry_intro_rule(reduced=False):
    xanchor 0.5
    xzoom (1.0 if reduced else 0.02)
    alpha (1.0 if reduced else 0.0)
    pause (0.0 if reduced else 0.55)
    ease (0.0 if reduced else 0.7) xzoom 1.0 alpha 1.0

transform entry_intro_glint(delay_time=0.0, reduced=False):
    alpha (0.55 if reduced else 0.0)
    yoffset 0
    pause (0.0 if reduced else delay_time)
    ease (0.0 if reduced else 0.7) alpha 0.55
    ease (0.0 if reduced else 1.0) yoffset (0 if reduced else -9) alpha 0.2

screen entry_intro_panel(reduced=False):
    modal True
    zorder 200

    # 鼠标左键、空格/回车、ESC 都只结束片头，不打开游戏内菜单。
    key "mousedown_1" action Return("skip")
    key "K_RETURN" action Return("skip")
    key "K_KP_ENTER" action Return("skip")
    key "K_SPACE" action Return("skip")
    key "K_ESCAPE" action Return("skip")
    key "game_menu" action Return("skip")
    timer 5.2 action Return("complete")

    add "bg echo morning"
    if not reduced:
        add "bg echo" at entry_intro_night(reduced)
    add Solid("#21172876")
    add Solid("#17132690") ypos 110 ysize 440

    # 年龄提示从第一帧完整显示，不参加分字动画。
    text "R18 · 仅限18岁以上" xalign 0.5 ypos 139 size 32 color "#fff1da" font "fonts/SourceHanSansCN-Regular.otf" outlines [(2, "#392535", 0, 1)]
    text "全员成年 · 角色均为30岁" xalign 0.5 ypos 187 size 19 color "#f0dfeb" outlines [(1, "#392535", 0, 1)]

    # 四角细线先成框，再逐字落下；没有开发状态或技术提示。
    fixed:
        xpos 342
        ypos 260
        xsize 596
        ysize 166
        at entry_intro_reveal(0.3, reduced)
        for corner_x, corner_y, inward_x, inward_y in ((0, 0, 0, 0), (568, 0, 27, 0), (0, 165, 0, -27), (568, 165, 27, -27)):
            add Solid("#edc9d9ad") xpos corner_x ypos corner_y xsize 28 ysize 1
            add Solid("#edc9d9ad") xpos (corner_x + inward_x) ypos (corner_y + inward_y) xsize 1 ysize 28

    hbox:
        xalign 0.5
        ypos 286
        spacing 7
        for index, letter in enumerate(("千", "t", "o", "万", "k", "e", "n")):
            text letter:
                font "fonts/SourceHanSerifCN-SemiBold.otf"
                size 80
                color "#fff8f2"
                outlines [(2, "#5b344c", 0, 0), (1, "#271d32b0", 0, 3)]
                at entry_intro_reveal(0.65 + index * 0.12, reduced)

    add Solid("#ffd5e4bc") xpos 640 ypos 397 xsize 370 ysize 1 at entry_intro_rule(reduced)
    text "一碗白饭，和十一份心事。" xalign 0.5 ypos 449 size 24 color "#fff1e8" font "fonts/SourceHanSerifCN-SemiBold.otf" outlines [(1, "#3b2c40", 0, 1)] at entry_intro_reveal(1.65, reduced)

    # 少量原生点缀，没有额外粒子贴图；减少移动时直接显示静止图形。
    for dot_x, dot_y, delay_time in ((298, 322, 0.8), (985, 366, 1.2), (375, 488, 1.5), (913, 236, 1.0)):
        text "◇" xpos dot_x ypos dot_y size 16 color "#ffe3d4" at entry_intro_glint(delay_time, reduced)

    if renpy.loadable("images/ui/deepseek_chibi_pet.png"):
        add Transform("images/ui/deepseek_chibi_pet.png", xysize=(160, 160), fit="contain") xpos 1060 ypos 529 at entry_intro_reveal(1.8, reduced)

    text "点击 / 回车 / ESC 跳过" xalign 0.5 ypos 657 size 17 color "#eee3ec" outlines [(1, "#251b30", 0, 1)]

label splashscreen:
    window hide
    # 与主菜单共用 music 通道；退出时停止，菜单自行播放已有曲目。
    play music "audio/festival.ogg" fadein 0.5
    call screen entry_intro_panel(reduced=persistent.reduce_motion)
    stop music
    scene black
    return
