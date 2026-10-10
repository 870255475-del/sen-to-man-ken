# 保留SDK默认键位；不覆盖回退、读屏或选项焦点按键。
screen help():
    tag menu
    use game_menu('键位与阅读 / 慢慢看也没关系'):
        viewport:
            id 'reading_help_scroll'
            xsize 930
            ysize 530
            mousewheel True
            draggable True
            arrowkeys False
            pagekeys True
            vbox:
                spacing 14
                text '方向键移动焦点，回车确认选项；高亮的按钮就是当前焦点。' style 'tok_ui_body' size 21 color TOK_UI_INK xmaximum 874
                text '这份列表可用滚轮或 Page Up / Page Down 翻页。' style 'tok_ui_note' size 18 color TOK_UI_MUTED
                for keys,meaning in [('左键 / 回车 / 空格','继续对话；文字还在出现时，先显示整句。'),('Esc / 右键','打开菜单；在菜单里返回，确认框里取消。'),('滚轮向上 / Page Up','回退对话；不能撤销已收入收藏的阅读记录。'),('滚轮向下 / Page Down','沿回退前已经看过的内容向前。'),('按住 Ctrl / Tab','快进 / 切换快进；默认只跳过已读文字，遇到选项停下。'),('方向键 / 回车','移动按钮焦点 / 确认；列表用Page Up/Down翻页。'),('H / 鼠标中键','临时隐藏对话窗口，再按一次恢复。'),('F / F11 / Alt+回车','切换窗口与全屏。'),('F1','打开这份键位说明。'),('V / Shift+A','系统读屏 / 无障碍设置；需要系统可用的中文语音。')]:
                    frame:
                        style 'tok_ui_panel'
                        xsize 886
                        padding (18,14)
                        background SoftPanel(TOK_UI_PAPER,TOK_UI_EDGE,10)
                        hbox:
                            spacing 20
                            text keys style 'tok_ui_body' size 21 color TOK_UI_ACCENT xsize 247
                            text meaning style 'tok_ui_body' size 20 color TOK_UI_INK xmaximum 579
                text '存档可分多页保留；删除已有档位前会确认。跳过短篇和关闭CG轻动效都不影响关系。' style 'tok_ui_note' size 20 color TOK_UI_MUTED xmaximum 874
                textbutton '调整文字、音乐与画面移动' id 'help_preferences' style 'tok_ui_button' action ShowMenu('preferences') text_size 23 xsize 440 ysize 52
