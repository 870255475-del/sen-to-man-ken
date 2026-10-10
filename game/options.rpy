init -10 python:
    gui.init(1280, 720)

init -9 python:
    import os
    # 试玩包存档随安装目录保存；本机交付在F，不占C盘AppData。
    # 自动验收仍尊重独立的测试存档位置。
    if not os.environ.get('RENPY_PATH_TO_SAVES'):
        config.savedir = os.path.join(config.basedir, 'userdata')

define config.name = "千to万ken"
define config.version = "0.20.0"
define config.save_directory = "SenToManKen-DeepSeek-20261001"
define config.window = "auto"
define config.window_icon = "images/ui/window_icon.png"
define config.default_text_cps = 35
# 8.5.3 applies this only to a fresh profile, preserving existing settings.
define config.default_afm_time = 15
define config.default_music_volume = 0.38
define config.has_voice = False
define config.has_music = True
define config.has_sound = False
define config.history_length = 250
define config.main_menu_music = "audio/festival.ogg"
define config.rollback_enabled = True
define config.autosave_on_choice = True
define config.autosave_slots = 6
define config.check_conflicting_properties = True
define config.thumbnail_width = 320
define config.thumbnail_height = 180
define build.name = "SenToManKen"
define build.version = "0.20.0"

init python:
    config.overlay_screens.append("quick_menu")
    build.classify("tests/**", None)
    build.classify("userdata/**", None)
    build.classify("game/testcases*.rpy", None)
    build.classify("game/testcases*.rpyc", None)
    build.classify("game/testcases.rpy", None)
    build.classify("game/testcases.rpyc", None)
    build.classify("game/saves/**", None)
    build.classify("game/cache/**", None)
    build.classify("**/__pycache__/**", None)
    build.classify("game/python-packages/**.py", "all")
    build.classify("game/story_data/**.json", "all")
    build.classify("game/audio/licensed/**.mp3", "all")
    build.classify("game/audio/licensed/LICENSE*", "all")
    build.classify("game/audio/licensed/v17_MUSIC_LICENSES.json", "all")
    build.classify("game/audio/licensed/v17_CREDITS.txt", "all")
    build.classify("**.log", None)
    build.classify("game/fonts/*LICENSE.txt", "all")
    build.classify("game/**.otf", "all")
    build.classify("**.txt", None)
    build.classify("**.json", None)
    build.classify("**.md", None)
    build.classify("**.png", "all")
    build.classify("game/**.rpy", "all")
    build.classify("game/**.rpyc", "all")
    build.classify("game/**.ttf", "all")
    build.classify("game/**.ogg", "all")
    build.classify("game/**.webm", "all")

default persistent.cg_moon = False
default persistent.cg_gpt = False
default persistent.cg_claude = False
default persistent.cg_grok = False
default persistent.cg_hug = False
default persistent.end_love = False
default persistent.end_wait = False
default persistent.end_friend = False
default affinity = 0
default chapter = "初见  /  祭典之前"
default ending_name = ""
default ending_note = ""
default quick_menu = True

init python:
    def choose_ending(score, promise):
        if promise and score >= 4:
            return "love"
        if score >= 2:
            return "wait"
        return "friend"

    def unlock_cg(key):
        setattr(persistent, "cg_" + key, True)
        renpy.save_persistent()

image bg shrine = Transform("images/deepseek_shrine.png", xysize=(1280, 720))
image bg moon = Transform("images/deepseek_moon.png", xysize=(1280, 720))
image bg gpt = Transform("images/gpt_candle.png", xysize=(1280, 720))
image bg claude = Transform("images/claude_window.png", xysize=(1280, 720))
image bg grok = Transform("images/grok_festival.png", xysize=(1280, 720))
image bg hug = Transform("images/lantern_hug.png", xysize=(1280, 720))

define ds = Character("DeepSeek", color="#a7d9ff")
define gpt = Character("GPT", color="#e0d6ff")
define cl = Character("Claude", color="#ffca9e")
define gr = Character("Grok", color="#f1cf83")
define you = Character("你", color="#e6efe9")

define build.directory_name = "SenToManKen-0.20.0"
