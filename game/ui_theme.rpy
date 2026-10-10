# Shared original interface palette. No assets, animation timers or network.
init -9 python:
    TOK_UI_INK = '#49384F'
    TOK_UI_MUTED = '#796977'
    TOK_UI_ACCENT = '#AF5D7D'
    TOK_UI_PAPER = '#FFF7F1'
    TOK_UI_EDGE = '#DEC2CF'
    TOK_UI_ACCENT_TEXT = '#8D4264'

init -6:
    style tok_ui_button is button:
        background SoftPanel('#FFF7F1', '#DEC2CF', 10)
        hover_background SoftPanel('#F5DDE8', '#AF5D7D', 10)
        selected_background SoftPanel('#EECFDA', '#AF5D7D', 10)
        activate_background SoftPanel('#E8BDCFFF', '#8D4264', 10)
        insensitive_background SoftPanel('#F1E9E8', '#DED3D7', 10)
        padding (16, 9)
        yminimum 44
    style tok_ui_button_text is button_text:
        font 'fonts/SourceHanSansCN-Regular.otf'
        size 21
        color TOK_UI_INK
        hover_color '#763A59'
        selected_color '#763A59'
        insensitive_color '#998B94'
        outlines []
    style tok_ui_heading is text:
        font 'fonts/SourceHanSerifCN-SemiBold.otf'
        size 29
        color TOK_UI_INK
        line_spacing 4
        outlines []
    style tok_ui_body is text:
        font 'fonts/SourceHanSansCN-Regular.otf'
        size 22
        color TOK_UI_INK
        line_spacing 5
        outlines []
    style tok_ui_note is tok_ui_body:
        size 17
        color TOK_UI_MUTED
    style tok_ui_panel is frame:
        background SoftPanel('#FFF7F1', '#DEC2CF', 12)
        padding (22, 18)

# Finite menu entrance; no repeat or scheduled displayable redraw.
transform tok_ui_enter:
    alpha (1.0 if persistent.reduce_motion else 0.0)
    yoffset (0 if persistent.reduce_motion else 6)
    ease (0.0 if persistent.reduce_motion else 0.16) alpha 1.0 yoffset 0
