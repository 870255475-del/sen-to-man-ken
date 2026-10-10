# Kimi第五章《这是我的记录》；第十三日，v0.13独立正文候选，未接入／未native。
# Kimi与玩家为30岁成年人；私人愿签为她今天亲写的新纸，非许葵已领回的原签。
# 只读完整第四章断点；不凭global seen制造第三章或更早的共有散步。
# 本章只写kimi5_与自身seen；无关系、UUID、周目、图库或不存在的API。

default persistent.main_kimi_ch05_seen = False
default kimi5_has_ch04 = False
default kimi5_previous_returning = ""
default kimi5_previous_walk = ""
default kimi5_returning = ""
default kimi5_departure = ""
default kimi5_wish_written = False
default kimi5_wish_returned = False
default kimi5_notebook_returned = False
default kimi5_addition_marked = False
default kimi5_bag_returned = False
default kimi5_cloth_lent = False
default kimi5_cloth_returned = False
default kimi5_solo_left = False
default kimi5_solo_returned = False
default kimi5_own_wish_kept = False

label kimi_ch05:
    $ kimi5_has_ch04 = main_last_chapter == "kimi_ch04" and persistent.main_kimi_ch04_seen is True and kimi4_owner_met is True and kimi4_wish_returned is True and kimi4_work_closed is True and kimi4_own_page_kept is True and kimi4_walk_complete is True and kimi4_name_written is True and kimi4_returning in ("now", "at_time") and ((kimi4_walk == "elm" and kimi4_elm_reached is True and kimi4_water_rest is False) or (kimi4_walk == "water" and kimi4_water_rest is True and kimi4_elm_reached is False))
    $ kimi5_previous_returning = ""
    $ kimi5_previous_walk = ""
    if kimi5_has_ch04:
        $ kimi5_previous_returning = kimi4_returning
        $ kimi5_previous_walk = kimi4_walk
    $ kimi5_returning = ""
    $ kimi5_departure = ""
    $ kimi5_wish_written = False
    $ kimi5_wish_returned = False
    $ kimi5_notebook_returned = False
    $ kimi5_addition_marked = False
    $ kimi5_bag_returned = False
    $ kimi5_cloth_lent = False
    $ kimi5_cloth_returned = False
    $ kimi5_solo_left = False
    $ kimi5_solo_returned = False
    $ kimi5_own_wish_kept = False
    call kimi05_scene1
    call kimi05_scene2
    call kimi05_scene3
    call kimi05_scene4
    call kimi05_scene5
    $ persistent.main_kimi_ch05_seen = True
    return

label kimi05_scene1:
    $ chapter = "Kimi 第五章 / 01 · 她今天写的"
    scene bg echo morning with dissolve
    show sprite kimi as kimi at sprite_breathe(0.63) with dissolve
    "第十三日上午八点四十五，Kimi把一只芝麻卷装进纸袋。袋口折了两次，她想起还没尝，又展开一次。"
    l_you "你在替它找出口？"
    l_kimi "替我自己。买回来还没吃。"
    "她咬下带芝麻的一角，把剩下的重新包好。桌边有她的私人薄册，一张窄纸夹在今天的新页里。"
    "窄纸是她今早从自己的空纸上剪的，上面写了第十三日与Kimi。没有寄存编号，也没有待人领取的空格。"
    "她用指尖点过纸头的小字：我的愿签。末尾已经有句号，下面还留着能写两行的白。"
    l_you "这一张也要收进工作格？"
    l_kimi "收我袋里。这个不用你找当事人。"
    "她把芝麻卷移到另一边，念了一遍自己写的：沿桥后另一侧独自走一回，到转弯处再决定要不要继续。"
    l_you "只有这一句？"
    l_kimi "今早只想到了这一句。够我先出门。"
    "她装好水瓶，手在瓶塞上转了一下。塞子没有坐正，她又取出来压稳，才把瓶子放进布袋外兜。"
    if kimi5_has_ch04:
        if kimi5_previous_returning == "now":
            l_you "昨天九点交回去的那张，和这个不同。"
            l_kimi "那张在许葵手里。这张是我的。"
        else:
            l_you "昨天十点半那张已经交回去了。"
            l_kimi "嗯。没留副本。今天重新拿了自己的纸。"
        if kimi5_previous_walk == "elm":
            "私人薄册前页留着第十二日榆树下的圈。她翻过两块高石与干台阶，今天在另一张纸上起笔。"
            l_kimi "昨天那棵树已经到了。今天想往没画的转弯走。"
        else:
            "前页记着第十二日的平石与凉豆浆，榆树仍在想去那格。她没有把那一格圈成已到。"
            l_kimi "榆树还想去。今天先挑另一边。"
    else:
        "她只给你指今天的日期。前面的纸压在册内，哪个圈与你有关，她没有拿出来说明。"
        l_you "今天这段从桥头开始？"
        l_kimi "嗯。前面我自己慢慢接。"
    "你说也要去桥头买午饭，能帮她带册子。她将薄册递给你，水瓶和芝麻卷仍拿在自己手里。"
    "你的盐饼装在另一只油纸包里。怕手上东西太多，你问能否先放她袋外侧，到桥头再取。"
    l_kimi "放这边。到桥头拿走，里面我要装自己的。"
    "你答应过，沿外侧空格放稳纸包。她把自己的芝麻卷留在上面，两只没有混进同一张包纸。"
    l_kimi "拿到桥头就给我。我要去取帽子，先替我压住纸角。"
    "她去廊后的挂钩取帽子。风把夹在新页里的愿签掀开，你把它抽出来，压在册子上，免得折到写字的地方。"
    "你看着那句独自走一回，想起桥头十一点半会开面摊。从自己的袋里拿出铅笔，在白处接了一句。"
    "回来一起吃面，再把后半段走完。你写完，才发现这行比她原来的字挤得更近，便将末尾往下带了一点。"
    $ kimi5_wish_written = True
    "Kimi回来时，你正把纸重新夹好。她先戴好自己的帽子，见你拿稳了薄册，就与你往院门走。"
    l_you "午饭不用再临时找了。"
    l_kimi "你已经想好吃什么？"
    l_you "面。桥头那家。"
    l_kimi "我还没想好。芝麻卷先跟我走。"
    "你按着刚夹回去的纸角，没说自己也替她写了回来。她把布袋提到肩上，停一下，将帽带从袋带下面抽出。"
    l_you "两根一起扣，不是更稳？"
    l_kimi "那我得连着帽子喝水。你试？"
    "你收回手。她分别理好两根带子，顺着院门的干石走出去，你仍拿着她的册子。"
    return

label kimi05_scene2:
    $ chapter = "Kimi 第五章 / 02 · 这句谁写的"
    scene bg river day with dissolve
    show sprite kimi as kimi at sprite_breathe(0.63) with dissolve
    "九点二十，桥后的路分成两边。Kimi在较低的石栏旁停住，向你伸手，要取回刚才托你拿的薄册。"
    "你把册子打开到今天，愿签从里面滑出一截。怕它掉进草里，你抽出来递给她，露出了自己新添的两行。"
    l_you "我把回来那段接上了。十一点半吃面。"
    "她低头看过，手指从自己那句末尾移到你的笔迹。你的再走完落在她签名旁，她将整张纸稍稍往上抬。"
    l_kimi "我写的是，到那里再决定。"
    l_you "午饭以后也有空，走完再回来就好。"
    l_kimi "谁说要走完？"
    $ hide_speaker_portrait = True
    call show_main_cg('kimi_notebook_press')
    "你正要指河堤尽头，她伸手按合你托着的薄册。你把愿签挪到封面外，空白的一角靠着薄册边。"
    l_kimi "还有，我想一个人走。"
    call show_main_cg('kimi_wish_reclaim')
    "她把袋带从指间松开，伸手来拿那张愿签。你还用两根手指夹着下边，纸在两只手之间弯成一个浅弧。"
    l_you "我只是想，回来有个人等你。"
    l_kimi "我今天没请你等。先把手松开。"
    scene bg river day with dissolve
    $ hide_speaker_portrait = False
    show sprite kimi as kimi at sprite_breathe(0.63) with dissolve
    "你松了一根手指，却又摸向新写的地方，想把字擦掉。她将自己的铅笔横放在封面上，挡住你伸来的手。"
    l_kimi "别再替我动这一张。"
    "你收回铅笔，刚写的两行仍在。桥上有人推着空车经过，木轮响了一阵，她等声音过去，手没有收回。"
    menu:
        "把愿签与册子分开交回，不再动字。":
            $ kimi5_returning = "separate"
            "你先把愿签平放到她掌心，再合好薄册，托着书脊交给她。自己的铅笔收进自己的袋子。"
            $ kimi5_wish_returned = True
            $ kimi5_notebook_returned = True
            "她将愿签顺着自己的旧折线折起，收入布袋内侧的小兜。册子另拿在手上，外角的空白还露着。"
            l_you "字留着。你想怎样收，自己来。"
            l_kimi "我现在想收起来。"
            "她把小兜按严，没马上替那两行做标记。你看着她腾出的手，原本要递水瓶，又停住。"
            l_you "水在你外兜。"
            l_kimi "我知道。刚才自己放的。"
            "她取瓶子喝过一口，塞好才把薄册转到另一只手。你退到石栏外侧，给她的袋子留出能提起的位置。"
            "愿签与册子都回到她手上。你那只先前压纸的手空了，掌心还留着封面边缘浅浅的印。"
        "指出我添的那行，再按她说的顺序交回。":
            $ kimi5_returning = "show_line"
            l_you "从回来一起吃面起，是我加的。连走完，也是我加的。"
            "你只指自己的笔迹，没有再次落笔。她看过，先取走愿签，再接过你合好的薄册，没把两件交接倒过来。"
            $ kimi5_wish_returned = True
            $ kimi5_notebook_returned = True
            l_kimi "我原来的句号在这里。"
            "她把纸垫在自己册子的封面上，在你添的两行外画一只细括号，写你添的。句号与她自己的签名留在原处。"
            $ kimi5_addition_marked = True
            l_you "这行不算今天的约。"
            l_kimi "本来就没约。我得把它认清。"
            "她将愿签折好，夹进自己合拢的薄册。铅笔也由她收回袋口，没有再把刚合上的册子给你看。"
            "你的手仍抬着，像还要替纸角挡一下风。她转过册脊，放到自己臂弯里，你才慢慢放下手。"
            l_you "我先把自己的笔收好。"
            l_kimi "嗯。别夹在我这本里。"
    "Kimi往岔口望了一眼。河边的草叶压向同一侧，她却没接着走，先将袋子靠在石栏内面。"
    l_you "你要回去？"
    l_kimi "我要把这句说完。再走。"
    "她把帽子摘下拿在手里，目光停在你脸上。那条未走的路还在她身后，刚才说好的午饭只在你的话里。"
    return

label kimi05_scene3:
    $ chapter = "Kimi 第五章 / 03 · 今天我不带你去"
    scene bg river day with dissolve
    show sprite kimi as kimi at sprite_breathe(0.63) with dissolve
    "九点半，Kimi把帽子搁在石栏上。她没将私人薄册重新打开，两只手轮流压过封面，仍有一点用力。"
    l_you "我以为一起走更好。你也不用记两次路。"
    l_kimi "我想记我自己的。也可能不记。"
    l_you "怕你绕到别处，回来没找到人。"
    "她望向你身后的桥头，又看了一眼袋里露出的芝麻卷。纸袋被瓶子压扁，她抬起瓶子，将它移到上面。"
    l_kimi "我带了水。也带了吃的。想停就有地方停。"
    l_you "那我只陪到前面？"
    l_kimi "你刚才就是要帮我接到前面。"
    "她说完，捏住纸袋的折边。芝麻掉了两粒在封面上，她逐粒拾起，搁回包纸内，没像平常那样顺手递给你。"
    l_you "这一回，是我想跟着。"
    "她抬眼看你。手里的小纸袋停在胸前，过了一会儿，她才咬下刚才剩着的那一角。"
    l_kimi "这句比刚才清楚。可我今天还是想自己走。"
    l_you "好。你不必为了让我陪，改成别的路。"
    "你站直，让开岔口。她却还没有提袋，只看着自己封面外那一角白纸，轻轻把它往内压。"
    l_kimi "今早那句写了三遍。"
    l_you "这一张之前还有两张？"
    l_kimi "写在废纸背面，试了试。都在我抽屉里。"
    "她用指甲轻压册脊的一道折线，没请你回院里去找那两张。你把手从自己的袋口移开，等她再说。"
    l_kimi "先写沿河。后来想，这样你看见，又会问沿哪边。"
    l_you "我刚才还想指尽头。"
    l_kimi "嗯。纸上连回来的面都长出来了。"
    "你笑了一下，笑到半截停住。她没有跟着笑，低头将水瓶摆正，瓶塞在指尖下轻轻响了一声。"
    l_kimi "我想过，要不要干脆不写。"
    l_you "这样我就没地方接字了。"
    l_kimi "那我想写的时候呢？"
    "你看着已经在她手中的薄册。刚才自己添的字没有再露出来，封面边角却一直被她按着。"
    l_you "这一张该先等你递来。我拿着，也不该续。"
    "她没接这句话，先戴好帽子。帽带刚勾到耳边，她拉回来理顺，动作比出门时慢了一点。"
    l_kimi "今天的这条路，我没想带你。也不想回来交一页给你查。"
    l_you "那我不在桥头等那一页。"
    l_kimi "人也不用等。我要在哪里坐，现在还不知道。"
    "你点头，挪开脚下挡着的小石块。刚挪开的地方是浅坑，她看见你又要站进去，用鞋尖点点旁边较高的一块。"
    l_kimi "你先顾一下自己的路。"
    l_you "这条我也没看好。"
    l_kimi "刚才倒是替我看得挺远。"
    "你踩回平地。她这回嘴角动了一下，又很快收住，提起自己的袋带，没把那一小下当成已经说好了。"
    "河边过来一阵风，帽沿向上翻，她自己压住。你在一旁把自己的帽子戴好，手没有再伸到她帽带下面。"
    l_you "要不要我说声对不起？"
    l_kimi "已经该说了。"
    l_you "对不起。我替你写了约，还想照自己写的带你走。"
    "她应了一声，掌心从封面上移开。一个空车轮从桥头滚过去，她将自己的袋子往干石上挪了挪。"
    l_kimi "我还生气。先别拿下一顿来填。"
    "你把准备问午饭的那句停在嘴边。她扶着帽沿，终于从石栏旁站开，自己挑了通向岔口的那一侧。"
    return

label kimi05_scene4:
    $ chapter = "Kimi 第五章 / 04 · 到岔口分开"
    scene bg river day with dissolve
    show sprite kimi as kimi at sprite_breathe(0.63) with dissolve
    "九点四十，Kimi走到岔口前的干石上，低头检查自己的布袋。册子在内层，芝麻卷放上面，水瓶立在外兜。"
    "瓶身凝出小水珠，浸湿了外兜下沿。她抽起布袋，想将瓶子挂到外面，提绳却藏在包纸下面。"
    "你帮她托了一下袋底。刚才放回去的瓶子挤到你放在侧边的一只小盐饼，那只饼是你早上买给自己的。"
    l_kimi "它也要跟我走？"
    l_you "我出门时塞的，自己忘了。"
    l_kimi "你自己的午饭，不用从我袋子里找。"
    "你将盐饼取出。包纸的一角被外兜水迹碰湿了，你拿它去擦袋底，她把袋子抬高一点，避开那块油纸。"
    l_kimi "这面有油。你擦完，我还得洗一次。"
    l_you "我换一面。"
    l_kimi "先收饼。两面都包过它。"
    "你把包纸折回，盐饼收入自己的袋子。Kimi拿起水瓶，让湿的袋角悬着，一手还托住册子所在的内层。"
    "她松开内层的小结，确认纸边仍干，再重新系好。愿签在她自己收的位置，你没有往里再摸一回。"
    l_you "我这条手巾是干的。"
    l_kimi "你拿着。先等我把绳子找出来。"
    "她要用袋上的短绳吊瓶子，却拎起了芝麻卷外的细纸绳。绳头一下松开，她按住纸袋，芝麻从折边弹出一粒。"
    l_you "它们今天也没一起扣。"
    l_kimi "这句现在轮到你笑。只笑这句。"
    "你轻轻笑过，把眼前一粒芝麻留给她自己拾。她把水瓶交到你手里，再找出真正的短绳，等着取回瓶子。"
    menu:
        "放稳她的袋子，取走自己的东西就离开。":
            $ kimi5_departure = "leave"
            "你将袋底放在平石上，水瓶交到她空出的手里。袋里的盐饼已经取净，你再把自己的帽带拉到下巴前。"
            "她用短绳绕过瓶颈，结打在能自己解开的那侧，再将瓶子吊在布袋外。湿外兜空出来，纸仍留在内层。"
            $ kimi5_bag_returned = True
            l_you "我的饼收好了。我从桥头回去。"
            l_kimi "嗯。今天别在那边替我占凳子。"
            "你答应过，先走向回桥的干道。她试了一下瓶子会不会敲到腿，把绳缩短一截，独自踏向另一条路。"
            "走过石栏时，你回头只见她按着帽沿。她的脚步没有为你停住，你也没从桥的另一面绕过去追。"
            "你的手巾留在自己袋里，盐饼拿出来吃了一口。桥头两只空凳都有太阳，你挑自己能坐的那一只。"
        "先问一声，借她干手巾垫瓶底，再各自走。":
            $ kimi5_departure = "lend_cloth"
            l_you "想借这条垫瓶底吗？我刚洗干净，今天还没用。"
            "你将自己的干手巾摊在空手上，没有塞到她袋里。她看看湿外兜，再看看水瓶，点了一下头。"
            l_kimi "借我。回院里洗过还你。"
            "她先拿回水瓶，再接手巾，自己围住瓶底，把较厚的一角垫向湿的那边。瓶子放入外兜，短绳仍收在她袋上。"
            $ kimi5_cloth_lent = True
            "你把布袋提环交回她手中，取好自己的盐饼和帽子。她试着走一步，瓶子没有敲到腿，册子仍在干的内层。"
            $ kimi5_bag_returned = True
            l_you "我从桥头回去。巾回来再还就行。"
            l_kimi "嗯。还巾不用你在这里等。"
            "你向桥头走，她提着自己的袋子走向另一侧。那条手巾的一角从外兜露着，她低头收好，没回身叫你同行。"
            "你到桥头才发觉手边没有干巾，便在自己的包纸上擦过指尖。盐饼有点硬，你给自己买一杯水，没再添第二杯。"
    $ kimi5_solo_left = True
    "你先沿镇路回院里，放好自己的盐饼。十一点半再独自到面摊，只问这一碗几点能吃。摊主说现在就能，你在炉子外坐下。"
    "摊主还问要不要多留一只凳子。你摇头，将袋子收到自己脚边，留出过道给端面的手。"
    "你吃得有点急，第一口烫着舌尖，只好放慢。她那只芝麻卷去了另一条路，你没写它吃到了哪一口。"
    return

label kimi05_scene5:
    $ chapter = "Kimi 第五章 / 05 · 册子仍在她手里"
    scene bg echo morning with dissolve
    show sprite kimi as kimi at sprite_breathe(0.63) with dissolve
    "下午一点五十，你在院里冲洗自己的碗。Kimi从门外回来，帽沿有一点草屑，布袋仍提在她自己手上。"
    "她先将水瓶放到空台，取下帽子。你望过她鞋边的干泥，没有问转弯后又走了多少路。"
    $ kimi5_solo_returned = True
    l_you "水凉着，在左边那只壶里。"
    l_kimi "我先倒自己的。"
    "她拿杯子倒满，喝一口，才把袋子放到膝上。芝麻卷的纸包折扁了，册子还好好留在内层。"
    if kimi5_departure == "lend_cloth":
        "她将借的手巾取出，去水台洗过两遍，再拧掉水，走回来平放在你空着的碗沿上。手巾仍有点潮。"
        l_kimi "你的。晾干再收，别裹住你那只饼。"
        l_you "我把它挂这边。"
        "你接过手巾，挂到自己杯旁的空钩。她等你接稳才松手，没有将自己的薄册一起推过来。"
        $ kimi5_cloth_returned = True
    else:
        "你用自己的手巾擦碗外的水。她将挂在袋外的瓶绳解开，瓶子放上空台，湿外兜翻出一点让它晾着。"
        l_you "袋底没再滴了？"
        l_kimi "路上吊着走，风吹干了一些。"
        "你收好自己的手巾，把空台另一边让出来。她将外兜拉平，册子所在的内层仍系着原来的结。"
    "她从袋中取出薄册，只翻到今天夹纸的那一侧。愿签在她自己手里，你能看见窄纸边，字面向着她。"
    if kimi5_returning == "separate":
        "她从小兜取出的愿签仍沿原折线收着。展开后，她在你添的两行外画一只细括号，写你添的，再将原纸折好。"
        $ kimi5_addition_marked = True
        l_you "那句还在。"
        l_kimi "我看见了。现在由我收。"
    else:
        "她摸过今早画的细括号，确认折边没有盖住自己原先的句号，再把纸顺着同一条折线收好。"
        l_you "你早上分开的那两行，没再续。"
        l_kimi "嗯。今天先到这里。"
    "她将愿签夹在私人薄册内，合册时留着一角没写字的白。工作格在另一张桌上，她没有将这张往那边递。"
    $ kimi5_own_wish_kept = True
    l_you "今天那一页，等你愿意时再给我看。"
    l_kimi "今天不给。以后给哪一页，再说。"
    "你点头，手里洗好的碗转了半圈。她看看你正要落下的地方，用指尖将垫子往外推一小段。"
    l_kimi "那边刚晾袋子，有水。你这只刚擦完。"
    l_you "我放这边。"
    "碗落在干垫上。她把杯子放回木垫，膝上的册子往袋口靠了靠。喝过一口，眼睛望着院门口。"
    l_you "午饭吃过了吗？"
    l_kimi "吃过。别从芝麻卷开始给我排一次。"
    l_you "好。我只问这一顿。"
    "她低低应过，去取留在桌侧的自己的小碗。你收起洗碗的布，没跟着把她的筷子也摆成两人份。"
    "她把薄册收入袋子内层，愿签由她一起带着。帽上的草屑掉到凳边，她弯腰捡起，夹在废包纸里。"
    l_you "这个也收？"
    l_kimi "带到院里了。总不能让它替我扫地。"
    "你给她指了纸屑筐，她自己丢过，回来把杯子喝完。杯沿离开嘴边时，她看了你一下，没接着翻册。"
    l_kimi "我还没消气。那两行我收着，别替我翻过去。"
    l_you "知道。我没去那条路找你。"
    l_kimi "嗯。今天我走自己的。"
    "她把空杯放好，拿起自己的袋子。你留在水台边将碗摞稳，听见她脚步过了廊角，才收起桌上自己的铅笔。"
    # 合册／返还／独行均为实际动作；本候选无CG调用或假解锁，动作需求见接力。
    return
