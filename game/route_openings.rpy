# Partial authored routes. This pause is not a route ending or a completed run.
init -4 python:
    OPENING_CHAPTER_LIMITS = {'claude': 8, 'kimi': 8}
    OPENING_ROLE_NAMES = {'claude': 'Claude', 'kimi': 'Kimi'}

label main_opening_from(role, number=1):
    if role not in OPENING_CHAPTER_LIMITS or not 1 <= number <= OPENING_CHAPTER_LIMITS[role]:
        $ renpy.error('Unavailable authored chapter')
    $ opening_role = role
    $ opening_cursor = number
    $ opening_route = next(r for r in LONG_ROUTES if r['id'] == role)
    if number == 1:
        $ setattr(store,role+'_ending','')
        $ setattr(store,role+'8_completed_run_id',None)
        $ setattr(store,role+'8_complete',False)
    $ ending_begin_route(role, number)
    while opening_cursor <= OPENING_CHAPTER_LIMITS[opening_role]:
        call expression opening_role + '_ch%02d' % opening_cursor
        if opening_cursor == 8 and (_return is not True or not getattr(store,opening_role+'8_complete',False) or getattr(store,opening_role+'8_ending','') not in ('love','wait','friend')):
            return False
        $ ending_visit_route_chapter(opening_role, opening_cursor)
        if opening_cursor in (6,7,8):
            $ setattr(renpy.store, opening_role+str(opening_cursor)+'_completed_run_id', ending_route_run_id)
        if opening_cursor == 8:
            $ setattr(persistent,'main_'+opening_role+'_ch08_seen',True)
        $ main_last_chapter = opening_role + '_ch%02d' % opening_cursor
        $ affection_award(opening_role,main_last_chapter)
        $ renpy.save_persistent()
        if opening_cursor < OPENING_CHAPTER_LIMITS[opening_role]:
            call mainline_finish_with_agent(opening_role, OPENING_ROLE_NAMES[opening_role]+'篇', opening_cursor, opening_route['chapters'][opening_cursor - 1]['title'], opening_route['chapters'][opening_cursor]['title'])
            if _return != 'next':
                return
        $ opening_cursor += 1
    $ opening_reply = getattr(store,opening_role+'8_ending','')
    $ opening_route_complete = opening_full_run_ready(opening_role,opening_reply)
    if opening_route_complete:
        $ setattr(store,opening_role+'_ending',opening_reply)
        $ setattr(persistent,'main_'+opening_role+'_'+opening_reply,True)
        $ ending_record_complete_route(opening_role,opening_reply)
        $ renpy.save_persistent()
    call screen opening_ending_card(opening_role,opening_reply,opening_route_complete)
    return True

label claude_ch01_play:
    call main_opening_from('claude', 1)
    return

label kimi_ch01_play:
    call main_opening_from('kimi', 1)
    return

label claude_ch02_play:
    call main_opening_from('claude', 2)
    return

label kimi_ch02_play:
    call main_opening_from('kimi', 2)
    return

label claude_ch03_play:
    call main_opening_from('claude', 3)
    return

label kimi_ch03_play:
    call main_opening_from('kimi', 3)
    return

label claude_ch04_play:
    call main_opening_from('claude', 4)
    return

label kimi_ch04_play:
    call main_opening_from('kimi', 4)
    return

label claude_ch05_play:
    call main_opening_from('claude', 5)
    return

label kimi_ch05_play:
    call main_opening_from('kimi', 5)
    return

screen main_opening_pause(role):
    modal True
    add Solid('#201a30e8')
    frame:
        align (0.5, 0.5)
        xsize 790
        padding (42, 36)
        background SoftPanel('#fcf2ee', '#ba7597', 15)
        vbox:
            spacing 20
            text (OPENING_ROLE_NAMES[role]+'篇 · 已写前'+str(OPENING_CHAPTER_LIMITS[role])+'章') size 29 color '#512d53'
            text '这一段相处先留在这里。' size 26 color '#75536e'
            text ('后面的'+str(8-OPENING_CHAPTER_LIMITS[role])+'章和路线结局仍在制作。这里不会增加完整通关次数。') size 21 color '#75536e' xmaximum 700
            text '本章选择会保存在存档中；已读章节可从标题回看。' size 18 color '#927889' xmaximum 700
            textbutton '保存这段进度' id 'opening_save' style 'navigation_button' action ShowMenu('save') text_size 22
            textbutton '看看后续路线设计' id 'opening_design' style 'navigation_button' action ShowMenu('route_followup', role=role) text_size 22
            textbutton '回到标题' id 'opening_return' style 'navigation_button' action Return() text_size 22

label claude_ch06_play:
    call main_opening_from('claude', 6)
    return

label kimi_ch06_play:
    call main_opening_from('kimi', 6)
    return

label claude_ch07_play:
    call main_opening_from('claude', 7)
    return

label kimi_ch07_play:
    call main_opening_from('kimi', 7)
    return

label claude_ch08_play:
    call main_opening_from('claude',8)
    return

label kimi_ch08_play:
    call main_opening_from('kimi',8)
    return
