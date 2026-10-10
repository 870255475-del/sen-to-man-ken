default player_name = '用户'

init python:
    def normalized_player_name(value):
        value = renpy.filter_text_tags(str(value), allow=[])
        value = ''.join(c for c in value if ord(c) >= 32 and c not in '[]{}')
        return value.strip()[:16] or '用户'

screen player_name_entry():
    modal True
    default draft = player_name
    add 'bg echo morning'
    add Solid('#49384f8f')
    frame:
        style 'tok_ui_panel'
        align (0.5,0.5)
        xsize 710
        padding (40,34)
        background SoftPanel(TOK_UI_PAPER,TOK_UI_EDGE,15)
        vbox:
            spacing 20
            text '这次，她该怎么叫你？' style 'tok_ui_heading' size 33 color TOK_UI_INK
            text '默认名字是「用户」。也可以写下你自己的名字。' style 'tok_ui_body' size 21 color TOK_UI_INK xmaximum 625
            frame:
                style 'tok_ui_panel'
                xsize 620
                padding (18,14)
                background SoftPanel('#F4E6EC',TOK_UI_EDGE,9)
                input id 'player_name_input' value ScreenVariableInputValue('draft') length 16 exclude '[]{}\r\n\t' size 28 color TOK_UI_INK pixel_width 584
            text '回车确认当前名字；Esc 使用默认名字。' style 'tok_ui_note' size 18 color TOK_UI_MUTED xmaximum 625
            hbox:
                spacing 16
                textbutton '就叫用户' id 'name_default' style 'tok_ui_button' action Return('用户') xsize 270 ysize 52 text_size 22
                textbutton '用这个名字开始' id 'name_confirm' style 'tok_ui_button' action Return(normalized_player_name(draft)) xsize 325 ysize 52 text_size 22
    key 'K_RETURN' action Return(normalized_player_name(draft))
    key 'K_ESCAPE' action Return('用户')
