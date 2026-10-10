# 原生 Ren'Py 呈现：使用生成 PNG 原文件，裁切仅发生在显示时。
default persistent.reduce_motion = False
default deepseek_expression = 'neutral'
default minimax_pose = 'neutral'

init -7 python:
    import math
    SPRITE_ROLES = ('deepseek', 'gpt', 'claude', 'grok', 'minimax', 'kimi',
                    'gemini', 'qwen', 'glm', 'opencode', 'zcode')
    SPEECH_ROLES = {
        'DeepSeek': 'deepseek', '大肥鱼': 'deepseek', '蓝色大肥鱼': 'deepseek',
        'GPT': 'gpt', 'ChatGPT': 'gpt', 'GPT娘': 'gpt',
        'Claude': 'claude', 'Claude娘': 'claude',
        'Grok': 'grok', 'Grok娘': 'grok',
        'MiniMax': 'minimax', 'MiniMax娘': 'minimax',
        'Kimi': 'kimi', 'Kimi娘': 'kimi',
        'Gemini': 'gemini', 'Gemini娘': 'gemini',
        'Qwen': 'qwen', '通义千问': 'qwen', '千问': 'qwen',
        'GLM': 'glm', '智谱': 'glm', '智谱娘': 'glm',
        'OpenCode': 'opencode', 'OpenCode娘': 'opencode',
        'ZCode': 'zcode', 'ZCode娘': 'zcode',
    }

    def sprite_file(role, pose='neutral'):
        role = str(role).lower()
        if role not in SPRITE_ROLES:
            raise ValueError('Unknown sprite role')
        valid_poses = {
            'deepseek': ('neutral','rice','shy','determined','annoyed','sleepy','happy','offer_rice','fix_lamp','shy_wave','summer','yukata','caught_turn','rice_proud'),
            'minimax': ('neutral','camera_shy'),
        }
        if pose not in valid_poses.get(role, ('neutral',)):
            pose = 'neutral'
        if not renpy.loadable('images/sprites/{}_{}.png'.format(role, pose)):
            pose = 'neutral'
        return 'images/sprites/{}_{}.png'.format(role, pose)

    def deepseek_body(pose):
        # Display normalization preserves the generated PNG and its alpha.
        return Transform(sprite_file('deepseek', pose), xysize=(941, 1672), fit='contain')

    def ai_display_pose(role, mood):
        if role != 'deepseek':
            return 'neutral'
        return {'happy':'happy', 'shy':'shy', 'serious':'determined', 'angry':'annoyed'}.get(mood, 'neutral')

    def speech_role(who):
        if not who:
            return None
        value = renpy.filter_text_tags(str(who), allow=[])
        return SPEECH_ROLES.get(value, value.lower() if value.lower() in SPRITE_ROLES else None)

    def speaker_portrait(role):
        pose = deepseek_expression if role == 'deepseek' else minimax_pose if role == 'minimax' else 'neutral'
        return Transform(sprite_file(role, pose), crop=(0.13, 0.0, 0.74, 0.34),
                         crop_relative=True, xysize=(262, 206), fit='contain')

    def sprite_breath_update(trans, st, at):
        # The unchanged entry transform owns the base offset of 102 pixels.
        trans.yoffset = 0 if persistent.reduce_motion else -1.5 * (1.0 - math.cos(st * math.pi / 2.1))
        return None if persistent.reduce_motion else 0.04

    def sprite_breath_rest(trans, st, at):
        trans.yoffset = 0
        return None

    def sprite_breathe_with_child(position, child):
        entering = sprite_breathe_entry(position, child=child)
        moving = Transform(entering, function=sprite_breath_update)
        still = Transform(entering, function=sprite_breath_rest)
        # ConditionSwitch reselects on interaction, including preference toggles.
        # Python Transform functions returning None can run again when selected;
        # an ATL function statement returning None would instead finish forever.
        return ConditionSwitch('persistent.reduce_motion', still,
                               'True', moving, predict_all=True)

    sprite_breathe = renpy.curry(sprite_breathe_with_child)

    class DialogueBand(renpy.Displayable):
        def render(self, width, height, st, at):
            width, height = max(1, int(width)), max(1, int(height))
            result = renpy.Render(width, height)
            canvas = result.canvas()
            for y in range(0, height, 4):
                t = float(y) / max(1, height - 1)
                rgba = [int(a + (b-a)*t) for a,b in zip((115,68,104,199),(52,36,63,242))]
                canvas.rect('#{:02x}{:02x}{:02x}{:02x}'.format(*rgba), (0, y, width, min(4,height-y)))
            canvas.line('#ffdbedb0', (0,2), (width,2), 1)
            canvas.line('#c789b682', (0,7), (width,7), 1)
            canvas.line('#f0bdd05c', (0,height-35), (width,height-35), 1)
            for x in range(16, width, 40):
                canvas.polygon('#f6c8dc2a', [(x,14),(x+3,17),(x,20),(x-3,17)])
            return result

    class ChapterRibbon(renpy.Displayable):
        def render(self, width, height, st, at):
            width,height=max(1,int(width)),max(1,int(height))
            result=renpy.Render(width,height)
            canvas=result.canvas()
            canvas.polygon('#ba6a85ec', [(0,0),(width-22,0),(width,height//2),(width-22,height),(0,height)])
            canvas.line('#ffdaeab0',(0,3),(width-25,3),1)
            canvas.line('#602a5466',(0,height-3),(width-25,height-3),1)
            return result

image bg echo = Transform('images/original/echo_shrine.png', xysize=(1280,720), fit='cover')
image bg echo morning = Transform('images/original/echo_shrine_morning.png', xysize=(1280,720), fit='cover')
image cg rice_break = Transform('images/original/rice_break.png', xysize=(1280,720), fit=('contain' if TOK_MOBILE else 'cover'))
image sprite deepseek = deepseek_body('neutral')
image sprite deepseek rice = deepseek_body('rice')
image sprite deepseek shy = deepseek_body('shy')
image sprite deepseek determined = deepseek_body('determined')
image sprite deepseek annoyed = deepseek_body('annoyed')
image sprite deepseek sleepy = deepseek_body('sleepy')
image sprite deepseek happy = deepseek_body('happy')
image sprite deepseek offer_rice = deepseek_body('offer_rice')
image sprite deepseek fix_lamp = deepseek_body('fix_lamp')
image sprite deepseek shy_wave = deepseek_body('shy_wave')
image sprite gpt = 'images/sprites/gpt_neutral.png'
image sprite claude = 'images/sprites/claude_neutral.png'
image sprite grok = 'images/sprites/grok_neutral.png'
image sprite minimax = 'images/sprites/minimax_neutral.png'
image sprite minimax camera_shy = Transform(sprite_file('minimax','camera_shy'),xysize=(941,1672),fit='contain')
image sprite kimi = 'images/sprites/kimi_neutral.png'
image sprite gemini = 'images/sprites/gemini_neutral.png'
image sprite qwen = 'images/sprites/qwen_neutral.png'
image sprite glm = 'images/sprites/glm_neutral.png'
image sprite opencode = 'images/sprites/opencode_neutral.png'
image sprite zcode = 'images/sprites/zcode_neutral.png'

transform sprite_stand(position=0.5):
    xalign position
    yalign 1.0
    zoom 0.48
    yoffset 102

transform sprite_enter(position=0.5):
    xalign position
    yalign 1.0
    zoom 0.48
    yoffset 102
    alpha (1.0 if persistent.reduce_motion else 0.0)
    xoffset (0 if persistent.reduce_motion else 28)
    ease (0.0 if persistent.reduce_motion else 0.32) alpha 1.0 xoffset 0

transform sprite_breathe_entry(position=0.5):
    xalign position
    yalign 1.0
    zoom 0.48
    yoffset 102
    alpha (1.0 if persistent.reduce_motion else 0.0)
    xoffset (0 if persistent.reduce_motion else 18)
    ease (0.0 if persistent.reduce_motion else 0.28) alpha 1.0 xoffset 0

transform sprite_dim:
    matrixcolor BrightnessMatrix(-0.12)

transform sprite_focus:
    matrixcolor BrightnessMatrix(0.0)
