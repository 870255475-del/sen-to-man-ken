# Formal closure support for the two authored eight-chapter routes.
default claude_ending = ''
default kimi_ending = ''
default claude8_completed_run_id = None
default kimi8_completed_run_id = None
default opening_reply = ''
default opening_route_complete = False
default persistent.main_claude_love = False
default persistent.main_claude_wait = False
default persistent.main_claude_friend = False
default persistent.main_kimi_love = False
default persistent.main_kimi_wait = False
default persistent.main_kimi_friend = False

init -2 python:
    ENDING_STATE_KEYS = tuple(dict.fromkeys(ENDING_STATE_KEYS + ('claude_ending', 'kimi_ending', 'claude8_completed_run_id', 'kimi8_completed_run_id', 'opening_reply', 'opening_route_complete', 'claude8_has_ch07', 'claude8_source_run_id', 'claude8_previous_snack', 'claude8_reply', 'claude8_reply_inherited', 'claude8_reply_confirmed', 'claude8_club_part', 'claude8_tea_order', 'claude8_frame_returned', 'claude8_club_opened', 'claude8_club_finished', 'claude8_turn_kept', 'claude8_bookmark_written', 'claude8_private_reading_kept', 'claude8_close_asked', 'claude8_close_agreed', 'claude8_wait_revisable', 'claude8_friend_turn_set', 'claude8_novel_chapter', 'claude8_ending', 'claude8_complete', 'kimi8_complete', 'kimi8_ending', 'kimi8_reply', 'kimi8_has_ch07', 'kimi8_has_ch06', 'kimi8_breakfast_fix', 'kimi8_record_order', 'kimi8_approach', 'kimi8_hand_choice', 'kimi8_breakfast_met', 'kimi8_breakfast_paid', 'kimi8_breakfast_finished', 'kimi8_new_stationery_bought', 'kimi8_record_permission', 'kimi8_bridge_met', 'kimi8_hand_asked', 'kimi8_hand_held', 'kimi8_hand_released', 'kimi8_solo_crossed', 'kimi8_solo_returned', 'kimi8_record_finished', 'kimi8_public_card_exchanged', 'kimi8_next_plan_agreed', 'kimi8_relation_closed')))

    def completed_opening_relationship_answer(role):
        if role not in ('claude','kimi') or getattr(store,'main_last_chapter','') != role+'_ch08':
            return ''
        run = getattr(store,'ending_route_run_id','')
        stamp = getattr(store,role+'8_completed_run_id',None)
        answer = getattr(store,role+'8_ending','')
        if (stamp is None or stamp != run or store.ending_route_run_role != role
                or not getattr(store,role+'8_complete',False) or answer not in ('love','wait','friend')
                or (run and 8 not in store.ending_route_run_chapters)):
            return ''
        return answer

    def opening_full_run_ready(role,reply):
        return bool(reply in ('love','wait','friend')
            and completed_opening_relationship_answer(role)==reply
            and store.ending_route_run_id
            and sorted(store.ending_route_run_chapters)==list(range(1,9))
            and persistent.main_common_ch07_seen
            and getattr(store,role+'8_has_ch07',False)
            and getattr(store,role+'7_completed_run_id',None)==store.ending_route_run_id)

init -1 python:
    SIDE_ROLE_NAMES.update(claude='Claude',kimi='Kimi')
    SIDE_ENDINGS.update({
        'claude': {'love': ('留下整页的空白','恋人'), 'wait': ('第十八日，书铺门口','等待'), 'friend': ('下一页轮到你','友人')},
        'kimi': {'love': ('书签朝向明天','恋人'), 'wait': ('三点见，答复还可以慢一点','等待'), 'friend': ('两张公开的卡','友人')},
    })
    ENDING_CG_LOVE_FLAGS.update(claude='main_claude_love',kimi='main_kimi_love')

screen opening_ending_card(role,reply,route_complete):
    modal True
    add Solid('#201a30e8')
    frame:
        align (0.5,0.5)
        xsize 790
        padding (42,36)
        background SoftPanel('#fcf2ee','#ba7597',15)
        vbox:
            spacing 20
            text (SIDE_ROLE_NAMES[role]+'篇 · '+SIDE_ENDINGS[role][reply][1]+('结局' if route_complete else '答复')) size 24 color '#a55983'
            text SIDE_ENDINGS[role][reply][0] size 35 color '#512d53' xmaximum 700
            text ('下一页，留给我们自己。' if role=='claude' else '各自的去处，也可以通向下一次见面。') size 23 color '#75536e' xmaximum 700
            text ('完整路线结局已收进收藏。回看不会再增加通关次数。' if route_complete else '本章已读完。这份记录中还有前面的章节未读，可从第一章继续相处。') size 18 color '#927889' xmaximum 700
            if route_complete:
                textbutton '查看结局收藏' id 'opening_ending_collection' style 'navigation_button' action ShowMenu('endings') text_color '#653657' text_size 22
            textbutton '回到标题' id 'opening_ending_return' style 'navigation_button' action Return('done') xsize 300 text_color '#653657' background SoftPanel('#f0d7e3','#b57d98',10)
