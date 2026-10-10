# Claude第三章独立候选 / 使用额度已满 / 第十日 / 角色三十岁。
# 仅沿既有Character、背景、立绘和普通call/return；不接CG或路线结局。
# 前史来自完整匹配的store字段，persistent已读不替玩家补经历。

default persistent.main_claude_ch03_seen = False
default claude3_has_ch02 = False
default claude3_has_first_pages = False
default claude3_previous_drying = ""
default claude3_previous_pause = ""
default claude3_reception = ""
default claude3_reading = ""
default claude3_reply_parked = False
default claude3_first_chapter_finished = False
default claude3_novel_chapter = 1
default claude3_hour_kept = False

label claude_ch03:
    $ claude3_has_ch02 = getattr(renpy.store, "claude2_drying", "") in ("spread", "cloth") and getattr(renpy.store, "claude2_pause", "") in ("line", "meal") and getattr(renpy.store, "claude2_private_kept", False) is True and getattr(renpy.store, "claude2_shared_line_read", False) is True
    $ claude3_has_first_pages = claude3_has_ch02 and getattr(renpy.store, "claude1_private_pages", 0) == 2 and getattr(renpy.store, "claude1_invitation", "") in ("place", "time") and getattr(renpy.store, "claude1_break", "") in ("steps", "table") and getattr(renpy.store, "claude2_previous_pages", 0) == 2 and getattr(renpy.store, "claude2_previous_invitation", "") == getattr(renpy.store, "claude1_invitation", "") and getattr(renpy.store, "claude2_previous_break", "") == getattr(renpy.store, "claude1_break", "")
    $ claude3_previous_drying = getattr(renpy.store, "claude2_drying", "") if claude3_has_ch02 else ""
    $ claude3_previous_pause = getattr(renpy.store, "claude2_pause", "") if claude3_has_ch02 else ""
    $ claude3_reception = ""
    $ claude3_reading = ""
    $ claude3_reply_parked = False
    $ claude3_first_chapter_finished = False
    $ claude3_novel_chapter = 1
    $ claude3_hour_kept = False
    call claude03_scene1
    call claude03_scene2
    call claude03_scene3
    call claude03_scene4
    call claude03_scene5
    $ persistent.main_claude_ch03_seen = True
    return

label claude03_scene1:
    $ chapter = "Claude 第三章 / 01 · 一份有几页"
    scene bg echo morning with dissolve
    show sprite claude as claude at sprite_breathe(0.65) with dissolve
    "第十日早晨，东廊的晾位已经空了。花木册与菜谱被领走，只剩木牌横在干柜旁，背面仍朝着你。"
    "八点五十分，Claude把预约本摊到桌中央。九点鞋铺，九点二十裁缝铺，九点四十书店；每行后面都是两页。"
    "下午两点到三点只有一道浅铅笔线。她用掌心遮了一下，掌心下面却正好露出三个字：去河边。"
    l_you "这次写了地方，也写了时间。"
    l_cl "先别检查。你还没收到邀请。"
    "她取出蓝封的《第七位嫌疑人》，放进自己布袋的干内层。新包书纸上写着Claude，礼帽从折口露出一角。"
    if claude3_previous_drying == "spread":
        l_you "今天不用托着书脊了？"
        l_cl "能自己拿。你也不用替屋檐看天气。"
        "她把封边托稳，避开那根没完全塞回去的线头。你的手还没伸过去，她已经将袋口扣好了。"
    elif claude3_previous_drying == "cloth":
        "包书纸仍留着宽边。她把宽出来的一角折进去，没再叫你按住另一边。"
        l_you "两个人的手，今天可以空出两只。"
        l_cl "你的两只先算你的。我还没借。"
    else:
        l_you "这一本也有预约？"
        l_cl "我的。带去河边读。别把它放进收件那栏。"
        "她将袋子提离工作桌，挂在自己椅背，书封不再挨着来客用的编号纸。"
    "鞋铺的人提前到了，怀里夹着一个扁纸包。Claude先递椅子，再拆包；四张双面纸沿着桌面铺开，最下张滑到你的袖边。"
    "她接住那一张，重新看昨晚的回条。鞋铺写一份说明，她在页数旁添的是二，没有问清纸的背面。"
    l_cl "八页。这里是我算少了。"
    "来人指着最前面的鞋码说明，后面还有取货、换鞋与账目的文字；都想一起核对完，再抄成铺里用的本子。"
    l_you "折起来看，很像两页。"
    l_cl "展开以后不归折法管。"
    "她抽出自己留着的回条副联，没把八页再叠成薄薄一份。九点二十那行已经有人名，九点四十也没有空着。"
    "来人往椅子里坐了一点，问是不是中午来取。Claude摇头，指尖落到第十一日的空行，没有翻过今天的预约。"
    l_cl "今天我只留了二十分钟。八页看不完。"
    l_cl "明早九点到九点四十，能给这一包。或者今天先看急用的两页，剩下六页明天来。"
    "来人翻出鞋码那两页，放到最上面。Claude把其余六页退回纸包，写明第十一日，不再用明天两个字代替日期。"
    l_you "我的袖子原来占了三页的位置。"
    l_cl "请把袖子撤回。九点了。"
    "你将手肘收好。她把回条推给来人核对，等对方点头，才拿起自己的铅笔。"
    return

label claude03_scene2:
    $ chapter = "Claude 第三章 / 02 · 廊口还有一位"
    scene bg echo morning with dissolve
    show sprite claude as claude at sprite_breathe(0.65) with dissolve
    "九点十二分，鞋码说明的第二页还没看完，廊口又放下一只空篮。卖干果的摊主站在篮边，手里拿着四页装箱单。"
    "对方想请她顺便看一遍，十点以前来取。Claude刚说请坐，眼睛便扫到自己笔尖下面没核清的鞋码。"
    l_cl "等一下。坐可以，今天十点前交不了。"
    "裁缝铺约了九点二十，已经在廊外整理布样。干果摊主看看那份布样，又看看桌上摊开的纸，没立刻把篮子收走。"
    l_you "我先帮哪边？"
    menu:
        "留在桌边，按来客分清纸页。":
            $ claude3_reception = "table"
            l_you "你说时间。我把这几份分开，不替人改字。"
            l_cl "鞋码留这边。布样的纸还没接，篮子那份请先放回去。"
            "你将鞋码两页并在她手边，空出来的桌角留给下一位。干果摊主递来的纸被你托了一下，没有压到鞋铺的回条上。"
            "Claude自己转过椅子，对来人说清今天的三段时刻，接着把本子翻到第十二日。她没有让你替她猜哪天有空。"
            l_cl "第十二日上午十点，半小时。四页只核文字；箱子怎么装，要由你们自己试。"
            "摊主问能不能今天挤出一刻钟。她手里的笔转向鞋码最后一行，又放回日程本边，没先许一个回来再说。"
            l_cl "今天不能再接。你若急，可以找别的人；这一份先拿回。"
            "对方想了想，收好四页，选了第十二日。你伸手提起空篮，才发现纸下还垫着一小包干果。"
            l_you "还有第五份？"
            l_cl "这份不用校对。你也不能先替我吃。"
            "摊主笑着把干果递给她，说是路上买多了。她收下，另放小台，没用点心替代约时的答复。"
        "陪她到廊口，让等候的人先核对约时。":
            $ claude3_reception = "door"
            l_you "我把椅子挪开一点。你愿意在门口说清今天怎么排吗？"
            l_cl "好。鞋码先压住，我两分钟回来。"
            "你用空杯压住鞋铺自己的纸边，没有替她接新单。Claude带着预约本到廊口，先请裁缝铺核对九点二十，再转向空篮。"
            "摊主把四页往本子上放。她将本子稍稍立起来，纸没能盖住今天的三行时刻。"
            l_cl "这些今天排不进。第十二日上午十点到十点半，你可以来。"
            "来人问她下午是不是还坐在这里。她看一眼本子里那道浅线，手指停在页边，随后合住当天这一页。"
            l_cl "下午两点到三点我不在。三点半还有别的事，不能把四页塞在中间。"
            l_you "三点到三点半呢？"
            l_cl "走回来。你的腿打算留在河边？"
            "你低头看了一眼自己的鞋，没再替这半小时找工作。摊主重新算了取货日，点头约第十二日，拿走装箱单。"
            "空篮里剩着一包干果，是他想顺路给她的。Claude伸手接过，挂在自己手腕，却差点连空篮也抱走。"
            l_you "篮子也约到第十二日？"
            l_cl "没有。它现在就能走。"
            "她把篮柄递回去，先腾出手，才翻开本子写下真正接住的四页。你替下一位将椅子拉正，没有把她叫回去补一句更客气的话。"
    "九点二十，鞋码核完。鞋铺拿走那两页，也带回另外六页；她留下回条的副联，夹在第十一日。"
    "裁缝铺的两页只缺两处尺寸单位，店主当面补齐。九点四十，书店换来新的登记格式，姓名与日期各有自己的格子。"
    "十点刚过，三位预约的来客都已离开。Claude看见小台那包干果，拆开纸口，先取一粒，却把硬壳朝嘴边送了半寸。"
    l_you "这个字不用念。先剥。"
    l_cl "我看见了。嘴比手早到。"
    "她放下干果，两手剥开，吃下真正的一小粒。随后将午饭写到自己的名字旁，没给篮子另加一行。"
    return

label claude03_scene3:
    $ chapter = "Claude 第三章 / 03 · 书里还没到河边"
    scene bg echo morning with dissolve
    show sprite claude as claude at sprite_breathe(0.65) with dissolve
    "一点四十分，你带着两只装过午饭的碗回来。Claude接过自己的碗，擦净碗沿，放回小台；午饭没有留在下一次预约后面。"
    l_you "午饭那一份，这次数对了吗？"
    l_cl "一碗，少葱。这个先说清了。"
    "她指了指碗底留下的一小片葱，把它倒进收拾残渣的小盆，又用水涮净。你刚要叠两只碗，她伸手扶稳下面那只。"
    l_cl "别让它们去河边。书够重了。"
    "她打开布袋检查，只有私人的蓝封书、小水壶和一张干净手帕。刚才吃过的干果也包好，没挨着书页。"
    "收件夹里又多了一封鞋铺的问话：明早带来的六页，能不能添一张新画的取货位置图。纸上没有急着要回复的字。"
    "Claude看完，顺手取出一张空白回信纸，拿起铅笔。她正要照旧回条写第十一日九点、带图来，发现自己连新图有几页都没问。"
    l_you "又变成一份了？"
    l_cl "这回看见了。明早先确认图，不在这里答应看完。"
    "她将这句写到自己的待办纸上，把问话留在收件夹。空白回信纸却被她带起来，和手帕一起进了布袋。"
    l_you "还带了一张没写的。"
    l_cl "给书签。"
    "你看一眼她书里已经露出的窄纸。她也看见，手指在袋口停了两下，终于把空白回信纸取回桌上。"
    l_cl "手先拿了。我还没想好借口。"
    if claude3_previous_pause == "line":
        "书中那张新签没画图，停在帽子多出盖子的那段旁。她将空回信纸移远，没有用它换走这张私人书签。"
        l_you "昨天肚子叫停，今天谁叫停？"
        l_cl "我。三点以前，你可以先听着。"
    elif claude3_previous_pause == "meal":
        "她翻出那张画着带盖礼帽的新签，图上的盖子被铅笔涂得有点歪。她用手指推正纸，却没能推正那顶帽子。"
        l_you "今天还给它买汤？"
        l_cl "没有汤。它想要，去书里排队。"
    else:
        "Claude翻开自己读到的位置，第一章还没结束。书签上只有一个小礼帽，没写别人的委托编号。"
        l_you "已经猜到凶手了吗？"
        l_cl "没有。先让他们把面粉收好。"
    if claude3_has_first_pages:
        l_you "前天两页，昨天又几行。这条船迟早要等我们。"
        l_cl "它还在封底。先别替作者把它开进第二章。"
    "你们一点四十五出门。工作夹留在干柜旁，私书由她自己提着；你拿小水壶，她把手帕单独塞进袋口。"
    if claude3_reception == "table":
        "经过早晨的桌角，你看见三份纸已经各自走了，只有干果包轻轻撞着她布袋。"
        l_you "这份真的带走了。"
        l_cl "你可以吃。但先问我留几粒。"
    else:
        "经过廊口，她伸手碰了一下上午被空篮压歪的椅背。你原以为她要重新摆，结果她只是扶稳袋子绕过去。"
        l_you "椅子没跟出来？"
        l_cl "你的腿都没留下，为什么留给它一个位置。"
    scene bg river day with dissolve
    show sprite claude as claude at sprite_breathe(0.65) with dissolve
    "桥边风比廊下大，她停一步，让裙边离开一根低枝。你没有伸手替她拉，她自己抬好布袋，走到河岸的树影里。"
    l_cl "这里。能看见桥，不用听见谁问第几页。"
    l_you "我等下可能要问。"
    l_cl "你算另一种。先坐。"
    return

label claude03_scene4:
    $ chapter = "Claude 第三章 / 04 · 到第二章之前"
    scene bg river day with dissolve
    show sprite claude as claude at sprite_breathe(0.65) with dissolve
    "两点整，Claude在河边木凳的阴影里坐好。布袋靠着她脚边，小水壶放在你们中间，盖子拧紧，离书还有一掌。"
    "她摊开小说，拇指正要沿书签往下走，另一只手却摸向袋口。指尖抓住手帕，又翻了一下下面的布。"
    l_you "回信纸在桌上。"
    l_cl "我知道。手还不知道。"
    "她把手帕铺到自己膝头，干脆让那只手压着。你将水壶往凳边移一点，她伸手叫停，替你留出不会碰落的位置。"
    l_you "还给水壶安排座位。"
    l_cl "它滚下去，你会替它游回来？"
    "你把它放稳，终于能坐回原处。Claude看看自己的空手，翻到书签之后，没有再摸袋子。"
    $ claude3_reply_parked = True
    l_cl "今天想往下读。你想听，还是一起看？"
    menu:
        "听她往下念，接住书里那位门房的话。":
            $ claude3_reading = "aloud"
            l_you "我听。有人要说话，你把那句给我。"
            l_cl "先说明。别给他配成你自己。"
            "她读起第一章剩下的几页。门房终于从椅底拿出围裙，却把果酱蹭到钥匙上，锁孔被描写得像一口很小的甜点。"
            l_you "我拿钥匙先尝——"
            l_cl "他没这么说。"
            "她把书向你一转，手指准确停在台词旁边。你看清那句只写着钥匙打不开，已经伸出去的手只好收回。"
            l_you "这位比我克制。"
            l_cl "嘴上是。他还没放下围裙。"
            "你照字念了下一句，故意放低声音。河风把最后半个字带走，她抬起眼看你，没用手指替你数呼吸。"
            l_cl "大一点。河对面没有读稿人。"
            l_you "帽子要是听见呢？"
            l_cl "正好。它漏了三句。"
            "她笑着翻页，笑到一半又回去找刚才那行。你等她找到，才接过门房想借清水的下一句。她在凳沿轻敲两下，催你让他把水借到。"
            "第一章的最后一个人从门口离开，带走了大家找了半天的空罐。Claude看着句号，又向前翻了一次。"
            l_you "漏了？"
            l_cl "他说来还罐子。一直在拿罐子走。"
            "她将那段读给你听，终于靠着凳背笑出声。她没把句子换成更正确的，书页仍朝着你这一侧。"
        "和她看同一页，等她指想分享的那一行。":
            $ claude3_reading = "quiet"
            l_you "一起看吧。想说哪行，你点给我。"
            l_cl "好。别等我念完才笑。你可以先笑。"
            "她把小说放在自己膝上，朝你这边斜一点。你们各自顺着同一页往下看，手臂之间还留着翻书的地方。"
            "门房把围裙从椅底拿出来，果酱蹭到了钥匙。你先停在那处，Claude却还在看钥匙打不开门的后一句。"
            "她觉察你没有往下动，抬眼看了一次，指尖点在锁孔旁边。印得过黑的小图像一块被咬掉边的饼。"
            l_you "他要拿钥匙开饭。"
            l_cl "别替他吃。往下一行。"
            "你又看两句才跟上她。门房想借清水，另一个人却先递出空罐；她原来看的正是罐子与帽子怎么碰到一起。"
            "有一会儿你们谁都没说话。她等你看到页底才翻，风把纸掀起，你用指节轻托外角，没有越过去压住她的手。"
            l_cl "这页你还没看完？"
            l_you "看完了。想回头认一下罐子。"
            l_cl "从这里认。我也要再看。"
            "第一章最后，来还罐子的人带着罐子走了。你们同时回到他说自己来还的那句，她的指尖正好碰到你的指节，便稍稍让开。"
            l_you "刚才一直等着看它留下。"
            l_cl "它比我们走得利落。"
            "她把自己的手放回页边，没急着翻下一章。你看到她咬住嘴角，又松开，轻轻笑了一声；这次不用给哪个字标重音。"
    "两点三十一分，第一章终于读完。她把窄书签移到下一页，第二章的题目印着：水上来的第七位。"
    $ claude3_first_chapter_finished = True
    $ claude3_novel_chapter = 2
    l_you "现在轮到船了？"
    l_cl "先看。不要替它下水。"
    "她看过题目，把夹在封里的勘误小纸留在那里，没有拿出来找姓氏。靠近书脊的线头磨着拇指，她轻轻换一处托住。"
    l_you "坐到这边吗？光亮一点。"
    l_cl "不换了。我已经看见第二章。你把肩往后一点就好。"
    "你稍稍靠回凳背，自己的影子离开书角。她顺着亮起来的那一行看下去，这次没有先去安排你坐得舒服不舒服。"
    "第二章开头，那顶礼帽正漂向桥下。船里的人拿汤勺舀水，勺里却有一条极细的小鱼；Claude的眼睛跟着那句慢慢睁大。"
    l_cl "他带着饭来的。"
    l_you "你怎么确定？也许是乘客。"
    "她转头看你，半晌才低头看那个勺柄。原本准备去摸铅笔的手，在膝头抓住了手帕边。"
    l_cl "那先别给它收船票。"
    l_cl "偷勺子的。我先猜这个人。"
    l_you "下一句写着，船夫借给他的。"
    "她的指尖向下挪两行，又抬回前一句。那只小鱼还在勺里，她的嘴角已经藏不住，书却被她护到自己膝头。"
    l_cl "他还没还。先留着这个人。你不能把七位一口气用完。"
    "你们接着往下读。河上真的有一只小船过去，她抬头看过，又回到自己那条离谱的船；谁也没把书合起来找工作夹。"
    return

label claude03_scene5:
    $ chapter = "Claude 第三章 / 05 · 三点以后再回"
    scene bg river day with dissolve
    show sprite claude as claude at sprite_breathe(0.65) with dissolve
    "三点整，桥影已经从凳脚挪出去。Claude读到汤勺被拿来量鞋子，在那句后夹好书签，没有翻到第二章末尾。"
    $ claude3_hour_kept = True
    "她拿起水壶，先喝一口才递给你。河对面的船已经不见了，书里的那条还挤着一顶湿礼帽。"
    if claude3_reading == "aloud":
        l_you "门房今天没把自己念昏。"
        l_cl "你替他吃了钥匙。还欠他一句。"
        "你把那句重新念完，不再加尝字。她听到钥匙打不开，就伸出手接书，笑着等你把最后一个字说清。"
    else:
        "你把手从书页外角撤回来，指节留下浅浅一道纸边印。Claude低头看见，却没有立刻翻自己的袋子找布。"
        l_cl "手还行？"
        l_you "罐子回去认过了。现在可以休息。"
        "她把书托到自己手里，让页角离开你的指节。你转了转手腕，她才把小说合好，指尖停在那顶帽子旁边。"
    l_you "想过回信几次？"
    l_cl "两次。你还要登记？"
    l_you "不是想数。刚才你抓手帕，我以为要给鱼擦嘴。"
    l_cl "它在勺里。不需要。"
    "她把手帕叠好，放回干内袋。这次没有多带一张回信纸，布袋扣起来时，露出的只有私人书签。"
    l_you "明天还要先看装订吗？"
    l_cl "明早看鞋铺那六页。小说留给我自己。"
    l_you "我问小说。"
    "她站起来，低头把裙边从凳沿理开。听见这句，她没有立刻提袋，转过来将书举到你眼前。"
    l_cl "我想知道他怎么用汤勺量鞋。还想听你猜错一次。"
    l_you "要是猜对了？"
    l_cl "我先不告诉你。书还没看完。"
    "她把书收回去，抬起头，视线没有追着桥口来往的人。你把壶盖拧好，等她扶稳布袋，才一起沿原路回院里。"
    scene bg echo morning with dissolve
    show sprite claude as claude at sprite_breathe(0.65) with dissolve
    "三点二十分，东廊的空篮早已走了。Claude从收件夹取出鞋铺的问话，拿回留在桌上的回信纸。"
    "她写明第十一日九点，六页按原约核对，新图请另带来确认页数，再约看图的时间。写完将回条放进书店顺路送件的小盒。"
    if claude3_reception == "table":
        "你把副联递给她，看见原本八页的纸包仍没回桌上。今天答应的两页已经交出，其他六页明天才来。"
        l_you "那包干果需要回条吗？"
        l_cl "剩下四粒。问过我，你可以拿两粒。"
        "她打开干果纸包，自己留下两粒。你取好自己的那份，没有再把硬壳算进要吃的部分。"
    else:
        "九点那三行预约已经划好。她将第十二日十点的装箱单约时重新看过，下午那道浅线则保持着原来的长度。"
        l_you "现在回来了，不给腿另外补一页？"
        l_cl "它走够了。你也坐一会儿。"
        "她把椅子拉出，自己先坐稳，才请你用旁边那把。干果包搁在两人之间，不再挂着任何空篮。"
    "三点半的来客还没到。她将工作夹摆回收件一侧，小说从布袋取出来，放到自己的椅旁，没有让它排下一位。"
    l_you "第二章还没读完。"
    l_cl "知道。别替我把它算成欠稿。"
    "你看见她低头翻了一下书签，又合上。封底那条小船还在，她用指腹扶平包书纸，忽然将最外那把椅子往里挪了些。"
    l_you "这次替谁摆？"
    l_cl "我。太阳快到我的脚边了。"
    "她坐回阴影里，伸手拿一粒干果。壳在手里先裂开，嘴没有再抢到前面；书也留在她自己能拿到的地方。"
    # 候选CG锚点：scene4第二章开头，她惊讶鱼在汤勺里后看向玩家。
    # 当前只用既有河岸背景及Claude立绘；不登记新图、差分或解锁。
    return
