# Kimi第四章《遗忘不是背叛》；第十二日，v0.12独立候选，未接入／未native。
# 沿52／route_followups愿签取回题纲；不提前执行第五章擅续私人愿签。
# 许葵34岁、弟弟许航31岁为本章原创成年街坊，无新Character或立绘。
# 愿签与工作登记不进私人地图；旧目录与42/43原页已第九日归还，不复用。

default persistent.main_kimi_ch04_seen = False
default kimi4_has_ch03 = False
default kimi4_previous_listen = ""
default kimi4_previous_finish = ""
default kimi4_previous_route = ""
default kimi4_returning = ""
default kimi4_walk = ""
default kimi4_owner_met = False
default kimi4_wish_returned = False
default kimi4_work_closed = False
default kimi4_own_page_kept = False
default kimi4_walk_complete = False
default kimi4_elm_reached = False
default kimi4_water_rest = False
default kimi4_name_written = False

label kimi_ch04:
    $ kimi4_has_ch03 = main_last_chapter == "kimi_ch03" and persistent.main_kimi_ch03_seen is True and kimi3_cheng_heard is True and kimi3_he_heard is True and kimi3_supplement_checked is True and kimi3_old_page_kept is True and kimi3_private_walk is True and kimi3_listen in ("times", "use") and kimi3_finish in ("check_first", "meal_first")
    $ kimi4_previous_listen = ""
    $ kimi4_previous_finish = ""
    $ kimi4_previous_route = ""
    if kimi4_has_ch03:
        $ kimi4_previous_listen = kimi3_listen
        $ kimi4_previous_finish = kimi3_finish
        if kimi3_previous_complete is True and persistent.main_kimi_ch02_seen is True and kimi2_page43_read is True and kimi2_old_returned is True and kimi2_own_circle is True and kimi2_notebook_kept is True and kimi2_route in ("together", "solo") and kimi2_prep in ("read_first", "pack_first") and kimi3_previous_route == kimi2_route and kimi3_previous_prep == kimi2_prep:
            $ kimi4_previous_route = kimi2_route
    $ kimi4_returning = ""
    $ kimi4_walk = ""
    $ kimi4_owner_met = False
    $ kimi4_wish_returned = False
    $ kimi4_work_closed = False
    $ kimi4_own_page_kept = False
    $ kimi4_walk_complete = False
    $ kimi4_elm_reached = False
    $ kimi4_water_rest = False
    $ kimi4_name_written = False
    call kimi04_scene1
    call kimi04_scene2
    call kimi04_scene3
    call kimi04_scene4
    call kimi04_scene5
    $ persistent.main_kimi_ch04_seen = True
    return

label kimi04_scene1:
    $ chapter = "Kimi 第四章 / 01 · 这一张有人来领"
    scene bg echo morning with dissolve
    show sprite kimi as kimi at sprite_breathe(0.63) with dissolve
    "第十二日上午八点四十五，Kimi把一只窄信封从工作格里取出。封面是寄存编号，封口没有粘。"
    "她先放到登记桌，再取自己的薄册。两样之间留着一只杯子的宽度，杯子却被她忘在另一边。"
    l_you "中间等谁坐？"
    l_kimi "我的水。你坐凳子。"
    "你替她拿来杯子，刚要搁下，她用指尖点点右侧的空垫。桌中那一段仍旧留着。"
    if kimi4_has_ch03:
        "她合好第十一日的补讲夹，夹内第六日原误判页仍有自己的署名。两页各在一边，没被新信封盖住。"
        l_you "昨天那两页还分着。"
        l_kimi "嗯。今天领的是另一张。"
    else:
        "工作格内的夹子各有日期。她把眼前的信封转来，只给你看今天这件要领回的编号。"
        l_you "今天要交出去？"
        l_kimi "本人来领。等她说清哪一张。"
    "三十四岁的许葵带着取回联走进院子。她把那张联纸放稳，指清自己的名字和寄存日，是第七日。"
    "她在镇里做染布活，弟弟许航三十一岁，平常住在外镇。今天弟弟回来，她想亲手把愿签带去。"
    "Kimi核过两处编号，再问她是否现在领取。许葵说签可以先收，也可以十点半回来拿，那时布就领好了。"
    "许葵自己提起那句话：想与弟弟再到桥后榆树下坐一会儿。今天两人未必走那条路，她仍想把原纸带给他。"
    l_kimi "取回以后，原签不留在这里？"
    "许葵点头，拍过空布袋，说她带了平纸的硬夹，不必另替她抄一张。她想要的是自己当时写的这一张。"
    "Kimi从信封里取签，只按边角拿着，让署名与编号露出来。许葵亲自看过，确认就是它。"
    $ kimi4_owner_met = True
    "原纸有一小截旧折痕。Kimi原本托住折痕的手没有立刻松，她把签放回垫纸上，再慢慢收手。"
    l_you "你还要看哪一行？"
    l_kimi "不用再看。认清了。"
    "她打开私人薄册，一处待走的小格旁写着榆树。字旁有自己画的小箭头，还没有亲脚到达的圈。"
    "她说许葵寄存时自愿指过地方，自己才想去看看。那张愿签一直留工作格，没夹进她的薄册。"
    l_you "拿走签，这一格也要拆下来？"
    l_kimi "我还没拆。你倒是帮它站起来了。"
    "你按住那格的纸角，才发现自己刚把垫纸碰歪。她抽回铅笔，却没有接着在榆树旁落笔。"
    l_kimi "我先还纸。那里……晚一点再想。"
    "许葵将硬夹留在桌边，去廊口取领布用的绳袋。Kimi给原签套好封，绳端绕在空着的手指上。"
    "许葵回来拿绳时，看见她正在找大些的封套，便比过自己带来的硬夹。纸平放进去就好，旧折痕不用压成新的。"
    l_kimi "这一角有点翘。"
    "许葵让她顺着旧折痕放，说弟弟认得这张纸边，先前寄布料回来时，也是这样夹住的。她自己将夹口留松。"
    "Kimi换回原来的纸套，指腹离开那处翘角。她低头确认原纸完整，没拿新空签替它换一张更好看的。"
    l_you "空封还用得上？"
    l_kimi "别塞我册子里。那个地方，我今天还想放自己的纸。"
    return

label kimi04_scene2:
    $ chapter = "Kimi 第四章 / 02 · 手里留了一会儿"
    scene bg echo morning with dissolve
    show sprite kimi as kimi at sprite_breathe(0.63) with dissolve
    "九点前，Kimi已将领回联与原签编号核清。登记的领取时刻还空着，纸套放在能交到许葵手里的那侧。"
    "她摸过套口，确认纸角没露出来，又摸了一次。同一处被抚得比旁边平，字仍在封内。"
    l_you "绳子缠住了？"
    l_kimi "没有。我在等自己松手。"
    "你把硬夹拿来，却先将空信封塞进夹子。Kimi看着你手里的轻薄一片，伸手将真正的纸套递过来。"
    l_kimi "那封还没装。你还得多等我一回。"
    l_you "我想先把能做的做好。"
    l_kimi "先拿对这一件。"
    "许葵在廊口问是否收妥。她仍愿按原先两种时间来领，没有催Kimi把纸掏出来解释心事。"
    menu:
        "先把原签交还本人，再收自己的地图页。":
            $ kimi4_returning = "now"
            "Kimi叫住许葵，将纸套装进硬夹，交到她伸来的双手里。绳结由许葵自己收好，没留一截在桌上。"
            "许葵核过原纸，折好领取联。Kimi在登记上写九点，勾上本人领回，留的仍是编号与交接时刻。"
            $ kimi4_wish_returned = True
            "硬夹出了院门，桌上的垫纸还压着长条影子。她伸手往影子旁碰一下，指下只有桌面。"
            l_you "我把这一块也收起来？"
            l_kimi "垫纸留下。杯子可以放这边了。"
            "你将杯子挪过去，她捧起来，却停在嘴边。隔了一会儿才喝，杯里的水已经没有刚倒时那么热。"
            "她把领回联的存根放进工作夹，私人薄册还开在原处。你坐下来，没有继续催她翻过去。"
            l_kimi "我知道她会来拿。可刚才那只手，还是慢了。"
            l_you "这会儿先坐着？"
            l_kimi "嗯。我不想马上去找另一张。"
            "她在空垫纸上摆正杯子。你拆开自己的麦饼，分开两半，等她自己伸手取了一块。"
            "杯壁在她指间留下浅浅的热，她的手指已经空了，原先绕着的一圈痕还没散。你将包纸推近些，空手留在桌边。"
            l_kimi "我上午原本想再对一下榆树的位置。"
            l_you "现在还问吗？"
            l_kimi "等她领布回来，我当面问。先不从她字里找。"
        "照她十点半的约交还，先把归还登记收好。":
            $ kimi4_returning = "at_time"
            "Kimi向廊口说好十点半，许葵应过才去领布。原签连套留在工作垫上，领取时刻仍空着。"
            "她先核登记页，将待本人领取留在编号后面，没有提前勾已领。你帮她把空信封收回另一格。"
            l_you "这栏写十点半？"
            l_kimi "先写约的时间。真正交到手，再填这一格。"
            "她将笔搁下，杯子拿得很慢。信封在桌上，她仍不翻开，手绕着纸套外那根松绳。"
            "你说还剩一会儿，可以替她照着留个副本。Kimi把手里的绳放直，抬眼看你，没把套口递来。"
            l_kimi "她刚才说，不用另抄。我也答应了。"
            l_you "我只想到你这一格会空。"
            l_kimi "先让它空。我现在不想填。"
            "你将刚拿起的空纸放回原格，换成两张干净包纸，包住自己的麦饼。她接了一半，先咬硬一点的边。"
            "直到十点半前，原签没有再出套。她把编号朝上放好，喝过水，自己将手从纸套旁移开。"
            "你把包纸揉成一个小团，想接住杯底的水，纸团却在桌上滚了一截。她用手背挡住，先替杯子找来平垫。"
            l_kimi "它圆成这样，不会自己学会接水。"
            l_you "我原来想省一张。"
            l_kimi "少揉一下就省了。"
            "你拆开自己揉的那团，按平再擦水。她望着那处皱纹笑过一下，回头仍将原签按约留在工作桌上。"
    if kimi4_previous_listen == "times":
        l_you "你昨天很快就写清那几个时刻。"
        l_kimi "今天这个也写得出。写完，还想坐一会儿。"
    elif kimi4_previous_listen == "use":
        l_you "昨天你还能让人拿灯罩比着讲。"
        l_kimi "今天不用比。她说要原纸，我听清了。"
    else:
        l_you "还要我递什么？"
        l_kimi "水。先不用递笔。"
    "麦饼的碎边落在包纸里，她用指尖拢起，没有扫到登记上。薄册里的榆树一格仍开着，她没去遮。"
    return

label kimi04_scene3:
    $ chapter = "Kimi 第四章 / 03 · 纸回到她的袋里"
    scene bg echo morning with dissolve
    show sprite kimi as kimi at sprite_breathe(0.62) with dissolve
    "十点半，许葵抱着领回的布经过院门。布卷遮住她半边手臂，袋口的硬夹还能稳稳露在外侧。"
    if kimi4_returning == "at_time":
        "Kimi起身，把原签套入许葵的硬夹。对方自己翻开确认，收好原纸与领回联，再将绳结绕紧。"
        l_kimi "原纸在这里。你看清了再收。"
        "许葵看完点头，Kimi这才在实际领取栏写十点半，勾本人领回。桌上不留下原文或新抄件。"
        $ kimi4_wish_returned = True
    else:
        "她停下来向Kimi示意，原纸已在九点交回的硬夹里。Kimi只看看夹边，没有再请她拿出来一次。"
        l_kimi "绳子够长吗？"
        "许葵将结收向布袋内侧，让它不扫到布面，笑着说刚好。原签仍由她自己保管。"
    "许葵主动问Kimi，榆树那一边去过没有。Kimi看了一眼自己的薄册，答还没走到。"
    if kimi4_has_ch03:
        "她补说昨天与你停在另一截石道。今天纸取回了，她仍想听清这段路。"
    else:
        "她把册内的想去小格转过去，说明这里还只写着地点，今天想核清方向。"
    "她补说自己想看那棵树，不是要替许葵和弟弟把路走完。许葵把布卷放到门边的高凳，才腾出手比方向。"
    "过桥后沿堤走，旧榆树在两块高石头后面。那棵与柳树分得开，树下有一段干台阶，不必涉水。"
    l_you "纸取走了，你还愿说这个？"
    "许葵点头，说地点一直在那里。她今天带弟弟先去吃面，哪天有空再走，没请Kimi替他们补个已完成。"
    l_kimi "那我只记路怎么走。你的那句不再留这里。"
    "许葵应过，提起布卷，先去接弟弟。她说两人会在桥头认面摊，没把所有午后的空闲都约给你们。"
    "你看那卷布要往凳边滑，赶紧扶住一侧。许葵先提好袋带，Kimi将凳脚挪开一点，让她能站稳再把布卷抱回去。"
    l_you "我拿的是重的这边吧？"
    l_kimi "你拿的是绳子。布还在凳上。"
    "你低头，将松绳收回袋口。许葵抱稳布卷才笑，说这回自己少带了一只筐，纸夹总算不用挤在底下。"
    "她抬手让原签夹避开门槛，边走边看一眼桥头。Kimi站在院门内等她走过转角，才回去拿登记夹。"
    "Kimi收起登记，将原签所在的工作格标成已交还。借来的纸套位置空了，格子没改作别人的待领。"
    l_you "写成没有这个愿望？"
    l_kimi "写本人领回。她刚才还在想带弟弟走。"
    "你把笔尖移到正确一栏，才发现墨点已经落在指甲上。她抽来干纸，指过墨点，没替你把手藏到桌下。"
    l_kimi "这点先擦。留着也不会变成编号。"
    "你擦净手指，把笔还到工作笔架。她将存根夹好，只留下需要交接的编号和时刻，不夹一张复制的愿望。"
    $ kimi4_work_closed = True
    "工作路线页中的榆树旁原有查签小记。Kimi将那张自己写的索引抽出，收入归还夹的编号页，不写愿签内容。"
    "薄册里还留着她画的小箭头与想去二字。她用掌心压过空出来的位置，隔着纸摸到自己旧页的折边。"
    l_you "要翻到新页吗？"
    l_kimi "先别。我还有点舍不得这一块。"
    "你把凳子拉近半步，坐得能帮她挡住风。她没合册，也没找一张别人的便条来补洞。"
    "中午的饭端来后，她先取自己的筷子。你刚想把一块菜夹到她那边，她已经把那片菜吃进嘴里。"
    l_kimi "这一口我挑了。你慢一步。"
    l_you "我还没开口。"
    l_kimi "筷子先到的。"
    "你收回筷子，夹自己的菜。她吃完这口才看薄册，将午后空白压平。筷子横在碗边，她的手在那格旁停了一会儿。"
    return

label kimi04_scene4:
    $ chapter = "Kimi 第四章 / 04 · 先去我想去的地方"
    scene bg echo morning with dissolve
    show sprite kimi as kimi at sprite_breathe(0.63) with dissolve
    "午饭后，Kimi将碗送到小台，取回私人薄册。工作夹留在原格，原签已随许葵走，不再装进随身袋。"
    "她拿出一张自己的空路线纸，写第十二日，停笔时抬头看你。你将帽子拿好了，却还坐在背阴的凳上。"
    l_you "这次想让我先找什么？"
    l_kimi "找你的鞋。今天不找纸。"
    "你低头，鞋确实被你踢到了凳子另一端。她低低笑了一声，把你刚拿稳的帽子接住，等你弯腰。"
    l_kimi "我还想喝凉豆浆。桥头那家午后卖。"
    l_you "先走路还是先喝？"
    l_kimi "买了带去。别帮我只留走路那半句。"
    "她在纸边写一小杯，将杯口画得比树大。自己看了一会儿，又将铅笔抬起来，给杯子多添一滴。"
    "榆树那边她仍想去；柳树下往水边的平石，她今天也想去坐一会儿。她把两条路分别点给你看。"
    "新纸的角比册子宽，她剪去多出来的一小条，没碰旧地图。你拾起细纸条想当书签，她拿过来围住包纸里的剩麦饼。"
    l_you "这条是我刚找到的。"
    l_kimi "我刚剪的。先借它绑一下午。"
    "她把麦饼放在袋子外层，纸册放内层，凉豆浆还没买。你将帽子取回，两人各拿自己能拿稳的那一份。"
    "她也从袋外取下自己的薄帽，戴好再试一下帽沿。你的那顶在你手里，两只没有被她收成一顶。"
    l_kimi "你陪我选一条？另一条，今天不硬塞。"
    menu:
        "陪她去榆树下，亲脚走完仍想去的那一段。":
            $ kimi4_walk = "elm"
            "她将榆树旁想去的那行圈出一小角，没画已到。新的路线纸夹进私人薄册，空杯图留在边上。"
            l_kimi "那就这边。走到再画圈。"
            scene bg river day with dissolve
            show sprite kimi as kimi at sprite_breathe(0.63) with dissolve
            "一点，你们各买一杯凉豆浆，沿桥往堤边走。Kimi用手巾包着自己的杯底，没将工作纸带来垫。"
            "高石头比你预想的近。你指错前面那棵柳树，她看过叶形，再将你的手转向沿堤的一侧。"
            l_kimi "柳树已经见过你了。今天让它歇一会儿。"
            "她在两块高石后找到旧榆树。树下的台阶是干的，你们站稳才从台阶旁绕过去，没有踏进水里找近路。"
            "她先看枝头，再看自己掌心贴着的杯子。风扫过树叶，杯外的小水珠从手巾边滚下来。"
            l_you "终于能喝了？"
            l_kimi "能。凉的也不会替我等到晚上。"
            "她坐到树下平一点的石面，双手捧杯，第一口喝得很小。你放好自己的杯子，替她将帽沿从树枝下挪开。"
            "一片干叶落在你帽顶，她先看着没说。等你认真问是不是走到正确位置，她才指过帽子，轻轻笑出声。"
            l_kimi "到了。树还留了个回条。"
            "你取下干叶放回地上，她将自己的杯子放到稳石上，再翻今日路线纸，画完两块高石和台阶，末端圈住实际坐到的地方。"
            "画到台阶边，她抬头数一遍，再低头补上最后一级。你指着她画的高石，说这边像半块饼，她看看，没把石头擦掉。"
            l_kimi "你那半块在袋里。这个不能吃。"
            $ kimi4_elm_reached = True
            "榆树旁那格从想去变成今天走到。旧箭头留在原页，不改成许葵和弟弟也已来过。"
        "陪她去水边平石，今天先坐着喝完凉豆浆。":
            $ kimi4_walk = "water"
            "她将今天路线的起点点在柳树旁，榆树那格仍写想去。你把两处看反，她伸指轻敲今日这一边。"
            l_kimi "今天先坐这里。那棵树没答应一下午看两回。"
            scene bg river day with dissolve
            show sprite kimi as kimi at sprite_breathe(0.63) with dissolve
            "一点，你们各买一杯凉豆浆。摊前的糖勺在你手里，你顺手抬向她的杯子，她将杯口向自己收一点。"
            l_kimi "我这杯够了。你那杯还没加。"
            l_you "刚才听你说想喝凉的。"
            l_kimi "凉的。没说多糖。"
            "你给自己的杯子加好，收回糖勺。过桥后，她沿柳树旁的小段走向平石，停在干岸上试过落脚处。"
            "她没有往更远的浅水里走，先用手巾拂过石面，挪出两杯能放稳的地方。你坐到旁边，她把薄册横放膝上。"
            l_you "今天这里够写一页？"
            l_kimi "够坐一会儿。页也没催我。"
            "她双手捧杯，肩慢慢松下来。河水碰过岸边的草，轻轻回去，杯口映出一小片摇动的树叶。"
            "你说想看杯里那片叶，伸头太近，帽沿碰到自己的吸管。她用手扶住杯底，等你重新坐直。"
            l_kimi "水里那片也能看。你不用把整顶帽子送进去。"
            "你摘下帽子放到膝边。她看着帽沿上一点湿，笑了一下，将自己的杯子放回石面，再翻路线纸，记今天停在平石。"
            "她将麦饼的小包取出来，解开刚剪的细纸条。你接住被风吹起的一端，她掰自己剩的那半块，留一小角配豆浆。"
            l_you "原来那条真的只借一下午。"
            l_kimi "刚才还没有这么快。你先别抢下一口。"
            $ kimi4_water_rest = True
            "榆树仍留在待走栏，她没将今天休息画成那边的完成。杯子喝过一半，她自己挑两粒饼屑，没全分给风。"
    $ kimi4_walk_complete = True
    $ kimi4_own_page_kept = True
    "新纸旁没有愿签原文，也没有许葵要等的人。Kimi确认杯子立稳在旁边，铅笔指过自己的今天，手才离开页角。"
    if kimi4_previous_route == "together":
        l_you "第九日那段，现在还能从旧页找。"
        l_kimi "嗯。今天另画。没把旧圈挪过来。"
    elif kimi4_previous_route == "solo":
        l_you "第十日你自己走的，也留在前面？"
        l_kimi "留着。今天你坐在旁边，是今天这页。"
    else:
        l_you "这里从今天起？"
        l_kimi "嗯。走到哪，就从哪接。"
    "她让你按住被风掀起的外角，自己在空出来的一侧写下平石或榆树，没请你替她补完下一段。"
    return

label kimi04_scene5:
    $ chapter = "Kimi 第四章 / 05 · 这一行写我自己"
    scene bg river day with dissolve
    show sprite kimi as kimi at sprite_breathe(0.63) with dissolve
    "一点四十，Kimi将杯底最后一点豆浆喝完。她捏着杯沿等了一会儿，才把空杯收进带来的小袋。"
    "私人薄册摊在她自己膝上。榆树那处不再靠一张可查询的愿签连到工作格，页角的折痕却还在原处。"
    l_you "现在不舍得那张纸了吗？"
    l_kimi "还会想。手已经不用替它捏着了。"
    "她看着原先待走的格子，指尖在格旁停过，又移到今天的纸。两页没有被她粘成同一张。"
    if kimi4_walk == "elm":
        l_kimi "今天这棵树，我自己想来。也确实来了。"
        "她把许葵当时指路的小箭头留在原页，今天的圈照亲脚走过的位置落下，不替谁登记愿望已成。"
    else:
        l_kimi "那棵树我还想去。今天先喝这一杯，也挺想。"
        "她没有擦掉榆树的待走字样，今天平石另画在新纸上。铅笔落稳后，她又给杯旁添了一小条水线。"
    l_you "这一页题什么？走出空白？"
    l_kimi "买豆浆。你取的题，要多付钱吗？"
    "你笑着摇头，她在日期下面写Kimi，接着写今天自己选的路。自己两个字写得挤，笔在最后一横停了一下。"
    l_you "这里留宽些？"
    l_kimi "下次留。今天我也坐得挺挤。"
    "她往旁边挪一点，让你看清纸上那行。你没拿笔，只用指背压住边角，等她将字的尾端写完。"
    $ kimi4_name_written = True
    if kimi4_previous_finish == "check_first":
        l_you "今天这杯没像昨天午饭那样等凉。"
        l_kimi "本来就买凉的。算我挑对了一次。"
    elif kimi4_previous_finish == "meal_first":
        l_you "昨天你说现在想吃，今天换这一杯。"
        l_kimi "今天也有想喝的。下次还会换。"
    else:
        l_you "糖还够？"
        if kimi4_walk == "water":
            l_kimi "够了。下次别先替我抬勺子。"
        else:
            l_kimi "够了。下次把帽子戴稳一点。"
    "她将新页收回私人薄册。工作格的领回存根还在院里，许葵的原签在本人袋中，册角只夹着她今天的路线纸。"
    l_you "回去以后，要给那格添点东西？"
    l_kimi "工作格今天不用。我的袋子里添个空杯，倒是真的。"
    "你伸手想接袋子，她先提过轻的那只，让你拿自己的杯。纸册留在她手里，她将自己的袋带往肩上提好。"
    "她把帽子转正，又看你自己的那顶。你这次先拿好了，没让帽沿碰杯口，她便将刚压好的册角朝你轻轻一抬。"
    l_you "现在能替你找下一处了？"
    l_kimi "下一处等下次。今天先陪我把杯子带回去。"
    "她指过桥头回收杯子的竹筐，你们各放自己的。麦饼的细纸条收回她袋里，不夹到别人的领回登记上。"
    "回程她在台阶前停下，将薄册收入内层，再往前走。你在旁边等她踩稳，她扶袋的手到平地才慢慢松开。"
    "桥头的风比石边紧，Kimi将帽子往下压一截。她望一眼还想走的方向，转回时却先叫住了你。"
    l_kimi "下次喝不加糖的那杯。先让我自己点。"
    l_you "好。我拿自己的勺子。"
    "她嘴角轻轻抬了一下，与你绕过桥边的水迹。今天的路线纸在她袋里，末端只到今天已经走过的地方。"
    # 无专属CG／解锁；候选动作锚点随接力交根选择，不改变旧图库。
    return
