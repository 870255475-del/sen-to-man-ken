init -5 python:
    LICENSED_MUSIC = [{'id': 'hyy_mei', 'title': '梅', 'artist': '黑耀耀，tohka', 'mood': '伤感与未说出口的告别', 'file': 'audio/licensed/hyy_mei.mp3', 'credit': '音乐：黑耀耀的素材小屋；曲目：梅；制作人：黑耀耀，tohka', 'source': 'https://www.heiyaoyao.cn/music/bgm/'}, {'id': 'hyy_clear_rain', 'title': '焉知晴雨', 'artist': '黑耀', 'mood': '温馨相处与婚后日常', 'file': 'audio/licensed/hyy_clear_rain.mp3', 'credit': '音乐：黑耀耀的素材小屋；曲目：焉知晴雨；制作人：黑耀', 'source': 'https://www.heiyaoyao.cn/music/bgm/'}, {'id': 'hyy_wafuu', 'title': '和风吹拂', 'artist': '黑耀', 'mood': '共通神社与小镇日常', 'file': 'audio/licensed/hyy_wafuu.mp3', 'credit': '音乐：黑耀耀的素材小屋；曲目：和风吹拂；制作人：黑耀', 'source': 'https://www.heiyaoyao.cn/music/bgm2/'}, {'id': 'hyy_clouds', 'title': '雾散云开', 'artist': '黑耀', 'mood': '轻喜剧与悠闲散步', 'file': 'audio/licensed/hyy_clouds.mp3', 'credit': '音乐：黑耀耀的素材小屋；曲目：雾散云开；制作人：黑耀', 'source': 'https://www.heiyaoyao.cn/music/bgm2/'}, {'id': 'hyy_moment', 'title': '永远的瞬间', 'artist': '黑耀', 'mood': '婚礼与纪念日', 'file': 'audio/licensed/hyy_moment.mp3', 'credit': '音乐：黑耀耀的素材小屋；曲目：永远的瞬间；制作人：黑耀', 'source': 'https://www.heiyaoyao.cn/music/bgm4/'}, {'id': 'hyy_far_smile', 'title': '遥远那日的笑容', 'artist': '黑耀', 'mood': '伤感IF与旧日回忆', 'file': 'audio/licensed/hyy_far_smile.mp3', 'credit': '音乐：黑耀耀的素材小屋；曲目：遥远那日的笑容；制作人：黑耀', 'source': 'https://www.heiyaoyao.cn/music/bgm4/'}]

    def story_music(cue, fade=1.2):
        track = next(t for t in LICENSED_MUSIC if t['id'] == cue)
        if list(renpy.music.get_loop(channel='music') or []) != [track['file']]:
            renpy.music.play(track['file'], channel='music', loop=True, fadeout=0.7, fadein=fade)
        renpy.music.set_pause(False, channel='music')

    def restore_story_music(previous, paused=False):
        if previous:
            if renpy.music.get_playing(channel='music') != previous:
                # A paused channel cannot finish an audio fade. Switch before pausing.
                renpy.music.play(previous, channel='music', loop=True, fadeout=0 if paused else 0.7, fadein=0 if paused else 0.7)
        else:
            renpy.music.stop(channel='music', fadeout=0 if paused else 0.7)
        renpy.music.set_pause(paused, channel='music')

screen music_room():
    tag menu
    default previous_music = renpy.music.get_playing(channel='music')
    default previous_pause = renpy.music.get_pause(channel='music')
    default selected_music = None
    on 'hide' action Function(restore_story_music, previous_music, previous_pause)
    on 'replaced' action Function(restore_story_music, previous_music, previous_pause)
    use game_menu('配乐鉴赏 / 音乐署名'):
        vbox:
            xsize 930
            spacing 10
            text '曲目来自黑耀耀的素材小屋与 Kevin MacLeod 官方发布页，按逐曲许可使用。' style 'tok_ui_body' size 20 color TOK_UI_INK xmaximum 900
            viewport:
                id 'music_tracks_scroll'
                xsize 930
                ysize 300
                mousewheel True
                draggable True
                arrowkeys False
                pagekeys True
                vbox:
                    spacing 8
                    for track in LICENSED_MUSIC:
                        frame:
                            style 'tok_ui_panel'
                            xsize 886
                            padding (12,8)
                            background SoftPanel(TOK_UI_PAPER,TOK_UI_EDGE,10)
                            hbox:
                                spacing 18
                                textbutton track['title'] id ('music_'+track['id']) style 'tok_ui_button' action [SetScreenVariable('selected_music',track['id']), Function(story_music,track['id'])] selected selected_music == track['id'] xsize 220 yminimum 48 padding (15,8) text_size 22
                                vbox:
                                    spacing 3
                                    text track['mood'].split('/',1)[0].strip() style 'tok_ui_body' size 19 color TOK_UI_INK xmaximum 600
                                    text track['artist'] style 'tok_ui_note' size 17 color TOK_UI_MUTED xmaximum 600
            hbox:
                spacing 16
                textbutton '暂停 / 继续' id 'music_pause' style 'tok_ui_button' action PauseAudio('music','toggle') text_size 20 xsize 190 ysize 44
                textbutton '音乐静音' id 'music_mute' style 'tok_ui_button' action Preference('music mute','toggle') text_size 20 xsize 170 ysize 44
                frame:
                    style 'tok_ui_panel'
                    background SoftPanel(TOK_UI_PAPER,TOK_UI_EDGE,8)
                    xsize 322
                    ysize 42
                    yalign 0.5
                    padding (12,15)
                    bar style 'bar' value Preference('music volume') xsize 298 ysize 12
            text '原六首：黑耀耀的素材小屋（《梅》另署名 tohka）；新增四首：Kevin MacLeod。CC BY 4.0。' style 'tok_ui_note' size 18 color TOK_UI_MUTED xmaximum 900
            hbox:
                spacing 13
                text '离开后恢复原配乐。完整许可：' style 'tok_ui_note' size 17 color TOK_UI_MUTED yalign 0.5
                textbutton '黑耀耀素材库' style 'tok_ui_button' action OpenURL('https://www.heiyaoyao.cn/') text_size 17 ysize 38 padding (12,6)
                textbutton 'CC BY 4.0' style 'tok_ui_button' action OpenURL('https://creativecommons.org/licenses/by/4.0/') text_size 17 ysize 38 padding (12,6)
                textbutton '新增曲目署名' id 'music_extra_credits' style 'tok_ui_button' action ShowMenu('v17_music_expansion_credits') text_size 17 ysize 38 padding (12,6)
