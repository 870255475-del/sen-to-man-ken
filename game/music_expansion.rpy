# v17 integrated extension; author-original audio files remain unchanged.
# The four audio files remain author-original bytes. No automatic scene hooks.
# licensed_music.rpy's LICENSED_MUSIC is initialized at -5; this appends at -4.
init -4 python:
    V17_EXTRA_MUSIC = [{'id': 'km_carefree',
      'title': 'Carefree',
      'artist': 'Kevin MacLeod',
      'file': 'audio/licensed/km_carefree.mp3',
      'credit': 'Carefree Kevin MacLeod (incompetech.com)\n'
                'Licensed under Creative Commons: By Attribution 4.0\n'
                'https://creativecommons.org/licenses/by/4.0/',
      'source': 'https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1400037',
      'mood': '日常 / 作者标注96 BPM；未听评',
      'license': 'CC BY 4.0',
      'license_url': 'https://creativecommons.org/licenses/by/4.0/'},
     {'id': 'km_spoons',
      'title': 'March of the Spoons',
      'artist': 'Kevin MacLeod',
      'file': 'audio/licensed/km_spoons.mp3',
      'credit': 'March of the Spoons Kevin MacLeod (incompetech.com)\n'
                'Licensed under Creative Commons: By Attribution 4.0\n'
                'https://creativecommons.org/licenses/by/4.0/',
      'source': 'https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1700008',
      'mood': '乌龙 / 作者标注85 BPM；未听评',
      'license': 'CC BY 4.0',
      'license_url': 'https://creativecommons.org/licenses/by/4.0/'},
     {'id': 'km_dreamer',
      'title': 'Dreamer',
      'artist': 'Kevin MacLeod',
      'file': 'audio/licensed/km_dreamer.mp3',
      'credit': 'Dreamer Kevin MacLeod (incompetech.com)\n'
                'Licensed under Creative Commons: By Attribution 4.0\n'
                'https://creativecommons.org/licenses/by/4.0/',
      'source': 'https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1600043',
      'mood': '约会 / 作者标注100 BPM；未听评',
      'license': 'CC BY 4.0',
      'license_url': 'https://creativecommons.org/licenses/by/4.0/'},
     {'id': 'km_bittersweet',
      'title': 'Bittersweet',
      'artist': 'Kevin MacLeod',
      'file': 'audio/licensed/km_bittersweet.mp3',
      'credit': 'Bittersweet Kevin MacLeod (incompetech.com)\n'
                'Licensed under Creative Commons: By Attribution 4.0\n'
                'https://creativecommons.org/licenses/by/4.0/',
      'source': 'https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1700004',
      'mood': '伤感 / 作者标注73 BPM；未听评',
      'license': 'CC BY 4.0',
      'license_url': 'https://creativecommons.org/licenses/by/4.0/'}]
    for _v17_track in V17_EXTRA_MUSIC:
        _v17_existing = next((t for t in LICENSED_MUSIC if t['id'] == _v17_track['id']), None)
        if _v17_existing is None:
            LICENSED_MUSIC.append(_v17_track)
        elif _v17_existing['file'] != _v17_track['file']:
            raise Exception('Conflicting v17 music id: ' + _v17_track['id'])
    del _v17_track, _v17_existing

    V17_MUSIC_FADES = {'km_carefree': {'fadein': 1.0, 'fadeout': 0.8},
     'km_spoons': {'fadein': 0.55, 'fadeout': 0.65},
     'km_dreamer': {'fadein': 1.8, 'fadeout': 1.2},
     'km_bittersweet': {'fadein': 2.2, 'fadeout': 1.8},
     'hyy_mei': {'fadein': 1.5, 'fadeout': 1.2},
     'hyy_clear_rain': {'fadein': 1.4, 'fadeout': 1.2}}
    V17_SCENE_MUSIC_CUES = {'common_ch01_scene2': 'km_spoons',
     'common_ch01_scene3': 'km_carefree',
     'common_ch01_scene5': 'km_carefree',
     'ds01_scene1': 'km_carefree',
     'ds01_scene3': 'km_dreamer',
     'ds01_scene4': 'km_carefree',
     'ds01_scene5': 'km_dreamer',
     'ds03_old_rice_memory': 'km_bittersweet',
     'ds03_scene4': 'hyy_mei',
     'ds03_scene5': 'hyy_clear_rain'}
    V17_EVENT_MUSIC_ROLES = ('deepseek', 'gpt', 'grok', 'claude', 'kimi', 'minimax', 'gemini', 'qwen', 'glm', 'opencode', 'zcode')
    V17_EVENT_ENTRY_CUES = {'swim': 'km_carefree', 'mishap': 'km_spoons', 'kiss': 'km_dreamer'}

    def v17_music_play(cue):
        track = next(t for t in LICENSED_MUSIC if t['id'] == cue)
        fade = V17_MUSIC_FADES[cue]
        if list(renpy.music.get_loop(channel='music') or []) != [track['file']]:
            renpy.music.play(track['file'], channel='music', loop=True,
                             fadeout=fade['fadeout'], fadein=fade['fadein'])
        renpy.music.set_pause(False, channel='music')
        return cue

    def v17_music_scene_cue(cue_key):
        return v17_music_play(V17_SCENE_MUSIC_CUES[cue_key])

    def v17_music_event_cue(role, kind, phase='entry'):
        if role not in V17_EVENT_MUSIC_ROLES or kind not in V17_EVENT_ENTRY_CUES:
            return False
        if phase not in ('entry', 'accepted_cg', 'decline', 'settled'):
            return False
        if not character_event_story_allowed(role, kind):
            return False
        cue = V17_EVENT_ENTRY_CUES[kind]
        if phase == 'decline' and kind != 'kiss':
            cue = 'km_carefree'
        elif phase == 'settled' and kind == 'mishap':
            cue = 'km_carefree'
        return v17_music_play(cue)

# Root can add this screen to the actual music room with:
# textbutton '新增曲目完整署名' action ShowMenu('v17_music_expansion_credits')
# The shared ten-track music room intro/footer also need accurate author wording.
screen v17_music_expansion_credits():
    tag menu
    use game_menu('新增配乐 / 完整许可署名'):
        viewport:
            id 'music_expansion_credits_scroll'
            arrowkeys False
            pagekeys True
            mousewheel True
            draggable True
            xsize 930
            ysize 470
            vbox:
                spacing 15
                text '作者原始音频未修改。仅在剧情中使用运行时淡入淡出。' style 'tok_ui_body' size 20 xmaximum 900
                for track in V17_EXTRA_MUSIC:
                    frame:
                        style 'tok_ui_panel'
                        background SoftPanel(TOK_UI_PAPER,TOK_UI_EDGE,10)
                        xsize 900
                        padding (16, 12)
                        vbox:
                            spacing 5
                            text track['credit'] style 'tok_ui_body' size 18 xmaximum 860
                            hbox:
                                spacing 16
                                textbutton '作者官方曲页' style 'tok_ui_button' action OpenURL(track['source']) text_size 18
                                textbutton 'CC BY 4.0 许可' style 'tok_ui_button' action OpenURL(track['license_url']) text_size 18
                text '原六首黑耀耀 / tohka 曲目的署名与许可继续保留在配乐鉴赏。' style 'tok_ui_note' size 18 xmaximum 900
