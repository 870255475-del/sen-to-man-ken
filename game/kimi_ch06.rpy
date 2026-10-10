# Kimi第六章《一起翻过这一页》；第十四日，v0.14独立候选，未接入／未native。
# 参与本章的新当事人、Kimi与玩家均为30岁成年人；玩家无立绘。
# 昨日回声须当前第五章完整断点；旧目录、原页、许葵愿签不再归还一次。
# 本章只写kimi6_、章节显示与自身seen；无关系结局、UUID、周目、图库调用。

default persistent.main_kimi_ch06_seen = False
default kimi6_has_ch05 = False
default kimi6_previous_returning = ""
default kimi6_previous_departure = ""
default kimi6_join = ""
default kimi6_pace = ""
default kimi6_archive_checked = False
default kimi6_archive_returned = False
default kimi6_public_index_closed = False
default kimi6_new_map_drawn = False
default kimi6_invited = False
default kimi6_met = False
default kimi6_bridge_crossed = False
default kimi6_shared_segment_finished = False
default kimi6_solo_left = False
default kimi6_solo_returned = False
default kimi6_map_kept = False

label kimi_ch06:
    $ kimi6_has_ch05 = persistent.main_kimi_ch05_seen is True and main_last_chapter == "kimi_ch05" and kimi5_returning in ("separate", "show_line") and kimi5_wish_written is True and kimi5_wish_returned is True and kimi5_notebook_returned is True and kimi5_addition_marked is True and kimi5_bag_returned is True and kimi5_solo_left is True and kimi5_solo_returned is True and kimi5_own_wish_kept is True and ((kimi5_departure == "leave" and kimi5_cloth_lent is False and kimi5_cloth_returned is False) or (kimi5_departure == "lend_cloth" and kimi5_cloth_lent is True and kimi5_cloth_returned is True))
    $ kimi6_previous_returning = ""
    $ kimi6_previous_departure = ""
    if kimi6_has_ch05:
        $ kimi6_previous_returning = kimi5_returning
        $ kimi6_previous_departure = kimi5_departure
    $ kimi6_join = ""
    $ kimi6_pace = ""
    $ kimi6_archive_checked = False
    $ kimi6_archive_returned = False
    $ kimi6_public_index_closed = False
    $ kimi6_new_map_drawn = False
    $ kimi6_invited = False
    $ kimi6_met = False
    $ kimi6_bridge_crossed = False
    $ kimi6_shared_segment_finished = False
    $ kimi6_solo_left = False
    $ kimi6_solo_returned = False
    $ kimi6_map_kept = False
    call kimi06_scene1
    call kimi06_scene2
    call kimi06_scene3
    call kimi06_scene4
    call kimi06_scene5
    $ persistent.main_kimi_ch06_seen = True
    return

label kimi06_scene1:
    $ chapter = "Kimi 第六章 / 01 · 今天借的这一件"
    scene bg echo morning with dissolve
    show sprite kimi as kimi at sprite_breathe(0.63) with dissolve
    "第十四日上午八点四十，院廊的桌上摊着一本灰封柜位册。Kimi坐在靠外的椅子上，脚边只放自己的布袋。"
    "她用手掌压平翘起的封角。杯里的麦茶已经凉了，她仍喝了一口，随后把杯子移到纸够不到的位置。"
    l_you "又是要补的旧目录？"
    l_kimi "今天刚借的。看封面。"
    "封面写着春季柜位册，书铺林杏的姓名在右下角。灰纸套另放在桌边，今早八点二十的借条夹在套口。"
    "林杏与她同岁，今天值书铺早柜。公共收件柜挪了三格，Kimi向她借旧册核位置，约九点半由本人来取。"
    l_you "你不是说今天休息？"
    l_kimi "做完这三格就休。午饭不替谁找页码。"
    "她把柜位册的左页翻开，右页用一枚木夹固定。你伸手去扶夹子，她看了看，等你发现夹住了自己的袖口。"
    l_you "这个夹得挺牢。"
    l_kimi "嗯。衣服可以先撤。"
    "你松开木夹，把袖子挽上去，再夹在她指的位置。她将册子稍稍推近，给你留出能看清编号的半边。"
    "第一格原放公共布告，第二格是借还回条，第三格收临时待认领的纸。你抄到第三格时，顺手写了待送信件。"
    l_kimi "这一格不寄。把地址那栏看完。"
    "地址栏只有柜位，没有街号。你划掉自己加的信件，按原页写回临时待认领，并在旁边留下改过的记号。"
    l_you "我看见纸封，就以为能送。"
    l_kimi "饼也有纸封。"
    l_you "饼至少知道要送到哪里。"
    l_kimi "那是你吃得快。"
    "你们照着册子核完三格。她起身拉开公共收件柜，取出今早单独放入第三格的一张无署名位置条。"
    "条上只画了一个窗角与几道线，没有人名。它不属于借来的柜位册，也没有夹在任何人的私册里。"
    "你把它转了半圈，以为画的是河边一户的门。Kimi拿过条子，走到柜旁，比了比朝向，又放回桌上。"
    l_kimi "我也认不出来。别替它找主人。"
    l_you "那这一格怎么记？"
    "她拿的是公共目录纸，只填第十四日收件、无署名位置条、第三格待领。用途那栏留待核，没有抄下图里的线。"
    l_kimi "有人来问，能找到这张。现在就到这里。"
    "她把位置条收入公共柜第三格的透明纸袋，封口仍能拆开。目录纸放回柜外夹板，私人布袋一直留在椅子旁。"
    $ kimi6_archive_checked = True
    "她回座位将木夹取下来，柜位册合好。杯沿留着一条茶色，她用自己的小刷子刷净，没有拿工作纸垫杯底。"
    if kimi6_has_ch05:
        if kimi6_previous_departure == "lend_cloth":
            l_you "我的手巾已经晾干了，今天带在自己袋里。"
            l_kimi "昨天洗了两遍。还给你以后，差点又想拧一次。"
            l_you "水都拧完了，再拧只能拧出脾气。"
            l_kimi "那个还剩一点。"
        else:
            "你提起自己的袋子，把水瓶挪到内侧。她看了一眼你空着的手，没有把自己袋子的提手递来。"
            l_kimi "今天东西不多，我拿得动。"
        if kimi6_previous_returning == "separate":
            l_kimi "昨天后来我标了你添的那行。纸还在我册里。"
        else:
            l_kimi "昨天当场括住的那行，我还留着。没有擦。"
        l_you "我今天带了铅笔，先放自己兜里。"
        "她点一下头，没打开私人薄册。你将铅笔扣回袋内，取空杯去接水，她重新把灰纸套展开。"
    else:
        "她的私人薄册合在袋内，你能看见一小截素色书签。她没有翻它，先把今天借的柜位册收入灰纸套。"
        l_kimi "等这件拿走，我就出门。"
    return

label kimi06_scene2:
    $ chapter = "Kimi 第六章 / 02 · 饼画得太大"
    scene bg echo morning with dissolve
    show sprite kimi as kimi at sprite_breathe(0.63) with dissolve
    "九点半，林杏按约来到院廊。Kimi先把春季柜位册交到她手里，再将灰纸套递过去，请她核左页的木夹印。"
    "林杏翻过核位置的那页，套好纸套，签收今早这张借条。册子与套一起拿走，借条存入公共借还格。"
    $ kimi6_archive_returned = True
    "Kimi在公共目录上记下交还时间。无署名位置条仍留第三格，没有跟着林杏出门，也没有进她自己的布袋。"
    $ kimi6_public_index_closed = True
    "她收起工作笔，起身将院廊椅子推回桌边。你还站在那里，手上空空，差一点把椅背也当成待交回的一件。"
    l_kimi "椅子留下。我下午可能还要坐。"
    l_you "今天已经还了这么多，顺手。"
    l_kimi "一本，一只套。你把三格都算成书了？"
    "你笑着松手，把木夹盒挪到桌角。她从自己的抽屉拿出新白纸，写第十四日与Kimi，纸头添了休息日地图。"
    "纸上没有愿签字样，也没有编号。她将自己的私人薄册留在袋内，只把这张新地图摊到干净的半张桌面。"
    l_you "你要画到哪里？"
    l_kimi "先画我今天想吃的。"
    "她在院门旁画一只圆饼，转笔又添三道南瓜纹。饼占了纸中央一大块，桥头那道短线只剩一个小角。"
    l_you "这饼一口能把桥吞了。"
    l_kimi "我饿的时候，差不多。"
    "她抬头看一眼河的方向，自己也笑了。橡皮擦到一半掉在膝上，她低头去捡，额发碰到了桌沿。"
    l_you "桥没事吧？"
    l_kimi "我的头碰的。问我。"
    l_you "疼不疼？"
    l_kimi "不疼。桥要是问，也说不疼。"
    "她把圆饼擦小，留下一圈淡淡的旧线。院门与桥头终于能接上，她拿自己的尺子比过距离，却没往桥后续线。"
    l_kimi "我想走一段慢的。十一点在桥头。"
    l_you "你想自己去，还是……"
    "她用笔尾轻敲一下新纸左边，眼睛朝你抬了抬。"
    l_kimi "这次在问你。来吗？"
    l_you "来。你想从哪一段开始？"
    "她把尺子收起来，只留笔在手上。院门到桥头的线还很淡，桥边的起点是一个没有涂实的小圆。"
    menu:
        "十点四十五在院门碰面，一起到桥头。":
            $ kimi6_join = "gate"
            l_you "院门吧。我十点四十五把自己的东西带齐。"
            l_kimi "那我买饼回来找你。别替我先定午饭。"
            "她在院门边写十点四十五，在桥头写十一点。两处都只记碰面安排，旁边没有已到的圈。"
            l_you "我要是站错门？"
            l_kimi "这院子就一个。真能错，我去看一下。"
        "十一点直接在桥头碰面，各自走过去。":
            $ kimi6_join = "bridge"
            l_you "桥头吧。我先把自己的水装好，十一点到。"
            l_kimi "我买完饼自己过去。在干砖这边等。"
            "她只在桥头写十一点，院门到桥头的线留给自己走。你没有把两个人的脚印提前添上去。"
            l_you "我要是找错了桥？"
            l_kimi "先别给铅笔找借口。看河。"
    $ kimi6_new_map_drawn = True
    $ kimi6_invited = True
    "她把新地图沿空处折好，收到自己布袋的平兜。笔有盖地扣在袋内，折线刚好避开桥头那个小圆。"
    "十点，她去桥头前的饼摊。你留在院廊洗自己的水瓶，瓶口漏出几滴，只好再拧开盖子找歪了的胶圈。"
    "她走到院门时听见你说找到罪魁祸首，回头看了一眼。你两只手举着胶圈，连干布都还没找来。"
    l_kimi "别审它。放正就行。"
    l_you "你放心买饼。十一点之前能结案。"
    "她从自己的袋里取出帽子戴好，跨出院门。你将胶圈按回盖内，重新装水，又把自己的布袋挂到近门的钩上。"
    return

label kimi06_scene3:
    $ chapter = "Kimi 第六章 / 03 · 手伸回来"
    scene bg river day with dissolve
    show sprite kimi as kimi at sprite_breathe(0.63) with dissolve
    if kimi6_join == "gate":
        "十点四十五，Kimi提着布袋回到院门。两只新南瓜饼各包一张油纸，她将袋子托稳，先等你锁好自己的水瓶。"
        l_you "已经放正了。要摇给你看吗？"
        l_kimi "不用。喝得到就算。"
        "你们从院门一起走，途中她停下来把鞋带末端塞进鞋侧。你握着自己的袋带，等她将两边都收好。"
        "十一点到了桥头，她才取出新地图，给院门到桥头添一道细线。纸上原先的碰面时间没有改成别的约定。"
        l_kimi "这一小段，可以画实了。"
    else:
        "十点五十五，你独自到了桥头，站在约好的干砖侧。自己的水瓶装满，瓶盖松紧也试过，没买两个人的午饭。"
        "十一点，Kimi从院子的方向走来，手里提自己的布袋。两只南瓜饼各有油纸包，水瓶还在袋的外兜。"
        l_kimi "早到了？"
        l_you "怕把河看错。现在确定了。"
        "她低头笑了一下，取出新地图，只给桥头的小圆添了点。院门那条是她独走的，没有补上你的名字。"
        l_you "这边是我今天的起点。"
        l_kimi "嗯。我在这里看见你。"
    $ kimi6_met = True
    "她把地图折回平兜，笔也扣回袋内，袋口扣好。你们走过桥面，到桥后干砖道的第一道高沿前停下，水面在石栏外。"
    "Kimi先跨上那道砖沿，确认两脚站稳。她将布袋提手挂到左前臂，腾出的右手伸回来，掌心朝上。"
    l_kimi "这边。要搭一下吗？"
    "你看了看她的手，又看高沿。你们之间还有半步，她的掌心停在那里，等着你抬手。"
    l_you "好。水瓶我自己拿。"
    "你把自己的布袋留在左肩，右手搭进她掌心。她指尖轻轻合住，你踏到干砖上，站稳后，两只手才松开。"
    $ kimi6_bridge_crossed = True
    "她右手落回袋边，拇指蹭过刚才压出的提手印。你慢半步走到她旁边，鞋底在干砖上蹭出一点细砂。"
    l_you "刚才还挺像去远方。"
    l_kimi "先把鞋里的砂倒了。远方等一下。"
    "你扶着石栏把鞋跟抬起，砂粒倒出来。她背过身笑了一声，等你穿好鞋，才把自己袋子换到右手。"
    l_you "你是不是早就看见砂了？"
    l_kimi "上台阶以后。你脚趾动得很忙。"
    "两只饼从袋里挤到一起，纸包都还完好。她将较小那只转过来，闻过暖气，又把它推回去，暂时没有开包。"
    l_you "饼都买好了，怎么还走？"
    l_kimi "想找个不用守着筷子快吃的地方。"
    "她指向砖道口的一小段树荫。树下是干台阶，旁边另有一段能走到东端石栏的平路，两边都看得见桥。"
    l_kimi "坐一会儿，或者先走到那头。你想哪样？"
    l_you "这一段你本来想叫我一起？"
    l_kimi "嗯。不是整张地图。"
    if kimi6_has_ch05:
        "她说完，手指停在布袋平兜上，没有抽出昨天的私人愿签。你把自己的铅笔往袋内按了按，继续看眼前的路。"
        l_you "昨天那两行，我确实不该替你写。"
        l_kimi "我还不喜欢。今天这张先让我自己画。"
        l_you "好。你问的那段，我认真走。"
        "她将袋子往肩上提稳，目光从你的袋口移回来。你们站在同一块干砖上，谁也没急着往转弯后看。"
    else:
        "她的平兜里只露着今天新纸的一角。你往她指的两条公共路看了一眼，没问合在袋内的私册写了什么。"
        l_you "先走你刚指的这段。后面等你想好。"
        l_kimi "我今天也没想好全部。"
    "十一点十分，树影刚好落到台阶前。她拿出小饼的纸包，轻轻按过折口，等你把自己的水瓶放稳。"
    return

label kimi06_scene4:
    $ chapter = "Kimi 第六章 / 04 · 慢一点也有地方去"
    scene bg river day with dissolve
    show sprite kimi as kimi at sprite_breathe(0.63) with dissolve
    "Kimi把纸包打开，小饼边上缺了一点，露出软黄的南瓜馅。她拿起来看过，先将另一只完整的放回布袋。"
    l_you "这个买来就被咬过？"
    l_kimi "被我。买完就试的，怕两只都不好吃。"
    l_you "你已经替它们结案了。"
    l_kimi "也有可能继续吃证据。"
    "她笑着把缺角那只留给自己，完整的仍包好。你拿出自己的水瓶，盖子这回没有漏到掌心。"
    menu:
        "在树荫的干台阶坐一会儿，再分开走。":
            $ kimi6_pace = "rest"
            "你指了指树荫里更干的一阶。她坐到靠栏侧，把自己的布袋立在脚旁，你在另一侧放好自己的袋子。"
            l_you "坐着吃，证据掉了也容易找到。"
            l_kimi "你要帮我捡的话，先看是不是砂。"
            "她掰下缺角旁一小块，自己吃了。另一只完整的饼从袋里拿出，她没有递到你嘴边，只将纸包放在两人之间。"
            l_kimi "这一只要吗？我还带了别的。"
            l_you "要。我拿这个，你留小的慢慢吃。"
            "你拿起自己的那包，拆到能托住饼底为止。她看你把油纸折成一个过高的筒，用指尖轻点了一下筒沿。"
            l_kimi "你在喂袖口。往下折。"
            "你将纸沿折低，她才咬下自己下一口。两人各拿各的饼，饼屑掉到纸上，她用指腹把自己的细屑拢到一边。"
            "她把小饼放回油纸，搁在脚旁立稳的布袋上。空出手取新地图，铺到自己膝上，先画砖沿，再画干台阶边的树影。"
            l_you "这里要画两只饼吗？"
            l_kimi "画两个人坐过。饼会把树吃掉。"
            "十一点二十五，她喝完自己瓶里一口水，盖严瓶盖，将余下的小饼包好。你吃完自己的那只，把油纸收入自己的袋。"
            "她把新图纸折回平兜，起身抚平裙边，等你也站稳了。你们走到树荫尽头，停在不挡人的干砖侧。"
        "沿平路走到东端石栏，再分开走。":
            $ kimi6_pace = "walk"
            "你把自己的水瓶盖紧，与她沿平路走。Kimi将开过的小饼重新包好，放进布袋上层，先留右手提稳袋口。"
            l_you "走到东端，应该不远。"
            l_kimi "你步子小一点。饼在追你。"
            "你放慢一步。她跟上来，转头看见你把速度放得过慢，鞋底拖出一道细响，便用袋边轻碰一下你的肘外侧。"
            l_kimi "正常走。又没叫你练蜗牛。"
            "十一点二十，你们到了东端石栏。她靠干砖侧站住，先把新地图取出，在石栏旁画今天走过的终点。"
            l_you "走到这里，饼追上了吗？"
            l_kimi "追上了。你可以收。"
            "她收好笔与图纸，才取出完整的饼递给你。你问过这只给自己，她点头，另一只缺角饼仍由她拿着。"
            "你们各自拆包，站在石栏内侧吃。她托着油纸折角慢慢咬，你咬得太大，南瓜馅差点沿纸缝挤到手指。"
            l_kimi "慢点。它没有第二场追逐。"
            l_you "我是怕掉下去。"
            l_kimi "咬小口，比追它有用。"
            "十一点二十五，她把剩下的小饼包回自己袋里，你将吃空的油纸收入自己的袋。两人各喝自己的水，瓶盖都收好。"
            "她把布袋移到身侧，沿来路走回不挡人的干砖口。你与她一起返回，这条短来路在新地图上由她添了箭头。"
    $ kimi6_shared_segment_finished = True
    "十一点半，Kimi停住，左手扶着布袋平兜。你们刚走过的桥还在身后，转弯后面从这里看不到。"
    l_kimi "下面我想自己走。先在这里分。"
    l_you "好。我回院里，不在转弯处等。"
    "她点头，提起自己的布袋。你从另一个方向回桥头，鞋里的砂已经倒净，没再借停步去看她往哪里走。"
    $ kimi6_solo_left = True
    "走到桥面中央，你摸到袋内的空油纸包，将它压在自己的水瓶旁。石栏外响起车铃，你沿干砖继续往院门走。"
    return

label kimi06_scene5:
    $ chapter = "Kimi 第六章 / 05 · 留在她手里"
    scene bg echo morning with dissolve
    show sprite kimi as kimi at sprite_breathe(0.63) with dissolve
    "下午一点二十，你在院廊把自己的水瓶晾好。Kimi从院门进来，鞋尖有几粒干灰，帽子拿在自己手里。"
    $ kimi6_solo_returned = True
    "她把帽子挂回近门的钩上，布袋留在自己椅边。你挪开桌上的杯子，给她留出一块干净地方，没伸手去接袋口。"
    l_you "给你留了空桌面。茶在壶里，想喝自己倒。"
    l_kimi "嗯。我先坐，脚底还有点热。"
    "她坐下，把鞋尖往椅下收了一点。你取出自己袋里的油纸，正想连饼屑一起倒进纸桶，她抬手指了过来。"
    l_kimi "那是木夹盒。"
    "你翻过盒底，才看见自己今早收桌时摆反的标签。木夹安稳地挤在里面，你把油纸送到真正的纸桶里。"
    l_you "它们今天差点加餐。"
    l_kimi "不用。早晨已经吃过你袖子了。"
    "你将标签转回正面，她抿着嘴笑了一下，给自己的杯子倒半杯麦茶。杯子离她准备铺纸的地方留着一掌宽。"
    "她从布袋平兜拿出今天的新地图，自己展开。剩下那半张折在纸背，只给你看桥与方才共走的一小段。"
    if kimi6_join == "gate":
        l_kimi "院门这里，十点四十五。你带着修好的瓶盖。"
        l_you "可以不把胶圈单独画出来吗？"
        l_kimi "没打算画。它太小，饼会找不到。"
    else:
        l_kimi "桥头这里，十一点。你已经站在干砖这边。"
        l_you "前面那条，是你自己走的。"
        "她点头，笔停在桥头的小圆上，没有将你的起点往院门挪。"
    if kimi6_pace == "rest":
        "台阶边的小树影已经画好，她加了一道短线，标两个座位。你看见树影落到饼原先的大圆外，没再提醒她擦净。"
        l_you "这里还有一点最早画的饼。"
        l_kimi "留着。我当时真的饿。"
    else:
        "东端石栏旁留着终点与返回的箭头。她在石栏里面加一个小方块，用来记你们站着吃饼时落脚的地方。"
        l_you "这一格没把我们圈在河里。"
        l_kimi "你今天鞋已经倒过一次，不想再倒水吧。"
    "她写下今天的日期，再在这段线的末尾添一个小点。笔没有越过折到纸背的那半张，新地图仍拿在她手里。"
    if kimi6_has_ch05:
        l_you "谢谢你今天愿意叫我。"
        "她端起自己的杯子，先喝掉含在嘴边的一口。指尖拢着杯沿，过了一会儿才抬眼。"
        l_kimi "昨天还在。今天也走了这一段。"
        "你托稳自己的杯子，等她将今天的图纸叠好。她把新地图收入自己布袋的平兜，私人薄册仍另外合着。"
    else:
        l_you "今天这段走得挺舒服。"
        l_kimi "我也是。下回想好了，再问你。"
        "她把今天的图纸重新折好，收进自己布袋的平兜。另合在袋内的私人薄册，封角压着那截素色书签。"
    $ kimi6_map_kept = True
    "她从袋里取出剩下的小饼，自己的油纸包还包得严。你已经吃完那只，她看了你一眼，先把最后一口放进自己嘴里。"
    l_you "我只是看有没有凉。"
    l_kimi "凉了也归我。你这借口不太热。"
    "你笑着拿回自己的杯子。她嚼完才把纸包折平，起身丢进纸桶，又把今早那枚木夹推回盒里，夹口朝着里面。"
    "公共柜外的目录夹板还在，柜位册已被主人取走。她把自己的布袋提到膝上，坐回有树影的那一侧。"
    l_you "下午还出去吗？"
    l_kimi "先休息。今天还有这一项。"
    "她把椅子往后挪一点，给自己的脚让出位置。你坐到隔桌的椅子上，两只杯子各在各的手边，布袋平兜的扣子已经扣稳。"
    return
