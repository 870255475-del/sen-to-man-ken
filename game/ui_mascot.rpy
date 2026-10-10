# 界面宠物只做本地演出，不调用AI或写入账号信息。
default ui_pet_treat = False

init -6 python:
    import math
    def whale_pet_idle_update(trans, st, at):
        trans.yoffset = 0 if persistent.reduce_motion else -3.0 * math.sin(st * math.pi / 2.2)
        return None if persistent.reduce_motion else 0.04

transform whale_pet_idle:
    function whale_pet_idle_update

screen ui_whale_pet(pet_x, pet_y, pet_size):
    if renpy.loadable('images/ui/deepseek_chibi_pet.png'):
        button:
            id 'whale_ui_pet'
            xpos pet_x
            ypos pet_y
            xsize pet_size
            ysize pet_size
            background None
            hover_background None
            padding (0,0)
            action ToggleVariable('ui_pet_treat')
            if persistent.reduce_motion:
                add Transform('images/ui/deepseek_chibi_pet.png',xysize=(pet_size,pet_size),fit='contain')
            else:
                add Transform('images/ui/deepseek_chibi_pet.png',xysize=(pet_size,pet_size),fit='contain') at whale_pet_idle
        if ui_pet_treat and pet_size > 100:
            frame:
                xpos (pet_x-198)
                ypos (pet_y+31)
                xsize 188
                background SoftPanel('#fff6faee','#c886ab',10)
                padding (12,10)
                text '给你留饭了。\n……不许数我碗里！' size 18 color '#6a365a' line_spacing 4
