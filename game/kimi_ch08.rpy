# v18接入：以下原稿保持冻结字节；旧候选阶段注释作为制作记录保留。
# 08 seen由main_opening_from仅在真实return True后写入；本文不设置正式路线旗标。
default persistent.main_kimi_ch08_seen = False
default kimi8_complete = False
default kimi8_ending = ''
default kimi8_reply = ''
default kimi8_has_ch07 = False
default kimi8_has_ch06 = False
default kimi8_breakfast_fix = ''
default kimi8_record_order = ''
default kimi8_approach = ''
default kimi8_hand_choice = ''
default kimi8_breakfast_met = False
default kimi8_breakfast_paid = False
default kimi8_breakfast_finished = False
default kimi8_new_stationery_bought = False
default kimi8_record_permission = False
default kimi8_bridge_met = False
default kimi8_hand_asked = False
default kimi8_hand_held = False
default kimi8_hand_released = False
default kimi8_solo_crossed = False
default kimi8_solo_returned = False
default kimi8_record_finished = False
default kimi8_public_card_exchanged = False
default kimi8_next_plan_agreed = False
default kimi8_relation_closed = False

# v0.18 Kimi第八章《书签朝向明天》独立正文候选。
# Kimi与玩家均为30岁成年人；无玩家立绘、无新CG/解锁/完成周目调用。
# 只继承本次实际第七章答复；runner/default/正式旗标接入见INTEGRATION_NOTES.md。
# 第十四日柜位册/灰套已归还；旧私人薄册与今天的新旅行册分开。
# 两张场景别名复用v17既有PNG，身份立绘仍为kimi_neutral。
image bg kimi08_shopfront_day = Transform('images/original/bg_event_shopfront_day.png', xysize=(1280,720), fit='cover')
image bg kimi08_stationery_day = Transform('images/original/bg_event_stationery_day.png', xysize=(1280,720), fit='cover')
# 当前45/95正文与Kimi7/8状态不因本候选改变；未native，不计完整线。

label kimi_ch08:
    $ kimi8_complete = False
    $ kimi8_ending = ""
    $ kimi8_reply = opening_relationship_answer("kimi")
    $ kimi8_has_ch07 = kimi8_reply in ("love", "wait", "friend") and kimi7_current_invited is True and kimi7_dessert_bought is True and kimi7_spoons_ready is True and kimi7_seat_reached is True and kimi7_book_put_down is True and kimi7_confession_spoken is True and kimi7_answer_spoken is True and kimi7_tonight_finished is True and kimi7_new_page_kept is True and kimi7_returned is True and kimi7_next_invitation_agreed is True and kimi7_next_invitation == kimi8_reply + "_breakfast" and ((kimi8_reply == "love" and kimi7_hand_asked is True and kimi7_hand_agreed is True and kimi7_hand_held is True and kimi7_hand_released is True) or (kimi8_reply == "wait" and kimi7_wait_accepted is True) or (kimi8_reply == "friend" and kimi7_friend_accepted is True))
    $ kimi8_has_ch06 = kimi8_has_ch07 and kimi7_has_ch06 is True
    $ kimi8_breakfast_fix = ""
    $ kimi8_record_order = ""
    $ kimi8_approach = ""
    $ kimi8_hand_choice = ""
    $ kimi8_breakfast_met = False
    $ kimi8_breakfast_paid = False
    $ kimi8_breakfast_finished = False
    $ kimi8_new_stationery_bought = False
    $ kimi8_record_permission = False
    $ kimi8_bridge_met = False
    $ kimi8_hand_asked = False
    $ kimi8_hand_held = False
    $ kimi8_hand_released = False
    $ kimi8_solo_crossed = False
    $ kimi8_solo_returned = False
    $ kimi8_record_finished = False
    $ kimi8_public_card_exchanged = False
    $ kimi8_next_plan_agreed = False
    $ kimi8_relation_closed = False
    if not kimi8_has_ch07:
        call kimi08_missing_history
        return False
    call kimi08_scene1
    call kimi08_scene2
    call kimi08_scene3
    call kimi08_scene4
    call kimi08_scene5
    $ kimi8_ending = kimi8_reply
    $ kimi8_complete = kimi8_breakfast_met and kimi8_breakfast_paid and kimi8_breakfast_finished and kimi8_new_stationery_bought and kimi8_record_permission and kimi8_bridge_met and kimi8_solo_crossed and kimi8_solo_returned and kimi8_record_finished and kimi8_next_plan_agreed and kimi8_relation_closed and (kimi8_reply != "friend" or kimi8_public_card_exchanged) and (kimi8_hand_choice != "hold" or (kimi8_hand_held and kimi8_hand_released))
    return kimi8_complete

label kimi08_missing_history:
    $ chapter = "Kimi 第八章 / 本次答复尚未接续"
    scene bg echo morning with dissolve
    $ main_cg = None
    $ hide_speaker_portrait = False
    "这份存档尚未接上本次第七章的当面答复。请从Kimi第七章继续阅读，再赴八点的早饭约。"
    return

label kimi08_scene1:
    $ chapter = "Kimi 第八章 / 01 · 这勺是辣的"
    scene bg echo morning with dissolve
    $ main_cg = None
    $ hide_speaker_portrait = False
    show sprite kimi as kimi at sprite_breathe(0.63) with dissolve
    "第十六日早上七点五十五，Kimi在院门内系好布袋。银白发尾压在袋带下，她停住，先把那一束抽出来。"
    "白裙外罩着平常的星月披层。昨晚那张小纸仍在旧私人薄册里，瓶子立在外兜。"
    l_you "我这回没带瓶盖当勺。"
    l_kimi "带了。还在瓶上。"
    "你看看自己手里的水瓶，把盖子拧紧。她将袋带挪到肩外一点，让头发不再跟着它走。"
    if kimi8_reply == "love":
        l_you "八点的第一次恋人早饭。"
        l_kimi "你提早了五分钟。第一次还没迟。"
        "她笑了一下，手仍在自己的袋带上。你站到门旁，等她确认鞋扣，才一起出门。"
    elif kimi8_reply == "wait":
        l_you "早饭以后，我想去河边走走。"
        l_kimi "我也有一条想走的。先吃饭。"
        "她看你一眼，把已经扣好的瓶盖又摸过一次，没有问你这一夜想出了什么。"
    else:
        l_you "我没替你点那一碗。"
        l_kimi "好。我想自己选。"
        "她站到门外，等你把自己的零钱收好。门边的人问你们去哪，她答去吃早饭，声音与平常一样。"
    scene bg kimi08_shopfront_day with dissolve
    show sprite kimi as kimi at sprite_breathe(0.63) with dissolve
    "八点，咸豆花摊前冒着白气。桌上有两罐配料，勺柄都朝外，旁边的馒头筐盖着干净布。"
    "Kimi先问分量，选一碗小的。你点自己的，她把自己的钱递给摊主，没有把两份合成谁请谁的一张账。"
    if kimi8_reply == "love":
        "摊主问是不是要坐同一桌。她点头，随后看向你，指尖轻轻碰过自己钱包的扣。"
        l_kimi "和恋人约了早饭。两碗分开算就好。"
        l_you "你昨晚说要自己告诉别人。"
        l_kimi "说了。现在告诉了一个。"
        "她耳边有一点红，仍把零钱数清。摊主指向空桌，她自己端起那碗，没躲到你的肩后。"
    elif kimi8_reply == "wait":
        "摊主给碗配了小碟。她拿起一碟腌菜，又放回半块，把剩下的留在自己碟里。"
        l_you "早上只吃这么一点？"
        l_kimi "先尝。昨天糖沉在下面，这回我先看。"
        "你各拿自己的一柄勺，她确认两柄都在，才往空桌走。昨晚尚未确定的答复没有变成一夜后的默认。"
    else:
        "摊主想替你们两碗都加同一种配料。Kimi将自己的那碗往旁边挪半寸，指向桌上另一个小罐。"
        l_kimi "我自己加。他那碗让他选。"
        l_you "朋友也得允许我吃得奇怪一点。"
        l_kimi "可以。别往我这里倒。"
        "你端起自己的碗，她捧稳她的，两人挑了能放下各自小碟的桌角。"
    $ kimi8_breakfast_met = True
    $ kimi8_breakfast_paid = True
    "她将布袋挂到自己的椅背，袋底离地一截。钱包收好，双手空下来，才转头去取配料。"
    "你想把自己的豆花碗挪近，指尖刚碰到热碗沿便收回。Kimi看见，先把自己的手巾垫在碗旁。"
    l_kimi "端的时候热，现在也热。"
    l_you "刚才记得，现在忘了。"
    "你用自己的手巾垫着挪好碗，碗放稳后才抽出手，没拿她那块去擦你桌边的汤。"
    "两罐颜色远看很像。她舀了半勺进碗，刚吃一口便停住，勺子落回碗沿，嘴唇抿了一下。"
    l_you "今天也先问早了？"
    l_kimi "这罐是辣的。"
    "她回身看标签。自己原本想拿的酱豆在左边，刚才手却伸向了右边的辣油。"
    l_you "要不要换一碗？"
    l_kimi "先救我这一碗。钱已经付它了。"
    "她喝过自己的水，把瓶子盖好。摊主听见，指指汤壶，说可以添一点清汤，也可以配一只新蒸的白馒头。"
    menu:
        "请摊主添一点清汤，慢慢尝她自己的这一碗。":
            $ kimi8_breakfast_fix = "broth"
            "她端着自己的碗回到摊边，请摊主添小半勺清汤。回来时碗满了一点，她双手捧住，没有再端去拿配料。"
            l_kimi "现在汤也来了。桌子等我一下。"
            "你将桌中间的空碟挪向自己这边。她把碗放稳，搅匀后只舀一小口，眉尖终于松开。"
            l_you "能吃了？"
            l_kimi "能。还是辣。今天慢一点。"
        "各买一只白馒头，她先吃两口再继续。":
            $ kimi8_breakfast_fix = "bun"
            "她买自己的馒头，你也另买一只。两只放在各人的小碟里，她先掰开一角，热气蹿到指尖。"
            l_kimi "这只也急。先凉一下。"
            "她把那一角放回碟边，吹了两次才吃。你伸手去碰自己的，也立刻松开。"
            l_you "你不是已经提醒了？"
            l_kimi "提醒了。手还归你管。"
    "八点二十，辣意退去一点。她端着自己的碗慢慢吃完，桌上没有一只换给你的碗，也没将失手的那勺推成你的口味。"
    "你吃完自己那份，把小碟送回摊边。她还剩最后一口汤，喝完才拿起自己的空碗，两人各交回碗、碟和勺。"
    if kimi8_breakfast_fix == "bun":
        "两只馒头也都吃完，筐边的纸袋没取走。她抹净指尖，才将钱包放回袋内。"
    else:
        "她用自己的手巾擦干碗底留在指尖的水，折好收到外兜，没有将湿角夹进册子。"
    "摊主问要不要替她留一碗明早的。她看了看还冒着气的锅，摇头，将已收好的手巾又往外兜推深一点。"
    l_kimi "明天来了再点。今天这碗够了。"
    l_you "你以前是不是也说过只要一点？"
    l_kimi "一点也有一整碗。你看，我吃完了。"
    "她把空出来的桌角让给新客人，侧身去拿椅背上的布袋。袋带被椅边勾住，她轻轻往回松，解开后才提到肩上。"
    l_you "它还想坐。"
    l_kimi "我想走。它跟着我。"
    "你先退到通道边，她自己将椅子收回桌下。刚才辣得停住的那一口没有变成整顿早饭的结尾，她站稳，向摊主道过谢。"
    l_you "今天准备记辣油？"
    l_kimi "想记。左罐右罐都写清。"
    l_you "下次只要记住左边。"
    l_kimi "摊主换位置呢？你准备抱着罐子守一夜？"
    "你朝那两只罐子看一眼，收回这个省事办法。她笑着戴好袋带，先让一位端碗的客人从桌旁过去。"
    $ kimi8_breakfast_finished = True
    return

label kimi08_scene2:
    $ chapter = "Kimi 第八章 / 02 · 新册先写名字"
    scene bg kimi08_stationery_day with dissolve
    show sprite kimi as kimi at sprite_breathe(0.63) with dissolve
    "八点四十，你们走到卖纸的小铺。Kimi用指尖摸过两种封面，选了一本能放进自己的袋平兜的薄册。"
    "她又拿两张空白路线卡、一条蓝色书签绳。你买自己的白卡和一条灰绳，钱分别付，找回的硬币也各收进各人的钱包。"
    "她出门才发现蓝绳的一头系得太短，纸孔旁只剩一小截，拉紧就快滑回去了。"
    l_you "它准备自己离职。"
    l_kimi "我让它站得太近。"
    "她解开这个结，重新留出两指长的绳尾。你拿自己的卡作比，才发现灰绳还没穿过纸孔，一直只缠在手指上。"
    l_kimi "你的还没上班。"
    l_you "我在等它自己找到孔。"
    l_kimi "那你等。我的先好了。"
    "你自己把绳穿过卡孔。她收回手，没有借走你的灰绳补自己的长度，蓝色那条终于稳稳留在她新册里。"
    $ kimi8_new_stationery_bought = True
    scene bg echo morning with dissolve
    show sprite kimi as kimi at sprite_breathe(0.63) with dissolve
    "九点，院廊的桌面已经擦干。你们回来坐一会儿，先把水瓶放到桌角，纸与湿杯垫分开。"
    "你从自己的袋里取笔，她打开她的笔袋，两支笔各放在各人的纸旁。"
    if kimi8_has_ch06:
        "公共柜外仍是借还目录。第十四日交给林杏的春季柜位册与灰纸套没有回来，她今天也没有去重新借。"
        "她取出自己平兜那张休息日地图，只确认折口完整，随即收回原处。旧私人薄册留在内层，今天新买的册子放到自己面前。"
        l_you "那张桥后的半页，今天要接着画？"
        l_kimi "我先走今天的。旧纸在袋里。"
    else:
        "公共柜外的借还目录留在原处。她没有取柜内的纸，只从自己的布袋拿出刚买的新册，旧私人薄册仍合在内层。"
        l_you "今天从这里起一页？"
        l_kimi "嗯。名字写我自己的。"
    if kimi8_reply == "love":
        "她在新册封里写Kimi，抬眼看你，笔尾指了指下一行。"
        l_kimi "这一本，我想拿来记我们出去玩的事。你也写名字吗？"
        l_you "写。旧薄册还归你。"
        l_kimi "嗯。那本我会自己收。"
        "她把今天新册推到桌中央，翻开第一张完整空页，用尺边比出左右两半。尺子拿走，笔仍在她手里。"
        l_kimi "我写左半。你写右半，可以吗？"
        l_you "可以。右半现在先归我写。"
        "她点头才将笔递来。你写下名字，将笔还回，她看了一遍，把两行字圈进同一个小方框。"
        "她没把旧薄册里的新纸搬过来。昨晚那张月下问话仍夹在她自己的册内，你能写的是她刚邀你写的这一本。"
    elif kimi8_reply == "wait":
        "她在新册封里写下Kimi，翻到第一页。你将自己的白卡放到另一侧，灰绳顺着卡角落在桌上。"
        l_you "这本你带着？"
        l_kimi "我带。你那张，给你自己。"
        "你点头，在自己的卡背写今天日期。她把两张空卡收入袋中，新册只铺在自己的半张桌上。"
        l_kimi "我想记今天走到的。你不必走成和我一样。"
        l_you "我想去河边的小码头看看。还没到，先不画。"
        l_kimi "我想过桥。各自到了再说。"
        "她将第一页往身边挪一点，好让你的卡不被压住。你拿起自己的笔，她也拿自己的，两人都没有替另一只笔落下路线。"
    else:
        "她在新册封里写名字，随后取出其中一张空白路线卡，另放在手边。"
        l_kimi "这本我自己写。这张卡，下午想和你交换。"
        l_you "想给我看哪一段？"
        l_kimi "走完再选。能告诉别人的那段。"
        "你翻过自己的白卡，写上日期，没写她的名字。她看见你留着空白，抬了抬眼。"
        l_you "我的也走完再选。现在换两张空纸，回去会认不出。"
        l_kimi "绳不一样。你别连绳都记丢。"
        "她在这张卡背记下今日日期，收进袋外的干纸兜，另一张空卡留作备用。自己的新册铺在内侧，与可交换的卡分开。"
    $ kimi8_record_permission = True
    "你的笔滚向桌边，笔帽却留在另一头。Kimi用新册背轻轻挡了一下，等你拿稳，才把自己的封面移回去。"
    l_you "谢谢。还没写就想走。"
    l_kimi "你给它这么长一张桌。"
    menu:
        "先写刚吃过的早饭，出去后再添亲自走过的路。":
            $ kimi8_record_order = "breakfast_first"
            if kimi8_reply == "love":
                "她在左半页画一只小碗，写辣油，旁边添上要看标签。你在右半写手碰到热碗，又把自己的名字圈大一点。"
                l_kimi "名字不用比碗大。"
                l_you "我怕下次只记得热碗。"
                "她将你还在写的纸角扶平，没有越过中线给你改字。你写完才放下笔，各自看一眼自己这一半。"
            else:
                "她在自己新册里写咸豆花与错拿辣油。你在自己的卡背写了早餐的小事，正面仍留给下午亲自走过的路线。"
                l_you "我写热碗这一下。"
                l_kimi "写你的手。碟没犯错。"
                "你补上是谁去摸，她合起自己新册，没拿来核对你是不是记齐了她那一勺。"
        "先把纸收好，回来后再写今天真正走到哪里。":
            $ kimi8_record_order = "after_walk"
            if kimi8_reply == "love":
                "她把今日日期写在页头，左右两半仍空。你收好自己的笔，将新册递回她手里，纸上没有提前画出的终点。"
                l_you "下午再各写半页。"
                l_kimi "嗯。别现在就把桥后的那一段画完。"
            else:
                "她只在新册页头写日期，扣好笔帽。你也收好自己的笔，卡正面没有路线，谁都没替还在袋里的水瓶记到码头。"
                l_you "带好它们，先出门。"
                l_kimi "你自己也要去。别只送纸。"
    "她将新册放进自己的袋平兜，蓝绳压在封面内，不垂到鞋边。旧私人薄册仍在另一层，两张路线卡都收到干纸兜。"
    "你将自己的白卡收入衣袋，灰绳沿卡背折好。桌上的尺子是她自己的，拿起来放回笔袋，没有借公共木夹留一摊纸。"
    return

label kimi08_scene3:
    $ chapter = "Kimi 第八章 / 03 · 桥头等人"
    scene bg echo morning with dissolve
    show sprite kimi as kimi at sprite_breathe(0.63) with dissolve
    "九点二十，门旁挂着今日的天气小牌。Kimi看过晴字，抬头却看见远处有一块薄云，便往袋里又放一条自己的手巾。"
    l_you "牌已经说晴了。"
    l_kimi "云没看牌。"
    "她摸摸瓶盖，确认水装够。你检查自己的，盖子拧得太牢，拧开时手腕轻轻一弹，水沿瓶口晃到指上。"
    l_you "它比昨晚更认真。"
    l_kimi "你也更用力了。"
    "你擦干手，将瓶子重新盖好。她收起自己的手巾，没有拿你这点水去湿刚写好的页。"
    "今天两人的布袋都装着自己的东西。院廊的工作夹板仍靠在公共柜外，Kimi经过时没有把它提起来。"
    l_you "你上午还要查柜子？"
    l_kimi "今天没有新借的册。我想先过桥。"
    "她看向门外，把袋带调到不会磨脖子的长度。你将自己的卡摸过一次，没有去摸她平兜里的新册。"
    l_kimi "十点桥头。到了还想坐一小会儿。"
    l_you "我想买副鞋带。旧的起毛了。十点前够买好。"
    l_kimi "记得比长度。别买一条来绑两只鞋。"
    l_you "我会数。先从这里一起走，还是各走过去？"
    "她用鞋尖拨开门槛边的一粒小石，先退到能让人进出的地方，才听你说完。"
    menu:
        "一起走到桥头，到了再分开走自己的那一段。":
            $ kimi8_approach = "together"
            l_you "先一起走。你想从那条有屋檐的街过去？"
            l_kimi "想。那边石缝少，裙边也少沾一点灰。"
            "你们把各自的门边物拿齐，一起沿有屋檐的街走。她没让你拎袋，走过青石缝时自己提了提裙边。"
            "一家小铺正在开门，门板压住半张地垫。她先停住，等店主移开，才绕过去。你险些跟着停到她鞋尖上。"
            l_kimi "我的鞋还要过桥。"
            l_you "我先放它过去。"
            scene bg river day with dissolve
            show sprite kimi as kimi at sprite_breathe(0.63) with dissolve
            "她瞥你一眼，走到更宽处才笑。九点五十，你们到了桥头，在近岸长石旁各放下自己的袋子。"
            l_you "还有十分钟。"
            l_kimi "够坐。你别拿这十分钟去追云。"
            "两人坐在长石的不同位置。她喝自己的水，随后把瓶盖扣好，袋子重新提回自己脚旁。"
        "各自到桥头，十点见；我先去街口买自己的鞋带。":
            $ kimi8_approach = "separate"
            l_you "我先去街口买。十点桥头见。"
            l_kimi "好。我从有屋檐的街过去。"
            "她将自己的袋带挂稳，向你点一下头，先往她选的街口走。你等她走出门外，才往自己选的小铺去。"
            hide kimi with dissolve
            scene bg kimi08_shopfront_day with dissolve
            "你看看鞋上这副旧绳，向店主问清长度，选下一副新的，当面付清钱。店主包好，你放进自己的袋中，沿近岸走向桥头。"
            scene bg river day with dissolve
            show sprite kimi as kimi at sprite_breathe(0.63) with dissolve
            "十点，Kimi已经在长石边，正把自己的裙边从袋底抽出来。她见你来了，先看看你仍穿着的旧鞋带。"
            l_kimi "买好了？"
            l_you "在袋里。先别在桥头换。"
            l_kimi "嗯。先找平地方，别踩着鞋带过桥。"
            "你坐到她留出的另一块干石面，纸包仍在自己的袋里。她喝完自己的水，盖紧瓶子，没有问你在街口说过每一句话。"
    $ kimi8_bridge_met = True
    "十点十分，桥上的行人稀下来。她起身看了一眼近岸的路牌，再坐回去，新册还没取出。"
    l_you "打算从哪一边过去？"
    l_kimi "桥上。旁边那道浅水，我今天不试。"
    "你指的是栏边步道，被她轻轻拆穿。她用鞋尖在干处点一下，随后认真指向对岸的小路。"
    l_kimi "过桥后，我想自己往石亭那边走。"
    l_you "我到这边的小码头。"
    l_kimi "午饭各自吃。下午三点回院门，你还方便吗？"
    l_you "方便。如果我要改时间，先回来留话。"
    l_kimi "我也会说。别让人一直坐门口。"
    "她从自己的笔袋拿出铅笔，在一张空卡角上写三点院门，紧接着在旁边画个小空圈，留下尚未到的那一处。"
    l_you "这里不用实圈？"
    l_kimi "下午再填。现在只约在这里。"
    "她把这张只写碰面安排的备用卡收好。你也在自己的卡背空角写三点，铅笔点到纸上，留下一个比字还重的小点。"
    l_kimi "你这个点，像已经回来喝过水。"
    l_you "笔比我先到了。"
    "你把点改成一只小水杯，日期仍写今天。她低头看了一眼，没把自己的空圈照样涂实，卡收回各人的地方。"
    "桥对岸有人推开石亭旁的窄门，门板反过来遮住一截窗。Kimi往那边看了很久，才把视线移回来。"
    l_you "想去看那扇窗？"
    l_kimi "想坐在旁边。以前从这边看，只看见树。"
    l_you "到了就能知道窗外有什么。"
    l_kimi "也可能还是树。我还是想去。"
    "她用鞋底轻轻擦掉长石上的一点沙，靠近桥口的那只脚往外挪了半掌。她今天挑的地方没有换成你比较熟的那边。"
    l_you "那你先挑你的位置。我到码头，也看看是不是真有地方坐。"
    l_kimi "别把墙画成椅子。你会坐疼。"
    "你望了望岸边那道矮墙，收回已经想靠过去的手。她笑过，等一位提篮的人走出桥口，才慢慢把腿边的袋子拢好。"
    return

label kimi08_scene4:
    $ chapter = "Kimi 第八章 / 04 · 走到我想去的那边"
    scene bg river day with dissolve
    show sprite kimi as kimi at sprite_breathe(0.63) with dissolve
    "十点二十，河面有一条窄亮线。Kimi把两只鞋都放到干的石面上，看一阵水，又看看你。"
    if kimi8_reply == "love":
        call kimi08_love
    elif kimi8_reply == "wait":
        call kimi08_wait
    else:
        call kimi08_friend
    "十点四十，她将自己的瓶子收进袋外兜，扣好干纸兜。新册在平兜里，旧私人薄册在内层，双手都空出来。"
    if kimi8_reply == "love" and kimi8_hand_choice == "hold":
        "刚才牵过的两只手已经松开。她低头确认裙边没有踩在鞋底下，才用自己的手调好肩带。"
    else:
        "你把自己的水瓶收入袋里。她自己调好肩带，两人之间没有一件一定要一起拎的东西。"
    l_kimi "我过去了。三点在院门。"
    l_you "好。你到石亭以后，想歇就歇。"
    l_kimi "我会。你也别只看船，忘记吃饭。"
    "她迈上桥面，步子比刚才进早饭摊时慢一点。到了桥中，她停下看过右侧河水，再继续走向对岸。"
    "走到桥中段，一片小叶子被风推到她裙边。她停在栏杆内侧，用空着的左手将披层压回腿旁，再往前走。袋子一直在她自己的肩上。"
    "桥上过来一个提空筐的人。Kimi先让到宽些的那块桥板，等筐角过去才继续。她没有退回近岸，脚下的步子也没为了抢先加快。"
    "你留在近岸，看见她自己走完桥的最后一段。她踏上对岸平地才回头，抬起右手挥一下。你回了一下手，她放下右手，再转向想去的小路。"
    $ kimi8_solo_crossed = True
    hide kimi with dissolve
    "她的白色裙边很快被转角遮住。你没跟过去，也没给看不见的那段补上风景，提起自己的袋子往近岸小码头走。"
    "码头没有你早上猜的那条长木栈。岸边只是三块宽石，你站到干处，看一只空船被绳子拉回原位。"
    l_you "还好没把栈桥画进卡里。"
    "你在自己的白卡正面画下三块石，旁边写近岸，小绳结画得太大，又重新缩成一小点。"
    "你添上刚才那只空船。船头一笔走偏，挤过第三块石，船在纸上成了码头两倍长。你翻到卡背看看，正面却已经写了近岸，只好把这只大船留下。"
    l_you "船在水里。石头在这边。先写清。"
    "你在船旁添一个小水字，收回笔。真船碰上岸石，船绳一紧又松，纸上那一只没有替它开往别处。"
    "十一点半，你去码头旁的小摊买自己的午饭，点一碗面。摊主问加不加葱，你看一眼罐上贴的字，先确认清楚才答加。"
    "找零和午饭钱当面数清。你坐在摊边，水瓶放到自己凳脚内侧，白卡留在衣袋里，免得碗沿的汤碰上去。"
    "吃到一半，你摸出卡，发现手指刚沾过油，便用纸擦净，把卡重新收好，等吃完才再拿。空碗交回，水瓶也提走，没有借空船当自己的桌子。"
    "卡面只记你亲自走到的小码头。远处石亭的路没有被你画进去，也没有因为下午要见她就替她完成自己的页。"
    if kimi8_approach == "together":
        scene bg kimi08_shopfront_day with dissolve
        "午后，你路过街口小铺，才去买早上说过的鞋带。你问清旧绳的长度，选好新的，付清这一副的钱，将纸包收入袋中。"
    else:
        "午后，早上买好的鞋带纸包仍在自己的袋里。你摸到包角，收紧袋扣，沿原路回院。"
    scene bg echo with dissolve
    "回到院里，你在自己的房门前换好这副鞋带，把旧的收在纸包内。碎纸也一并带进房间，没落在廊边。"

    return

label kimi08_love:
    "Kimi把袋子提到自己脚内侧，坐回长石。她取出今天的新旅行册，蓝绳的一角露在封面下。"
    l_kimi "我现在想把刚才这段先留下。你那一半想写吗？"
    l_you "想。我们坐稳了再拿笔。"
    "她把册子摊在自己膝上，你将自己的水瓶盖紧放进袋里。两人的手都擦干，她才把新册放到中间那块干石面上。"
    "她从笔袋取出自己的笔，你也拿出自己的，笔帽各留在各人的膝边。"
    if kimi8_record_order == "breakfast_first":
        "第一页左右都写过早饭。她在左半空处添桥头，你在右半写一起坐到十点二十，没有擦掉她那一勺辣油。"
        l_you "早饭占得比这段路多。"
        l_kimi "路还没走完。它先等等。"
    else:
        "第一页只有日期。她在左半记早饭与错拿配料，你写自己的热碗，再在右半添了桥头坐下。"
        l_kimi "那一下你记住了。"
        l_you "手帮我记的。"
        "她笑过，用指尖比了比右半那行字。左右两半的字大小不同，她在自己的左半添完这一句，便停了笔。"
    "你写完自己的半页，扣好自己的笔帽。她看见右半只剩一小块空处，用自己的笔尾指了指下一张。"
    l_kimi "后面还有。别把午饭写到字缝里。"
    l_you "以后每次出去都要写？"
    l_kimi "我想写再写。你那半也一样。"
    "你点头，没有先替她把下一页标满日期。她把笔扣好，新册合回封面，蓝绳压在今天这一页。"
    l_kimi "第十九日下午，我想去北坡看看。听说那里有卖梨的。"
    l_you "一起去？"
    l_kimi "想和你去。还没吃过，也没走过。"
    l_you "我有空。午饭后在院门碰面，路上要是累了就改走短一点。"
    "她重新翻开新册，拔开笔帽，在下一页写第十九日、午后、北坡。三项旁边只留空圈，没有把听说过的梨画成已经买到。"
    l_kimi "这个先约好。我出发前还会来问你。"
    l_you "我也会告诉你当天能不能照原来走。"
    "她应一声，扣好笔帽，将笔收回袋内，再把新册放进自己的袋平兜。旧薄册没取出，她压好袋扣，手指从封面离开，停在自己膝上。"
    $ kimi8_next_plan_agreed = True
    l_kimi "现在，想牵一小会儿。可以吗？"
    $ kimi8_hand_asked = True
    "她将右手掌心朝上，放在自己膝边，没有先合住你的手。你坐稳，左手仍空着。"
    menu:
        "可以。我把左手给你，在这里坐一会儿。":
            $ kimi8_hand_choice = "hold"
            l_you "可以。我也想。"
            "你把左手递过去。她轻轻合住指尖，先看着你笑，再将自己的右手落到两人中间。"
            $ kimi8_hand_held = True
            l_kimi "今天手没拿勺。"
            l_you "也没拿笔。先放着。"
            "河风将她的披层下摆掀起一小截。她用空着的左手按回腿侧，你没有握紧右侧那只来替她固定衣服。"
            "你们坐到桥头阴影越过小半块石面。她看看时刻，先松开指尖，让你的左手也落回自己膝边。"
            $ kimi8_hand_released = True
            l_kimi "好了。我还想走自己的那段。"
            l_you "三点再见。我也去我的。"
        "今天先并坐。手留给自己，陪你看一会儿水。":
            $ kimi8_hand_choice = "sit"
            l_you "今天先这样坐。我想和你看一会儿。"
            "她听见，把右手收回自己膝上，掌心轻轻搭住白裙边。她没拿第七章那次牵手来追问。"
            l_kimi "好。那你看这边。"
            "她指向水上被桥影分开的亮线，你顺着看去，终于发现那只小船刚才一直只是绕着同一个绳结转。"
            l_you "我以为它要出门。"
            l_kimi "绳没解。你替它想得太远。"
            "你笑着坐回去。她也笑，直到自己想出发才提起袋子，这一回没牵手的上午仍是你们约好的恋人早饭。"
    return

label kimi08_wait:
    "Kimi把自己的布袋提回膝上，取出今天的新册和自己的笔。蓝绳从她自己写过的名字旁边露出一小角。"
    if kimi8_record_order == "breakfast_first":
        "早饭那一页只写过她自己的事。她添桥头坐一会儿，笔尖停在下一行，没有把你去码头的路接到她后面。"
    else:
        "她在新册第一行写辣油，再写早饭后坐到桥头。你将自己的卡留在自己膝上，没有看她尚未写的下半页。"
    l_you "你那条石亭路，想走多远？"
    l_kimi "到了看。我中午想坐着吃饭。"
    l_you "我也还没想好在码头坐多久。"
    l_kimi "那就不用先跟齐。"
    "她扣好笔帽，新册收回自己的袋平兜，旧薄册仍在内层。你将自己的卡收入衣袋，两只水瓶各回各的外兜。"
    "她看了你一会儿，手指沿着袋边的一根线往回捋。线头早已压住，她捋到末端才停。"
    l_kimi "昨晚那句话，我今天还会想。"
    l_you "我今天还是没确定。"
    l_kimi "嗯。听见了。"
    "你没有把手伸过去，她也没有伸手等你接。河边的船碰过岸石，两人一起朝那声轻响看了看。"
    l_you "你想让我今天少说一点吗？"
    l_kimi "这句说清就够。我还想说午饭。"
    "她取出自己的小零钱袋，摸到钱包才发现新册的蓝绳尾被压在袋扣下面。她松开扣子，把绳收进平兜，重新合严。"
    l_you "它今天第二次想走错门。"
    l_kimi "我第二次放错。别只算它。"
    "你笑了一声，她也笑。刚才她说还会想的那句话留在两人之间，没有被一声笑改成已经不在意。"
    l_kimi "这个月我想找一个上午，自己去更远一点。还没选日子。"
    l_you "你定了以后，想告诉我再告诉我。"
    l_kimi "嗯。你也可以先走你的。"
    "她看向桥对岸，紫色眼睛在日光里亮了一点。你把脚从桥面入口前挪开，给准备过桥的人留出路。"
    l_you "以后我想约你，会先问当天有没有空。"
    l_kimi "可以。有空也可能想自己待着，到时我会说。"
    l_you "我听你的答复。也会把我想好的那句当面说。"
    "她点头，没有替你写一个最后期限。你们已经说定下午三点，那是今日碰面的时刻，纸上也只有今日的日期。"
    l_kimi "三点回去喝水。今天先把这个走完。"
    l_you "我会来。你要多走一段，记得先留话。"
    l_kimi "你也是。船不用你一直陪。"
    "她合好自己的小零钱袋，收回布袋内侧。待桥口两个人走开，她把脚挪到干石上试了试鞋底。"
    $ kimi8_next_plan_agreed = True
    return

label kimi08_friend:
    "Kimi把空路线卡取出来，在自己膝上转过一面。纸上只有今日日期，没有从你的卡背抄来的字。"
    l_you "现在交换吗？"
    l_kimi "先留着。等我真走过去。"
    "她收回自己的卡，看着桥对岸，抬手把披层袖边拉离袋扣。布料又滑回去，她把袋带换到稍外的位置才停。"
    l_you "这条带子也想跟你走里面那段。"
    l_kimi "它已经跟着。我不想让袖子也挤过去。"
    "你将自己的袋带往肩外调一点，差点把整只袋子提到胸前。她看过来，嘴角先动了一下。"
    if kimi8_approach == "separate":
        l_kimi "你慢点。鞋带还在里面。"
    else:
        l_kimi "你慢点。卡还在里面。"
    l_you "没给它赶下船。"
    "她笑一声，用自己空着的右手扶正K字链。你把袋子放回腿边，各自喝过一点水，才继续说下午的事。"
    l_you "你想给我那张卡画石亭？"
    l_kimi "如果走到了。桥上那段也能画给你。"
    l_you "我会给你码头这边。自己画的，难看也别退。"
    l_kimi "难看可以说。纸还归你画。"
    "你答应了，灰绳从自己的卡角落到衣袋内。她将蓝绳留在自己新册里，没有给两张将交换的卡系成一对。"
    "近岸来了一个端茶的人，只向你们问哪边能坐。Kimi指指长石另一头，随后把自己的袋子收近膝边。"
    l_you "下午回来，还想在这里坐？"
    l_kimi "今天回院门。晚上我想自己泡茶。"
    l_you "我也有要做的，先回自己的那边。"
    "她听见，手掌在自己的袋口停了一下，然后轻轻点头。你没有改口把两件各自的事又排成必须一块做。"
    l_kimi "你昨晚说朋友。我按这句跟你约。"
    l_you "嗯。我没有等你把喜欢忘掉才过来。"
    "她看向你，眼睛没有躲开。风把银白发尾吹到肩前，她慢慢理回去，留出一小段安静。"
    l_kimi "还没那么快。可我想吃早饭，也想走桥。"
    l_you "今天都可以走。你不用替我加别的事。"
    l_kimi "那你也别替我把下午画满。"
    "你举起还留着空面的卡，她看见，嘴角又有一点笑。两个人将各自那张收好，没有交换尚未发生的路线。"
    l_kimi "下次我想去你常走的那条街。你有空再带路。"
    l_you "可以。到时候我先告诉你，我想在哪家吃。"
    l_kimi "好。我也会挑自己那碗。"
    "你们说的是下一次朋友间的出门。没有加上改口答应恋爱的附注，今天三点的院门仍是今天这一次的约。"
    $ kimi8_next_plan_agreed = True
    return

label kimi08_scene5:
    $ chapter = "Kimi 第八章 / 05 · 书签留在今天"
    scene bg echo with dissolve
    show sprite kimi as kimi at sprite_breathe(0.63) with dissolve
    "下午两点五十五，你将换好的鞋带系紧，走到院门。Kimi从另一边回来，布袋仍在自己肩上，瓶子里只剩一小口水。"
    l_you "我刚到。"
    l_kimi "我还差五分钟。先到了。"
    "她低头看看鞋底，绕开门前的湿石，自己跨进廊下。你让出门口，她把袋子放到自己的椅边才坐下。"
    $ kimi8_solo_returned = True
    "她先将自己的水瓶放到桌角，取自己杯子接水。你也给自己倒半杯，纸留在干的那一边，没人先替另一张找终点。"
    l_you "石亭到了？"
    l_kimi "到了。先以为石墙后面就是，绕过去才看见还隔着一条路。"
    l_you "有没有把那堵墙画成亭？"
    l_kimi "画了半道。到了以后改回墙。"
    "她自己笑了一下，指尖摸到纸兜，先取那张只写三点院门的备用卡，在空圈里添了一点。"
    l_kimi "这个到了。水也喝了。"
    "她把卡收回干纸兜，才拿今天新买的册。旧私人薄册仍合在内层，第十五日的小纸没有被翻给你补写。"
    if kimi8_reply == "love":
        "新旅行册翻到今日这页。左半已经记早饭与桥头，右半也有你坐下的那一句，蓝绳留在两半之间。"
        l_kimi "我想告诉你石亭那段。能写在左边，还剩一小块。"
        l_you "我写码头这边。三块石，比画的船还宽。"
        "她从笔袋取出自己的笔，你也拿出自己的。她先写左半的路，告诉你到石亭以后坐了二十分钟，中午买一份热饼。你写自己的那三块石与吃完午饭才拿卡，没有将她的路补到右半。"
        l_kimi "你的船画大了。"
        l_you "你今天不负责替它改。"
        l_kimi "我先说。下回你还想画大的，也行。"
        "你看着自己的那只大船笑，没把纸撕掉。她将新册转回自己这一侧，等墨干了才合上。"
        "第十九日那页仍只有约好的日期、午后与北坡，空圈没有被今日的石亭填上。她翻回今天，蓝绳夹稳。"
        l_you "这本先由你带着。下次我想写右半，就当面拿给我。"
        l_kimi "好。我会带。你也带你自己。"
        "她将新旅行册收入自己平兜，旧私人薄册仍在另一层。两种封面分开，她指尖摸过扣子，确认都没压住绳尾。"
        l_kimi "今天喜欢你。也走了我自己想走的路。"
        l_you "我也喜欢你。下次一起出门前，先问你想去哪。"
        "她看着你笑，脚尖在自己的椅子下轻轻挪了一下。杯子还没喝完，她端起来，又给自己添一点水。"
    elif kimi8_reply == "wait":
        "她翻开自己新册，在早饭那页之后另起一行。你取出自己的卡，两张都只向各自的主人展开。"
        l_kimi "我在石亭歇了二十分钟。还想多走，先饿了。"
        l_you "我在码头也先去吃午饭。船还留在那里。"
        "她取出自己的笔，写下吃饭的位置，把先前绕错的墙线留在旁边。你在自己的卡背补上午饭的位置，没有替她挑何时再走更远。"
        "她将蓝绳夹到自己刚写完那页，册子收进自己平兜。你的灰绳仍系在自己的卡角，卡也回到你自己的衣袋。"
        l_kimi "下午没等到你带回答案。可等到你人了。"
        l_you "我没确定的那句仍在。今天三点这一句，我答应了。"
        "她点一下头，端杯喝水，杯底在桌上落得轻。你也喝过自己的，没有用替她拿册子或握她手给尚未答出的恋爱作答。"
        l_kimi "下回我想叫你，会再问。也会自己出去。"
        l_you "我想约你，也会先问。我们都可以改时间。"
        "她把椅子往自己这边收半寸，避开脚旁袋带。你站起，将自己的杯子带走，她仍坐着喝完余下那一点。"
        l_kimi "今天就到这里。我还想洗个头，晚饭前别来敲门。"
        l_you "好。我的鞋带已经换完，不找你检查了。"
        "她朝你鞋尖看一眼，笑出一点声音。你的卡与她的册各收在各人的地方，等待这一种关系被说清，也有今天已经走完的路。"
    else:
        "她从干纸兜取出今日的公开路线卡，拿笔画出桥头、桥面与对岸石亭。你等她画完，她转来给你看，私人薄册与新册仍在她自己的袋里。"
        l_kimi "这段我想给你。到亭子前先绕过那道石墙，别把墙当屋檐。"
        l_you "我给你码头这段。岸边是三块石，没有我早上猜的木栈。"
        "她等卡上的笔迹干了，才接过你亲自画好的白卡。看完后，她将自己那张递给你。两张只交换可公开的路，今日碰面安排的备用卡仍在她自己兜里。"
        $ kimi8_public_card_exchanged = True
        "她在你画的大船旁点一下，指尖落在灰绳根上。纸面干了，原先换鞋带的纸包也早收在你自己的房里。"
        l_kimi "你这船占了三块石。"
        l_you "实际在水里。你别按画把它搬上岸。"
        l_kimi "我去看的时候，会看水。"
        "她收好你这张公开卡。你也将她送来的石亭卡放进自己衣袋，没有翻她私册，没去公共柜为两人添一条借阅记录。"
        "她随后取出自己的新册，先在今日页补上早饭、绕过石墙和回院的时刻。她扶住页头转折处，画自己的记号，等笔尖停下才合上。你收好她给的路线卡。"
        if kimi8_record_order == "breakfast_first":
            l_kimi "辣油今天写了两遍。早上已经记过。"
            l_you "它占两个位置？"
            l_kimi "第二个划掉。明天不想再给它一页。"
            "她自己划去重复那行，蓝绳留在走到石亭这一页。"
        else:
            l_kimi "我那页也写完了。早饭到这里。"
            l_you "私册归你，卡归我。"
            l_kimi "嗯。别把你的三块石塞到我的亭子上。"
            "她自己夹好蓝绳，将新册放回平兜。"
        l_you "下次想来南街，先叫我。时间也先问一声。"
        l_kimi "好。你想去石亭，也先看天。今天有一小段晒。"
        "你答应过，把自己的杯子拿回手里。她喝完自己的那杯，将椅子推回自己平常的位置，袋带留在手边。"
        l_kimi "朋友早饭吃完了。路线也真的换了。"
        l_you "今天没有让你再拿回少的一柄勺。"
        l_kimi "今天拿错的是辣油。你别提前把它擦掉。"
        "你笑，她也笑着把自己的新册收回袋里。交换的卡各有新的主人，旧私人薄册仍留在她自己手中。"
    "你们把各自的笔扣好，收到各人的袋内。纸与杯子分开，桌面没有留下一支滚到边角的笔。"
    $ kimi8_record_finished = True
    $ kimi8_relation_closed = True
    "三点二十，廊下有人来收空椅。Kimi起身将自己的椅子推回桌内，自己的杯子送到水台洗净，晾在自己用的杯位。"
    "你也收好自己的杯子。她把布袋提回肩上，先理开夹在带下的银白发尾，没有将新册留到公共柜旁等谁来核。"
    if kimi8_reply == "love":
        l_kimi "第十九日下午。出门前再来找我。"
        l_you "来找你，一起走。今天先各自休息。"
        "她点头，带着两人刚写过的新旅行册回自己的房间。今日这一页已经写好，下一次的空圈还在，等真到那天再填。"
    elif kimi8_reply == "wait":
        l_kimi "我先回去。下回见面再问。"
        l_you "好。我也去做自己那边的事。"
        "她沿廊下往自己房门走，你没有留在门口等一个今晚必须补交的答复。今天的两条路都走过，各人的记录各自带走。"
    else:
        l_kimi "石亭那张，想给别人看也可以。我只画了那一段。"
        l_you "我知道。你别的页，我没有拿。"
        "她朝你摆一下右手，转过廊角。你带着她愿意交换的那张卡回自己的地方，灰绳那张也随她进了自己的袋内。"
    return

# 正文候选静态冻结信息与all_writing_ended见FREEZE.json；未native，不计完整线。

