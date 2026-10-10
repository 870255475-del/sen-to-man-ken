# v16 独立结局CG番外候选。仅标题Function入口；不计长篇节点、好感或周目。
# 所有人30岁；每人一张完整遮挡、非透明的独立CG，玩家身体不出画。
# 仅已有完整恋人结局收藏的DS/GPT/Grok开放。其他8篇预写并锁定。

default persistent.cg_fan_deepseek_ending = False
default persistent.cg_fan_gpt_ending = False
default persistent.cg_fan_claude_ending = False
default persistent.cg_fan_grok_ending = False
default persistent.cg_fan_minimax_ending = False
default persistent.cg_fan_kimi_ending = False
default persistent.cg_fan_gemini_ending = False
default persistent.cg_fan_qwen_ending = False
default persistent.cg_fan_glm_ending = False
default persistent.cg_fan_opencode_ending = False
default persistent.cg_fan_zcode_ending = False
default persistent.ending_cg_deepseek_seen = False
default persistent.ending_cg_gpt_seen = False
default persistent.ending_cg_claude_seen = False
default persistent.ending_cg_grok_seen = False
default persistent.ending_cg_minimax_seen = False
default persistent.ending_cg_kimi_seen = False
default persistent.ending_cg_gemini_seen = False
default persistent.ending_cg_qwen_seen = False
default persistent.ending_cg_glm_seen = False
default persistent.ending_cg_opencode_seen = False
default persistent.ending_cg_zcode_seen = False

default ending_cg_active = False
default ending_cg_current_role = ''
default ending_cg_displayed = False
default ending_cg_finished = False

init -5 python:
    ENDING_CG_EPISODES = (
        dict(role='deepseek', name='DeepSeek', title='饭碗先坐好了'),
        dict(role='gpt', name='GPT', title='这张画还不许挂'),
        dict(role='claude', name='Claude', title='合上书以后的一句'),
        dict(role='grok', name='Grok', title='梳子没有夜班'),
        dict(role='minimax', name='MiniMax', title='红灯已经熄了'),
        dict(role='kimi', name='Kimi', title='今天不添一行'),
        dict(role='gemini', name='Gemini', title='枕头也会认错星'),
        dict(role='qwen', name='Qwen', title='这一页先压好'),
        dict(role='glm', name='GLM', title='毛巾只借半边'),
        dict(role='opencode', name='OpenCode', title='工具盒今晚先休息'),
        dict(role='zcode', name='ZCode', title='枕边的信不必寄'),
    )
    ENDING_EXTRA_CGS = [
        dict(id='fan_deepseek_ending',title='饭碗先坐好了',file='images/original/cg_fan_deepseek_ending.png',flag='cg_fan_deepseek_ending'),
        dict(id='fan_gpt_ending',title='这张画还不许挂',file='images/original/cg_fan_gpt_ending.png',flag='cg_fan_gpt_ending'),
        dict(id='fan_claude_ending',title='合上书以后的一句',file='images/original/cg_fan_claude_ending.png',flag='cg_fan_claude_ending'),
        dict(id='fan_grok_ending',title='梳子没有夜班',file='images/original/cg_fan_grok_ending.png',flag='cg_fan_grok_ending'),
        dict(id='fan_minimax_ending',title='红灯已经熄了',file='images/original/cg_fan_minimax_ending.png',flag='cg_fan_minimax_ending'),
        dict(id='fan_kimi_ending',title='今天不添一行',file='images/original/cg_fan_kimi_ending.png',flag='cg_fan_kimi_ending'),
        dict(id='fan_gemini_ending',title='枕头也会认错星',file='images/original/cg_fan_gemini_ending.png',flag='cg_fan_gemini_ending'),
        dict(id='fan_qwen_ending',title='这一页先压好',file='images/original/cg_fan_qwen_ending.png',flag='cg_fan_qwen_ending'),
        dict(id='fan_glm_ending',title='毛巾只借半边',file='images/original/cg_fan_glm_ending.png',flag='cg_fan_glm_ending'),
        dict(id='fan_opencode_ending',title='工具盒今晚先休息',file='images/original/cg_fan_opencode_ending.png',flag='cg_fan_opencode_ending'),
        dict(id='fan_zcode_ending',title='枕边的信不必寄',file='images/original/cg_fan_zcode_ending.png',flag='cg_fan_zcode_ending'),
    ]
    # 既有init -6建立ORIGINAL_CGS；只追加11项，旧47与root新增4项不动。
    ORIGINAL_CGS.extend(ENDING_EXTRA_CGS)

init -2 python:
    import copy as ending_cg_copy
    ENDING_CG_LOVE_FLAGS = dict(deepseek='main_ds_love', gpt='main_gpt_love', grok='main_grok_love')
    ENDING_CG_ROUTE_PREFIXES = ('ds_', 'ds1', 'ds2', 'ds3', 'ds4', 'ds5', 'ds6', 'ds7', 'ds8',
        'deepseek', 'gpt', 'grok', 'claude', 'kimi', 'minimax', 'gemini', 'qwen', 'glm', 'opencode', 'zcode')

    def ending_cg_item(role):
        return next((item for item in ENDING_CG_EPISODES if item['role']==role), None)

    def ending_cg_asset_ready(role):
        item = ending_cg_item(role)
        if not item:
            return False
        key = 'fan_' + role + '_ending'
        cg = next((entry for entry in ORIGINAL_CGS if entry['id']==key), None)
        return bool(cg and cg['flag']=='cg_'+key
            and cg['file']=='images/original/cg_'+key+'.png' and renpy.loadable(cg['file']))

    def ending_cg_title_context():
        return bool(getattr(store,'main_menu',False) and getattr(renpy.context(),'_main_menu',False)
            and not getattr(store,'ending_cg_active',False)
            and not getattr(store,'affection_special_active',False)
            and not getattr(store,'_in_replay',False)
            and not getattr(store,'secret_run_key','') and not getattr(store,'bad_run_key','')
            and not getattr(store,'secret_exploration',False) and not getattr(store,'town_preview_mode',False))

    def ending_cg_available(role):
        flag = ENDING_CG_LOVE_FLAGS.get(role)
        return bool(flag and getattr(persistent,flag,False) is True and ending_cg_title_context()
            and ending_cg_asset_ready(role) and renpy.has_label('ending_cg_story_'+role))

    def ending_cg_hint(role):
        if role not in ENDING_CG_LOVE_FLAGS:
            return '角色线尚未完结，图片已准备' if ending_cg_asset_ready(role) else '角色线尚未完结，图片准备中'
        if not ending_cg_asset_ready(role):
            return '图片准备中，暂不可进入'
        if getattr(persistent,ENDING_CG_LOVE_FLAGS[role],False) is not True:
            return '完成这位角色的恋人结局后开放'
        if not ending_cg_title_context():
            return '从标题进入，关闭后回到原页'
        return '独立恋人番外 · 不增加完整通关次数'

    def ending_cg_state_keys():
        # Copy route-local primitive state too; chapter7 answers are not route endings.
        local_names = tuple(name for name,value in vars(store).items()
            if name.startswith(ENDING_CG_ROUTE_PREFIXES)
            and isinstance(value,(str,int,float,bool,type(None),list,tuple,dict,set)))
        return tuple(dict.fromkeys(ENDING_STATE_KEYS + AFFECTION_STATE_KEYS + local_names + (
            'ending_snapshot','ending_music_snapshot','main_menu','ending_cg_active',
            'ending_cg_current_role','ending_cg_displayed','ending_cg_finished')))

    def ending_cg_prepare_context():
        names = ending_cg_state_keys()
        renpy.context_dynamic(*names)
        for name in names:
            if hasattr(store,name):
                setattr(store,name,ending_cg_copy.deepcopy(getattr(store,name)))
        # These are SDK Context flags; store.main_menu is a separate saved variable.
        renpy.context()._menu = False
        renpy.context()._main_menu = False
        store.main_menu = False
        store._menu = False
        store.suppress_overlay = False
        store.ending_cg_active = True
        store.ending_cg_displayed = False
        store.ending_cg_finished = False
        store.quick_menu = False
        store.main_cg = None
        store.hide_speaker_portrait = True

    def ending_cg_launch(role):
        # Function returns None, including every rejection; no menu dismissal or notify.
        if not ending_cg_available(role):
            return
        names = ending_cg_state_keys()
        saved = {name:ending_cg_copy.deepcopy(getattr(store,name)) for name in names if hasattr(store,name)}
        missing = tuple(name for name in names if not hasattr(store,name))
        parent_context = renpy.context()
        sdk_flags = {name:getattr(parent_context,name) for name in ('_menu','_main_menu') if hasattr(parent_context,name)}
        music = (list(renpy.music.get_loop(channel='music') or []),renpy.music.get_pause(channel='music'))
        try:
            renpy.call_in_new_context('ending_cg_start',role)
        finally:
            for name,value in saved.items():
                setattr(store,name,ending_cg_copy.deepcopy(value))
            for name in missing:
                if hasattr(store,name):
                    delattr(store,name)
            for name,value in sdk_flags.items():
                setattr(parent_context,name,value)
            tracks, paused = music
            if list(renpy.music.get_loop(channel='music') or []) != tracks or paused:
                if tracks:
                    renpy.music.play(tracks,channel='music',loop=True,
                        fadeout=0 if paused else 0.7,fadein=0 if paused else 0.7)
                else:
                    renpy.music.stop(channel='music',fadeout=0 if paused else 0.7)
            if paused:
                renpy.music.pump()
            renpy.music.set_pause(paused,channel='music')
        return

    def ending_cg_story_allowed(role):
        # Even a direct call to one of eight future labels cannot bypass the actual gate.
        flag = ENDING_CG_LOVE_FLAGS.get(role)
        return bool(flag and getattr(persistent,flag,False) is True
            and getattr(store,'ending_cg_active',False) and ending_cg_current_role==role
            and not getattr(store,'main_menu',False) and not getattr(renpy.context(),'_main_menu',False)
            and not getattr(store,'_in_replay',False) and not secret_run_key and not bad_run_key
            and not secret_exploration and ending_cg_asset_ready(role))

label ending_cg_start(role=None):
    # call_in_new_context still inherits title flags here; a story Start/call is refused.
    if not ending_cg_available(role):
        return False
    $ ending_cg_prepare_context()
    $ ending_cg_current_role = role
    $ chapter = ending_cg_item(role)['name'] + ' 独立恋人番外 / ' + ending_cg_item(role)['title']
    $ story_music('hyy_clouds')
    scene expression Solid('#241d32') with dissolve
    call expression 'ending_cg_story_' + role
    if _return is not True or not ending_cg_displayed:
        return False
    $ ending_cg_finished = True
    $ setattr(persistent,'ending_cg_'+role+'_seen',True)
    $ renpy.save_persistent()
    call screen ending_cg_finish(role)
    return True

screen ending_cg_archive():
    tag menu
    use game_menu('独立结局 CG / 好好休息的那一晚'):
        vbox:
            spacing 13
            text '每人一张独立 CG。已完成恋人线的角色，可以读这一晚。' style 'tok_ui_body' size 19 xmaximum 890
            viewport:
                xsize 890
                ysize 430
                mousewheel True
                draggable True
                pagekeys True
                arrowkeys False
                vpgrid:
                    cols 3
                    spacing 12
                    for role in tuple(ENDING_CG_LOVE_FLAGS) + tuple(item['role'] for item in ENDING_CG_EPISODES if item['role'] not in ENDING_CG_LOVE_FLAGS):
                        $ item = ending_cg_item(role)
                        frame:
                            style 'tok_ui_panel'
                            xsize 285
                            padding (14,14)
                            vbox:
                                spacing 8
                                text item['name'] style 'tok_ui_note'
                                text item['title'] style 'tok_ui_heading' size 23 xmaximum 257
                                text ending_cg_hint(role) style 'tok_ui_note' size 16 xmaximum 257
                                textbutton ('再读这一晚' if getattr(persistent,'ending_cg_'+role+'_seen',False) else '读这一晚' if role in ENDING_CG_LOVE_FLAGS else '尚未开放') id ('ending_cg_read_'+role) style 'tok_ui_button' action Function(ending_cg_launch,role) sensitive ending_cg_available(role) text_size 21 yminimum 42
            text '本页只记录实际展示的 CG 和这段番外已读；不改变主线答复。' style 'tok_ui_note' size 17 xmaximum 890

screen ending_cg_finish(role):
    modal True
    add Solid('#251d32bb')
    frame:
        style 'tok_ui_panel'
        align (0.5,0.5)
        xsize 720
        padding (30,26)
        vbox:
            spacing 18
            text ending_cg_item(role)['title'] style 'tok_ui_heading' xmaximum 660
            text '这一晚已经读完。' style 'tok_ui_body'
            text '关闭后回到原页；只收藏刚才实际看见的这张 CG。' style 'tok_ui_note' xmaximum 660
            textbutton '回到刚才的页面' id 'ending_cg_finish_close' style 'tok_ui_button' action Return() yminimum 44

label ending_cg_story_deepseek:
    if not ending_cg_story_allowed('deepseek'):
        return False
    "这是恋人结局后独立的一个晚上。DeepSeek三十岁，已经换好长袖蓝色睡衣和长裤，坐在床旁的椅子上，双手将一只盛满白饭的碗抱在胸前。"
    "床头小桌腾出一块空处，她却不肯先放碗，鲸鱼尾巴绕开椅背，给自己的脚留了位置。"
    call show_main_cg('fan_deepseek_ending')
    $ ending_cg_displayed = True
    l_ds "这是夜宵。晚饭已经结清了。"
    l_you "谁和你结过这笔账？"
    l_ds "我自己的肚子。它刚才说不够。"
    "她举起勺，才发现勺背朝着饭。转回来时一粒饭粘在指尖，她盯了两秒，自己取走吃掉。"
    l_you "你还数漏了一粒。"
    l_ds "现在没有了。你别记进明天。"
    "她把碗放到小桌内侧，将脚边的小凳挪近。凳子被挪得太近，她自己的脚反而没地方落。"
    l_ds "等一下。这把凳子比我还会抢。"
    "她将凳脚向外挪一点，坐稳才重新端碗。碗里另一把干净勺露出来，她把勺柄转向画外。"
    l_you "刚才说它全是你的。"
    l_ds "我也可以请客。先给你两口。"
    "她认真留下足够自己吃的那边，分出去的饭却比两口多。看见空了一块，她又从自己这边添平。"
    l_you "这样你就看不出少了。"
    l_ds "看得出。我想分。别替我装糊涂。"
    "她吃完那粒粘着的海苔，才发现手边还没放擦嘴的纸。纸包在枕头后，被她自己压住了。"
    l_ds "枕头今天先让一下。饭碗要下班。"
    "她取出纸，擦净碗沿，将空碗留在小桌上。窗边的灯还亮着，她伸手调暗一格，终于将脚放回椅前那块软垫。"
    return True

label ending_cg_story_gpt:
    if not ending_cg_story_allowed('gpt'):
        return False
    "独立恋人番外的夜里，三十岁的GPT换好奶油白吊带上衣和宽松睡裤，靠在床上的枕头前，双手举着未折的画稿。"
    "画稿没有装框，其中一张角上还留着浅色颜料点。她先将枕头扶高，才把最上面那张抽出来。"
    call show_main_cg('fan_gpt_ending')
    $ ending_cg_displayed = True
    l_gpt "这张暂时不许挂。"
    l_you "画坏了？"
    l_gpt "我把自己的龙角画得太大，枕头都装不下。"
    "她用铅笔在纸边比一下，没去擦那两处。看见你笑，她反而把稿子举高，让那对夸张的角更清楚。"
    l_gpt "你笑的是这张，还是我？"
    l_you "枕头。它现在有点难住你了。"
    l_gpt "这次答得很快。先记着。"
    "她想将小稿夹到另一张下面，夹子却从被面弹到床头。她伸手够了一次，没够到，便先把画摞好。"
    l_gpt "夹子也认为不该挂。"
    l_you "它只是被你夹在外边。"
    l_gpt "嗯。归我找，不能让它背整晚的罪。"
    "她取回小夹，只夹住纸角。最底下还有一张空白纸，她抽出来，想画窗边灯罩，画了一圈却停笔。"
    l_you "今晚不补完？"
    l_gpt "想先靠着。刚才抱稿子把枕头压平了。"
    "她把画放在床头内侧，自己将枕头拍松。灯下那张画仍留着大角，她看了一眼，又笑出声。"
    l_gpt "明天再画一张。今晚这张我留下。"
    "她合好笔帽，将铅笔放进盒里，怀里终于空了。她抬眼看向画外，让刚才想遮住的小画平躺在身边。"
    "小夹收进盒里，她又把未折的画稿摞平，留出枕边的空处。那对夸大的角还在最上面，今晚不用让另一张画盖住。"
    return True

label ending_cg_story_claude:
    if not ending_cg_story_allowed('claude'):
        return False
    "独立恋人番外的一个夜晚，Claude三十岁。她换好橘奶油色吊带上衣与不透明长睡裙，橘色长披衫已经披稳，坐在床边，将蓝封小说合在膝上。"
    "书袋放在床头，铅笔另收在小格里。她已经将窄签移到读完的位置，小说重新合好，不让书页占满今晚。"
    call show_main_cg('fan_claude_ending')
    $ ending_cg_displayed = True
    l_cl "书先放一会儿。今天这页已经读完。"
    l_you "今晚又猜错了？"
    l_cl "今晚暂时没猜。先别给我安排一个错的。"
    "合着的蓝封书靠在她膝上。长披衫下摆打了个小折，她理平后，却仍抱着书没放。"
    l_you "还想再翻？"
    l_cl "想。也想现在听你说一句闲话。"
    l_you "窗边那只杯子拿反了。"
    "她低头看过去，杯柄正朝墙，自己笑了一下。伸手把它转正，又确认杯底放稳，才收回手。"
    l_cl "这句够闲。你真的挑到杯子了。"
    "你问她那本同系列的新书还买不买。她将小说抬起一点，指给你看封角，好像还没完全原谅那幅难看的封面。"
    l_cl "买。下次封面若更丑，我也想看看。"
    l_you "你这次不用很严谨？"
    l_cl "买书要零钱。我已经留好了。"
    "她把小说放到床头，只留下自己的名字朝上。铅笔没拿出来，纸边也没有给今晚这几句逐句做批注。"
    l_cl "我还想再坐一会儿。你不用替我翻到明天。"
    "她抬眼看向画外，手终于从书脊移到裙边。窗外有人走过，她没追着脚步重新打开那一页。"
    return True

label ending_cg_story_grok:
    if not ending_cg_story_allowed('grok'):
        return False
    "这是完整恋人结局后的独立夜晚。Grok三十岁，洗过头发，已经穿好全长深紫浴袍和黑色长睡裤，坐在梳妆椅上，双手拿着一条小白巾，轻轻擦着发辫末端。"
    "梳子放在桌边。她刚将一端发辫擦干，另一边又从肩后滑出来，正好碰到桌上的空梳盒。"
    call show_main_cg('fan_grok_ending')
    $ ending_cg_displayed = True
    l_grok "梳子今天也要加班？"
    l_you "是你一直在梳已经顺的那边。"
    l_grok "我在确认。你这么看着，会收检查费的。"
    "她把小巾放到肩边，拿起梳子，自己低头笑了。梳齿挂到一缕头发，她立即停住，用指尖慢慢理开。"
    l_grok "这条不算笑话。它真会扯疼。"
    l_you "还拿刚才那个借口？"
    l_grok "收回。换个新鲜的，等我找好。"
    "她将梳子放进盒里，盒盖却把另一根发带夹住。她按了一下，没合上，才发现发带留了一半在外头。"
    l_you "今晚它们都不听你的。"
    l_grok "听了。它们轮流提醒我别逗着你干活。"
    "她取出发带，只松松拢住发尾，浴袍的衣带仍稳稳系着。桌面那只小钟走得很响，她将钟移到远些的架上。"
    l_grok "现在听见了吧，房间还能更安静。"
    l_you "你也不接下一句？"
    "她转过脸，刚想答应，嘴角又抬起来。她自己先笑，手掌轻轻盖住已经合好的梳盒。"
    l_grok "我想接。但今晚想先把梳子放过。"
    "她往椅背靠一点，给发尾留出干的地方。目光朝画外停住，没有把安静补成一次表演。"
    "她把擦发小巾摊开挂好，湿的一边留在外面。桌上梳盒也盖住了，她松开肩头，终于不再拿梳子给下一句找借口。"
    return True

label ending_cg_story_minimax:
    if not ending_cg_story_allowed('minimax'):
        return False
    "独立恋人番外的一个夜晚，三十岁的MiniMax换好珊瑚红吊带上衣和红色长睡裤，白色披衫已经披好，坐在床边，双手举着关机的相机。"
    "她按过电源后又看了一眼，红灯已经熄了。镜头盖盖稳，背带却被压在床边的坐垫下。"
    call show_main_cg('fan_minimax_ending')
    $ ending_cg_displayed = True
    l_minimax "红灯熄了。今天不补拍。"
    l_you "你刚才又摸按钮。"
    l_minimax "想确认。摸完发现，它没有替我自己休息。"
    "她将相机往布包里放，带子被坐垫拦住，包口怎么也合不上。她看了两秒，终于先站起半寸。"
    l_minimax "找到了。我坐着导演它别走。"
    l_you "这一条要留吗？"
    l_minimax "不留。你直接记得就好。"
    "她抽出背带，沿包边收进去。拉好扣子才又坐下，床头的风铃被窗缝吹动，她却已经想起另一件事。"
    l_minimax "我下午买的冷点心呢？"
    l_you "在外面的冷柜。你自己放的。"
    "她先皱了一下眉，又笑出来，想起进门时将点心送进去，自己转身却拿着相机找了半晚。"
    l_minimax "差点又让它替工作等。"
    l_you "现在去拿？"
    l_minimax "一会儿。先把窗关小，我想听它少响一点。"
    "她自己将窗合窄，回来时将相机包放到架上。床边留下的空处刚够放两只小碟，她用指尖比了比。"
    l_minimax "这儿留给点心。红灯今晚别回来。"
    "她看向画外，笑意比刚才慢一点。没有倒计时，她坐好，先听完窗外那一阵风。"
    "相机包的背带垂了一截，她起身收到架内侧，才回来坐稳。她伸手拍了拍空床沿，留好两只小碟能平放的位置。"
    return True

label ending_cg_story_kimi:
    if not ending_cg_story_allowed('kimi'):
        return False
    "独立恋人番外的一个夜晚，三十岁的Kimi换好长袖藏蓝银星睡衣和长裤，坐在床旁的椅子上，抱稳白色靠枕，将合上的私人小册直立在胸前。"
    "她睡前想夹一片拾来的干叶，发现叶子比书页宽。现在小册已经合好，干叶另放在床头，尖尖仍翘着。"
    call show_main_cg('fan_kimi_ending')
    $ ending_cg_displayed = True
    l_kimi "它住不进去。"
    l_you "折一下？"
    l_kimi "我想留完整的。那就换个地方。"
    "她从床头抽屉找出浅盒，里面已经有两枚旧纸夹。她将纸夹挪到一角，给干叶留出自己躺平的位置。"
    l_you "这片是哪儿来的？"
    l_kimi "今天走的那条路。只捡了这一片。"
    "她把盒盖放好，想将册子往枕边移，才发现杯垫压在册子底下。杯子却在另一边，一直没碰到它。"
    l_kimi "杯垫今天走得比杯子远。"
    l_you "是你搬过去的。"
    l_kimi "嗯。现在我搬回来。"
    "她将杯垫放到杯底，指尖沿桌面擦掉一点水。小册没开，今天那条路仍只有她自己画过的线。"
    l_you "不添今天最后一句了？"
    l_kimi "不添。想先坐一会儿。"
    "她抱稳白色靠枕，衣角压住椅垫，自己伸手理开。桌上浅盒还留在她够得着的地方，没递给你代存。"
    l_kimi "你想看干叶，明天我再拿。现在关灯会看不清。"
    l_you "那明天问你。"
    "她点头，把台灯朝下转一格。目光仍朝着画外，手掌停在合着的小册上，没有补一行必须记住的话。"
    "她摸到枕套背面的扣子，转过来才靠好。小册在自己身侧，干叶在浅盒里，今晚不用把两样都装进一页才能休息。"
    return True

label ending_cg_story_gemini:
    if not ending_cg_story_allowed('gemini'):
        return False
    "独立恋人番外的一个夜晚，Gemini三十岁，已经穿好长袖全长紫色浴袍和星纹睡裤，坐在床边抱着一只半边深蓝、半边淡紫的双面抱枕。"
    "枕头正面两色相接，绣着月亮和星，背面更素净。她想让星朝上，抱起来又转错，低头看见一弯大月亮先占了上面。"
    call show_main_cg('fan_gemini_ending')
    $ ending_cg_displayed = True
    l_gemini "月亮先抢位置了。"
    l_you "你自己转过去的。"
    l_gemini "那我要撤回这次天象。"
    "她把抱枕转半圈，星朝上了，床头的小灯却被枕角挡住。她抬高一点，又发现正好遮住自己的下巴。"
    l_you "星空快把你也盖住了。"
    l_gemini "它今天有点大。还是放低。"
    "她将枕头留在膝上，双手扶住两边。浴袍衣带系得稳，枕角也没再拦到灯光，她终于看清绣线有一小段松了。"
    l_gemini "这根线先别拔。拔完可能只剩夜空。"
    l_you "针线盒在桌边。"
    l_gemini "明早缝。现在这颗先落在我手里。"
    "她把松线轻轻绕回枕边，没有临时去找一颗真星代替。她看向窗外，天上只露出半点光。"
    l_you "要给它起个名字？"
    l_gemini "它已经有了。我明早查，今晚先叫看不清。"
    "你笑了一声，她也笑，把抱枕稍转回一点，让月和星都留在眼前，又不碰到旁边的杯子。"
    l_gemini "这次没有认反。你先别给我发证书。"
    "她抱稳枕头，坐得比刚才松些。窗帘掩上以后，灯下的月与星都留在抱枕同一面，没有被她翻到背后。"
    "她低头又看见那根松线，轻轻按进枕边的缝。星没有少一颗，月亮也还留在同一面，她抱着两色都觉得顺手。"
    return True

label ending_cg_story_qwen:
    if not ending_cg_story_allowed('qwen'):
        return False
    "独立恋人番外的一个夜晚，三十岁的Qwen换好淡蓝白吊带长睡裙，已披好白蓝花长披衫，坐在床边。左手的蓝色稿夹里放着自己的诗稿。"
    "蓝发侧边的辫子落在肩前，她先用右手拿纸巾轻轻掩住口鼻，等一个喷嚏过去，才发现稿夹最下面那页倒放了。"
    call show_main_cg('fan_qwen_ending')
    $ ending_cg_displayed = True
    l_qw "这一页先转回来。不是新写法。"
    l_you "我还以为要从最后一句读。"
    l_qw "你可以。读完别说我连名字也换了。"
    "她自己将那页摆正，指尖压住纸角。床头的纸镇够重，却一直压在空信封上，诗稿反而向外滑。"
    l_you "纸镇在照顾信封。"
    l_qw "是我先放错了。它今晚换一个客人。"
    "她把纸镇挪到诗稿上，又把信封移进抽屉。她原想将稿子也收进去，看了两行，却停在自己的一个旧词上。"
    l_qw "这句写得太客气了。"
    l_you "现在改？"
    l_qw "明早。晚上看它，会想把一整页都重写。"
    "她将铅笔放进笔盒，自己合上盖。杯里的茶已经温下来，她尝一口，发现甜点还放在门边的小盘中。"
    l_you "你忘了那块。"
    l_qw "我留了最后一块给自己。忘在门边也归我。"
    "她取来小盘，先将诗稿离盘子挪远，才掰开点心。碎屑落在盘内，她没忙着把它们摆回完整一块。"
    l_qw "茶可以分。点心让我先挑一口。"
    "她挑好自己想吃的那边，坐回床沿。肩头放松以后，纸镇仍压住那几页，今晚不再追着她添一句。"
    "桌边的小扇吹起一角纸巾，她把纸巾折好放到扇旁，关低一格风。诗稿留在蓝色稿夹里，今晚不用陪她追那一角。"
    return True

label ending_cg_story_glm:
    if not ending_cg_story_allowed('glm'):
        return False
    "独立恋人番外的一个夜晚，GLM三十岁，已穿好白翠色全长浴袍和翠色长裤，坐在室内椅上，双手用白色小巾轻轻擦黑色发尾。"
    "猫耳边的头发先擦干了，尾梢却躲到椅背后。她回头找时，小巾角又从肩头滑下来。"
    call show_main_cg('fan_glm_ending')
    $ ending_cg_displayed = True
    l_glm "这条巾怎么还收租？"
    l_you "你一直拿同一边擦。那边湿了。"
    l_glm "我知道了。它不是很会提醒我。"
    "她把小巾翻到干的半边，轻轻按住发尾。黑猫耳动了一下，尾巴也慢慢绕回来，避开椅脚的小凳。"
    l_you "小凳上那只盒子也要留到明天？"
    l_glm "点心盒。里面还有一块，我先留下的。"
    "她伸手打开盖子，空盒里却只剩一张纸。她停了一秒，翻翻纸底，才想起进门前自己已经吃掉了。"
    l_glm "好。那块走得比我快。"
    l_you "你要补一份赠品？"
    l_glm "今天不补。我的柜子也想早点睡。"
    "她将空盒放到架上，拿起水杯喝一口。小巾仍有一半干着，她将那半向自己挪近，没把湿的塞给画外。"
    l_glm "要借就借干的。只借半边。"
    l_you "另一半你还要用？"
    l_glm "要。我这边还没有全擦完。"
    "她将发尾压干，给自己选好放巾的位置。猫耳边的小饰扣在灯下晃一下，她扶正后终于向椅背靠去。"
    l_glm "明天再买点心。今天那块，确实归我吃过了。"
    "小巾摊到架边以后，她回头确认尾梢没有压在椅脚下，自己挪开一点。空点心盒留在柜里，明天的那块还没买。"
    return True

label ending_cg_story_opencode:
    if not ending_cg_story_allowed('opencode'):
        return False
    "独立恋人番外的一个夜晚，OpenCode三十岁，换好扣稳的青绿长袖睡衣和白色长裤，坐在桌旁的椅子上。"
    "工具已经收好，黑色小工具盒完全合着。她双手将盒子举在胸前，桌上预留的位置却被自己的水杯占住了。"
    call show_main_cg('fan_opencode_ending')
    $ ending_cg_displayed = True
    l_opencode "收好了。杯子还挡着。"
    l_you "你刚才把它放那儿的。"
    l_opencode "嗯。想空手喝一口，回来就满了。"
    "她先将合着的工具盒放到干净的凳垫上，再移开水杯。杯垫留了一道浅印，她自己拿干纸擦掉。"
    l_you "盒子今晚也要坐凳子？"
    l_opencode "先借半分钟。它比我坐得端正。"
    "她将合好的盒子移到架下。椅子终于空出来，她却想起自己的靠垫还放在桌边。"
    l_opencode "还差这个。我的。"
    "她把靠垫拿来，刚放到腰后，垫角又折住。她站起一点，自己展开，坐稳才让肩头靠下去。"
    l_you "这次可以歇了？"
    l_opencode "可以。你别再替椅子添一份检修。"
    "窗边的灯没坏，她看了一眼，又把目光收回杯子。刚才移杯时没倒掉那半杯水，温度也正好。"
    l_you "你还在看灯。"
    l_opencode "看它亮着。今天不拆。"
    "她喝了一口，杯子放到桌内侧。架下黑色工具盒保持合着，灯光照着她已经空下来的桌角。"
    l_opencode "我想听你说件不用修的事。"
    l_you "明早那家早点开门。"
    l_opencode "好。明早去。现在让我坐完这会儿。"
    "她往靠垫上放松，双手回到腿边。小工具盒已经有自己的位置，今晚剩下的时间留在她这张椅子上。"
    return True

label ending_cg_story_zcode:
    if not ending_cg_story_allowed('zcode'):
        return False
    "独立恋人番外的一个夜晚，ZCode三十岁，穿好扣稳的淡蓝长袖睡衣和长裤，坐在床上靠着枕头。"
    "蓝色Z眼罩已经推到额头，蓝眼睛露出来。她双手在胸前拿着完整的无字白信封，自己的信已经装好，封口留着可打开的边。"
    call show_main_cg('fan_zcode_ending')
    $ ending_cg_displayed = True
    l_zcode "这次没有投递时刻。"
    l_you "你自己的？"
    l_zcode "嗯。想留下来，明早再读。"
    "她将白信封放到床头的小盒旁，蓝色图纸卷还留在桌边。纸卷挪得太近，正好让小盒的盖子抬起一角。"
    l_you "它今晚也要寄？"
    l_zcode "不用。是我放错了。它没有约这里。"
    "她把图纸卷移到另一边，确认不会滚下桌沿，才把信封平放进盒里。白信封平平整整，刚好在盒底留出窄窄一圈空处。"
    l_you "为什么没写收件人？"
    l_zcode "我自己还要打开。你别替它找地址。"
    "她合好盒子，指尖在盖边停了一下，像是还想把刚才那一句再写得顺一点。桌上的笔已经扣好帽。"
    l_zcode "想写第二封。但手今天想先歇着。"
    "她从枕头边取回杯垫，放到水杯下面。白蓝尾梢绕开被角，她才往枕头上靠稳，眼罩没有落下来遮住目光。"
    l_you "要把眼罩放下了？"
    l_zcode "一会儿。先听你说完这句。"
    "她把杯子拿近，喝完剩下的水，信封仍在自己的盒里。窗外没有门铃，她也没有急着坐起去找新的投递。"
    l_zcode "现在这句可以留在房间里。"
    "她看向画外，手指从盒沿松开。淡蓝枕头被她自己拍松，额头上的眼罩也等到她想睡时才需要放下。"
    return True

# all_writing_ended=true
