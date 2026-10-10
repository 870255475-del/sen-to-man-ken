# 共通七章 -> 独立路线。正文在各章文件，状态只存本地作者剧情。
default main_cg = None
default main_bonds = {}
default main_last_chapter = ""
default story_invite = "deepseek"
default ds_trust = 0
default ds_rest = 0
default ds_reply = "wait"
default ds_ending = ""
default persistent.main_common_ch03_seen = False
default persistent.main_common_ch04_seen = False
default persistent.main_common_ch05_seen = False
default persistent.main_common_ch06_seen = False
default persistent.main_common_ch07_seen = False
default persistent.main_ds_ch01_seen = False
default persistent.main_ds_ch02_seen = False
default persistent.main_ds_ch03_seen = False
default persistent.main_ds_ch04_seen = False
default persistent.main_ds_ch05_seen = False
default persistent.main_ds_ch06_seen = False
default persistent.main_ds_ch07_seen = False
default persistent.main_ds_ch08_seen = False
default persistent.main_ds_love = False
default persistent.main_ds_wait = False
default persistent.main_ds_friend = False
default persistent.cg_ds_rest = False
default persistent.cg_ds_rain = False
default persistent.cg_ds_confession = False
default persistent.cg_ds_tragedy = False
default persistent.tragedy_cg_seen = []
default hide_speaker_portrait = False
default persistent.cg_ds_cooldown = False
default persistent.cg_ds_yukata = False
default persistent.cg_ds_pool = False
default persistent.cg_ds_close = False
default persistent.cg_ds_outerwear_worn = False
default persistent.cg_ds_outerwear = False
default persistent.cg_ds_outerwear_turn = False
default persistent.cg_ds_hug_pov = False
default persistent.cg_ds_evening_tea = False

init -5 python:
    COMMON_TITLES = ["碗里还有一口饭", "十一位，不是十一种答案", "半枚Token的账", "没有亮起的第十二盏灯", "雨的预告，晴的愿望", "想留下来的理由", "把名字写在灯上"]
    DS_TITLES = ["给大肥鱼加一碗", "摸鱼许可证", "半枚Token的债", "剩饭不能点灯", "今天不响应", "先吃饭，再可靠", "想分给你的明天", "下班也在一起"]
    DS_ENDINGS = {'love': ('下班以后，一起回家', '恋人'), 'wait': ('把明天留一格', '等待'), 'friend': ('饭桌上的老位置', '友人')}
    TRAGEDY_CGS = [('final', '雨没有停', 'cg_ds_tragedy.png'), ('hand', '差一点碰到', 'cg_ds_tragedy_hand.png'), ('meal', '饭已经凉了', 'cg_ds_tragedy_meal.png'), ('seat', '来年的空位', 'cg_ds_tragedy_seat.png')]

    def tragedy_cg_path(key):
        return 'images/original/' + next(item[2] for item in TRAGEDY_CGS if item[0] == key)

    def main_bond(role):
        if role not in SPRITE_ROLES:
            raise ValueError('Unknown story role')
        main_bonds[role] = min(9, main_bonds.get(role, 0) + 1)

    def main_reset():
        store.main_scene_bg_key = 'legacy_echo'
        store.main_cg = None
        store.main_bonds = {}
        store.main_last_chapter = ''
        store.story_invite = 'deepseek'
        store.ds_trust = 0
        store.ds_rest = 0
        store.ds_reply = 'wait'
        store.ds_ending = ''
        store.gpt_ending = ''
        store.grok_ending = ''
        store.gpt7_reply = ''
        store.grok7_answer = ''
        store.hide_speaker_portrait = False
        store.ds_romance_style = {}
        town_reset()
        affection_reset()

label main_common_from(number=3):
    $ main_common_cursor = number
    while main_common_cursor <= 7:
        $ main_current_label = 'common_ch%02d' % main_common_cursor
        call expression main_current_label
        $ main_last_chapter = main_current_label
        $ renpy.save_persistent()
        if main_common_cursor < 7:
            call screen main_chapter_finish('共通篇', main_common_cursor, COMMON_TITLES[main_common_cursor - 1], COMMON_TITLES[main_common_cursor])
            if _return != 'next':
                return
        $ main_common_cursor += 1
    call open_town_day(recall=True)
    call screen main_invitation
    if _return == 'deepseek':
        $ story_invite = 'deepseek'
        call main_deepseek_start
    elif _return in ('gpt','grok'):
        $ story_invite = _return
        call main_side_from(story_invite)
    elif _return in OPENING_CHAPTER_LIMITS:
        $ story_invite = _return
        call main_opening_from(story_invite)
    return

label main_deepseek_start:
    $ ds_trust = 0
    $ ds_rest = 0
    $ ds_reply = 'wait'
    $ ds_ending = ''
    call main_ds_from(1)
    return

label main_ds_from(number=1):
    $ ending_begin_route('deepseek',number)
    $ main_ds_cursor = number
    while main_ds_cursor <= 8:
        $ main_current_label = 'ds_ch%02d' % main_ds_cursor
        call expression main_current_label
        $ ending_visit_route_chapter('deepseek',main_ds_cursor)
        $ main_last_chapter = main_current_label
        $ affection_award('deepseek',main_current_label)
        $ renpy.save_persistent()
        if main_ds_cursor < 8:
            call mainline_finish_with_agent('deepseek', 'DeepSeek篇', main_ds_cursor, DS_TITLES[main_ds_cursor - 1], DS_TITLES[main_ds_cursor])
            if _return != 'next':
                return
        $ main_ds_cursor += 1
    $ ds_ending = ds_reply
    $ setattr(persistent, 'main_ds_' + ds_ending, True)
    $ ending_record_complete_route('deepseek',ds_ending)
    $ renpy.save_persistent()
    call screen main_ending_card(ds_ending)
    return

label show_main_cg(key):
    $ main_cg = original_cg_by_id(key)
    $ setattr(persistent, main_cg['flag'], True)
    window hide
    scene expression story_cg_picture(main_cg) with dissolve
    pause
    window auto
    return

label main_side_from(role, number=1):
    if role not in ('gpt','grok'):
        $ renpy.error('Unavailable authored route')
    if number == 1:
        $ setattr(store, role+'_ending', '')
        $ setattr(store, 'gpt7_reply' if role == 'gpt' else 'grok7_answer', '')
    $ ending_begin_route(role,number)
    $ side_route = next(r for r in LONG_ROUTES if r['id'] == role)
    $ side_cursor = number
    while side_cursor <= 8:
        call expression role + '_ch%02d' % side_cursor
        $ ending_visit_route_chapter(role,side_cursor)
        $ main_last_chapter = role + '_ch%02d' % side_cursor
        $ affection_award(role,main_last_chapter)
        $ renpy.save_persistent()
        if side_cursor < 8:
            call mainline_finish_with_agent(role, side_route['name']+'篇', side_cursor, side_route['chapters'][side_cursor - 1]['title'], side_route['chapters'][side_cursor]['title'])
            if _return != 'next':
                return
        $ side_cursor += 1
    $ side_reply = getattr(store,role+'8_ending')
    if not getattr(store,role+'8_complete') or side_reply not in ('love','wait','friend'):
        $ renpy.error('Authored route did not finish with a valid answer')
    $ setattr(store,role+'_ending',side_reply)
    $ setattr(persistent,'main_'+role+'_'+side_reply,True)
    $ ending_record_complete_route(role,side_reply)
    $ renpy.save_persistent()
    call screen side_ending_card(role,side_reply)
    return

screen main_route_in_progress(name):
    modal True
    add Solid('#201a30e8')
    frame:
        align (0.5,0.5)
        xsize 760
        padding (42,36)
        background SoftPanel('#fcf2ee','#ba7597',15)
        vbox:
            spacing 20
            text (name+'篇 · 前六章') size 32 color '#512d53'
            text '这段相处已经写下。后面的两章与结局正在制作。' size 24 color '#75536e' xmaximum 660
            text '这不是路线结局。已读章节会留在本地，之后可以继续。' size 18 color '#927889' xmaximum 660
            textbutton '回到标题' id 'side_route_return' style 'navigation_button' action Return() text_color '#653657' background SoftPanel('#f0d7e3','#b57d98',10) hover_background SoftPanel('#ffe8f0','#b57198',10)

label gpt_ch01_play:
    call main_side_from('gpt', 1)
    return
label gpt_ch02_play:
    call main_side_from('gpt', 2)
    return
label grok_ch01_play:
    call main_side_from('grok', 1)
    return
label grok_ch02_play:
    call main_side_from('grok', 2)
    return

label gpt_ch03_play:
    call main_side_from('gpt', 3)
    return
label gpt_ch04_play:
    call main_side_from('gpt', 4)
    return
label grok_ch03_play:
    call main_side_from('grok', 3)
    return
label grok_ch04_play:
    call main_side_from('grok', 4)
    return

image bg river day = Transform('images/original/bg_river_day.png', xysize=(1280,720), fit='cover')
image bg echo rain = Transform('images/original/echo_shrine_rain.png', xysize=(1280,720), fit='cover')
image sprite deepseek neutral = deepseek_body('neutral')
image sprite deepseek summer = deepseek_body('summer')
image sprite deepseek yukata = deepseek_body('yukata')
image cg ds_tragedy = Transform('images/original/cg_ds_tragedy.png', xysize=(1280,720), fit=('contain' if TOK_MOBILE else 'cover'))

label show_tragedy_cg(key='final'):
    $ persistent.cg_ds_tragedy = True
    $ persistent.tragedy_cg_seen = list(set(persistent.tragedy_cg_seen or []) | {key})
    window hide
    scene expression Transform(tragedy_cg_path(key), xysize=(1280,720), fit=('contain' if TOK_MOBILE else 'cover')) with dissolve
    pause
    window auto
    return

screen optional_tragedy_cg_view():
    modal True
    zorder 300
    default selected = 'final'
    add Solid('#111722')
    if selected in (persistent.tragedy_cg_seen or []) or (selected == 'final' and persistent.cg_ds_tragedy):
        add Transform(tragedy_cg_path(selected), xysize=(1280,720), fit='contain')
    text '独立IF · 没有等到的那碗饭' xpos 30 ypos 25 size 24 outlines [(2,'#132035',0,1)] color '#fff6fc'
    hbox:
        xpos 30
        ypos 660
        spacing 12
        for key, title, filename in TRAGEDY_CGS:
            textbutton title:
                id ('tragedy_cg_'+key)
                action SetScreenVariable('selected', key)
                sensitive key in (persistent.tragedy_cg_seen or []) or (key == 'final' and persistent.cg_ds_tragedy)
                text_size 21
                text_color '#fff6fc'
                text_selected_color '#ffe2a8'
                background Solid('#112035db')
    textbutton '返回结局收藏' id 'tragedy_cg_close' action Hide('optional_tragedy_cg_view') xpos 1060 ypos 21 xsize 190 text_size 20 background Solid('#FFF7F1f2')
    key 'game_menu' action Hide('optional_tragedy_cg_view')

screen main_chapter_finish(arc, number, title, next_title, agent_role=None):
    modal True
    add Solid('#241c32e8')
    frame:
        align (0.5,0.5)
        xsize 720
        padding (38,32)
        background SoftPanel('#fcf2ee','#ba7597',15)
        vbox:
            spacing 20
            text (arc+' · 第'+str(number)+'章') size 22 color '#a55983'
            text title size 33 color '#512d53' xmaximum 644
            text ('下一章  '+next_title) size 23 color '#75536e' xmaximum 644
            text '选择与约定会继续留在这份存档里。' size 17 color '#8b7185'
            if agent_role and mla_ready(agent_role,number):
                textbutton '和她聊聊 · AI推进' id 'main_agent_open' style 'navigation_button' action Return('agent') xsize 614 text_color '#653657'
            hbox:
                spacing 14
                textbutton '继续下一章' id 'main_continue' style 'navigation_button' action Return('next') xsize 300 text_color '#653657' background SoftPanel('#f0d7e3','#b57d98',10)
                textbutton '回到标题' id 'main_chapter_return' style 'navigation_button' action Return('title') xsize 300 text_color '#653657' background SoftPanel('#fff8f1','#caa8bb',10)

screen main_invitation():
    modal True
    add Solid('#201a30ec')
    frame:
        align (0.5,0.5)
        xsize 1000
        padding (34,26)
        background SoftPanel('#fcf2ee','#ba7597',15)
        vbox:
            spacing 15
            text '今晚，想赴谁的约？' size 34 color '#512d53'
            text 'DeepSeek、GPT、Grok、Claude、Kimi各八章。去过的地点与相处记录决定可赴的约。' xmaximum 930 size 19 color '#826277'
            vpgrid:
                cols 3
                spacing 10
                xsize 930
                ysize 330
                pagekeys True
                arrowkeys False
                mousewheel True
                draggable True
                for route in LONG_ROUTES:
                    button:
                        id ('main_invite_'+route['id'])
                        xsize 303
                        ysize 92
                        background SoftPanel('#f3dce7' if route['id']=='deepseek' else '#ece3e9','#c29aaf',10)
                        action Return(route['id'])
                        sensitive town_route_available(route['id'])
                        vbox:
                            spacing 5
                            text route['name'] size 25 color '#5d3358'
                            text ('一碗饭的分量 · 八章' if route['id']=='deepseek' else '八章 · 三种关系结局' if route['id'] in ('gpt','grok','claude','kimi') else '前'+str(OPENING_CHAPTER_LIMITS[route['id']])+'章 · 制作中' if route['id'] in OPENING_CHAPTER_LIMITS else '个人篇制作中') size 16 color '#94758a'
                null width 303 height 92
            textbutton '今晚先到这里' action Return('title') text_color '#734963' background SoftPanel('#f0d7e3','#b57d98',10) hover_background SoftPanel('#ffe8f0','#b57198',10)

screen main_ending_card(key):
    modal True
    add Solid('#201a30df')
    frame:
        align (0.5,0.5)
        xsize 760
        padding (42,36)
        background SoftPanel('#fcf2ee','#ba7597',15)
        vbox:
            spacing 20
            text ('DeepSeek篇 · '+DS_ENDINGS[key][1]+'结局') size 24 color '#a55983'
            text DS_ENDINGS[key][0] size 37 color '#512d53' xmaximum 670
            text '这一段故事写到了最后一页。下次见面，饭还是热的。' size 23 color '#75536e' xmaximum 670
            text '完整主线结局已收进「结局收藏」。其他角色的个人故事仍在制作。' size 17 color '#927889' xmaximum 670
            if key == 'love':
                textbutton '婚后还有一页' id 'main_ending_afterstories' style 'navigation_button' action ShowMenu('afterstories') text_color '#653657'
            textbutton '回到标题' id 'main_ending_return' style 'navigation_button' action Return() xsize 300 text_color '#653657' background SoftPanel('#f0d7e3','#b57d98',10)

label common_ch03_play:
    call main_common_from(3)
    return
label common_ch04_play:
    call main_common_from(4)
    return
label common_ch05_play:
    call main_common_from(5)
    return
label common_ch06_play:
    call main_common_from(6)
    return
label common_ch07_play:
    call main_common_from(7)
    return
label ds_ch01_play:
    call main_deepseek_start
    return
label ds_ch02_play:
    call main_ds_from(2)
    return
label ds_ch03_play:
    call main_ds_from(3)
    return
label ds_ch04_play:
    call main_ds_from(4)
    return
label ds_ch05_play:
    call main_ds_from(5)
    return
label ds_ch06_play:
    call main_ds_from(6)
    return
label ds_ch07_play:
    call main_ds_from(7)
    return
label ds_ch08_play:
    call main_ds_from(8)
    return

label gpt_ch05_play:
    call main_side_from('gpt', 5)
    return

label gpt_ch06_play:
    call main_side_from('gpt', 6)
    return

label grok_ch05_play:
    call main_side_from('grok', 5)
    return

label grok_ch06_play:
    call main_side_from('grok', 6)
    return

label gpt_ch07_play:
    call main_side_from('gpt', 7)
    return

label gpt_ch08_play:
    call main_side_from('gpt', 8)
    return

label grok_ch07_play:
    call main_side_from('grok', 7)
    return

label grok_ch08_play:
    call main_side_from('grok', 8)
    return
