default gpt_ending = ''
default grok_ending = ''
default persistent.main_gpt_love = False
default persistent.main_gpt_wait = False
default persistent.main_gpt_friend = False
default persistent.main_grok_love = False
default persistent.main_grok_wait = False
default persistent.main_grok_friend = False

init -5 python:
    SIDE_ROLE_NAMES={'gpt':'GPT','grok':'Grok'}
    SIDE_ENDINGS={
        'gpt':{'love':('两个人，半张新纸','恋人'),
            'wait':('下周休息日，先问你','等待'),
            'friend':('各自的画，常来的茶','友人')},
        'grok':{'love':('散场以后，我来见你','恋人'),
            'wait':('下午见，这次不交答案','等待'),
            'friend':('白天坐坐，各有去处','友人')}}

screen side_ending_card(role,key):
    modal True
    add Solid('#201a30e8')
    frame:
        align (0.5,0.5)
        xsize 790
        padding (42,36)
        background SoftPanel('#fcf2ee','#ba7597',15)
        vbox:
            spacing 20
            text (SIDE_ROLE_NAMES[role]+'篇 · '+SIDE_ENDINGS[role][key][1]+'结局') size 24 color '#a55983'
            text SIDE_ENDINGS[role][key][0] size 35 color '#512d53' xmaximum 700
            text ('纸和茶各有位置，下一次来坐坐。' if role=='gpt' else '摊子收好，各自的明天也安排好了。') size 23 color '#75536e' xmaximum 700
            text '已收入主线结局收藏。回看结尾不会自动增加周目。' size 18 color '#927889' xmaximum 700
            textbutton '查看结局收藏' id 'side_ending_collection' style 'navigation_button' action ShowMenu('endings') text_color '#653657' text_size 22
            textbutton '回到标题' id 'side_ending_return' style 'navigation_button' action Return() xsize 300 text_color '#653657' background SoftPanel('#f0d7e3','#b57d98',10)
