# v0.15 候选独立番外；仅由标题 Function(ds_tipsy_launch) 打开。
# 两新CG须根按原件登记，未登记/未落盘时入口不开放。
default persistent.ds_tipsy_seen = False
default ds_tipsy_choice = ''
default ds_tipsy_water_done = False
default ds_tipsy_rest_done = False
default ds_tipsy_consent = False
default ds_tipsy_cardigan_on = False
default ds_tipsy_finished = False
default ds_tipsy_active = False

# 既有庭景的暗调窗外切镜；不是新室内BG，不借旧女仆立绘冒充换装。
image bg ds_tipsy_night = Transform('images/original/echo_shrine.png', xysize=(1280,720), fit='cover', matrixcolor=BrightnessMatrix(-0.20))

init -2 python:
    import copy as ds_tipsy_copy

    def ds_tipsy_cgs_ready():
        return all(any(cg['id'] == key and renpy.loadable(cg['file'])
            for cg in ORIGINAL_CGS) for key in ('ds_tipsy_wait','ds_tipsy_pounce'))

    def ds_tipsy_available():
        return bool(main_menu and getattr(persistent,'main_ds_love',False) is True
            and not ds_tipsy_active and not affection_special_active
            and not secret_run_key and not bad_run_key and not secret_exploration
            and not getattr(store,'_in_replay',False) and ds_tipsy_cgs_ready())

    def ds_tipsy_state_keys():
        # Also isolate say/history/window/side-image caches, as real special contexts do.
        return tuple(dict.fromkeys(ENDING_STATE_KEYS + AFFECTION_STATE_KEYS + (
            'ending_snapshot','ending_music_snapshot','ds_tipsy_active','main_menu')))

    def ds_tipsy_prepare_context():
        names = ds_tipsy_state_keys()
        renpy.context_dynamic(*names)
        for name in names:
            if hasattr(store,name):
                setattr(store,name,ds_tipsy_copy.deepcopy(getattr(store,name)))
        renpy.context()._menu = False
        renpy.context()._main_menu = False
        store.main_menu = False
        store._menu = False
        store.suppress_overlay = False
        store.ds_tipsy_active = True
        # Title-only replay has a parent save context, not an episode midpoint save.
        store.quick_menu = False
        store.main_cg = None

    def ds_tipsy_launch():
        # Function returns None so it does not dismiss the parent menu.
        if not ds_tipsy_available():
            return
        names = ds_tipsy_state_keys()
        previous_state = {name:ds_tipsy_copy.deepcopy(getattr(store,name))
            for name in names if hasattr(store,name)}
        missing = tuple(name for name in names if not hasattr(store,name))
        music = (list(renpy.music.get_loop(channel='music') or []),
            renpy.music.get_pause(channel='music'))
        ending_capture_state()
        parent_state = ds_tipsy_copy.deepcopy(ending_snapshot)
        try:
            renpy.call_in_new_context('ds_tipsy_start')
        finally:
            store.ending_snapshot = parent_state
            ending_restore_state()
            for name,value in previous_state.items():
                setattr(store,name,ds_tipsy_copy.deepcopy(value))
            for name in missing:
                if hasattr(store,name):
                    delattr(store,name)
            # get_playing may still report an outgoing fade: compare queued loop.
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

label ds_tipsy_start:
    # call_in_new_context inherits title flags until prepare clears only the child.
    # Start(label) or a story call has main_menu=False and is refused.
    if not ds_tipsy_available():
        return False
    $ ds_tipsy_prepare_context()
    $ ds_tipsy_choice = ''
    $ ds_tipsy_water_done = False
    $ ds_tipsy_rest_done = False
    $ ds_tipsy_consent = False
    $ ds_tipsy_cardigan_on = False
    $ ds_tipsy_finished = False
    $ chapter = 'DeepSeek 独立番外 / 最后一口，先分给你'
    $ story_music('hyy_clouds')
    call ds_tipsy_evening
    call ds_tipsy_sofa
    menu:
        "答应靠近，先把靠垫放稳。":
            $ ds_tipsy_choice = 'close'
            $ ds_tipsy_consent = True
            call ds_tipsy_close
        "扶她坐稳，慢慢喝完清水。":
            $ ds_tipsy_choice = 'settle'
            call ds_tipsy_settle
        "留在这边陪她聊一会儿。":
            $ ds_tipsy_choice = 'chat'
            call ds_tipsy_chat
    call ds_tipsy_goodnight
    $ ds_tipsy_finished = True
    $ persistent.ds_tipsy_seen = True
    $ renpy.save_persistent()
    call screen ds_tipsy_finish
    return True

label ds_tipsy_evening:
    scene bg ds_tipsy_night with dissolve
    $ main_cg = None
    $ hide_speaker_portrait = True
    "这是恋人线里一个独立的晚饭后。你与DeepSeek都三十岁，今晚没有排队等修的灯，也没有谁临时来借梯子。"
    "茶屋窗外亮着月光。晚饭的盘子空了，她却为夜宵另盛了满满一小碗白饭，抱到休息角。饭上有几点绿色的海苔碎，碗沿还搭着一片。"
    l_ds "这个不能算剩饭。它是在等我。"
    l_you "那你为什么把碗推给我？"
    l_ds "等一下。我还没决定等谁。"
    "她把碗拉回半寸，先将两只洗净的勺子并排放好。你搬来小茶几，正好挡住她想把空盘偷偷放下的地方。"
    l_you "这里也算休息角？"
    l_ds "盘子休息，人就能跟着休息。"
    l_you "人可以，盘子得先洗。"
    "她看一眼盘底，又看你。尾巴在沙发前停住，没替她把盘子藏到身后。"
    l_ds "我洗了两只。这只轮到你。"
    l_you "刚才那两只是勺子。"
    l_ds "它们也有面积。"
    "你伸手接盘时，碗沿被袖口带得一歪。她立刻按住桌边，将饭碗挪到茶几内侧，另一只手把勺子收进碟里。"
    l_ds "先别转身。左边这只脚碰到毯子了。"
    "你停下来，把卷起的毯角铺平。她这才松开手，白饭仍满满地留在碗里，一粒也没洒。"
    l_you "这下真是现场监督了。"
    l_ds "重要物品差点损失。"
    l_you "饭？"
    l_ds "……还有盘子。你别只听前半句。"
    "盘子放进水槽后，你回来坐到沙发右边。她将满碗白饭留在茶几上，先拆了另一小包烤海苔，铺在两只小碟里。"
    l_ds "分你一片。大的先让我挑。"
    l_you "你拿的那片，看着大些。"
    l_ds "它先到我手里的。"
    "她却把那片掰开，将厚些的半片推给你。碎屑落在碟沿，她用指尖拢好，没有再往饭上撒。"
    l_you "这碗为什么还不吃？"
    l_ds "放一会儿。凉一点好拌，不会把海苔闷软。"
    "你本想把勺子插进饭里替她散热，她立刻将勺柄按到碟边，指了指碗里的白饭。"
    l_ds "先别挖。我要那一整碗。"
    l_you "我只想让它凉快一点。"
    l_ds "那你陪它吹风。手不用忙。"
    "茶几左侧放着一只小酒杯。她晚饭时只尝了两小口梅酒，杯里还剩一些，脸颊比平时红一点。"
    l_you "这杯还要继续吗？"
    l_ds "不续。梅子已经尝到了。"
    "她把酒杯搁回小托盘，托盘推到茶几最远的一角。杯子没有跟着她的手再靠近嘴边。"
    l_ds "给我倒清水吧。别用这只杯。"
    l_you "要凉一点的？"
    l_ds "常温。我要慢慢喝，还想把饭吃完。"
    "你把水递过去。她接稳杯子，试过一口，指给你看沙发旁没有扶正的靠垫。"
    l_ds "那只先放正。它一直想占我的地方。"
    return

label ds_tipsy_sofa:
    "她在沙发左侧坐下，两脚落在铺平的毯子上。清水杯握在手中，白饭与两只小碟还留在左边茶几。"
    "你把靠垫放到她腰后。她自己调整了一下位置，肩头放松，低头又喝两口水。"
    l_ds "我先休息一会儿。你也别站着。"
    l_you "这次不是把洗盘子拖到明天吧？"
    l_ds "盘子都进水槽了。你回来时没看见？"
    l_you "看见了。碗还在这里。"
    l_ds "碗里有饭。分类别弄混。"
    "你们坐了十来分钟。窗边的钟走到七点二十，她看一眼时间，又准确点了点你碟里那半片海苔。白饭仍满碗放着。"
    l_ds "你那半快碎了。刚才一直拿着逗我。"
    l_you "你自己的不也没吃？"
    l_ds "我在想怎么不让海苔先吃完。"
    "她说得清楚，握杯的手也稳。她把清水喝到半杯，亲手放回茶几内侧，给自己空出两只手。"
    $ ds_tipsy_water_done = True
    $ ds_tipsy_rest_done = True
    "你伸手去捞掉到垫缝里的纸巾，纸巾没够到，反倒把自己的垫子拉歪了。她含着一口清水，先用空着的手拍住垫角。"
    "等水咽下，她才把纸巾从你身后抽出来，展开给你看。你刚才一直坐在它上面。"
    l_ds "不用再下去找。底下没有第二张。"
    l_you "你什么时候看见的？"
    l_ds "刚才。你特别认真，我想再看一下。"
    "你将纸巾折好放在桌边。她把水杯放稳，轻轻揉了一下自己刚才忍笑的脸颊。"
    l_ds "我脸还有点热，先不喝酒了。"
    l_you "那我们就坐着。"
    "她点头，却没有就此靠过来。侧边的蝴蝶结被她轻轻理好，她转过脸，目光落在你坐着的位置。"
    l_ds "我想坐近一点，抱你一下。可以吗？"
    "她的膝盖仍在自己那半边坐垫上，两只手放松地停在腿前，等你回答。"
    return

label ds_tipsy_close:
    l_you "可以。先把靠垫放稳，我们都坐好了再抱。"
    "你将身边的靠垫扶正，留出半个坐垫。她往前挪一点，先确认茶几没有挡住脚边。"
    $ hide_speaker_portrait = True
    call show_main_cg('ds_tipsy_wait')
    l_ds "我先等你坐近。"
    l_you "水杯也放稳了。"
    scene bg ds_tipsy_night with dissolve
    $ main_cg = None
    $ hide_speaker_portrait = True
    "她看了看窗边的凉意，起身去侧间换衣。你留在沙发这边，把拆开的海苔袋折好，用小碟压住，没有跟过去。"
    "片刻后，她换好蓝色高领便服回来，外面穿着浅蓝开衫。她自己扣好前面的扣子，才伸手理平袖口。"
    $ ds_tipsy_cardigan_on = True
    l_ds "这身暖些。刚才靠垫挪出来，窗边风也跟着进来了。"
    l_you "要把窗关上吗？"
    l_ds "留一条缝就行。我想听外面那只虫。"
    "她把小茶几推到窗边，收走剩梅酒的杯子和酒托盘。她又将饭上那几点海苔碎拨回小碟，免得放久了泡软。桌上留下清水与白米饭，脚边多出一块宽敞的毯子。"
    l_you "你连饭碗也安排好了。"
    l_ds "它不参加抱一下。"
    "你坐回刚腾出的地方。她站在沙发前，弯眼看你一下，双脚稳稳踩在毯子上。"
    l_ds "准备好了吗？我会慢一点。"
    l_you "好了。"
    "她笑着往你这边轻扑半步。你及时垫稳旁边的软靠垫，沙发发出一声小小的气音，她也跟着笑了。"
    "开衫衣袖里的双手撑住左右靠垫，她自己稳住身体，在离你很近的地方停下。"
    $ hide_speaker_portrait = True
    call show_main_cg('ds_tipsy_pounce')
    l_ds "先抱一下。"
    l_you "垫子接住了，饭也没动。"
    l_ds "我还没抢饭呢。"
    scene bg ds_tipsy_night with dissolve
    $ main_cg = None
    $ hide_speaker_portrait = True
    "她确认你坐得舒服，才把这一抱留了几秒。放开时，她先扶稳自己的靠垫，没让你一直悬着肩。"
    l_ds "刚才那一声，算沙发替我笑。"
    l_you "你自己也笑了。"
    l_ds "我可以笑两次。又不收钱。"
    "你们重新并肩坐好。她抬手拿起清水，喝过才把满碗白饭端回来，往两只小碟里各分了两勺。"
    l_ds "剩下的归我。你那边再加海苔。"
    l_you "我刚才接住垫子，有没有多一勺？"
    l_ds "有。最后再给，免得你边抱边惦记。"
    "她给你的碟里又添一勺，自己先吃白饭，再咬一点海苔。你们的碟子没有端过沙发中间，勺子也没有碰到对方袖口。"
    return

label ds_tipsy_settle:
    l_you "我先扶你坐稳。我们慢慢把清水喝完。"
    l_ds "好，那我这次坐里面一点。"
    "她把腰后的靠垫抽出来，递给你放正，自己扶着沙发侧边挪好位置。你扶的是她伸来的小臂，等她坐稳便松开。"
    l_ds "这样就好。你不用一直举着手。"
    l_you "我怕放早了，你又怪垫子抢地方。"
    l_ds "它今天的确抢了。刚才还想滑到地上。"
    "她把垫角压回腰侧，自己试着靠了一下。水杯始终在茶几上，重新坐好后她才伸手去拿。"
    l_ds "饭要不要热一下？"
    l_you "你不是打算整晚不动？"
    l_ds "那是清水的安排，没包括饭。"
    "她说完自己也笑，笑声很轻，杯里的水没有晃出来。你将碟子移到茶几中间，她往两只碟里各分了几勺白饭。"
    l_you "不用热。我这份现在吃正好。"
    l_ds "那先吃你那份。我这边还要挑海苔。"
    "你们把饭吃完。她最后一粒米没有漏掉，又将空碗放回托盘，手指从碗底托着，没有靠到你的肩上。"
    l_ds "今晚就这样坐着，也挺舒服。"
    "你将自己的清水杯摆在她杯子旁，两只杯之间留着一指宽。她看一眼，笑着把靠垫往自己这边收好。"
    return

label ds_tipsy_chat:
    l_you "我今晚想陪你聊一会儿。就坐在这边，好吗？"
    l_ds "好。那你把那只垫子留给我。"
    "她没有往前挪，反而将你让出的靠垫抱到膝上。清水放在伸手能拿到的地方，两个人仍各坐一边。"
    l_ds "今天饭锅揭盖时，你有闻到吗？"
    l_you "你刚才也问过一次。"
    l_ds "我问的是揭盖那一秒。后来你去洗勺子了。"
    l_you "有。你还把锅盖举得很高。"
    l_ds "蒸气会躲到盖子里。我给它放出来。"
    "你模仿她当时认真抬盖子的样子，她一下笑出声，抱着的靠垫往上提了提，没拿它丢你。"
    l_you "是不是还少学了一句？"
    l_ds "有。不要站在我挑饭的那边。"
    l_you "这句我记得特别牢。"
    "她用手指在靠垫边上划了一小格，假装那里是饭锅。你点点另一边，说这边以后留给你盛。"
    l_ds "这边米会薄一点。你真的要？"
    l_you "我可以多盛一勺。"
    l_ds "……算盘也会打了。"
    "她把碟子推到你这侧，自己端起水杯。你们说起明天想吃的东西，她报出白米饭，停一下，又补上烤海苔。"
    l_you "我还没问明天晚上呢。"
    l_ds "先写着，不用临时再想。"
    "她把两只海苔碟分开摆好，往里面各添了几勺饭。你正想问她还留那么多做什么，她已经将碗拉近，低头吃了一口。"
    l_ds "这边是我的。你那边不够再说。"
    l_you "我还没开口。"
    l_ds "你的勺子先过来了。"
    "你将勺子退回碟里，她看着你笑，又替你添了一小勺。窗外虫声响了一次，她指给你听，等那一声过去才接话。"
    return

label ds_tipsy_goodnight:
    scene bg ds_tipsy_night with dissolve
    $ main_cg = None
    $ hide_speaker_portrait = True
    "七点四十，白饭吃完了，茶几上的清水也少了一半。你起身收碗，她这次没有把自己的那只推到你面前。"
    if ds_tipsy_choice != 'close':
        "她先将小酒托盘连着酒杯送回柜边，回来才端起自己的空饭碗。两只水杯留给你拿，桌边没有晾着半杯梅酒。"
    l_ds "我拿这个。你拿两个杯子。"
    l_you "酒杯呢？"
    l_ds "已经收走了。今晚没有下一杯。"
    "到门边时，她发现碗沿粘着那片海苔，认真看了两秒，终于把碗放下，用干净勺子取出来。"
    l_you "重要物品还没走完？"
    l_ds "最后一口。先分给你。"
    "她将海苔掰开，把完整的一边放到你的勺子上，自己留着较小那半，吃完才把两只勺子并在碗里。"
    if ds_tipsy_choice == 'close':
        l_ds "明天抱的时候，我也会先问。靠垫可以提前摆好。"
    elif ds_tipsy_choice == 'settle':
        l_ds "明天这只垫子还给我。我们不用急着换坐法。"
    else:
        l_ds "明天揭饭锅盖之前，我会叫你来听那一声。"
    l_you "那我先把勺子洗好。"
    l_ds "好。我监督最后一只碗。"
    "她刚说完，自己先笑了，拿着碗往水槽走去。你将门边的毯角再铺平，听见她从里面叫你慢慢来。"
    return

screen ds_tipsy_finish():
    modal True
    add Solid('#251d32bb')
    frame:
        style 'tok_ui_panel'
        align (0.5,0.5)
        xsize 760
        padding (30,26)
        vbox:
            spacing 18
            text '最后一口，先分给你' style 'tok_ui_heading' xmaximum 700
            text ('靠垫先接住了笑声。' if ds_tipsy_choice == 'close' else '两杯清水，慢慢喝完。' if ds_tipsy_choice == 'settle' else '明天揭盖时，也叫你来听。') style 'tok_ui_body' xmaximum 700
            text '独立番外已读。从标题完整回看，关闭后回到原页；只收藏实际看过的CG。' style 'tok_ui_note' xmaximum 700
            textbutton '回到刚才的页面' id 'ds_tipsy_finish_close' style 'tok_ui_button' action Return() yminimum 44
