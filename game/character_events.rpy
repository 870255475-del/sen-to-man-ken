# v17独立平行邀约IF控制器候选。所有角色30岁，主线结局不作为前提。
# CG只由实际正文选择支show_main_cg解锁。正文与root真实BG/33PNG另行接入。
default persistent.cg_fan_deepseek_swim = False
default persistent.character_event_deepseek_swim_seen = False
default persistent.cg_fan_deepseek_mishap = False
default persistent.character_event_deepseek_mishap_seen = False
default persistent.cg_fan_deepseek_kiss = False
default persistent.character_event_deepseek_kiss_seen = False
default persistent.cg_fan_gpt_swim = False
default persistent.character_event_gpt_swim_seen = False
default persistent.cg_fan_gpt_mishap = False
default persistent.character_event_gpt_mishap_seen = False
default persistent.cg_fan_gpt_kiss = False
default persistent.character_event_gpt_kiss_seen = False
default persistent.cg_fan_claude_swim = False
default persistent.character_event_claude_swim_seen = False
default persistent.cg_fan_claude_mishap = False
default persistent.character_event_claude_mishap_seen = False
default persistent.cg_fan_claude_kiss = False
default persistent.character_event_claude_kiss_seen = False
default persistent.cg_fan_grok_swim = False
default persistent.character_event_grok_swim_seen = False
default persistent.cg_fan_grok_mishap = False
default persistent.character_event_grok_mishap_seen = False
default persistent.cg_fan_grok_kiss = False
default persistent.character_event_grok_kiss_seen = False
default persistent.cg_fan_minimax_swim = False
default persistent.character_event_minimax_swim_seen = False
default persistent.cg_fan_minimax_mishap = False
default persistent.character_event_minimax_mishap_seen = False
default persistent.cg_fan_minimax_kiss = False
default persistent.character_event_minimax_kiss_seen = False
default persistent.cg_fan_kimi_swim = False
default persistent.character_event_kimi_swim_seen = False
default persistent.cg_fan_kimi_mishap = False
default persistent.character_event_kimi_mishap_seen = False
default persistent.cg_fan_kimi_kiss = False
default persistent.character_event_kimi_kiss_seen = False
default persistent.cg_fan_gemini_swim = False
default persistent.character_event_gemini_swim_seen = False
default persistent.cg_fan_gemini_mishap = False
default persistent.character_event_gemini_mishap_seen = False
default persistent.cg_fan_gemini_kiss = False
default persistent.character_event_gemini_kiss_seen = False
default persistent.cg_fan_qwen_swim = False
default persistent.character_event_qwen_swim_seen = False
default persistent.cg_fan_qwen_mishap = False
default persistent.character_event_qwen_mishap_seen = False
default persistent.cg_fan_qwen_kiss = False
default persistent.character_event_qwen_kiss_seen = False
default persistent.cg_fan_glm_swim = False
default persistent.character_event_glm_swim_seen = False
default persistent.cg_fan_glm_mishap = False
default persistent.character_event_glm_mishap_seen = False
default persistent.cg_fan_glm_kiss = False
default persistent.character_event_glm_kiss_seen = False
default persistent.cg_fan_opencode_swim = False
default persistent.character_event_opencode_swim_seen = False
default persistent.cg_fan_opencode_mishap = False
default persistent.character_event_opencode_mishap_seen = False
default persistent.cg_fan_opencode_kiss = False
default persistent.character_event_opencode_kiss_seen = False
default persistent.cg_fan_zcode_swim = False
default persistent.character_event_zcode_swim_seen = False
default persistent.cg_fan_zcode_mishap = False
default persistent.character_event_zcode_mishap_seen = False
default persistent.cg_fan_zcode_kiss = False
default persistent.character_event_zcode_kiss_seen = False

default character_event_active = False
default character_event_role = ''
default character_event_kind = ''
default character_event_age_confirmed = False
default character_event_parallel_confirmed = False
default character_event_finished = False
default character_event_displayed = False
default character_event_run_id = None
default character_event_background_phase = 'entry'

init -5 python:
    CHARACTER_EVENT_ROLES = [["deepseek","DeepSeek"],["gpt","GPT"],["claude","Claude"],["grok","Grok"],["minimax","MiniMax"],["kimi","Kimi"],["gemini","Gemini"],["qwen","Qwen"],["glm","GLM"],["opencode","OpenCode"],["zcode","ZCode"]]
    CHARACTER_EVENT_KINDS = [["swim","泳装邀约"],["mishap","生活乌龙"],["kiss","轻吻之前"]]
    CHARACTER_EVENT_CGS = [
        {"id":"fan_deepseek_swim","title":"泳圈不装饭","file":"images/original/cg_fan_deepseek_swim.png","flag":"cg_fan_deepseek_swim"},
        {"id":"fan_deepseek_mishap","title":"空盒今天也要坐好","file":"images/original/cg_fan_deepseek_mishap.png","flag":"cg_fan_deepseek_mishap"},
        {"id":"fan_deepseek_kiss","title":"五分钟不添一餐","file":"images/original/cg_fan_deepseek_kiss.png","flag":"cg_fan_deepseek_kiss"},
        {"id":"fan_gpt_swim","title":"泳圈比画大","file":"images/original/cg_fan_gpt_swim.png","flag":"cg_fan_gpt_swim"},
        {"id":"fan_gpt_mishap","title":"这一角我不裁","file":"images/original/cg_fan_gpt_mishap.png","flag":"cg_fan_gpt_mishap"},
        {"id":"fan_gpt_kiss","title":"杯柄转回来以后","file":"images/original/cg_fan_gpt_kiss.png","flag":"cg_fan_gpt_kiss"},
        {"id":"fan_claude_swim","title":"今天只拿五枚","file":"images/original/cg_fan_claude_swim.png","flag":"cg_fan_claude_swim"},
        {"id":"fan_claude_mishap","title":"花园后面的两个字","file":"images/original/cg_fan_claude_mishap.png","flag":"cg_fan_claude_mishap"},
        {"id":"fan_claude_kiss","title":"这句我没有改","file":"images/original/cg_fan_claude_kiss.png","flag":"cg_fan_claude_kiss"},
        {"id":"fan_grok_swim","title":"第十只环","file":"images/original/cg_fan_grok_swim.png","flag":"cg_fan_grok_swim"},
        {"id":"fan_grok_mishap","title":"花盆先到第三桌","file":"images/original/cg_fan_grok_mishap.png","flag":"cg_fan_grok_mishap"},
        {"id":"fan_grok_kiss","title":"这次不抢下一句","file":"images/original/cg_fan_grok_kiss.png","flag":"cg_fan_grok_kiss"},
        {"id":"fan_minimax_swim","title":"MiniMax · 泳装邀约","file":"images/original/cg_fan_minimax_swim.png","flag":"cg_fan_minimax_swim"},
        {"id":"fan_minimax_mishap","title":"MiniMax · 生活乌龙","file":"images/original/cg_fan_minimax_mishap.png","flag":"cg_fan_minimax_mishap"},
        {"id":"fan_minimax_kiss","title":"MiniMax · 轻吻之前","file":"images/original/cg_fan_minimax_kiss.png","flag":"cg_fan_minimax_kiss"},
        {"id":"fan_kimi_swim","title":"Kimi · 泳装邀约","file":"images/original/cg_fan_kimi_swim.png","flag":"cg_fan_kimi_swim"},
        {"id":"fan_kimi_mishap","title":"Kimi · 生活乌龙","file":"images/original/cg_fan_kimi_mishap.png","flag":"cg_fan_kimi_mishap"},
        {"id":"fan_kimi_kiss","title":"Kimi · 轻吻之前","file":"images/original/cg_fan_kimi_kiss.png","flag":"cg_fan_kimi_kiss"},
        {"id":"fan_gemini_swim","title":"Gemini · 泳装邀约","file":"images/original/cg_fan_gemini_swim.png","flag":"cg_fan_gemini_swim"},
        {"id":"fan_gemini_mishap","title":"Gemini · 生活乌龙","file":"images/original/cg_fan_gemini_mishap.png","flag":"cg_fan_gemini_mishap"},
        {"id":"fan_gemini_kiss","title":"Gemini · 轻吻之前","file":"images/original/cg_fan_gemini_kiss.png","flag":"cg_fan_gemini_kiss"},
        {"id":"fan_qwen_swim","title":"Qwen · 泳装邀约","file":"images/original/cg_fan_qwen_swim.png","flag":"cg_fan_qwen_swim"},
        {"id":"fan_qwen_mishap","title":"Qwen · 生活乌龙","file":"images/original/cg_fan_qwen_mishap.png","flag":"cg_fan_qwen_mishap"},
        {"id":"fan_qwen_kiss","title":"Qwen · 轻吻之前","file":"images/original/cg_fan_qwen_kiss.png","flag":"cg_fan_qwen_kiss"},
        {"id":"fan_glm_swim","title":"GLM · 泳装邀约","file":"images/original/cg_fan_glm_swim.png","flag":"cg_fan_glm_swim"},
        {"id":"fan_glm_mishap","title":"GLM · 生活乌龙","file":"images/original/cg_fan_glm_mishap.png","flag":"cg_fan_glm_mishap"},
        {"id":"fan_glm_kiss","title":"GLM · 轻吻之前","file":"images/original/cg_fan_glm_kiss.png","flag":"cg_fan_glm_kiss"},
        {"id":"fan_opencode_swim","title":"OpenCode · 泳装邀约","file":"images/original/cg_fan_opencode_swim.png","flag":"cg_fan_opencode_swim"},
        {"id":"fan_opencode_mishap","title":"OpenCode · 生活乌龙","file":"images/original/cg_fan_opencode_mishap.png","flag":"cg_fan_opencode_mishap"},
        {"id":"fan_opencode_kiss","title":"OpenCode · 轻吻之前","file":"images/original/cg_fan_opencode_kiss.png","flag":"cg_fan_opencode_kiss"},
        {"id":"fan_zcode_swim","title":"ZCode · 泳装邀约","file":"images/original/cg_fan_zcode_swim.png","flag":"cg_fan_zcode_swim"},
        {"id":"fan_zcode_mishap","title":"ZCode · 生活乌龙","file":"images/original/cg_fan_zcode_mishap.png","flag":"cg_fan_zcode_mishap"},
        {"id":"fan_zcode_kiss","title":"ZCode · 轻吻之前","file":"images/original/cg_fan_zcode_kiss.png","flag":"cg_fan_zcode_kiss"},
    ]
    ORIGINAL_CGS.extend(CHARACTER_EVENT_CGS)
    # 背景阶段候选；必需PNG未齐时入口关闭，不以黑场冒用场景。
    CHARACTER_EVENT_BACKGROUNDS = {'fan_deepseek_swim': 'images/original/bg_event_pool_day.png',
     'fan_deepseek_mishap': 'images/original/bg_event_kitchen_day.png',
     'fan_deepseek_kiss': 'images/original/bg_event_home_entry_night.png',
     'fan_gpt_swim': 'images/original/bg_event_pool_day.png',
     'fan_gpt_mishap': 'images/original/bg_event_atelier_day.png',
     'fan_gpt_kiss': 'images/original/bg_event_home_studio_night.png',
     'fan_claude_swim': 'images/original/bg_event_pool_day.png',
     'fan_claude_mishap': 'images/original/bg_event_cafe_window_day.png',
     'fan_claude_kiss': 'images/original/bg_event_courtyard_river_dusk.png',
     'fan_grok_swim': 'images/original/bg_event_pool_day.png',
     'fan_grok_mishap': 'images/original/bg_event_courtyard_river_dusk.png',
     'fan_grok_kiss': 'images/original/bg_event_market_street_night.png',
     'fan_kimi_swim': 'images/original/bg_event_bay_day.png',
     'fan_kimi_mishap': 'images/original/bg_event_shopfront_day.png',
     'fan_kimi_kiss': 'images/original/bg_event_courtyard_river_dusk.png',
     'fan_minimax_swim': 'images/original/bg_event_bay_day.png',
     'fan_minimax_mishap': 'images/original/bg_event_bay_day.png',
     'fan_minimax_kiss': 'images/original/bg_event_courtyard_river_dusk.png',
     'fan_gemini_swim': 'images/original/bg_event_bay_day.png',
     'fan_gemini_mishap': 'images/original/bg_event_kitchen_day.png',
     'fan_gemini_kiss': 'images/original/bg_event_roof_terrace_dusk.png',
     'fan_qwen_swim': 'images/original/bg_event_bay_day.png',
     'fan_qwen_mishap': 'images/original/bg_event_cafe_window_day.png',
     'fan_qwen_kiss': 'images/original/bg_event_courtyard_river_dusk.png',
     'fan_glm_swim': 'images/original/bg_event_pool_day.png',
     'fan_glm_mishap': 'images/original/bg_event_courtyard_river_dusk.png',
     'fan_glm_kiss': 'images/original/bg_event_grass_slope_sunset.png',
     'fan_opencode_swim': 'images/original/bg_event_pool_day.png',
     'fan_opencode_mishap': 'images/original/bg_event_cafe_window_day.png',
     'fan_opencode_kiss': 'images/original/bg_event_bus_shelter_day.png',
     'fan_zcode_swim': 'images/original/bg_event_bay_day.png',
     'fan_zcode_mishap': 'images/original/bg_event_stationery_day.png',
     'fan_zcode_kiss': 'images/original/bg_event_home_entry_night.png'}
    CHARACTER_EVENT_BACKGROUND_PHASES = {'fan_deepseek_swim': {'entry': 'images/original/bg_event_pool_day.png'},
     'fan_deepseek_mishap': {'entry': 'images/original/bg_event_kitchen_day.png'},
     'fan_deepseek_kiss': {'entry': 'images/original/bg_event_home_entry_night.png',
                           'door_light_on': 'images/original/bg_event_home_entry_night.png'},
     'fan_gpt_swim': {'entry': 'images/original/bg_event_pool_day.png'},
     'fan_gpt_mishap': {'entry': 'images/original/bg_event_atelier_day.png'},
     'fan_gpt_kiss': {'entry': 'images/original/bg_event_home_studio_night.png'},
     'fan_claude_swim': {'entry': 'images/original/bg_event_pool_day.png'},
     'fan_claude_mishap': {'entry': 'images/original/bg_event_cafe_window_day.png'},
     'fan_claude_kiss': {'entry': 'images/original/bg_event_courtyard_river_dusk.png',
                         'river_lights': 'images/original/bg_kimi_courtyard_night.png'},
     'fan_grok_swim': {'entry': 'images/original/bg_event_pool_day.png'},
     'fan_grok_mishap': {'entry': 'images/original/bg_event_courtyard_river_dusk.png',
                         'window_table': 'images/original/bg_event_cafe_window_dusk.png',
                         'courtyard_exit': 'images/original/bg_event_courtyard_river_dusk.png'},
     'fan_grok_kiss': {'entry': 'images/original/bg_event_market_street_night.png'},
     'fan_kimi_swim': {'entry': 'images/original/bg_event_bay_day.png'},
     'fan_kimi_mishap': {'entry': 'images/original/bg_event_shopfront_day.png',
                         'side_lane': 'images/original/bg_event_shopfront_day.png',
                         'window_table': 'images/original/bg_event_cafe_window_day.png'},
     'fan_kimi_kiss': {'entry': 'images/original/bg_event_courtyard_river_dusk.png',
                       'home_inside': 'images/original/bg_event_home_studio_night.png'},
     'fan_minimax_swim': {'entry': 'images/original/bg_event_bay_day.png'},
     'fan_minimax_mishap': {'entry': 'images/original/bg_event_bay_day.png'},
     'fan_minimax_kiss': {'entry': 'images/original/bg_event_courtyard_river_dusk.png',
                          'home_inside': 'images/original/bg_event_home_studio_night.png'},
     'fan_gemini_swim': {'entry': 'images/original/bg_event_bay_day.png'},
     'fan_gemini_mishap': {'entry': 'images/original/bg_event_kitchen_day.png',
                           'picnic_shade': 'images/original/bg_river_day.png'},
     'fan_gemini_kiss': {'entry': 'images/original/bg_event_roof_terrace_dusk.png'},
     'fan_qwen_swim': {'entry': 'images/original/bg_event_bay_day.png'},
     'fan_qwen_mishap': {'entry': 'images/original/bg_event_cafe_window_day.png',
                         'shop_exit': 'images/original/bg_event_shopfront_day.png',
                         'river_rest': 'images/original/bg_river_day.png'},
     'fan_qwen_kiss': {'entry': 'images/original/bg_event_courtyard_river_dusk.png'},
     'fan_glm_swim': {'entry': 'images/original/bg_event_pool_day.png'},
     'fan_glm_mishap': {'entry': 'images/original/bg_event_courtyard_river_dusk.png'},
     'fan_glm_kiss': {'entry': 'images/original/bg_event_grass_slope_sunset.png'},
     'fan_opencode_swim': {'entry': 'images/original/bg_event_pool_day.png'},
     'fan_opencode_mishap': {'entry': 'images/original/bg_event_cafe_window_day.png',
                             'outside': 'images/original/bg_event_shopfront_day.png',
                             'window_table': 'images/original/bg_event_cafe_window_day.png'},
     'fan_opencode_kiss': {'entry': 'images/original/bg_event_bus_shelter_day.png'},
     'fan_zcode_swim': {'entry': 'images/original/bg_event_bay_day.png'},
     'fan_zcode_mishap': {'entry': 'images/original/bg_event_stationery_day.png'},
     'fan_zcode_kiss': {'entry': 'images/original/bg_event_home_entry_night.png',
                        'lamp_turn': 'images/original/bg_event_home_entry_night.png',
                        'home_inside': 'images/original/bg_event_home_studio_night.png'}}

init -2 python:
    import copy as character_event_copy
    import uuid as character_event_uuid
    CHARACTER_EVENT_LOCAL_PREFIXES = ('event_', 'character_event_', 'ds_', 'ds1','ds2','ds3','ds4','ds5','ds6','ds7','ds8',
        'deepseek','gpt','grok','claude','kimi','minimax','gemini','qwen','glm','opencode','zcode')
    CHARACTER_EVENT_READING_FLAGS = ('reduce_motion','cg_motion_enabled')

    def character_event_key(role,kind):
        return 'fan_'+str(role)+'_'+str(kind)

    def character_event_item(role,kind):
        key=character_event_key(role,kind)
        return next((item for item in CHARACTER_EVENT_CGS if item['id']==key),None)

    def character_event_no_other_context():
        return bool(not getattr(store,'_in_replay',False)
            and not getattr(store,'secret_run_key','') and not getattr(store,'bad_run_key','')
            and not getattr(store,'secret_exploration',False) and not getattr(store,'town_preview_mode',False)
            and not getattr(store,'affection_special_active',False) and not getattr(store,'ending_cg_active',False)
            and not getattr(store,'ds_tipsy_active',False))

    def character_event_title_context():
        return bool(getattr(store,'main_menu',False) is True
            and getattr(renpy.context(),'_main_menu',False) is True
            and not getattr(store,'character_event_active',False) and character_event_no_other_context())

    def character_event_asset_ready(role,kind):
        item=character_event_item(role,kind)
        if not item:
            return False
        registered=[entry for entry in ORIGINAL_CGS if entry['id']==item['id']]
        return bool(len(registered)==1 and registered[0]==item
            and item['flag']=='cg_'+item['id']
            and item['file']=='images/original/cg_'+item['id']+'.png' and renpy.loadable(item['file']))

    def character_event_scene_path(role,kind,phase=None):
        phases=CHARACTER_EVENT_BACKGROUND_PHASES.get(character_event_key(role,kind),{})
        current=getattr(store,'character_event_background_phase','entry') if phase is None else phase
        path=phases.get(current)
        return path if isinstance(path,str) and path and renpy.loadable(path) else None

    def character_event_scene_ready(role,kind):
        if not character_event_item(role,kind):
            return False
        phases=CHARACTER_EVENT_BACKGROUND_PHASES.get(character_event_key(role,kind))
        return bool(isinstance(phases,dict) and isinstance(phases.get('entry'),str) and phases.get('entry')
            and phases.get('entry')==CHARACTER_EVENT_BACKGROUNDS.get(character_event_key(role,kind))
            and all(isinstance(path,str) and path and renpy.loadable(path) for path in phases.values()))

    def character_event_available(role,kind):
        return bool(character_event_title_context() and character_event_asset_ready(role,kind)
            and character_event_scene_ready(role,kind) and renpy.has_label('event_story_'+role+'_'+kind))

    def character_event_story_allowed(role,kind):
        return bool(character_event_item(role,kind) and getattr(store,'character_event_active',False) is True
            and getattr(store,'character_event_age_confirmed',False) is True
            and getattr(store,'character_event_parallel_confirmed',False) is True
            and bool(getattr(store,'character_event_run_id',None))
            and getattr(renpy.context(),'_character_event_run_id',None)==store.character_event_run_id
            and renpy.context_nesting_level()>0
            and getattr(store,'character_event_role','')==role and getattr(store,'character_event_kind','')==kind
            and getattr(store,'main_menu',False) is False
            and getattr(renpy.context(),'_main_menu',False) is False
            and character_event_no_other_context() and character_event_asset_ready(role,kind)
            and character_event_scene_ready(role,kind))

    def character_event_hint(role,kind):
        if not character_event_asset_ready(role,kind):
            return '图片尚未就绪'
        if not renpy.has_label('event_story_'+role+'_'+kind):
            return '故事尚未接入'
        if not character_event_scene_ready(role,kind):
            return '场景图片尚未就绪'
        if not character_event_title_context():
            return '请从标题页主动进入'
        return '独立恋人邀约 · 进入前确认'

    def character_event_state_keys():
        local=tuple(name for name,value in vars(store).items()
            if name.startswith(CHARACTER_EVENT_LOCAL_PREFIXES)
            and isinstance(value,(str,int,float,bool,type(None),list,tuple,dict,set)))
        return tuple(dict.fromkeys(ENDING_STATE_KEYS+AFFECTION_STATE_KEYS+local+(
            'ending_snapshot','ending_music_snapshot','main_menu','_game_menu_screen')))

    def character_event_persistent_keys(role,kind):
        allowed={'cg_'+character_event_key(role,kind),'character_event_'+role+'_'+kind+'_seen',
            *CHARACTER_EVENT_READING_FLAGS}
        return tuple(name for name,value in vars(persistent).items() if not name.startswith('_')
            and name not in allowed and isinstance(value,(str,int,float,bool,type(None),list,tuple,dict,set)))

    def character_event_prepare(role,kind):
        names=character_event_state_keys()
        renpy.context_dynamic(*names)
        for name in names:
            if hasattr(store,name):
                setattr(store,name,character_event_copy.deepcopy(getattr(store,name)))
        renpy.context()._menu=False
        renpy.context()._main_menu=False
        store.main_menu=False
        store._menu=False
        store.suppress_overlay=False
        store.character_event_active=True
        store.character_event_role=role
        store.character_event_kind=kind
        store.character_event_background_phase='entry'
        store.character_event_age_confirmed=True
        store.character_event_parallel_confirmed=True
        store.character_event_finished=False
        store.character_event_displayed=False
        store.character_event_run_id=str(character_event_uuid.uuid4())
        renpy.context()._character_event_run_id=store.character_event_run_id
        store.quick_menu=False
        store.main_cg=None
        store.hide_speaker_portrait=True
        store._game_menu_screen='preferences'

    def character_event_note_display(event,**kwargs):
        # First actual say on the CG follows show_main_cg's scene and pause.
        # No persistent writes here; old collected flags alone cannot mark this visit.
        if event!='show_done':
            return
        role=getattr(store,'character_event_role','')
        kind=getattr(store,'character_event_kind','')
        if not character_event_story_allowed(role,kind):
            return
        item=character_event_item(role,kind)
        cg=getattr(store,'main_cg',None)
        if cg and cg.get('id')==item['id'] and original_cg_unlocked(item):
            store.character_event_displayed=True

    config.all_character_callbacks.append(character_event_note_display)

    def character_event_launch(role,kind):
        if not character_event_available(role,kind):
            return
        names=character_event_state_keys()
        saved={name:character_event_copy.deepcopy(getattr(store,name)) for name in names if hasattr(store,name)}
        missing=tuple(name for name in names if not hasattr(store,name))
        persistent_keys=character_event_persistent_keys(role,kind)
        protected={name:character_event_copy.deepcopy(getattr(persistent,name)) for name in persistent_keys}
        parent_context=renpy.context()
        sdk={name:getattr(parent_context,name) for name in ('_menu','_main_menu','_character_event_run_id') if hasattr(parent_context,name)}
        music=(list(renpy.music.get_loop(channel='music') or []),renpy.music.get_pause(channel='music'))
        outcome=None
        try:
            outcome=renpy.call_in_new_context('character_event_start',role,kind)
        finally:
            child_names=character_event_state_keys()
            for name in set(child_names)-set(names):
                if hasattr(store,name):
                    delattr(store,name)
            for name,value in saved.items():
                setattr(store,name,character_event_copy.deepcopy(value))
            for name in missing:
                if hasattr(store,name):
                    delattr(store,name)
            for name in set(character_event_persistent_keys(role,kind))-set(persistent_keys):
                delattr(persistent,name)
            for name,value in protected.items():
                if not hasattr(persistent,name) or getattr(persistent,name)!=value:
                    setattr(persistent,name,character_event_copy.deepcopy(value))
            for name,value in sdk.items():
                setattr(parent_context,name,value)
            tracks,paused=music
            if list(renpy.music.get_loop(channel='music') or [])!=tracks or paused:
                if tracks:
                    renpy.music.play(tracks,channel='music',loop=True,fadeout=0 if paused else .7,fadein=0 if paused else .7)
                else:
                    renpy.music.stop(channel='music',fadeout=0 if paused else .7)
            if paused:
                renpy.music.pump()
            renpy.music.set_pause(paused,channel='music')
        if outcome is True:
            renpy.save_persistent()
        return

label character_event_start(role=None,kind=None):
    if not character_event_available(role,kind):
        return False
    call screen character_event_confirm(role,kind)
    if _return != 'adult_parallel_yes':
        return False
    if not character_event_available(role,kind):
        return False
    $ character_event_prepare(role,kind)
    $ chapter = dict(CHARACTER_EVENT_ROLES)[role]+' / '+character_event_item(role,kind)['title']
    $ v17_music_event_cue(role,kind,'entry')
    call character_event_restore_scene
    if _return is not True:
        return False
    call expression 'event_story_'+role+'_'+kind
    if _return is not True:
        return False
    $ character_event_finished = True
    $ setattr(persistent,'character_event_'+role+'_'+kind+'_seen',True)
    # Parent wrapper commits persistent only after protected counts have been restored.
    call screen character_event_finish(role,kind)
    return True

label character_event_restore_scene(phase=None):
    if not character_event_story_allowed(character_event_role,character_event_kind):
        return False
    if not character_event_scene_path(character_event_role,character_event_kind,phase):
        return False
    if phase is not None:
        $ character_event_background_phase = phase
    $ main_cg = None
    $ hide_speaker_portrait = True
    # scene clears all old master-layer sprites; no old outfit portrait is reused.
    scene expression Transform(character_event_scene_path(character_event_role,character_event_kind),xysize=(1280,720),fit='cover')
    return True

screen character_event_archive():
    tag menu
    default event_category='swim'
    default event_role_page=0
    $ event_page_roles=CHARACTER_EVENT_ROLES[event_role_page*3:(event_role_page+1)*3]
    use game_menu('独立邀约 / 泳装 · 乌龙 · 轻吻'):
        vbox:
            spacing 10
            text '本篇采用双方已是恋人的平行前提。全员30岁；不会替主线决定关系。' style 'tok_ui_body' size 19 xmaximum 900
            hbox:
                spacing 14
                for kind,caption in CHARACTER_EVENT_KINDS:
                    textbutton caption id ('character_event_tab_'+kind) style 'tok_ui_button' action SetScreenVariable('event_category',kind) selected event_category==kind text_size 21 xsize 185
                textbutton '减少画面移动' id 'character_event_reduce_motion' style 'tok_ui_button' action ToggleField(persistent,'reduce_motion') selected persistent.reduce_motion text_size 17
            hbox:
                spacing 20
                textbutton '上一页' id 'character_event_prev' style 'tok_ui_button' action SetScreenVariable('event_role_page',event_role_page-1) sensitive event_role_page>0 text_size 19
                text ('角色 '+str(event_role_page*3+1)+'–'+str(min(11,(event_role_page+1)*3))+' / 11') style 'tok_ui_note' yalign .5
                textbutton '下一页' id 'character_event_next' style 'tok_ui_button' action SetScreenVariable('event_role_page',event_role_page+1) sensitive event_role_page<3 text_size 19
            for role,name in event_page_roles:
                $ item=character_event_item(role,event_category)
                frame:
                    style 'tok_ui_panel'
                    xsize 905
                    padding (16,12)
                    hbox:
                        spacing 15
                        vbox:
                            xsize 490
                            spacing 5
                            text (name+' · '+item['title']) style 'tok_ui_heading' size 23 xmaximum 490
                            text character_event_hint(role,event_category) style 'tok_ui_note' size 17
                        vbox:
                            spacing 5
                            textbutton '进入这次邀约' id ('character_event_read_'+role+'_'+event_category) style 'tok_ui_button' action Function(character_event_launch,role,event_category) sensitive character_event_available(role,event_category) text_size 20 xsize 345 yminimum 38
                            textbutton '欣赏已收藏CG' id ('character_event_cg_'+item['id']) style 'tok_ui_button' action Show('original_cg_view',cg_key=item['id']) sensitive (character_event_asset_ready(role,event_category) and original_cg_unlocked(item)) text_size 17 xsize 345 yminimum 32
            text '可以陪聊、留在岸边或拒绝亲吻；不会扣好感。图片只在实际展示后收藏。' style 'tok_ui_note' size 16 xmaximum 900

screen character_event_confirm(role,kind):
    modal True
    zorder 250
    add Solid('#20182bce')
    frame:
        style 'tok_ui_panel'
        align (.5,.5)
        xsize 810
        padding (32,28)
        vbox:
            spacing 18
            text character_event_item(role,kind)['title'] style 'tok_ui_heading'
            text 'R18 / 仅限18岁以上 · 角色均为30岁' style 'tok_ui_body'
            text '这是一场独立邀约，采用你们已相互选择恋人的平行前提。\n这次选择不会替主线回答，也不代表角色线已经通关。' style 'tok_ui_body' size 22 xmaximum 745
            text '进入后仍可拒绝下水、一起做事或亲吻。' style 'tok_ui_note'
            textbutton '我已满18岁，按本篇恋人前提开始' id 'character_event_confirm_yes' style 'tok_ui_button' action Return('adult_parallel_yes') yminimum 47
            textbutton '暂不进入，回到原页' id 'character_event_confirm_no' style 'tok_ui_button' action Return('adult_parallel_cancel') yminimum 43
    key 'game_menu' action Return('adult_parallel_cancel')

screen character_event_finish(role,kind):
    modal True
    add Solid('#20182bad')
    frame:
        style 'tok_ui_panel'
        align (.5,.5)
        xsize 730
        padding (30,26)
        vbox:
            spacing 18
            text character_event_item(role,kind)['title'] style 'tok_ui_heading'
            text '这次邀约已经读完。' style 'tok_ui_body'
            text ('本次CG已收藏，可以稍后再看。' if character_event_displayed else '这次没有展示CG，保留你选过的相处方式。') style 'tok_ui_note' xmaximum 660
            textbutton '回到刚才的页面' id 'character_event_finish_close' style 'tok_ui_button' action Return() yminimum 44

# all_writing_ended=true
