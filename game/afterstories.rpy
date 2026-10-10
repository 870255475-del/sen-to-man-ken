# 新后日谈与独立IF。新家庭场景完全非性化，独立于新增恋爱CG额度。
default persistent.after_ds_wedding_seen = False
default persistent.after_ds_family_seen = False
default persistent.after_ds_departure_seen = False
default persistent.after_ds_unremembered_seen = False
default persistent.after_ensemble_preview_seen = False
default persistent.cg_ds_wedding = False
default persistent.cg_ds_family = False
default ds_wedding_detail = ''
default ds_family_detail = ''
default ds_if_keepsake = ''
define l_child = Character('小满', color='#f5ceac')

init -4 python:
    AFTERSTORIES = [
        dict(id='wedding', title='两只碗，今天算一桌', tag='DeepSeek · 婚礼', label='ds_after_wedding', flag='after_ds_wedding_seen', gate='love', note='恋人结局两年后，她32岁。'),
        dict(id='family', title='第三只小碗', tag='DeepSeek · 家庭', label='ds_after_family', flag='after_ds_family_seen', gate='love', note='婚礼五年后，她37岁；孩子4岁。全篇家庭日常。'),
        dict(id='departure', title='饭要趁热，信可以慢一点', tag='独立虐心IF · 远行', label='ds_if_departure', flag='after_ds_departure_seen', gate='any_ds', note='长期分离与未到的回信。不是拒绝恋爱的惩罚。'),
        dict(id='unremembered', title='她替陌生人添了一碗', tag='独立虐心IF · 遗忘', label='ds_if_unremembered', flag='after_ds_unremembered_seen', gate='any_ds', note='架空平行设定：相处记忆丢失。与现实AI产品无关。'),
        dict(id='ensemble', title='一桌十二碗', tag='全员共同篇 · 序章', label='ensemble_table_preview', flag='after_ensemble_preview_seen', gate='common', note='共同生活提案；十一条恋爱确认与完整终章仍待制作。')]

    def afterstory_available(item):
        if item['gate'] == 'love': return bool(persistent.main_ds_love)
        if item['gate'] == 'common': return bool(persistent.main_common_ch07_seen)
        return any(bool(getattr(persistent,'main_ds_'+k,False)) for k in ('love','wait','friend'))

screen afterstories():
    tag menu
    use game_menu('后日谈 / 平行的另一页'):
        viewport:
            ysize 530
            mousewheel True
            draggable True
            pagekeys True
            arrowkeys False
            vbox:
                spacing 14
                text '婚后篇在恋人结局后开放；IF由你主动选择。' size 20 color '#49384F'
                textbutton '结局与秘密 / 十三页隐藏故事' id 'after_hidden_archive' action ShowMenu('ending_archive') text_size 24
                textbutton '角色小夜话 / 单人结局 CG' id 'afterstory_ending_cg_archive' action ShowMenu('ending_cg_archive') text_size 23
                textbutton '泳装·乌龙·轻吻 / 独立恋人邀约' id 'afterstory_character_events' action ShowMenu('character_event_archive') text_size 23
                if not main_menu:
                    text '这页可查看收藏；后日谈从标题进入。返回后仍停在原来的对白。' size 18 color '#796977' xmaximum 890
                frame:
                    style 'tok_ui_panel'
                    xsize 890
                    padding (21,15)
                    vbox:
                        spacing 7
                        text 'DeepSeek · 独立恋人番外' style 'tok_ui_note'
                        text '最后一口，先分给你' style 'tok_ui_heading' size 26
                        text '小酌后的清水与夜宵。可以轻抱、扶稳坐好，或各坐一边陪聊。' style 'tok_ui_body' size 19 xmaximum 843
                        hbox:
                            spacing 18
                            textbutton ('再读这一个晚上' if persistent.ds_tipsy_seen else '一起吃这份夜宵') id 'afterstory_ds_tipsy' style 'tok_ui_button' action Function(ds_tipsy_launch) sensitive ds_tipsy_available() text_size 21 yminimum 44
                            text ('从标题完整回看 · 不改主线记录' if ds_tipsy_available() else '恋人结局后，从标题进入' if main_menu else '从标题进入 · 返回继续原故事') style 'tok_ui_note' size 17 yalign 0.5
                for item in AFTERSTORIES:
                    $ available = afterstory_available(item)
                    frame:
                        background SoftPanel('#f7e8ee','#b586a5',10)
                        xsize 890
                        padding (21,15)
                        vbox:
                            spacing 7
                            text item['tag'] size 18 color '#9b5d7c'
                            text item['title'] size 26 color '#663758'
                            text item['note'] size 18 color '#8e6c81' xmaximum 843
                            hbox:
                                spacing 18
                                textbutton ('再次阅读' if getattr(persistent,item['flag'],False) else '阅读这一页') id ('after_read_'+item['id']) style 'navigation_button' action Start('after_'+item['id']+'_start') sensitive available and main_menu text_size 21 text_color '#653657'
                                text ('已读' if getattr(persistent,item['flag'],False) else '开放' if available else '恋人结局后开放' if item['gate']=='love' else '读完DeepSeek任一结局后开放' if item['gate']=='any_ds' else '共通第七章后开放') size 17 color '#8e6c81' yalign 0.5

screen new_if_notice(title, note):
    modal True
    add Solid('#111722f0')
    frame:
        align (0.5,0.5)
        xsize 850
        padding (36,32)
        background SoftPanel('#FFF7F1','#DEC2CF',12)
        vbox:
            spacing 23
            text title xmaximum 775 size 32 color '#49384F'
            text note size 23 color '#49384F' xmaximum 775
            text '独立阅读，不改主线关系和结局。' size 20 color '#49384F'
            textbutton '阅读这篇IF' id 'new_if_accept' action Return(True) text_size 23
            textbutton '先返回' id 'new_if_cancel' action Return(False) text_size 23
    key 'game_menu' action Return(False)

screen afterstory_finish(title, preview=False):
    modal True
    add Solid('#201a30e8')
    frame:
        align (0.5,0.5)
        xsize 790
        padding (38,34)
        background SoftPanel('#fcf2ee','#ba7597',15)
        vbox:
            spacing 20
            text ('共同篇序章 · 待续' if preview else '这一页 · 终') size 22 color '#a55983'
            text title size 33 color '#512d53' xmaximum 710
            text ('这里只完成共同生活提案，不代表十一条恋爱线已攻略。' if preview else '这页已收进后日谈，主线里的回答仍然保留。') size 21 color '#75536e' xmaximum 710
            hbox:
                spacing 16
                textbutton '返回后日谈' id 'after_finish_hub' style 'navigation_button' action ShowMenu('afterstories') text_color '#653657' text_size 22
                textbutton '返回标题' id 'after_finish_title' style 'navigation_button' action Return() text_color '#653657' text_size 22

label after_wedding_start:
    $ afterstory_requested = 'wedding'
    jump afterstory_entry
label after_family_start:
    $ afterstory_requested = 'family'
    jump afterstory_entry
label after_departure_start:
    $ afterstory_requested = 'departure'
    jump afterstory_entry
label after_unremembered_start:
    $ afterstory_requested = 'unremembered'
    jump afterstory_entry
label after_ensemble_start:
    $ afterstory_requested = 'ensemble'
    jump afterstory_entry

label afterstory_entry:
    $ item_id = afterstory_requested
    $ after_item = next(i for i in AFTERSTORIES if i['id'] == item_id)
    if not afterstory_available(after_item):
        return
    if after_item['gate'] == 'any_ds':
        call screen new_if_notice(after_item['title'], after_item['note'])
        if not _return:
            return
    call expression after_item['label']
    $ setattr(persistent, after_item['flag'], True)
    $ renpy.save_persistent()
    call screen afterstory_finish(after_item['title'], item_id == 'ensemble')
    return

label ds_after_wedding:
    $ chapter = 'DeepSeek 后日谈 / 婚礼 · 两只碗'
    $ ds_wedding_detail = ''
    $ story_music('hyy_clear_rain')
    scene bg echo morning with dissolve
    $ hide_speaker_portrait = False
    $ deepseek_expression = 'shy'
    show sprite deepseek shy_wave as deepseek at sprite_breathe(0.72) with dissolve
    '恋人结局两年后。DeepSeek三十二岁，今天比你醒得早。'
    '院子里的桌布还没铺完，她先往你手里塞了半只饭团。'
    l_you '你不是说裙子的腰带刚刚好？'
    l_ds '这是你的。'
    '她另一只手藏在背后。尾巴替那只手挡得很认真。'
    l_you '你的半只呢？'
    l_ds '负责确认味道。已经确认完了。'
    '衣架上的白裙蒙着一层薄纱。她站在前面看了好一会儿，又低头去看桌上两只碗。'
    l_ds '那个大的换过去。'
    l_you '哪边？'
    l_ds '都在一桌了，还要分哪边。'
    '你把碗并在一起。她这回没有借机挪走大的，反而将两只碗的缺口转到背面。'
    l_ds '这点刮痕，拍照别拍得太清楚。'
    l_you '你上周还说是饭碗的资历。'
    l_ds '今天资历先休息一下。'
    'Qwen送来的喜糖用两个纸袋装着，一袋给宾客，一袋写着小字：别在入场前偷吃。'
    l_ds '她特意写给谁的？'
    l_you '不知道。先把你的手从袋子里拿出来。'
    '她把糖捏回袋底，转过身，背上的蝴蝶结歪了。'
    l_ds '你能帮我看一下？这个结。'
    menu:
        '问过她，再帮她把腰带的结摆正。':
            $ ds_wedding_detail = 'ribbon'
            l_you '可以碰这里吗？'
            l_ds '可以。慢一点，我不想重新系。'
            '你只扶住外层的缎带。她垂着手，等你把两边的长度调齐。'
            l_ds '好了没有？'
            l_you '好了。'
            l_ds '那也可以再等一下。'
            '她在原地多停了一小会儿，才转回来。'
        '把镜子拿给她，陪她自己调整。':
            $ ds_wedding_detail = 'mirror'
            '你扶稳镜框，让她能看见结的两端。'
            l_ds '左边？'
            l_you '你的左边。'
            l_ds '早说。我差点又给它多系一层。'
            '她调好缎带，却没有把镜子放下。两个人的脸挤在同一角里。'
            l_ds '这样也拍一张。'
    '门外传来MiniMax挪相机的声音。她没有闯进来，只问你们还要几分钟。'
    l_ds '三分钟。'
    l_you '哪一件事还要三分钟？'
    l_ds '紧张。'
    '她把手放到你的掌心边上，等你接住。手指有一点凉。'
    l_ds '前两年下雨那天，我说下班也一起。'
    l_you '记得。'
    l_ds '今天这个，会不会把下班也弄得很忙？'
    l_you '今晚不用招待到最后。我们先回去。'
    l_ds '说好了。别看见谁的灯歪了就留下来。'
    '她先用指节轻轻碰了一下你的手，像在确认这个约定听得见。'
    $ story_music('hyy_moment')
    $ hide_speaker_portrait = True
    call show_main_cg('ds_wedding')
    '院子的花被风吹向一边。她站在桌旁，亮出那枚刚戴好的戒指。'
    l_ds '看见了没有？'
    l_you '看见了。'
    l_ds '不是问灯。'
    l_you '戒指。很合适。'
    '她笑起来，尾巴碰了一下椅背，又立刻收回去。'
    l_ds '那你今天的名字旁边，要留我的位置。'
    '你把座位牌挪近。两只碗上方，两个名字没有写成一个。'
    '仪式结束后，有人想让她再站远一点拍全景。她看了你一眼，牵起你的手。'
    l_ds '这张不站远。'
    if ds_wedding_detail == 'ribbon':
        '你扶过的那只缎带结仍端端正正。她轻轻用背碰了你一下，没让镜头拍见。'
    else:
        '镜子里的那张合照还在你的手机里。她低声说，那张不放给大家看。'
    '晚些时候，客人去廊下听Grok唱跑调的祝福歌。你们在另一边坐下吃饭。'
    l_ds '我终于能说了。'
    l_you '什么？'
    l_ds '这个碗，刚才一直装少了。'
    '你把她的饭添到平平一层。她没有立刻吃，先将你面前也添满。'
    l_ds '今晚不抢你的。'
    l_you '今晚限定？'
    l_ds '……你先吃，别把条款念出来。'
    scene bg echo with dissolve
    $ hide_speaker_portrait = False
    show sprite deepseek happy as deepseek at sprite_breathe(0.72) with dissolve
    '回家的路上，她将花束托在另一只手里，牵着你的那只没有松。'
    l_ds '明天不用这么早起了吧。'
    l_you '不用。'
    l_ds '那第一顿早饭，先别叫我。'
    l_you '第二顿呢？'
    l_ds '一起吃。'
    return

label ds_after_family:
    $ chapter = 'DeepSeek 后日谈 / 家庭 · 第三只小碗'
    $ ds_family_detail = ''
    $ story_music('hyy_clear_rain')
    scene bg echo morning with dissolve
    $ hide_speaker_portrait = False
    show sprite deepseek neutral as deepseek at sprite_breathe(0.72) with dissolve
    '你们成婚第二年，DeepSeek把早餐端得比平时慢。'
    l_ds '先坐好。今天有件事。'
    l_you '锅又坏了？'
    l_ds '没有。也不是想换一只大的。'
    '她把检查单放到桌边，用饭碗压住最外面的角。'
    l_ds '以后这桌，可能要多一个人。'
    '你看了两遍纸上的名字。她的耳尖比热饭冒出的白气更红。'
    l_you '你刚才一个人在厨房想了多久？'
    l_ds '从米洗完开始。'
    l_you '怎么不叫我？'
    l_ds '叫你以后，饭就没人做了。'
    '你在她旁边坐下，没有伸手收走那张纸。她把筷子往你手里一放。'
    l_ds '先吃。吃完陪我把那只小柜子腾出来。'
    '你们没有一天把家里都改完。柜子腾出一格，又被她放进去两条买错大小的小毛巾。'
    '她曾半夜叫你看一眼洗好的小衣服。你醒了很久，第二天才发现她已经在椅子上睡着。'
    '生产那天下午，雨停在窗外。你听见孩子的第一声哭，看见她困得睁不开眼，却还想确认你有没有吃午饭。'
    l_ds '我的那份……别倒掉。'
    l_you '盖好了。等你。'
    '那顿饭后来又热了一次。你替她托好碗，她只吃了几口，手一直轻轻放在襁褓旁。'
    '小满的名字，由你们一起写在第一张照片背后。她写完又补了一笔：不用每次都吃得很满。'
    '婚礼五年后。DeepSeek三十七岁，小满四岁，已经会把饭锅的开关和家里的门铃分清。'
    '只有今天没有分清。'
    l_child '妈妈，饭在叫！'
    l_ds '那是门。谁家的饭站在门外？'
    'DeepSeek端着小碗走到门边，才发现自己也拿错了东西。'
    l_you '饭来接客？'
    l_ds '我正准备放下。'
    '门外没有客人，只有ZCode放在干燥格里的信。小满踮着脚想看邮戳，你把信递低了一点。'
    l_child '这只鸟是给我的？'
    l_you '先看名字。'
    l_child 'Deep……Seek。'
    l_ds '是给我的。你可以帮我拆开，不可以把鸟拆走。'
    '信里是Qwen寄来的新年茶袋。DeepSeek把茶收高一层，给小满留了一张印着小鸟的纸。'
    '孩子抱着纸去桌边，自己摆好第三只小碗。碗沿画着几条蓝色的小鲸鱼。'
    l_child '我的比较小。'
    l_ds '是。吃完还想要，我们再添。'
    l_child '不要堆山。'
    'DeepSeek看向你。'
    l_ds '昨天是谁堆的？'
    l_you '有人说像妈妈那样。'
    l_ds '妈妈今天也不堆。'
    menu:
        '和小满一起洗米，让DeepSeek坐一会儿。':
            $ ds_family_detail = 'rice'
            '你扶稳小盆，让小满的手够得到水。孩子把米洗得像在捞一片很小的海。'
            l_child '会跑掉！'
            l_you '沿着这里，慢一点。'
            'DeepSeek坐在桌旁，给下一封信剪开折边。她看了你们一会儿，没抢着把小盆接回去。'
            l_ds '漏掉的一粒，等下找给我。'
        '一起摆三只碗，让小满挑今天的位置。':
            $ ds_family_detail = 'bowls'
            '小满把自己的碗摆在你们中间，又觉得够不到凳子，拖着椅脚挪了半天。'
            l_ds '等一下。我们把桌子挪近。'
            '你搬过小椅子，她扶着桌沿。孩子抬头看两边，终于点了一下头。'
            l_child '这样。'
            l_ds '好了，今天不搬家了。'
    $ hide_speaker_portrait = True
    call show_main_cg('ds_family')
    '饭香从桌边升起来。DeepSeek侧身给孩子递小勺，另一只碗留在你坐下就能碰到的位置。'
    l_child '妈妈也吃。'
    l_ds '我有。'
    '小满还是给她夹了一小块萝卜，夹偏了，掉进你碗里。'
    l_you '送到了。'
    l_ds '送错了。'
    l_child '都是家里的。'
    'DeepSeek笑得差点让勺子碰到碗边。她把掉错的那块留给你，自己重新夹了一块。'
    l_ds '那你慢慢吃，家里的不会被谁抢走。'
    '午后，孩子趴在小桌上画鸟。DeepSeek把洗净的三只碗晾在一起，坐到你旁边。'
    l_ds '以前两只碗，也觉得架子很满。'
    l_you '现在呢？'
    l_ds '得换架子了。'
    '她用肩轻轻碰了你一下，眼睛却看着小满怎么给纸鸟补上另一边翅膀。'
    l_ds '小一点的就行。别又买到门都过不去。'
    scene bg echo morning with dissolve
    $ hide_speaker_portrait = False
    show sprite deepseek happy as deepseek at sprite_breathe(0.72) with dissolve
    '你们在购物单上写好尺寸，留着下午一起量。小满将纸鸟放进信格，写了一个还歪着的“家”。'
    return

label ds_if_departure:
    $ chapter = '独立IF / 远行 · 饭要趁热'
    $ ds_if_keepsake = ''
    $ story_music('hyy_mei')
    scene bg echo morning with dissolve
    $ hide_speaker_portrait = False
    show sprite deepseek determined as deepseek at sprite_breathe(0.72) with dissolve
    '这一页从另一种将来开始。北边的镇子要重新点亮整条街，DeepSeek接下了半年不能回家的工作。'
    '车票摆在两只饭碗之间。发车时间是七点零五，早得连茶屋的门都还没开。'
    l_ds '我带小锅，不带你那只。'
    l_you '那只盖子松。'
    l_ds '扎一下就好。'
    '她把锅收进袋里，又取出来，给盖子多绕了一圈绳。'
    '你帮她叠外套。袋里没有给纪念品留下空位，全是没开封的灯芯和一叠防水纸。'
    l_you '不是说那边都有？'
    l_ds '到了以后不一定找得到。别的可以晚一天。'
    '她指着装米的布袋，没把“别的”往里再塞。'
    '你们最后一顿晚饭比平时安静。她把盛多的饭挪回锅里，没有像从前那样非说自己吃得完。'
    l_ds '这些明早能热。'
    l_you '你不在家吃早饭。'
    '她的筷子停在锅沿。'
    l_ds '……对。那是你的。'
    '你将碗放回原处。她看着那个位置，又用纸巾擦了一下已经很干净的碗底。'
    menu:
        '把饭碗装进行李，家里留她的小钟。':
            $ ds_if_keepsake = 'clock'
            '她说一路会磕坏，还是接过你剪好的垫纸，绕了两圈。'
            l_ds '等我回来，你别把这只钟养得不走了。'
            l_you '会换电池。'
        '把饭碗留在桌上，替她挑一只轻便的新碗。':
            $ ds_if_keepsake = 'bowl'
            '新碗轻得她掂了两次。旧碗仍留在她那边，蓝色的缺口背着门。'
            l_ds '新碗也得多洗一遍。'
            l_you '知道。'
    '天亮以后，她背着袋子站在桥边，袖口压出一道红印。你问要不要替她提一会儿。'
    l_ds '现在不用。'
    '她说完，将袋子放到长凳上，空出手来抱你。'
    l_ds '现在用这个。'
    '你听见桥下水声，车站那边却已经有人催上车。她没有说一定很快，额头抵在你肩上，停到必须松开。'
    l_ds '等我找到住处，写地址给你。'
    l_you '我等。'
    '第一封信在第九天到。她画了一只新碗，画到一半嫌太小，旁边又补一只。'
    '第二封写着当地的米偏硬。第三封夹了一片叶子，说晚上风很大，锅盖总响。'
    '你按地址寄去了她忘带的厚袜子。那封回信隔了四十七天。'
    l_ds '收到。不是不回。白天回来就睡着了。'
    '最后半行被米粒留下的浅印压住。她没有擦掉。'
    $ story_music('hyy_far_smile')
    scene bg echo with dissolve
    hide deepseek with dissolve
    '半年到期的那天，街口的班车没有停下。你回家时，信格里躺着一只熟悉的信封。'
    '新桥还没通，收尾改到下个季节。她将旧车票贴在纸背，写了两次对不起，又划掉第二次。'
    '你站着看完，锅里已经咕嘟响了很久。'
    if ds_if_keepsake == 'clock':
        '小钟提醒了两次。你换过电池，却忘了把它从两点四十改开。'
    else:
        '她的碗还在桌上。你擦过缺口，以为新的一季总该用得上。'
    '你把饭盛到自己的碗里，不再给空位添满。然后坐下来写信。'
    l_you '我还是想你。今天特别想。'
    '后面一行是热饭的照片。你没有拍空着的座位。'
    '等到秋末，你收到了一个轻包裹。里面是她修好的那只锅盖，和一张折得很小的纸。'
    '她说该添的那圈绳已经拆掉，带回来的东西里，希望能先有一件真的回家。'
    '你把盖子按在锅上。没有再响。'
    '这一晚，桌边仍少了一个人。你将写到一半的回信放远，先把饭吃完。'
    return

label ds_if_unremembered:
    $ chapter = '独立IF / 遗忘 · 陌生人的一碗饭'
    $ story_music('hyy_mei')
    scene bg echo rain with dissolve
    $ hide_speaker_portrait = False
    show sprite deepseek neutral as deepseek at sprite_breathe(0.72) with dissolve
    '这是镇上没有发生过的另一种假设。回声灯断线之后，DeepSeek仍记得怎么煮饭、怎么修灯，却不再认识你。'
    '她坐在厨房的老位置，抬头问你是不是来领灯罩。'
    l_ds '蓝边那只还没干。先坐吧。'
    l_you '我不是来领灯罩。'
    '她把手擦在围裙边上，等你说完。你从口袋里取出一张被折软的纸。'
    '纸上有一只很胖的鲸鱼，写着“摸鱼许可证”。名字在鲸鱼肚子下面，两个都还在。'
    l_ds '是我的字。'
    l_you '你给我写的。'
    '她仔细看了一会儿，没有顺着你的话点头。'
    l_ds '那天我说了什么？'
    '你想起她午后嫌钟像开饭，想起她醒来揉眼时以为你没看见。能说的太多，第一句却说不出来。'
    l_you '你说只看一次时间。其他时候，连手也轮休。'
    '她笑了一下。与你记得的一样短，又不是给你的那一种。'
    l_ds '确实像我偷懒会说的。'
    '你也跟着笑，声音停在喉咙里。'
    '接下来一周，你每天都带一件旧东西来。灯牌、纸垫、她后来愿意一起吃的那只碗。'
    '她能找到每件东西的用途。灯牌下面松了一颗钉子，她顺手拧好；纸垫该晾干，她替你换了干净的。'
    '只有你放在旁边的名字，她问过三次。'
    l_ds '是不是以前很常来？'
    l_you '很常。'
    l_ds '那我可能一直没让你喝到热茶。'
    '她把茶端过来，放在你惯用的位置。你猛地抬起头。'
    l_ds '这边没有钉头，杯子不会晃。'
    '杯子停得那么准，你却迟迟没碰。'
    '第八天，你没有把新挑的照片拿给她。她已经会在门口认出你，又给你留了一把椅子。'
    l_ds '今天不用修？'
    l_you '不用。来吃饭。'
    l_ds '早说，我会多煮一点。'
    '她把自己的那一小半分过来，动作很快，像怕你看见缺了一块。'
    l_you '你够吗？'
    l_ds '饭锅里还有。'
    '饭锅已经空了。她假装没听见你揭开盖子的声音。'
    '你把分来的饭留下一半，另一半推回去。她皱了一下鼻子，终于把锅拿去添水。'
    l_ds '等一下。我刚才算错。'
    '窗外雨停了。你没有再问她想起来没有。你坐在厨房里，手握着那张已经空白的照片背面。'
    '旧日子没有因此回来。她也没有在最后一刻叫出只有你们知道的昵称。'
    $ story_music('hyy_far_smile')
    l_ds '下次想吃什么？'
    l_you '和今天一样。'
    l_ds '今天这个有点少。'
    l_you '下次多一点。'
    '她点头，将你的名字写到新的一张纸上。不是请她恢复的名单，只是一份明天的饭量。'
    '你将旧纸折好，放回口袋。站起来时，她跟到门边，仍很客气地说慢走。'
    '路过石桥，你第一次没有回头看厨房那扇窗。眼泪落在纸上，恰好盖住鲸鱼肚子下面的那个名字。'
    return

label ensemble_table_preview:
    $ chapter = '共同篇序章 / 一桌十二碗'
    $ story_music('hyy_clouds')
    scene bg echo morning with dissolve
    $ hide_speaker_portrait = False
    show sprite deepseek rice as deepseek at sprite_breathe(0.72)
    show sprite gpt as gpt at sprite_breathe(0.28)
    '这是一场公开约好的晚饭。来的人有十一位，DeepSeek却端出来十三只碗。'
    l_you '算错了？'
    l_ds '你一只，我们十一只。'
    l_you '还有一只？'
    l_ds '饭如果要加……先不洗它。'
    'Qwen把备用碗收进柜子，只留下十二只。Grok看着中间拼起来的两张桌子，将自己的牌子也搬来了。'
    l_grok '今晚R18。十二个人，一共十八包饼。'
    l_qw '饼我买的。也不是你那块牌子的意思。'
    'GPT想给座位画一张长卷，被Claude按住了还没摊开的纸。'
    l_cl '先吃。现在桌上没有纸的位子。'
    l_gpt '好。那今天先不把你们画成饭。'
    'MiniMax将关机的相机放在玄关。Kimi把两张大小不同的凳子调到能坐稳的位置。'
    'Gemini给每只碗旁边画了一颗纸星，画到第十二颗，手上还剩两张。她看了一眼DeepSeek。'
    l_gemini '不为备用碗预留。这个先讲好。'
    'GLM把一盆有叶子的绿植搬到窗边，没有加价。OpenCode只检查了一下拼桌的横板，就把工具箱关上。'
    'ZCode将准备很久的小纸条塞到信格。等大家动筷以后，她自己又取回来。'
    l_zcode '这次当面说。'
    '纸条写着一个提案：祭典以后，大家是否愿意每周留一天，一起吃饭。没有谁必须住进来，也没有预先填好的关系称谓。'
    l_you '先试四周？没空的那周，不用补请。'
    l_qw '买菜也轮着。'
    l_ds '煮饭可以叫我。洗锅别全写我。'
    l_grok '你连计划都还没看。'
    l_ds '我看得见。'
    '你们用十二只杯子投票。愿意先试的人把杯子摆在桌边；想再想的人留在手边，饭仍照样添。'
    '有一只杯子晚了半顿才放出来，没有人敲着桌子催。'
    '吃完以后，Claude将提案下面的“永久”划掉，留下下一次日期。GPT在空白处画了一张可以搬走的椅子。'
    l_you '以后如果喜欢上彼此，也当面说。'
    l_grok '先别替全桌答应。'
    l_you '嗯。一个一个问，一个一个听。'
    'DeepSeek端着剩下的饭走回来，将锅盖掀开。'
    l_ds '问的时候也能吃吧？'
    'Grok没有接这句，只先替ZCode拿过干净的小碟。窗外的灯一盏盏亮起来，下一次聚餐的日期还没有被谁擦掉。'
    '共同篇在这里留下一张新桌子。每个人独立的关系、嫉妒与协商，仍要在后续十一条线和共同篇中逐步写完。'
    return

