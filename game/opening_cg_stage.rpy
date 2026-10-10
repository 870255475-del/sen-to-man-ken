# v17 opening display hooks; all old prose/menu stays in its parent label.
default persistent.cg_opening_ds_first_bowl = False
default persistent.cg_opening_ds_rice_offer = False

init -5 python:
    OPENING_CGS = [
        dict(id='opening_ds_first_bowl', title='宵夜要趁早', file='images/original/cg_opening_ds_first_bowl.png', flag='cg_opening_ds_first_bowl'),
        dict(id='opening_ds_rice_offer', title='这一碗先给你', file='images/original/cg_opening_ds_rice_offer.png', flag='cg_opening_ds_rice_offer'),
    ]
    ORIGINAL_CGS.extend(OPENING_CGS)

image sprite deepseek caught_turn = deepseek_body('caught_turn')
image sprite deepseek rice_proud = deepseek_body('rice_proud')

label opening_ds_first_bowl_begin:
    hide deepseek
    $ hide_speaker_portrait = True
    call show_main_cg('opening_ds_first_bowl')
    return

label opening_ds_first_bowl_clear:
    $ main_cg = None
    call v20_restore_background
    $ hide_speaker_portrait = False
    $ deepseek_expression = 'rice'
    show sprite deepseek rice as deepseek at sprite_breathe(0.72) with dissolve
    return

label opening_ds_caught_pose:
    $ deepseek_expression = 'caught_turn'
    show sprite deepseek caught_turn as deepseek at sprite_breathe(0.72) with dissolve
    return

label opening_ds_caught_pose_clear:
    $ deepseek_expression = 'rice'
    show sprite deepseek rice as deepseek at sprite_breathe(0.72) with dissolve
    return

label opening_ds_proud_pose:
    $ deepseek_expression = 'rice_proud'
    show sprite deepseek rice_proud as deepseek at sprite_breathe(0.72) with dissolve
    return

label opening_ds_rice_offer_begin:
    hide deepseek
    hide qwen
    $ hide_speaker_portrait = True
    call show_main_cg('opening_ds_rice_offer')
    return

label opening_ds_rice_offer_clear:
    $ main_cg = None
    call v20_restore_background
    $ hide_speaker_portrait = False
    $ deepseek_expression = 'rice_proud'
    show sprite deepseek rice_proud as deepseek at sprite_breathe(0.72) with dissolve
    show sprite qwen as qwen at sprite_breathe(0.28) with dissolve
    return
