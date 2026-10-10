# Grok第八章《散场后有人等》。v0.9候选；未复制入当前game、未native验证。
# 继承第七章明确答复；仅空/非法答复的直接回看补三选一。
# 本章不注册全线结局、不解锁CG；root统一runner收取grok8_ending/grok8_complete。
default persistent.main_grok_ch08_seen = False
default grok8_answer = ""
default grok8_inherited = False
default grok8_activity = ""
default grok8_snack = ""
default grok8_near = False
default grok8_ending = ""
default grok8_complete = False

label grok_ch08:
    $ grok8_inherited = grok7_answer in ("love", "wait", "friend")
    $ grok8_answer = grok7_answer if grok8_inherited else ""
    $ grok8_activity = ""
    $ grok8_snack = ""
    $ grok8_near = False
    $ grok8_ending = ""
    $ grok8_complete = False
    call grok08_scene1
    call grok08_scene2
    call grok08_scene3
    call grok08_scene4
    call grok08_scene5
    $ grok8_ending = grok8_answer
    $ grok8_complete = True
    $ persistent.main_grok_ch08_seen = True
    return

label grok08_relationship_choice:
    # 自身helper，只在本存档没有有效第七章答复时call；不回写grok7_answer。
    l_grok "我想约你坐一会儿。不是叫你值班，时间我们自己说清。"
    l_you "那我也说清，想以什么身份来。"
    menu:
        "我喜欢你。今晚九点，想作为恋人来见你。":
            $ grok8_answer = "love"
            l_you "我喜欢你。今晚九点，作为恋人来见你。"
            l_grok "好。第十五日晚九点，院角。我会把营业的事先收好。"
        "我还没想好。明天下午见面，这次不交恋爱答案。":
            $ grok8_answer = "wait"
            l_you "我还没想好。明天下午有空，愿意见你，但不是交答案。"
            l_grok "第十六日下午，我先来问有没有空。你也可以改期。"
        "我想继续做朋友。白天一起坐坐就好。":
            $ grok8_answer = "friend"
            l_you "我想继续做朋友。白天一起坐坐就好。"
            l_grok "知道了。今天白天见，不把你的到场改成恋爱答复。"
    return

label grok08_scene1:
    $ chapter = "Grok 第八章 / 01 · 时刻写清，人才会来"
    if grok8_answer not in ("love", "wait", "friend"):
        scene bg echo morning with dissolve
        show sprite grok as grok at sprite_breathe(0.63) with dissolve
        "第十五日，院里还没有开摊。Grok把营业牌靠在桌内，向你留出能坐的位置。"
        "两人先讲清相处的身份，再各自安排今天的事情。Grok把手从杯子旁收回，等你开口。"
        call grok08_relationship_choice
    if grok8_answer == "love":
        scene bg echo with dissolve
        show sprite grok as grok at sprite_breathe(0.63) with dissolve
        "第十五日晚九点，你到了院门。Grok正把零钱放回收款盒，最后一位客人已经拿稳纸袋。"
        "她看见你，先报出还要做的事，没把人招进来才发现桌边又多了一位帮手。"
        l_grok "两只杯子和那盏小灯，还没归位。两分钟，能等吗？"
        l_you "能。我没打算从门口冲进去抢你的盘子。"
        "你说得轻松，手却还抓着随身袋。她没跟着回一句抢盘另收费，走到院门前。"
        l_grok "真不用抢。杯子明天洗也行，我现在先出来见你。"
        "她把门边能挡路的空篮推进桌下，自己跨过门槛。你松开袋绳，终于往里走了一步。"
        if grok8_inherited:
            l_you "你昨天说我来见你，你来见我。现在两边都到了。"
            l_grok "嗯。第一句先兑现，别让盘子抢走。"
        else:
            l_you "早上定的九点。你记得很清楚。"
            l_grok "自己想约的人，时刻也得自己记。"
    elif grok8_answer == "wait":
        scene bg river day with dissolve
        show sprite grok as grok at sprite_breathe(0.63) with dissolve
        "第十六日下午，你在河边理好自己的东西。Grok从桥那边走来，停在你身旁，先问现在有空吗。"
        l_you "有空。我今天想坐一会儿。"
        l_grok "那去院角？白天凉快。不是晚场，也没有答题台。"
        if grok8_inherited:
            l_you "昨天忙完很晚。没拿那段时间硬挤一场散步，挺好的。"
            l_grok "我昨天挑自己的李子去了。后天来问那句，没有偷偷挪成当晚九点。"
        else:
            l_you "昨天说的这次见面，只是见面。"
            l_grok "听清了。我想听你今天过得怎样，不是催那句没想好。"
        "她侧身等你收好袋口，没接过你还没整理完的东西。你们走回院子时，太阳仍照着门槛。"
        scene bg echo morning with dissolve
        show sprite grok as grok at sprite_breathe(0.63) with dissolve
        "营业牌靠在桌内，十八点那一行还没到。她给自己留的下午，确实没有装进今夜的订单。"
    else:
        scene bg river day with dissolve
        show sprite grok as grok at sprite_breathe(0.63) with dissolve
        "第十五日白天，你经过河边。Grok拎着一小包刚买的熟李子，问你要不要到院角坐坐。"
        l_you "要。今天只带自己来，没领工具箱。"
        l_grok "朋友入场也不查工具。能坐下就行，少一把螺丝刀没事。"
        if grok8_inherited:
            "她说话还留着一点慢，却能看着你笑。你没拿昨天的拒绝当成必须送礼赔偿的事。"
            l_you "你说白天可以来问。我今天也想问，所以来了。"
        else:
            l_you "早上把朋友说清了。现在就照这句坐。"
        l_grok "好。夜里的盘子还是我的，不收朋友陪洗费。"
        "你们绕过晒篮子的石阶，各拿好自己的袋子，走到院门。没有一路换成秘密约会的名字。"
        scene bg echo morning with dissolve
        show sprite grok as grok at sprite_breathe(0.63) with dissolve
    "Grok取出两只杯子，给你们各倒一点温水。小灯搁在外侧架上，营业牌的背面朝着院门。"
    "桌内的小本露出一角，她把它压稳，先把属于营业的东西收回去。"
    if grok6_settled and grok6_meet_set and grok6_supply == "ledger" and grok6_fulfilled == 4 and grok6_refunded == 6:
        l_you "那批十份的账，还留着原来的数？"
        l_grok "四份交出，六份退款。漏交的六份也在，没改成原来只卖四份。"
        "她翻给你看一眼，随后合本，手掌从写着份数的那一页挪回自己的杯边。"
    elif grok6_settled and grok6_meet_set and grok6_supply == "fetch" and grok6_fulfilled == 6 and grok6_refunded == 4:
        l_you "后来另买的两袋，没和退款挤在一起？"
        l_grok "分着。六份交出，四份退款；另买两袋的钱另记，原来漏单也还留着。"
        "她用手指点过两栏，将副联折好放回内袋，空出来的手把杯子推到你面前。"
    else:
        "她把今天领料的记录与私下买水果的小票分开，抹平纸角，合好小本。"
        l_you "今天该交的，你自己记；这包李子不用开成工单。"
        l_grok "是我的馋嘴小票。不能让它挤进客人的领料联。"
    "你们喝完温水。她把两只空杯放到同一只托盘，指向院内不挡路的小桌，问你想怎么坐。"
    return

label grok08_scene2:
    $ chapter = "Grok 第八章 / 02 · 两分钟，不必算帮工"
    if grok8_answer == "love":
        scene bg echo with dissolve
    else:
        scene bg echo morning with dissolve
    show sprite grok as grok at sprite_breathe(0.63) with dissolve
    "小桌旁有两把椅子，椅脚都落在平地。Grok拍掉座面两片碎叶，等你自己坐。"
    "外侧那盏带提环的小灯，夜里照过摊位，白天也一直占着出入的路。杯子则是你们刚喝空的两只。"
    l_you "我愿意收一件。不是为了换下一分钟。"
    l_grok "那我收另一件。结束就坐，不给你添一个隐藏任务。"
    "她先指清小灯要放的架子，又把洗杯盆挪到能站稳的位置。两件都不会把你拖进下一单营业。"
    menu:
        "提回摊前的小灯，让她归好两只空杯。":
            $ grok8_activity = "lamp"
            "你试了试提环，确认灯芯已经熄灭，才把小灯提到院内的小架上。Grok端着托盘去了水盆边。"
            l_grok "放低一格。我坐下来也能拿，不然明天又要叫高个客人续服务。"
            l_you "这一格？"
            "她点头，洗完第一只杯，冲掉杯口的水印。你退后看清路面，小架没有挡住椅子的去路。"
            if grok8_answer == "love":
                "她擦干两只杯，回到桌边才点亮小灯。光从你刚放好的那一格落下，够照手，也不晃眼。"
            else:
                "她擦干杯子，小灯仍熄着放在低格。白天的光够用，没有为了把下午改成夜约而点亮。"
            l_grok "好了。你收灯，我收杯，名单到这里就关了。"
        "洗好刚用过的两只杯子，让她提回小灯。":
            $ grok8_activity = "cups"
            "你端杯子到盆边。Grok提回小灯，先放稳在低格，再把托盘留到你转身就能放下的地方。"
            "其中一只杯口窄，你的指节碰到杯耳，差点让布卷在里面。她伸手按住盆沿，没有抢走杯子。"
            l_grok "布拆开一点。杯子没要求你把手也洗进去。"
            l_you "我看它太小，还想一次擦完。"
            "你摊开布，绕过杯耳擦净。两只杯各自倒扣片刻，水流完，再被你翻正放上托盘。"
            if grok8_answer == "love":
                "她点亮小灯，等你退开洗杯盆才去拿水壶。低格的光照着刚洗净的杯耳。"
            else:
                "她把未点的小灯放好，没有借收灯添一场夜间安排。杯子在日光下干得很快。"
            l_grok "好了。我收灯，你收杯。没有第三只突然报名。"
    "你们将擦过的布放到待洗处，空托盘归到桌内。水壶留在手边，路也空出来，两件活到此结束。"
    "Grok坐下时把怀表放回袋里。你看了一眼，不由得笑着说，好像今天自己的时间挺昂贵。"
    l_grok "你想说怕浪费吗？"
    l_you "怕说出来，听着像我在计较。"
    "她没有抬手给你一个贵宾表情。椅子在你旁边停稳，她把想抢先接的半句话咽回去。"
    l_grok "可以计较今天。刚才我说两分钟，就只用两分钟。"
    l_you "我不是要罚你。我只是有时候不想用一句没事，把想见的人让给所有别的事。"
    "你说到最后，手指已经松开。她的水壶提了一半，听完才放到桌边，拧开盖子。"
    l_grok "听到了。今天要坐的人，也有你。"
    "她将另一把椅子推到你能坐稳的位置，自己留着一段距离。你坐下，她也没有立刻问还有哪里需要修。"
    "院门外有人走过，两人都没有抬头招手。那一阵脚步过去，桌上仍是你们刚归好的两只杯子。"
    return

label grok08_scene3:
    $ chapter = "Grok 第八章 / 03 · 先挑自己想吃的"
    if grok8_answer == "love":
        scene bg echo with dissolve
    else:
        scene bg echo morning with dissolve
    show sprite grok as grok at sprite_breathe(0.63) with dissolve
    "Grok拿出今天买的熟李子，另外放下一块咸饼。果子已经洗好，两颗各包着新的薄纸。"
    "她拈出自己那颗，颜色深，靠果梗的地方还有一小点皱。放到掌心后，她不急着给你评分。"
    l_grok "这颗我先留。摊主说熟了，我想自己试。"
    l_you "会不会还酸？"
    l_grok "酸也先让我吃第一口。今天不拿客人的脸替我验货。"
    if grok7_walk == "bridge":
        l_you "桥边那颗，你还想看看里面会不会甜一点。"
        l_grok "今天换熟的。至少第一口不再赌了。"
    elif grok7_walk == "steps":
        l_you "坐石阶也没救那张皱起来的脸。"
        l_grok "石阶只管坐稳，不替水果改配方。今天挑的时候我问清了。"
    else:
        "她把果梗旁的皱点转给你看，让你分清自己留的那颗，再将余下一颗推到空处。"
        l_grok "另一个可以给你。饼也有，今天照自己胃口挑。"
    "咸饼被干纸包好，半点油都没蹭到水果。她要你先选一份，自己留好的那颗不会因此被算成赠品。"
    menu:
        "拿另一颗熟李子，陪她试试今天的甜味。":
            $ grok8_snack = "plum"
            "你接过另一颗李子，沿着干净纸角拿稳。Grok先咬自己那颗，嘴边没有马上皱起来。"
            l_you "今天真的甜？"
            "她点头，嚼完才答。果汁沾到拇指，她把手举离小本的位置，先拿纸擦净。"
            l_grok "甜。没有先安排你夸我，我也能宣布这个。"
            "你尝了自己的，告诉她果梗附近还略酸。她笑着点头，把剩下的咸饼包回去，留给自己之后吃。"
        "拿咸饼慢慢吃，让她把喜欢的李子留给自己。":
            $ grok8_snack = "cake"
            "你拿起咸饼。Grok没有说选错套餐，把另一颗李子重新包好，放进自己袋子的外层。"
            l_you "我今天想吃咸的。你慢慢尝那颗。"
            l_grok "好。朋友也好，恋人也好，都不能命令味觉统一出场。"
            "她尝了一口，满意地眯起眼。你掰饼时落下一小片，她拿空纸接住，不让碎屑滚到椅缝里。"
            l_grok "这片也能吃。捡完别再给它评选最感动落点。"
    "她将用过的薄纸与食物分开放，给干净的杯子重新倒水。拇指上的果汁擦净了，她才碰水壶把手。"
    "你们静了一阵。Grok看向背面朝外的营业牌，伸手把它靠稳，免得风吹倒，不往上添一句两人节目。"
    l_you "今天没有人来替你打圆场。"
    l_grok "我也没喊人。想知道你有没有吃饱，可以自己问。"
    "她问完真等了一下。你笑着说还没到需要加演的程度，发现自己又想把回答换成一句热闹。"
    l_you "吃饱了。我还想坐，不是因为盘子没洗完。"
    "Grok手指在杯沿停住。她看你，声音低了些，没立刻把这段停留命名成顾客续时。"
    l_grok "我听见了。也想留在这里。"
    "她从桌内抽出一张干净纸，本来想写个下次带什么，抬笔以后却没有落下。"
    l_you "你要给李子开回访表？"
    l_grok "差点。想问你下次来不来，一拿笔就想顺便列三件东西。"
    "她把笔盖好，纸仍留在桌内。今天已经做完的事不需要再写一遍，接下来的问句也不必夹在它下面。"
    l_grok "先把今天过完。下次想约，我直接说。"
    "你看着她终于空出来的手。杯子、纸和小本都放稳了，她的手背轻轻靠在桌边，指尖不再扣着袖口。"
    return

label grok08_scene4:
    $ chapter = "Grok 第八章 / 04 · 不用笑声替你回答"
    if grok8_answer == "love":
        scene bg echo with dissolve
    else:
        scene bg echo morning with dissolve
    show sprite grok as grok at sprite_breathe(0.62) with dissolve
    if grok8_answer == "love":
        "小灯只照到桌边。Grok看了看你旁边空出的宽度，没先把椅子拉过去等你承认已经靠近。"
        l_grok "我想挪过去一点，可以吗？今晚不是靠近就能多卖一份。"
        l_you "可以。我也想近一点。"
        "她把椅子移到侧边，让你的腿前还留着路。两只椅脚落稳以后，肩膀才轻轻碰到一起。"
        $ grok8_near = True
        if grok8_inherited and grok7_hand_held:
            l_you "昨天你的手有一点凉。今天暖了。"
            l_grok "今天握过杯子。还有一点紧张，没全洗掉。"
        else:
            l_you "你把手伸过来就好，不用先设计一个借东西的理由。"
            l_grok "那我真伸了。你想松开的时候也直接松。"
        "她掌心朝上，停在两人之间。你把手放上去，她接稳，拇指只轻轻挨着，没有把你扣到椅子上。"
        $ hide_speaker_portrait = True
        call show_main_cg('grok_after_close')
        l_you "刚才站在门口，我其实怕你又还没空。"
        l_grok "所以你先说不抢盘子。"
        l_you "那句比较好笑。说我怕自己不重要，听起来像要你马上证明。"
        "她没将你的手握得更紧来截断这句。等你说完，才抬眼看你，笑意也收得很慢。"
        l_grok "今天我确实有两只杯子没收好。但你来见我，我得先出来。刚才出来，是我想。"
        l_you "我看见了。不是要你再做一遍。"
        "她点头，肩头往你这边松了一点。你没有把这一下讲成看见关门就能获得拥抱。"
        l_grok "现在也想。还能这么坐一会儿吗？"
        l_you "能。我会告诉你什么时候该走。"
        $ hide_speaker_portrait = False
        scene bg echo with dissolve
        show sprite grok as grok at sprite_breathe(0.63) with dissolve
        "Grok低下头笑了一下，这回不用等旁人捧场。她把额前的发束拨开，露出能直接看你的眼睛。"
        l_grok "我以前真的能用三句笑话，讲出一百句不想让人发现的慌。"
        l_you "今天三句够用了，剩下的慌可以直接说。"
        l_grok "那我直接说。我想再见你，明天也想。可今晚先不拿明天抢位置。"
        "你轻轻回握。桌上有没吃完的东西，院门有各自回去的路，恋人的这一刻仍由两个人亲手留下。"
    elif grok8_answer == "wait":
        "午后的光从门槛移到桌脚。Grok把椅子摆在原来的距离，你没有被邀请挪进一个已经写好情侣名的位置。"
        l_grok "你今天还没想好。我知道，不用又从第一句讲起。"
        l_you "嗯。我今天愿意见你，和想成为恋人是两件事。"
        "她点头，给自己的杯子添一点水。你的杯还满着，她没有伸手把两只挪成一对。"
        l_grok "我有想早点听答案的念头。刚才想问，但不打算每次见面都拿它开场。"
        l_you "你能说这个。也不用为了等我，把其他下午都空着。"
        "她将怀表链理回袋边，告诉你一会儿要去挑一张自己喜欢的桌布，地点不在你们今天坐的院角。"
        l_grok "不是挑给你看的。我想换掉总沾油的那块，颜色也想自己选。"
        l_you "你选好了，下次有空我可以看。"
        l_grok "可以。不用夸好看来交作业。"
        "你们都笑了一下。笑完，她没有趁轻松把喜欢再问一次，你也没有答应一个自己还不知道的日期。"
        l_you "下一次我想见，会来问你。你有空再答。"
        l_grok "我想见也会问。你可以说今天不了。"
        "她停了一会儿，把原本想补的那句我总会等收回去。两人的时间都还在各自手里，没有全部抵押到同一天。"
        l_grok "现在这个下午，我过得挺高兴。说了也不需要你换个关系名。"
        l_you "我也高兴。今天没有把话说满，反而能真的坐下。"
        "她拿起自己的李子纸，折好果核包，放进袋外侧。她有要买的桌布，你也有晚饭前想做的事。"
    else:
        "白天的路仍很亮。Grok顺着你的目光看见院外岔口，把自己的椅脚收进桌边，给你留出起身的空间。"
        l_grok "朋友今天吃饱了，不能让它自动升级成恋人吃饱。"
        l_you "同意。也不升级成没话说的陌生人。"
        "她笑出声，先将杯子放稳。你没有为了逗回她的笑，补一句其实以后也许可以来掩掉明确的回答。"
        if grok8_inherited:
            l_grok "昨天那一点难过还没全没。不过今天想坐，是我今天的想法。"
            l_you "我不替你说已经没事。以后不想见的时候，也可以说。"
        else:
            l_grok "我今天想坐一会儿。以后想自己待着，也会直接说。"
            l_you "我听你实际说的，不把笑一下当成什么都答应。"
        "她将那张没写字的纸留回桌内，没有给你开一张永久朋友卡，也没用卡片规定你应该多待多久。"
        l_grok "一会儿我要去看新来的布摊。不是经营考察，我自己缺一块喜欢的。"
        l_you "我去帮自己的事，晚点找个地方吃饭。"
        l_grok "那各走各的。下次想一起逛，我先问。"
        "你告诉她自己在哪个时刻方便。她听完记住，不把今天你留了一会儿换算成必须接受下次邀请。"
        l_grok "也不是永远顺路。我想找朋友，绕一点路可以承认。"
        l_you "我今天也是绕来的，回去刚好走另一边。"
        "她挑眉，本来要给绕路收费，话到嘴边变成一句那就别走错。你们笑完，仍知道谁走哪一边。"
    "Grok看过桌面，两只杯都有能放稳的位置。她用指尖敲一下自己的杯耳，示意再喝完这一口，就按说好的时刻收好。"
    return

label grok08_scene5:
    $ chapter = "Grok 第八章 / 05 · 散场以后，各有明天"
    if grok8_answer == "love":
        scene bg echo with dissolve
    else:
        scene bg echo morning with dissolve
    show sprite grok as grok at sprite_breathe(0.63) with dissolve
    if grok8_answer == "love":
        "你们先松开手，各自端起杯子。她等你伸展开刚扣在一起的手指，才扶着椅背起身。"
    "你们喝完杯里的水。Grok把自己的杯子拿稳，再与你一同往洗杯盆边走。"
    if grok8_activity == "lamp":
        "你擦干自己这只，递给她。她将两只归到已经空出来的架上，你提回的小灯仍在低格。"
        l_grok "灯没挡椅子，刚才想靠近或者想起身，都不用先借路。"
    else:
        "刚才是你洗好杯子，这回她自己冲净两只，你站在盆边收稳托盘。没有把重复用杯算成你欠下第二轮。"
        l_grok "两只都放好了。你前面摊开的布，也没卷回杯耳。"
    if grok8_snack == "plum":
        "两颗果核各包好，新的薄纸已用过。没动的咸饼留在干纸里，她收入袋内，打算之后自己吃。"
        l_you "甜味试完了，饼还有自己的时间。"
        l_grok "对。不能因为我们坐得高兴，就逼它现在也陪着出场。"
    else:
        "你的咸饼已经吃完，她把自己那颗的果核包紧。没拆的另一颗李子还在外袋，打算留到回去再吃。"
        l_you "饼屑也收好了。没有被选的李子不用罚站。"
        l_grok "我带回去。明早想吃就吃，不用等你来确认它甜不甜。"
    "她把湿布归到待洗处，干净纸另放，没有将水果的小票插回领料联。桌面真的空了一段。"
    if grok1_private == "note":
        l_you "那张旧券还在我房里。今天没有带来要你添一次签名。"
        l_grok "留原样。它是那天的邀请，不是现在每次见面都要核销的通行证。"
    elif grok1_private == "cup":
        l_you "旧厚纸的水痕还留着半圈。今天没想把它拿来补圆。"
        l_grok "它就留那半圈。我们今天说清的，也不用冒充当时已经发生。"
    else:
        "你拿起自己的随身袋。Grok没有向里面找一件旧信物来替今天作证，只确认你没落下钥匙。"
    if grok4_first == "source" and grok4_old_leaflet_kept:
        "她拿袋子时，旧小报和补页仍夹在小本原处。今天的私人称呼没有被写上去，旧事也没有被撕掉。"
    if grok8_answer == "love":
        "你说到该走的时刻。Grok先把门边的路让出来，再和你一起走到院门。"
        l_grok "想送你到岔口，可以吗？我今天自己的事已经收好了。"
        l_you "可以。到了以后，你走回来的路也要看。"
        "她笑着伸出手，你接住。两人只走一小段。她迈出院门，先朝你看一眼，才把步子放快。"
        "岔口风凉，她把手收回袖边，站到你能看清的位置。你没有立刻松开眼神，等她也看回来。"
        l_you "明天想见你，我会来问。不是从今天自动续上。"
        l_grok "我也会问。晚了就告诉你，想多坐一会儿也自己说。"
        "你轻轻碰了一下她已经伸来的指尖。她这才低头笑，没把脸藏到营业牌后面。"
        l_grok "今晚有人等，我自己也来了。这个散场，挺好。"
        "回到院门前，她收起仍亮着的小灯。你走向自己的住处，知道下一次会听见她亲口说出的邀请。"
    elif grok8_answer == "wait":
        "第十六日的下午仍没过完。你拿好袋子，Grok也起身，要去把自己想买的桌布先看一看。"
        l_you "今天不需要交完一个答案才走。"
        l_grok "不用。该走了就是该走，不是我替你改成答应。"
        "她将你送到院门，没有借告别要求抱一下。你们各报一句自己接下来去哪儿，说的都是能实际去的地方。"
        l_you "下次想坐的时候，再来问。不是预订你一直等在这里。"
        l_grok "好。我可能去看花，也可能在开摊。问到就说清。"
        "你往河桥走，她沿院旁的小路去看布。那盏小灯没有点成晚九点的恋人约，午后的路也没有被改名。"
        "河桥上的风把你的袋角吹起来。你按住袋口再回头，Grok已到了布摊前，正抬手翻看摊前的布样。"
    else:
        "你们一起走到白天的岔口。Grok去布摊，你沿河回去，都有自己的方向，没有谁要装成留下才算善良。"
        l_you "那下次见，朋友。"
        l_grok "下次见。真想一起出来，叫我，不用先把杯子碰坏。"
        "你说不会，她笑着点头，先把落到眼前的发束拨开。路上有一小片树影，你们同时绕过，又同时回头看了一眼。"
        l_you "今天没把影子当水洼。"
        l_grok "很好。朋友散步，不靠湿鞋收尾。"
        "她在自己的路上先走几步，回身挥手。你也挥一下，继续走向另一边，没把背影读成一次没说完的告白。"
        "晚些时候你经过夜摊，Grok抬手招呼，先把眼前客人的饼包好。你站到队尾，她隔着两个人朝你扬了扬眉。"
    # 当前无CG：以上沿句动作只由实存背景与Grok基础立绘承载，不调用未知image、不空unlock。
    return
