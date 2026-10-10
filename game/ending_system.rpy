# 作者本地隐藏结局/独立IF；不会联网，不把单篇回看计为新周目。
default persistent.secret_traces = []
default persistent.secret_endings_seen = []
default persistent.bad_endings_seen = []
default persistent.completed_route_runs = []
default ending_route_run_id = ''
default ending_route_run_role = ''
default ending_route_run_chapters = []
default secret_run_key = ''
default bad_run_key = ''
default secret_exploration = False
default ending_story_finished = False
default ending_snapshot = {}
default ending_music_snapshot = (None, False)
default ending_requested = ''

init -3 python:
    import copy as ending_copy
    import uuid as ending_uuid
    import json as ending_json
    ENDING_CATALOG = []
    if renpy.loadable('story_data/ending_catalog.json'):
        with renpy.file('story_data/ending_catalog.json') as ending_file:
            ENDING_CATALOG = ending_json.load(ending_file)['endings']
    ENDING_STATE_KEYS = ('main_scene_bg_key','main_bonds','main_last_chapter','story_invite','ds_trust','ds_rest',
        'ds_reply','ds_ending','ds_romance_style','hide_speaker_portrait','deepseek_expression',
        'minimax_pose','chapter','quick_menu','town_slot','town_visits','town_bonds',
        'town_event_flags','town_current_role','town_selected','town_day_finished',
        'town_ended_early','town_preview_mode','town_preview_bonds_backup','town_recall',
        'gpt_ending','grok_ending','gpt7_reply','grok7_answer',
        'claude6_completed_run_id','claude7_completed_run_id','claude7_answer','claude7_answer_run_id',
        'kimi6_completed_run_id','kimi7_completed_run_id','kimi7_response','kimi7_response_run_id',
        'ending_route_run_id','ending_route_run_role','ending_route_run_chapters',
        'affection_points','affection_events','affection_special_seen',
        'affection_last_change','affection_special_active')

    def ending_playthrough_stage():
        return 1 + len(persistent.completed_route_runs or [])

    def ending_begin_route(role, number):
        if number == 1:
            store.ending_route_run_id = str(ending_uuid.uuid4())
            store.ending_route_run_role = role
            store.ending_route_run_chapters = []
        elif store.ending_route_run_role != role:
            store.ending_route_run_id = ''
            store.ending_route_run_role = role
            store.ending_route_run_chapters = []

    def ending_visit_route_chapter(role, number):
        if (store.ending_route_run_id and store.ending_route_run_role == role
                and number not in store.ending_route_run_chapters):
            store.ending_route_run_chapters.append(number)

    def ending_record_complete_route(role, reply):
        if (not store.ending_route_run_id or store.ending_route_run_role != role
                or sorted(store.ending_route_run_chapters) != list(range(1,9))
                or reply not in ('love','wait','friend')
                or not persistent.main_common_ch07_seen):
            return False
        records = list(persistent.completed_route_runs or [])
        if any(r['run_id'] == store.ending_route_run_id for r in records):
            return False
        records.append(dict(run_id=store.ending_route_run_id, role=role, reply=reply))
        persistent.completed_route_runs = records
        renpy.save_persistent()
        return True

    def ending_by_id(key):
        return next((e for e in ENDING_CATALOG if e['id']==key),None)

    def ending_available(item):
        if not item or not renpy.has_label(item['label']):
            return False
        if not persistent.main_common_ch07_seen:
            return False
        gate = item['gate']
        if gate == 'trace':
            return item['role'] in (persistent.secret_traces or [])
        if gate == 'common':
            return True
        if gate == 'any_ds':
            return any(getattr(persistent,'main_ds_'+k,False) for k in ('love','wait','friend'))
        if gate == 'ds_third':
            return (ending_playthrough_stage()>=3 and
                any(getattr(persistent,'main_ds_'+k,False) for k in ('love','wait','friend')))
        if gate == 'ds_family':
            return bool(persistent.main_ds_love and persistent.after_ds_wedding_seen)
        return False

    def ending_hint(item):
        if not persistent.main_common_ch07_seen:
            return '先读完共通第七章。'
        if item['gate']=='trace':
            return '在自由日或寻访散步中，亲自与'+TOWN_ROLE_NAMES[item['role']]+'完成一次小事。'
        if item['gate']=='ds_third':
            return '完整读完两次个人篇，再进入第三周目；还需DeepSeek任一主线结局。'
        if item['gate']=='ds_family':
            return 'DeepSeek恋人结局后，先读婚礼后日谈。'
        if item['gate']=='common':
            return '共通第七章后开放。'
        return '先读完DeepSeek任一主线结局。'

    def ending_seen(item):
        entries = persistent.secret_endings_seen if item['kind']=='secret' else persistent.bad_endings_seen
        return item['id'] in (entries or [])

    def ending_guard(key, kind):
        item=ending_by_id(key)
        active=store.secret_run_key if kind=='secret' else store.bad_run_key
        return bool(item and item['kind']==kind and active==key and ending_available(item))

    def secret_guard(key):
        return ending_guard(key,'secret')

    def bad_guard(key):
        return ending_guard(key,'bad')

    def ending_capture_state():
        store.ending_snapshot={k:ending_copy.deepcopy(getattr(store,k)) for k in ENDING_STATE_KEYS}
        store.ending_music_snapshot=(renpy.music.get_playing(channel='music'),renpy.music.get_pause(channel='music'))

    def ending_restore_state():
        for key,value in store.ending_snapshot.items():
            setattr(store,key,ending_copy.deepcopy(value))
        restore_story_music(*store.ending_music_snapshot)
        store.ending_snapshot={}

    def ending_discover(role):
        if (persistent.main_common_ch07_seen and role in TOWN_ROLE_NAMES
                and (not store.town_preview_mode or store.secret_exploration)):
            traces=list(persistent.secret_traces or [])
            if role not in traces:
                persistent.secret_traces=traces+[role]
                renpy.save_persistent()

    def ending_finish(key, kind):
        if not ending_guard(key,kind):
            return False
        collection='secret_endings_seen' if kind=='secret' else 'bad_endings_seen'
        seen=list(getattr(persistent,collection) or [])
        if key not in seen:
            setattr(persistent,collection,seen+[key])
        store.ending_story_finished=True
        renpy.save_persistent()
        return True

label secret_ending_finish(key):
    $ ending_finish(key,'secret')
    return

label bad_ending_finish(key):
    $ ending_finish(key,'bad')
    return

label ending_entry(key):
    $ ending_item=ending_by_id(key)
    if not ending_available(ending_item):
        return
    if ending_item['kind']=='bad':
        call screen new_if_notice(ending_item['title'],ending_item['note'])
        if not _return:
            return
    $ ending_capture_state()
    $ ending_story_finished=False
    $ story_music('hyy_mei' if ending_item['kind']=='bad' or key=='secret_12' else 'hyy_clear_rain' if key=='secret_13' else 'hyy_clouds')
    $ secret_run_key=key if ending_item['kind']=='secret' else ''
    $ bad_run_key=key if ending_item['kind']=='bad' else ''
    call expression ending_item['label']
    $ ending_restore_state()
    $ secret_run_key=''
    $ bad_run_key=''
    if ending_story_finished:
        call screen ending_story_card(ending_item)
    return

label secret_trace_walk:
    if not persistent.main_common_ch07_seen:
        return
    $ ending_capture_state()
    $ secret_exploration=True
    $ town_reset()
    $ town_preview_mode=True
    call open_town_day(reset_day=False)
    $ secret_exploration=False
    $ ending_restore_state()
    call screen secret_walk_finish
    return

screen secret_walk_finish():
    modal True
    add Solid('#201a30e8')
    frame:
        align (0.5,0.5)
        xsize 750
        padding (36,30)
        background SoftPanel('#fcf2ee','#ba7597',15)
        vbox:
            spacing 18
            text '把路上遇见的小事记下来' size 29 color '#512d53'
            text ('已认识 '+str(len(persistent.secret_traces or []))+' 位 / 11 位') size 23 color '#75536e'
            text '散步不重置原来的自由日，也不改主线里的回答。下一次还能再去其他地方。' size 20 color '#75536e' xmaximum 675
            textbutton '看看隐藏的另一页' id 'secret_walk_hub' style 'navigation_button' action ShowMenu('ending_archive') text_size 22 text_color '#653657'
            textbutton '返回标题' id 'secret_walk_title' style 'navigation_button' action Return() text_size 22 text_color '#653657'

screen ending_story_card(item):
    modal True
    add Solid('#201a30e8')
    frame:
        align (0.5,0.5)
        xsize 790
        padding (38,34)
        background SoftPanel('#fcf2ee','#ba7597',15)
        vbox:
            spacing 19
            text ('隐藏的另一页 · 终' if item['kind']=='secret' else '平行IF · 终') size 22 color '#a55983'
            text item['title'] size 32 color '#512d53' xmaximum 710
            text '已收入收藏。主线的回答与关系仍保留；这次回看不会增加周目。' size 20 color '#75536e' xmaximum 710
            textbutton '返回结局与秘密' id 'ending_finish_hub' style 'navigation_button' action ShowMenu('ending_archive') text_size 22 text_color '#653657'
            textbutton '返回标题' id 'ending_finish_title' style 'navigation_button' action Return() text_size 22 text_color '#653657'

screen ending_archive():
    tag menu
    default ending_kind='secret'
    use game_menu('结局与秘密 / 另外的生活'):
        vbox:
            spacing 12
            hbox:
                spacing 15
                textbutton '十三个隐藏结局' id 'ending_tab_secret' action SetScreenVariable('ending_kind','secret') selected ending_kind=='secret' text_size 22
                textbutton '刀子与遗憾 IF' id 'ending_tab_bad' action SetScreenVariable('ending_kind','bad') selected ending_kind=='bad' text_size 22
                textbutton '去镇上寻访' id 'secret_trace_walk' action Start('secret_trace_walk') sensitive persistent.main_common_ch07_seen and main_menu text_size 22
            if not main_menu:
                hbox:
                    spacing 16
                    text '这页可查看收藏；短篇与寻访从标题进入，保留当前对白位置。' size 18 color '#796977' xmaximum 675
                    textbutton '先保存进度' id 'ending_save_current' action ShowMenu('save') text_size 19
            text ('当前第'+str(ending_playthrough_stage())+'周目 / 已完整读完个人篇 '+str(len(persistent.completed_route_runs or []))+' 次') size 19 color '#796977'
            if main_menu and not persistent.main_common_ch07_seen:
                text '寻访散步：先读完共通第七章。' size 18 color '#796977'
            text '回看最后一章或短篇不算新周目；旧版已读收藏保留，完整通关次数从本版开始记录。' size 17 color '#796977' xmaximum 900
            viewport:
                ysize (370 if main_menu else 330)
                mousewheel True
                draggable True
                arrowkeys False
                pagekeys True
                vbox:
                    spacing 11
                    for e in ENDING_CATALOG:
                        if e['kind']==ending_kind:
                            $ opened=ending_available(e)
                            frame:
                                xsize 890
                                padding (21,14)
                                background SoftPanel('#f7e8ee','#b586a5',10)
                                vbox:
                                    spacing 7
                                    text (e['title'] if opened or ending_seen(e) else '还没翻开的另一页 · '+e['id'][-2:] if e['kind']=='secret' else e['title']) size 25 color '#663758' xmaximum 845
                                    text (TOWN_ROLE_NAMES.get(e['role'],'共同篇')+' / '+e['note']) size 18 color '#8e6c81' xmaximum 845
                                    hbox:
                                        spacing 18
                                        textbutton ('再次阅读' if ending_seen(e) else '阅读这一页') id ('ending_read_'+e['id']) style 'navigation_button' action Start(e['id']+'_start') sensitive opened and main_menu text_size 21 text_color '#653657'
                                        text ('已收藏' if ending_seen(e) else '从标题进入阅读' if opened and not main_menu else '可以阅读' if opened else ending_hint(e)) size 17 color '#8e6c81' xmaximum 665 yalign 0.5
