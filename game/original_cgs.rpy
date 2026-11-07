default persistent.cg_claude_river_confess = False
default persistent.cg_claude_river_relax = False
default persistent.cg_kimi_moon_offer = False
default persistent.cg_kimi_moon_lean = False
default persistent.cg_ds_tipsy_wait = False
default persistent.cg_ds_tipsy_pounce = False
default persistent.cg_kimi_notebook_press = False
default persistent.cg_kimi_wish_reclaim = False
default persistent.cg_claude_poster_hold = False
default persistent.cg_claude_poster_stop = False
default persistent.cg_kimi_private_map = False
default persistent.cg_kimi_private_map_offer = False
default persistent.cg_claude_wet_book_warn = False
default persistent.cg_claude_wet_book = False
default persistent.cg_ds_cooldown_exchange = False
default persistent.cg_ds_birth = False
default persistent.cg_ds_other_hand = False
default persistent.cg_minimax_take_lookback = False
default persistent.cg_garden_chart_turn = False
default persistent.cg_garden_chart_support = False
default persistent.cg_cart_repair_retry = False
default persistent.cg_rice_break_caught = False
default persistent.cg_ds_rest_awake = False
default persistent.cg_gpt_self_laugh = False
default persistent.cg_gpt_self_quiet = False
default persistent.cg_minimax_take = False
default persistent.cg_garden_chart = False
default persistent.cg_cart_repair = False

default persistent.cg_gpt_shared_drawing = False
default persistent.cg_grok_after_close = False

init -6 python:
    ORIGINAL_CGS = [
        dict(id='minimax_take', title='拍的人也在画面里', file='images/original/cg_minimax_take_vn.png', flag='cg_minimax_take'),
        dict(id='garden_chart', title='星图与未开的花', file='images/original/cg_garden_chart_vn.png', flag='cg_garden_chart'),
        dict(id='cart_repair', title='修好一辆车，留下一把凳子', file='images/original/cg_cart_repair_vn_clean.png', flag='cg_cart_repair'),
        dict(id='rice_break', title='一碗饭还没藏好', file='images/original/rice_break.png', flag='rice_cg_seen'),
        dict(id='moon', title='月下浴衣', file='images/deepseek_moon.png', flag='cg_moon'),
        dict(id='gpt', title='烛光里的GPT', file='images/gpt_candle.png', flag='cg_gpt'),
        dict(id='claude', title='窗边的Claude', file='images/claude_window.png', flag='cg_claude'),
        dict(id='claude_poster_hold', title='更正·压纸', file='images/original/cg_claude_poster_hold.png', flag='cg_claude_poster_hold'),
        dict(id='claude_poster_stop', title='更正·叫停', file='images/original/cg_claude_poster_stop.png', flag='cg_claude_poster_stop'),
        dict(id='claude_wet_book', title='书页里的余温', file='images/original/cg_claude_wet_book.png', flag='cg_claude_wet_book'),
        dict(id='claude_wet_book_warn', title='护书差分 · 先看这一页', file='images/original/cg_claude_wet_book_warn.png', flag='cg_claude_wet_book_warn'),
        dict(id='kimi_notebook_press',title='愿签·收册',file='images/original/cg_kimi_notebook_press.png',flag='cg_kimi_notebook_press'),
        dict(id='kimi_wish_reclaim',title='愿签·取回',file='images/original/cg_kimi_wish_reclaim.png',flag='cg_kimi_wish_reclaim'),
        dict(id='kimi_private_map', title='今天的路，画到这里', file='images/original/cg_kimi_private_map.png', flag='cg_kimi_private_map'),
        dict(id='kimi_private_map_offer', title='私人地图差分 · 抬眼递笔', file='images/original/cg_kimi_private_map_offer.png', flag='cg_kimi_private_map_offer'),
        dict(id='grok', title='Grok的祭典邀约', file='images/grok_festival.png', flag='cg_grok'),
        dict(id='hug', title='花灯有回音', file='images/lantern_hug.png', flag='cg_hug'),
        dict(id='ds_rest', title='今天这份休息，分给你', file='images/original/cg_ds_rest.png', flag='cg_ds_rest'),
        dict(id='ds_rain', title='先吃饭，再可靠', file='images/original/cg_ds_rain.png', flag='cg_ds_rain'),
        dict(id='ds_confession', title='想分给你的明天', file='images/original/cg_ds_confession.png', flag='cg_ds_confession'),
        dict(id='ds_cooldown', title='再凉五分钟', file='images/original/cg_ds_cooldown.png', flag='cg_ds_cooldown'),
        dict(id='ds_cooldown_exchange', title='点心差分 · 交换这一口', file='images/original/cg_ds_cooldown_exchange.png', flag='cg_ds_cooldown_exchange'),
        dict(id='ds_yukata', title='这次夸得太直白了', file='images/original/cg_ds_yukata.png', flag='cg_ds_yukata'),
        dict(id='ds_pool', title='大肥鱼也要练习', file='images/original/cg_ds_pool.png', flag='cg_ds_pool'),
        dict(id='ds_close', title='今天不用急着回去', file='images/original/cg_ds_close.png', flag='cg_ds_close'),
        dict(id='ds_outerwear_worn', title='外衣差分 · 还没解开的结', file='images/original/cg_ds_outerwear_worn.png', flag='cg_ds_outerwear_worn'),
        dict(id='ds_outerwear', title='外衣差分 · 衣带交给你', file='images/original/cg_ds_outerwear.png', flag='cg_ds_outerwear'),
        dict(id='ds_outerwear_turn', title='外衣差分 · 回头确认一眼', file='images/original/cg_ds_outerwear_turn.png', flag='cg_ds_outerwear_turn'),
        dict(id='ds_hug_pov', title='接住这条大肥鱼', file='images/original/cg_ds_hug_pov.png', flag='cg_ds_hug_pov'),
        dict(id='ds_evening_tea', title='今晚的第二杯茶', file='images/original/cg_ds_evening_tea.png', flag='cg_ds_evening_tea'),
        dict(id='gpt_self_laugh', title='自画像差分 · 笑得太快', file='images/original/cg_gpt_self_laugh.png', flag='cg_gpt_self_laugh'),
        dict(id='gpt_self_quiet', title='自画像差分 · 正在选下一笔', file='images/original/cg_gpt_self_quiet.png', flag='cg_gpt_self_quiet'),
        dict(id='rice_break_caught', title='偷饭差分 · 被发现了', file='images/original/cg_rice_break_caught.png', flag='cg_rice_break_caught'),
        dict(id='ds_rest_awake', title='午睡差分 · 比你早一点', file='images/original/cg_ds_rest_awake.png', flag='cg_ds_rest_awake'),
        dict(id='fan_deepseek_01', title='水里那块石头', file='images/original/cg_fan_deepseek_01.png', flag='cg_fan_deepseek_01'),
        dict(id='ds_wedding', title='两只碗，今天算一桌', file='images/original/cg_ds_wedding.png', flag='cg_ds_wedding'),
        dict(id='ds_family', title='第三只小碗', file='images/original/cg_ds_family.png', flag='cg_ds_family'),
        dict(id='gpt_shared_drawing', title='共同自画像 · 留着这条线', file='images/original/cg_gpt_shared_drawing.png', flag='cg_gpt_shared_drawing'),
        dict(id='grok_after_close', title='散场以后 · 伸过来的手', file='images/original/cg_grok_after_close.png', flag='cg_grok_after_close'),
        dict(id='ds_birth', title='小满来到的早晨', file='images/original/cg_ds_birth.png', flag='cg_ds_birth'),
        dict(id='ds_other_hand', title='那只牵着别人的手', file='images/original/cg_ds_other_hand.png', flag='cg_ds_other_hand'),
        dict(id='minimax_take_lookback', title='拍摄差分 · 先确认镜头', file='images/original/cg_minimax_take_lookback.png', flag='cg_minimax_take_lookback'),
        dict(id='garden_chart_turn', title='星图差分 · 转了半圈', file='images/original/cg_garden_chart_turn.png', flag='cg_garden_chart_turn'),
        dict(id='garden_chart_support', title='花盆差分 · 托稳另一侧', file='images/original/cg_garden_chart_support.png', flag='cg_garden_chart_support'),
        dict(id='cart_repair_retry', title='修车差分 · 拆回原轮', file='images/original/cg_cart_repair_retry.png', flag='cg_cart_repair_retry'),
        dict(id='ds_tipsy_wait',title='微醺小夜曲 · 等你坐近',file='images/original/cg_ds_tipsy_wait.png',flag='cg_ds_tipsy_wait'),
        dict(id='ds_tipsy_pounce',title='微醺小夜曲 · 靠垫接住笑声',file='images/original/cg_ds_tipsy_pounce.png',flag='cg_ds_tipsy_pounce'),
        dict(id='claude_river_confess', title='河边告白 · 想靠近是真的', file='images/original/cg_claude_river_confess.png', flag='cg_claude_river_confess'),
        dict(id='claude_river_relax', title='河边告白 · 比草稿难一点', file='images/original/cg_claude_river_relax.png', flag='cg_claude_river_relax'),
        dict(id='kimi_moon_offer', title='月下邀请 · 等你回答', file='images/original/cg_kimi_moon_offer.png', flag='cg_kimi_moon_offer'),
        dict(id='kimi_moon_lean', title='月下邀请 · 坐近一点', file='images/original/cg_kimi_moon_lean.png', flag='cg_kimi_moon_lean'),
    ]
    def original_cg_by_id(key):
        for cg in ORIGINAL_CGS:
            if cg['id'] == key:
                return cg
        raise ValueError('Unknown original CG')
    def original_cg_unlocked(cg):
        return bool(getattr(persistent, cg['flag'], False))

    def original_cg_short_title(cg):
        if cg['id'].startswith('opening_') or (cg['id'].startswith('fan_') and cg['id'].endswith(('_ending','_swim','_mishap','_kiss'))): return cg['title']
        if cg['id']=='claude_river_confess': return '告白·抬眼'
        if cg['id']=='claude_river_relax': return '告白·松肩'
        if cg['id']=='kimi_moon_offer': return '月下·掌心'
        if cg['id']=='kimi_moon_lean': return '月下·坐近'
        if cg['id']=='ds_tipsy_wait': return '微醺·等你坐近'
        if cg['id']=='ds_tipsy_pounce': return '轻抱·靠垫笑声'
        if cg['id']=='gpt_shared_drawing': return '共同自画像'
        if cg['id']=='grok_after_close': return '散场以后'
        if cg['id']=='ds_birth': return '小满的早晨'
        if cg['id']=='ds_other_hand': return '另一只手'
        return {'minimax_take':'拍的人也在','garden_chart':'星图与晚兰','cart_repair':'米车与凳子',
                'rice_break':'藏不住的饭','moon':'月下浴衣','gpt':'烛光GPT',
                'claude':'窗边Claude','grok':'祭典Grok','hug':'花灯有回音',
                'ds_rest':'河堤轮休','ds_rain':'廊下热饭','ds_confession':'鲸灯与明天',
                'ds_cooldown':'再凉五分钟','ds_cooldown_exchange':'点心·交换','ds_yukata':'浴衣与真心话','ds_pool':'大肥鱼练泳','ds_close':'靠近一点',
                'ds_outerwear_worn':'外衣·衣结','ds_outerwear':'外衣·解带','ds_outerwear_turn':'外衣·回头','ds_hug_pov':'接住大肥鱼','ds_evening_tea':'第二杯茶','gpt_self_laugh':'自画像·笑','gpt_self_quiet':'自画像·静','rice_break_caught':'偷饭·发现','ds_rest_awake':'午睡·醒来','fan_deepseek_01':'浅水同行','ds_wedding':'两只碗·婚礼','ds_family':'第三只小碗',
                'minimax_take_lookback':'拍摄·回头','garden_chart_turn':'星图·转纸','garden_chart_support':'花盆·托稳','cart_repair_retry':'修车·拆回',
                'claude_wet_book':'雨后护书','claude_wet_book_warn':'护书·提醒',
                'kimi_private_map':'树影·添圈','kimi_private_map_offer':'树影·递笔',
                'claude_poster_hold':'更正·压纸','claude_poster_stop':'更正·叫停',
                'kimi_notebook_press':'愿签·收册','kimi_wish_reclaim':'愿签·取回',
                'v20_ds01_sort':'十分钟小盒','v20_ds01_rest_plan':'先空一段','v20_ds01_hairclip':'别拔夹子',
                'v20_c01_safe_connect':'安全连接'
            }.get(cg['id'], cg['title'])

    def original_cg_role(cg):
        key=cg['id']
        if key.startswith(('opening_','v20_c')): return 'common'
        if key in ('minimax_take','minimax_take_lookback','garden_chart','garden_chart_turn','garden_chart_support','cart_repair','cart_repair_retry','rice_break','rice_break_caught'): return 'common'
        if key.startswith(('ds_','fan_deepseek_','v20_ds')) or key in ('moon','hug'):return 'deepseek'
        if key.startswith('gpt'):return 'gpt'
        if key.startswith('grok'):return 'grok'
        if key.startswith('claude_'):return 'claude'
        if key.startswith('kimi_'):return 'kimi'
        if key.startswith('fan_'): return key.split('_')[1]
        return key

    def gallery_role_filters():
        return [('all','全部'),('common','共通')]+[(r['id'],r['name']) for r in LONG_ROUTES]

    def gallery_filtered_cgs(role,only_seen):
        return [c for c in ORIGINAL_CGS if (role=='all' or original_cg_role(c)==role) and (not only_seen or original_cg_unlocked(c))]

    def original_cg_variants(key):
        groups=[(('ds_outerwear_worn','穿好'),('ds_outerwear','解带'),('ds_outerwear_turn','回头')),
                (('gpt_self_laugh','笑出声'),('gpt_self_quiet','安静侧脸')),
                (('rice_break','吃饭'),('rice_break_caught','被发现')),
                (('ds_rest','午睡'),('ds_rest_awake','醒来')),
                (('ds_cooldown','尝一口'),('ds_cooldown_exchange','递近碗')),
                (('minimax_take','站稳'),('minimax_take_lookback','回头')),
                (('garden_chart','初见'),('garden_chart_turn','转纸'),('garden_chart_support','托盆')),
                (('cart_repair','装轮'),('cart_repair_retry','拆回')),
                (('claude_wet_book','护书'),('claude_wet_book_warn','提醒')),
                (('kimi_private_map','添圈'),('kimi_private_map_offer','递笔')),
                (('claude_poster_hold','压纸'),('claude_poster_stop','叫停')),
                (('kimi_notebook_press','收册'),('kimi_wish_reclaim','取签')),
                (('ds_tipsy_wait','等你坐近'),('ds_tipsy_pounce','换衣后轻抱')),
                (('claude_river_confess','开口'),('claude_river_relax','松肩')),
                (('kimi_moon_offer','掌心'),('kimi_moon_lean','支凳'))]
        return next((group for group in groups if key in [i[0] for i in group]),())

    def original_cg_picture(cg, size=(1280,720)):
        picture = Transform(cg['file'], xysize=(1280,720), fit=('contain' if TOK_MOBILE else 'cover'))
        if cg['id'] in ('minimax_take','minimax_take_lookback'):
            # Text belongs to the game UI; the generated original stays intact.
            picture = Composite((1280,720),
                (0,0), picture,
                (324,414), Text('R18',font='fonts/SourceHanSerifCN-SemiBold.otf',size=48,color='#e6c786',outlines=[(1,'#664b29',0,1)]),
                (340,474), Text('18:00',font='fonts/SourceHanSansCN-Regular.otf',size=21,color='#e6c786'))
        return Transform(picture, xysize=size, fit='contain')

image cg minimax_take = original_cg_picture(original_cg_by_id('minimax_take'))
image cg garden_chart = Transform('images/original/cg_garden_chart_vn.png', xysize=(1280,720), fit=('contain' if TOK_MOBILE else 'cover'))
image cg cart_repair = Transform('images/original/cg_cart_repair_vn_clean.png', xysize=(1280,720), fit=('contain' if TOK_MOBILE else 'cover'))

screen original_cg_gallery():
    tag menu
    default selected_cg = next((c['id'] for c in ORIGINAL_CGS if original_cg_unlocked(c)), 'rice_break')
    default cg_filter = 'all'
    default cg_only_seen = False
    default cg_choose_role = False
    default cg_scroll = ui.adjustment()
    $ visible_cgs = gallery_filtered_cgs(cg_filter, cg_only_seen)
    $ chosen = next((c for c in visible_cgs if c['id'] == selected_cg), next(iter(visible_cgs),None))
    $ selected_cg = chosen['id'] if chosen else None
    $ opened = bool(chosen and original_cg_unlocked(chosen))
    use game_menu('回忆手帐 / CG鉴赏'):
        vbox:
            spacing 12
            hbox:
                spacing 15
                text ('已收藏 '+str(sum(original_cg_unlocked(c) for c in ORIGINAL_CGS))+' / '+str(len(ORIGINAL_CGS))) size 20 color '#49384F' yalign 0.5
                textbutton ('角色 / '+dict(gallery_role_filters())[cg_filter]) id 'cg_filter_role' action SetScreenVariable('cg_choose_role',True) xsize 240 text_size 19
                textbutton '只看已收藏' id 'cg_filter_seen' action [ToggleScreenVariable('cg_only_seen'), Function(cg_scroll.change,0)] selected cg_only_seen text_size 19
                textbutton '清除筛选' id 'cg_filter_clear' action [SetScreenVariable('cg_filter','all'), SetScreenVariable('cg_only_seen',False),Function(cg_scroll.change,0)] text_size 19
            hbox:
                spacing 24
                vbox:
                    xsize 496
                    spacing 12
                    frame:
                        background SoftPanel('#f8eee9','#c397b2',12)
                        xsize 496
                        ysize 290
                        padding (7,7)
                        if opened:
                            add original_cg_picture(chosen,(482,271)) align (0.5,0.5)
                        else:
                            text ('这一页，还等着与你相遇。' if chosen else '暂无符合筛选的回忆。') size 22 color '#956d85' align (0.5,0.5)
                    text (chosen['title'] if opened else '未发现的回忆' if chosen else '换个角色，或清除筛选') size 26 color '#49384F' xmaximum 496
                    if chosen:
                        text ('共通篇的回忆' if original_cg_role(chosen)=='common' else dict(gallery_role_filters())[original_cg_role(chosen)]+'的回忆') size 19 color '#796977'
                        $ variants = original_cg_variants(chosen['id'])
                        if variants:
                            hbox:
                                spacing 8
                                for state_id, state_name in variants:
                                    textbutton state_name id ('cg_variant_'+state_id) action SetScreenVariable('selected_cg',state_id) sensitive original_cg_unlocked(original_cg_by_id(state_id)) selected selected_cg == state_id xsize (145 if len(variants)==3 else 218) text_size 19
                    textbutton '全屏欣赏' id 'original_cg_open' action Show('original_cg_view',cg_key=selected_cg) sensitive opened xsize 230 text_size 21
                vbox:
                    xsize 419
                    spacing 14
                    text ('本次筛选 '+str(len(visible_cgs))+' 张 / 动作差分分别收藏') size 17 color '#796977'
                    vpgrid:
                        cols 3
                        spacing 7
                        xsize 419
                        ysize 355
                        yadjustment cg_scroll
                        pagekeys True
                        arrowkeys False
                        mousewheel True
                        draggable True
                        for cg in visible_cgs:
                            $ seen = original_cg_unlocked(cg)
                            button:
                                id ('original_cg_'+cg['id'])
                                action SetScreenVariable('selected_cg',cg['id'])
                                selected selected_cg == cg['id']
                                xsize 135
                                ysize 113
                                padding (5,5)
                                background SoftPanel('#f5e8e5','#ad819a',7)
                                hover_background SoftPanel('#f9dce8','#e1a7c7',7)
                                selected_background SoftPanel('#f9dce8','#e1a7c7',7)
                                vbox:
                                    spacing 5
                                    fixed:
                                        xsize 125
                                        ysize 70
                                        if seen:
                                            add original_cg_picture(cg,(125,70))
                                        else:
                                            add Solid('#e4d4dd')
                                            text '未解锁' align (0.5,0.5) size 15 color '#73576b'
                                    text (original_cg_short_title(cg) if seen else '尚未相遇') size 14 color '#72566b' xmaximum 125
                        for empty in range((-len(visible_cgs)) % 3):
                            null width 135 height 113
                    text '经过真实剧情后收藏。尚在策划的图片不会显示或解锁。' size 18 color '#796977' xmaximum 419 line_spacing 4
    if cg_choose_role:
        key 'game_menu' action SetScreenVariable('cg_choose_role',False)
        add Solid('#151022c9')
        button:
            xysize (1280,720)
            background None
            hover_background None
            action SetScreenVariable('cg_choose_role',False)
        frame:
            align (0.5,0.5)
            xsize 850
            padding (26,25)
            background SoftPanel('#fcf2ee','#ba7597',15)
            vbox:
                spacing 16
                text '选择回忆里的角色' size 29 color '#512d53'
                vpgrid:
                    cols 3
                    spacing 9
                    xsize 795
                    ysize 310
                    pagekeys True
                    arrowkeys False
                    mousewheel True
                    draggable True
                    for role_id, role_name in gallery_role_filters():
                        textbutton role_name id ('cg_filter_'+role_id) style 'navigation_button' action [SetScreenVariable('cg_filter',role_id),SetScreenVariable('cg_choose_role',False), Function(cg_scroll.change,0)] selected cg_filter == role_id xsize 257 ysize 50 text_size 21 text_color '#653657' background SoftPanel('#f0d7e3','#b57d98',10)
                    for empty in range((-len(gallery_role_filters()))%3):
                        null width 257 height 50
                textbutton '返回鉴赏' id 'cg_filter_cancel' style 'navigation_button' action SetScreenVariable('cg_choose_role',False) text_color '#653657' text_size 21 background SoftPanel('#f0d7e3','#b57d98',10)

screen original_cg_view(cg_key):
    modal True
    zorder 300
    default displayed_key = cg_key
    $ cg = original_cg_by_id(displayed_key)
    if original_cg_unlocked(cg):
        add story_cg_picture(cg)
    else:
        add Solid('#FFF7F1')
        text '这页尚未收藏。' align (0.5,0.5) size 28 color TOK_UI_INK
    $ full_variants = original_cg_variants(displayed_key)
    if full_variants:
        hbox:
            xpos 30
            ypos 660
            spacing 12
            for state_id, state_name in full_variants:
                textbutton state_name id ('full_cg_variant_'+state_id) action SetScreenVariable('displayed_key',state_id) sensitive original_cg_unlocked(original_cg_by_id(state_id)) selected displayed_key == state_id text_size 20 background Solid('#FFF7F1f2')
    frame:
        xpos 24
        ypos 18
        xmaximum 780
        padding (14, 9)
        background SoftPanel('#FFF7F1ee', '#DEC2CF', 10)
        text cg['title'] size 22 xmaximum 748 color TOK_UI_INK
    if cg['id'] in CG_MOTION_KEYS + DYNAMIC_CG_KEYS and original_cg_unlocked(cg):
        textbutton (('眨眼微笑 / 开' if dynamic_cg_enabled_for(cg['id']) else '眨眼微笑 / 关') if cg['id'] in DYNAMIC_CG_KEYS else ('轻动效 / 开' if cg_motion_enabled_for(cg['id']) else '轻动效 / 关')) id 'full_cg_motion_toggle' action ToggleField(persistent,'cg_motion_enabled') xpos 846 ypos 21 xsize 193 text_size 20 background Solid('#FFF7F1f2')
    textbutton '返回CG鉴赏' id 'original_cg_close' action Hide('original_cg_view') xpos 1060 ypos 21 xsize 190 text_size 20 background Solid('#FFF7F1f2')
    key 'game_menu' action Hide('original_cg_view')

image cg minimax_take_lookback = original_cg_picture(original_cg_by_id('minimax_take_lookback'))

image cg garden_chart_turn = original_cg_picture(original_cg_by_id('garden_chart_turn'))

image cg garden_chart_support = original_cg_picture(original_cg_by_id('garden_chart_support'))

image cg cart_repair_retry = original_cg_picture(original_cg_by_id('cart_repair_retry'))
