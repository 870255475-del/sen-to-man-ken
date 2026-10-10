# Claude第四章候选 / 这一句我不同意 / 第十一日 / 全员成年三十岁。
# 只用既有scene/show、l_cl/l_you和sprite_breathe；无新CG或路线结束API。
# 前史需第三章合法动作、末场状态与真实外层章节断点共同成立。

default persistent.main_claude_ch04_seen = False
default claude4_has_ch03 = False
default claude4_previous_reception = ""
default claude4_previous_reading = ""
default claude4_response = ""
default claude4_repair = ""
default claude4_old_print_cost = 0
default claude4_new_print_cost = 0
default claude4_own_print_paid = 0
default claude4_lost_wage_repaid = False
default claude4_claim_withdrawn = False
default claude4_sites_changed = 0
default claude4_meal_taken = False
default claude4_private_page_shared = False
default claude4_novel_chapter = 2

label claude_ch04:
    $ claude4_has_ch03 = getattr(persistent, "main_claude_ch03_seen", False) is True and getattr(renpy.store, "main_last_chapter", "") == "claude_ch03" and getattr(renpy.store, "claude3_reception", "") in ("table", "door") and getattr(renpy.store, "claude3_reading", "") in ("aloud", "quiet") and getattr(renpy.store, "claude3_reply_parked", False) is True and getattr(renpy.store, "claude3_first_chapter_finished", False) is True and getattr(renpy.store, "claude3_novel_chapter", 0) == 2 and getattr(renpy.store, "claude3_hour_kept", False) is True
    $ claude4_previous_reception = getattr(renpy.store, "claude3_reception", "") if claude4_has_ch03 else ""
    $ claude4_previous_reading = getattr(renpy.store, "claude3_reading", "") if claude4_has_ch03 else ""
    $ claude4_response = ""
    $ claude4_repair = ""
    $ claude4_old_print_cost = 0
    $ claude4_new_print_cost = 0
    $ claude4_own_print_paid = 0
    $ claude4_lost_wage_repaid = False
    $ claude4_claim_withdrawn = False
    $ claude4_sites_changed = 0
    $ claude4_meal_taken = False
    $ claude4_private_page_shared = False
    $ claude4_novel_chapter = 2
    call claude04_scene1
    call claude04_scene2
    call claude04_scene3
    call claude04_scene4
    call claude04_scene5
    $ persistent.main_claude_ch04_seen = True
    return

label claude04_scene1:
    $ chapter = "Claude 第四章 / 01 · 名字下面那句话"
    scene bg echo morning with dissolve
    show sprite claude as claude at sprite_breathe(0.65) with dissolve
    "第十一日九点，鞋铺的六页按约放到东廊桌上。Claude将双面纸一张张分开，回条压在最外侧，空杯没有压住任何一个字。"
    if claude4_has_ch03:
        l_you "这回六页都在。没有跟着袖子多出来。"
        l_cl "你把手放好，我才能数到最后。"
        "她翻出昨天三点二十分写的回信，新图另约那句还在。来人将地点图单独交来，没有混进这六页。"
    else:
        "她让你先看本子上的约时：九点到九点四十，六页。旁边另夹着来客带来的地点图，没有写进同一份任务里。"
        l_cl "这边按约核。那张图先看清有几处，再约。"
        l_you "不用把两份折成一份？"
        l_cl "纸会听，字不会少。"
    "九点四十，取货和换鞋的说明核清，鞋铺自己改好账目旁缺的一行。地点图只有一张，四处还要标清，另约第十三日九点到九点二十。店主将两份都收回。"
    "Claude在本子上划掉六页那行，翻到第十二日，确认十点到十点半仍留给干果摊的四页装箱单。"
    l_you "那一格没让给鞋子？"
    l_cl "它们各走各的。箱子比鞋多，挤不进。"
    "她把本子合好，从椅背的布袋里取出蓝封小说。新包书纸写着她的名字，第二章那枚窄签仍从上沿露出来。"
    if claude4_previous_reading == "aloud":
        l_you "门房今天还开饭吗？"
        l_cl "他没说过。是你给钥匙加的那一口。"
    elif claude4_previous_reading == "quiet":
        l_you "罐子昨天走得太快，今天先认哪一个？"
        l_cl "汤勺。它刚去量鞋，我怕认晚了变尺子。"
    else:
        l_you "读到哪儿了？"
        l_cl "第二章。有人用汤勺量鞋，凶手还没看见。"
    "她把包书纸展开一角，封底的小船与汤勺露出来。你看到那顶礼帽像是比船更大，她将书换一只手拿，终于没挡住船头。"
    l_you "只载帽子，会不会快一点？"
    l_cl "它得留下一个划船的。你不能全替它卸掉。"
    "她刚想往下翻，十点整，印铺的人拿来一卷祭典书廊的告示。第一张还卷着，她先看见自己的名字。"
    "名字下面印着两行：经Claude逐篇审定。免费接稿，当日全改好。原本只说今天午后共读一页的小活动，变成了整日的接稿承诺。"
    "Claude摊开原稿。她之前只改过十三点三十分那个时刻，并补上东廊二字；原稿里没有这两行，也没有署名。"
    l_cl "这一句我不同意。还有下一句。都得拿掉。"
    "来人把整卷放到桌上，说十二张都已印好，四张贴出，八张还没送；一共收了十八元纸工钱。"
    $ claude4_old_print_cost = 18
    l_you "已经有人看见了。"
    l_cl "所以先收住这八张。那四张请现在取回来。"
    "她用干净木夹夹住待送的一叠，没有往落款处伸笔。蓝封书被她合好，放回自己的椅旁，离告示留出半张桌。"
    return

label claude04_scene2:
    $ chapter = "Claude 第四章 / 02 · 已经花掉的十八元"
    scene bg echo morning with dissolve
    show sprite claude as claude at sprite_breathe(0.65) with dissolve
    "十点十五分，印铺主事来到东廊。他把原稿与印好的纸并排，看见Claude添的只有时刻和地点，先将笔放下。"
    "那两行是主事为了招人自己加的。他以为她既然替原稿看过时间，也会愿意接住来参加的人；十八元已经用在纸墨上，退纸不能变回零钱。"
    "Claude将第一行指给他看，再把自己的小本子打开。今天没有任何一格写着逐篇审定。"
    l_cl "活动还办。带一页来，当面读。长稿要另外约，我没有说过当天改完。"
    "主事问能否只在最下面添一行以现场为准。她把卷起的下边展开，上面的全改好三个字依旧比小字大一倍。"
    l_cl "这三个字先撤。不能让人站到桌前才知道不算。"
    "主事摸了摸印纸的收条，问你们能否先撑过今天。午后换稿也要时间，还会多花一笔。你看了一眼她夹住的那八张。"
    menu:
        "陪她说清损失，先撤旧承诺再补告示。":
            $ claude4_response = "stand"
            l_you "那十八元已经花掉。先问四处看见告示的人，不拿新来的稿补这笔钱。"
            l_cl "你愿意跟我去？我说范围，你帮我记还有谁看过。"
            "你把空便纸拿到手边，只列地点。她向主事确认廊口、暖窗书店、茶摊、桥头四处，没往你的纸上替来客写姓名。"
            l_you "新纸钱怎么出，也当面谈。"
            l_cl "我愿意出一半新印费。原稿是我交的，交完没来取样张。"
            "她从自己的零钱袋里取钱，先放在空盘中。主事没有伸手拿，重新算起重印和覆贴各要多少。"
            l_cl "钱放在这里。先把旧四张收回来。"
            "你移开桌旁挡路的空凳，跟送纸的人核对该往哪儿走。Claude把那个大字全圈住，没替它找一句听着舒服的借口。"
        "劝她让旧稿撑过今天，别让印费白花。":
            $ claude4_response = "press"
            l_you "今天先别撤吧。十八元都花了，你多接几份，也许就撑过去了。"
            "Claude握着笔，笔尖在落款前停住。她抬头看你，原来准备推给你的地点纸被她留回自己一侧。"
            l_cl "多接几份，哪几份？你知道要多久？"
            l_you "至少先别把人赶走。名字先留着，回头慢慢解释。"
            "她将笔横放到两张纸之间，没有在自己的名字旁补签。主事等了一下，没等到她改口。"
            l_cl "我不接这个承诺。你可以不跟我去，别替它说成我答应过。"
            "她把地点纸转向主事，亲自问清那四张的位置。你伸手想接，她只将最外面那张没有姓名的路线单推过来。"
            l_cl "想帮忙，就把这四处记准。我今天不会一边撤字，一边替那句话接稿。"
            "你照着记，没有得到她之前那枚好借的铅笔。她把自己的笔夹回本子，用手指点着错印的落款，等主事答复取回时刻。"
            "桌上那张小说没有被她递过来。主事让人出门收旧告示，她看着卷纸，没有再问你想听哪一页。"
    "十一点前，原四张告示陆续取回。桥头那张被贴得很牢，边缘撕掉一小块，错误的大字仍完整落在桌上。"
    "一位看米铺的镇民也到了。他信了全改好，请人替自己看摊，付出四元代班钱，带来的却是十二页赊账记录。"
    "Claude先递凳子，听他把来路说完，再将稿子的页数数清。她没有翻到末页便答应下午拿走，也没让这十二页挤进鞋铺或装箱单的约时。"
    l_cl "今天不能改完十二页。你这趟是看了错告示来的，代班那四元也已经花了。"
    "印铺主事从自己的钱袋取出四元补给来人，另写旧告示撤回的说明。镇民数好钱，收回稿子，选择先回去看摊，没有被劝留下参加活动。"
    $ claude4_lost_wage_repaid = True
    "Claude在原稿上改清服务范围，主事将两行承诺整段划掉，重新交她看过。她只在新的活动范围旁留名，没有签回那张旧稿。"
    $ claude4_claim_withdrawn = True
    return

label claude04_scene3:
    $ chapter = "Claude 第四章 / 03 · 面要先吃"
    scene bg echo morning with dissolve
    show sprite claude as claude at sprite_breathe(0.65) with dissolve
    "十一点四十五，主事去取新样纸。Claude站起来，才发现自己的椅子被那卷告示顶在桌下，拉两次都没出来。"
    l_you "它又没收到预约。"
    l_cl "这回先退纸。椅子留下。"
    "她把卷纸移到空凳，你扶稳椅背，终于将椅子完整拉出。她坐下时，肩头松了一点，却马上又去够本子。"
    l_you "想起第十二日了？"
    l_cl "装箱四页。十点到十点半还在。我在看午饭。"
    "本子上已写好一碗汤面，少葱。你去摊边取了两份，她将一碗推回你面前，没拿今日的麻烦替你改口味。"
    "你们把碗放在小台，告示另留桌上。Claude拆开筷子的纸套，准备拿它当书签，抽到一半先看见自己手指上的汤。"
    l_cl "先吃面。书不借这张。"
    "她擦净手，把新纸套折起来放在碗旁，没有塞进小说。第一口面绕得太长，筷子抬高一点，她自己又用汤匙托住下面。"
    l_you "你也带着勺上船。"
    l_cl "这把能盛汤。书里那把先别借来。"
    "她低头吃掉托稳的那一段，嘴角沾了一滴汤。你将干净纸巾推过去，没有拿着纸去碰她的脸。她接过擦净，才放下汤匙。"
    l_you "刚才看到自己的名字，高兴过一下吗？"
    "Claude看着桌上卷起的那一张。她没立刻摇头，先将筷子里的面放回汤里，认真想了片刻。"
    l_cl "有。写得挺好看。比我在包书纸上写的齐。"
    l_you "后面那两行呢？"
    l_cl "想让它们走远一点。名字可以跟真正的活动放一起。"
    "她翻开小说，只看封里自己写的名字，没有从面碗上端着书读。窄书签还停在第二章，没被新的宣传话盖住。"
    l_cl "我也想有人来听。今天读一页，笑不笑都可以。不是带十二页来等我救。"
    l_cl "刚才还想过，只把我的名字缩小一点。"
    l_you "两句承诺还留着？"
    l_cl "所以没这么说。看着很像我只嫌名字占地方。"
    "她低头重新卷一口面，筷子在碗沿轻碰一下，面还是滑回去。她没叫你帮她夹，挪近汤匙，一边托着一边自己吃掉。"
    l_you "这份不用排版。"
    l_cl "请让我吃到它的最后一行。"
    "她把书合上，留回椅旁。这一页共读的素材用活动准备的短文，私人侦探小说没有交给主事印，也没有供旁人评她猜得对不对。"
    if claude4_response == "stand":
        l_you "四处旧告示都回来，午后我跟你去挂新的。"
        l_cl "先吃完。你碗里那段面也挂了挺久。"
        "你低头将那段面收回来。她看着你小心绕面，忍不住笑了一下，自己也把汤匙往近处挪。"
    else:
        l_you "刚才我只想别白花钱。没算你还要花多少时间。"
        "她听完，手仍握着自己的筷子，没马上把本子转给你。汤里剩的面被她慢慢拨开，才接下一句。"
        l_cl "我听见了。午后要改哪里，我会再说一遍，你照真正的那张做。"
        "你点头，将取回的旧纸留在另一张凳上。她用空手敲一下原稿，请你把错误的大字朝下，留出午后拿茶盘的位置。"
    "两碗面都吃完，汤匙留在碗内。她把油纸和筷子套单独收好，擦干小台，才重新打开用于工作的小本子。"
    $ claude4_meal_taken = True
    return

label claude04_scene4:
    $ chapter = "Claude 第四章 / 04 · 纸要换，人也要知道"
    scene bg echo morning with dissolve
    show sprite claude as claude at sprite_breathe(0.65) with dissolve
    "十二点十分，新稿的样张送到。下午一点半到两点半，东廊共读，一页以内；长稿另约，不承诺当日校完。Claude把三行读给主事听。"
    "原十二张都在这里，四张取回的纸与八张没发出的分开。主事给出两种办法：重印十二张十八元，或印十二条足够遮住旧承诺的更正条，六元。"
    "她拿起其中一条样纸，比在大字上。名字和两句错误承诺都被遮住，新范围印得比旧小注醒目，时刻与地点没有藏在背面。"
    l_cl "旧的不能只添一粒字。两种都要把这整块撤掉。"
    l_you "你出的一半，会选哪种？"
    l_cl "想跟你商量。哪种能做好，就做哪种。十八元旧印费已经算在主事那里。"
    menu:
        "重印十二张，拿新稿逐处换回去。":
            $ claude4_repair = "reprint"
            $ claude4_new_print_cost = 18
            $ claude4_own_print_paid = 9
            l_you "重新印吧。旧纸不再出去，我拿四张新的跟你换位置。"
            l_cl "好。旧纸留印铺，不要拿背面空着当新稿送。"
            "她从空盘里数出九元，主事也放下九元。新纸印齐后，她逐张核对句子，你在下面点出午后时刻，没有替她补任何保证。"
            "旧十二张的错误段落被剪去，没再夹进待送那一叠。新的十二张分成四张张贴、八张送往原本要发的书摊。"
            if claude4_response == "press":
                l_cl "你刚才让我留的那句话，已经不在新纸上。再念一遍现在的。"
                l_you "共读一页。长稿另约。不保证当天改完。"
                "她听到最后，才把四张新纸交给你。她的笔仍留在自己本子里，没有为了你终于念对便把原话忘掉。"
            else:
                "她将最上面一张递给你，你读完，她用拇指按住卷起的边，与你一起等它展平。"
                l_cl "这回写着我愿意做的事。你可以拿着走了。"
        "覆贴十二条，把更正后的范围当面读清。":
            $ claude4_repair = "overlay"
            $ claude4_new_print_cost = 6
            $ claude4_own_print_paid = 3
            l_you "用更正条。但这整块要遮住，不能留给人自己猜是哪几个字作废。"
            l_cl "好。十二条全贴，我数，你按平边角。"
            "她数出三元，主事也付三元。你们先在桌上将旧字整段覆住，试着从侧面读；纸色够厚，底下的大字没再透出来。"
            $ hide_speaker_portrait = True
            call show_main_cg('claude_poster_hold')
            "她按住纸的上沿，你从中间向外抹平。"
            call show_main_cg('claude_poster_stop')
            "第一张的右角被你贴歪一点，她叫停，让你揭起未干的那角重新对齐，没有替你一口气全做完。"
            l_you "少花的钱，得拿手补。"
            l_cl "你的手可以补边。不能补出另一句全改好。"
            $ hide_speaker_portrait = False
            scene bg echo morning
            show sprite claude as claude at sprite_breathe(0.65)
            if claude4_response == "press":
                "她让你亲口读更正后的范围，读到长稿另约才松开纸边。手从你这一侧收回，没有留给你替她签名的位置。"
                l_cl "按这句说。早晨那句不算。"
            else:
                "更正条压到最后一张，她把掌心翻给你看，一小点浆糊黏在指腹。你递来干净湿布，她擦过再去碰本子。"
                l_cl "第十二日的纸还没来。先别把它们粘进今天。"
    "付清后，她将空盘里剩余的零钱收回袋里。主事另开新印费的条，她对清自己承担的那半，才把收条夹进工作本。"
    "十二点五十分，你们带四张改好的告示出门。主事让送纸的人带走其余八张，并叮嘱按新范围说明，不接整日改稿的要求。"
    "廊口与暖窗书店先挂好，茶摊的人问早晨看到的当天全改是不是取消。Claude自己站到柜旁，回答那两句原本就未经她同意，今天撤掉。"
    "她指清一点半开场，只能当面读一页，是否另约由来人自己选。有人收起长稿回家，也有人只摘出一页放进袋子，茶摊没有替她拉住要走的人。"
    "桥头最后一张摆正时，一位赶路的镇民指着更正后的纸，说怕自己这一趟白来。她将具体时刻念清，没许诺补回对方所有耽搁。"
    l_cl "若只想当天校完长稿，今天这场做不到。你可以现在回去，不用坐到散场才问。"
    "回到东廊前，她检查四处的位置都已经换成真实范围，没有把取回的旧纸留下另一张在柜底。"
    $ claude4_sites_changed = 4
    "一点半，活动按新稿开始。几位愿意留下的人各带一页，读到缺地点名就停下找原作者确认；没有冒出替他们全部写完的桌子。"
    "两点半收场，长稿由来人带回。Claude将预约方式单独放在收件位，没有把第二天十点已约的装箱单划掉。她把最后一把空椅挪回阴影，终于坐下来。"
    return

label claude04_scene5:
    $ chapter = "Claude 第四章 / 05 · 名字写在哪一边"
    scene bg echo morning with dissolve
    show sprite claude as claude at sprite_breathe(0.65) with dissolve
    "两点四十分，告示已经挂好，共读的短文收回工作夹。Claude在小台上放了两只茶杯，给自己那只先倒水，壶嘴这回朝着她。"
    "她把重印或覆贴的费用记到自己的小本子，钱袋扣好。印铺那十八元旧成本和四元代班补付另在主事的纸上，没有混作新印费。"
    if claude4_repair == "reprint":
        l_you "你那九元，要不要用侦探来讨回？"
        l_cl "他拿汤勺量鞋。账不交给他。"
        "她把新告示的副样放回工作夹，原十二张已经留在印铺，桌上没有一卷同样的大承诺。"
    else:
        "她翻过手指，浆糊已经擦净，指腹留下的一点浅白被她搓掉。你将湿布挂到廊口，不留在书封上。"
        l_you "三元之外，还搭上了两只手。"
        l_cl "手还在。别又替它们开一张回条。"
    "蓝封的《第七位嫌疑人》被她取出来，第二章题目还在窄签前面。她顺着汤勺量鞋的句子往后看，没有把新告示夹到私人书里。"
    "门房发现量出来的鞋大了一寸，原来勺柄上系着绳结。船上的人仍没肯把礼帽还回去，新的嫌疑只多了一个结。"
    if claude4_has_ch03:
        l_you "现在能把偷勺子的撤掉吗？"
        l_cl "他还没还。下一页再问。"
    else:
        l_you "你先猜哪一位？"
        l_cl "借勺子的。他说借，到现在没还。先留他。"
    if claude4_response == "stand":
        "她将书转向你，手指停在绳结那里。你坐到旁边，等她挪开自己的指尖，才把那句接下去。"
        $ claude4_private_page_shared = True
        l_you "至少这次量错，能知道差哪一寸。"
        l_cl "你想替他校吗？我想看看他敢不敢把鞋穿走。"
        "你们一起往下看两段。她笑到那个人试鞋，书脊在膝上轻轻抬起，却没往工作夹那头挪。"
        l_you "你的名字，在这本上没印得那么齐。"
        l_cl "我写的。它没替我答应任何一份稿。"
        "她将包书纸上自己写的字摸平，抬眼看你，没忙着把那点不齐重写。桌外的风翻过新告示，你们没有因此合上书。"
    else:
        "她把书留在自己膝头，没有像早晨那样转给你。你坐到另一把椅子，把自己的茶杯放稳，等她读到一段结束。"
        l_you "刚才更正后的话，我都照着说了。"
        l_cl "我听见。纸改了。你让我多接几份那句，还得留着算。"
        "你没有替它添上为你好的几个字。她端茶喝一口，目光回到第二章，手仍自己托着书脊。"
        l_you "我也想听后面。但我先问，不替你把页翻过来。"
        l_cl "今天先让我自己看这一段。茶可以一起喝。"
        "你点头，把壶留在两人都够得到的地方。她看完一段才说那双鞋真穿走了，没将整页递出，也没有把你帮着换完纸当成已经说清。"
    "桥外有小车经过，轮声盖过一句。Claude停在那儿，等车走远，再把没听清的几个字自己慢慢念出来。她没有把书合到来人能看不见的地方。"
    l_you "也可以看更安静的书。"
    l_cl "这本不是车推过来的。我自己买的。"
    "她将蓝封朝自己翻过来，礼帽正好压在指尖下。那根翘出来的线头又蹭过手，她托住书脊，没像早晨那卷大纸一样退回桌上。"
    "三点刚过，Claude把窄签向后移了一小段，仍停在第二章。小说没有翻到末页，凶手是谁也没有被她写在工作本上。"
    l_you "第十二日的箱子，明早会来？"
    l_cl "十点。四页。现在不用提前搬空这张桌。"
    "她将本子收回干柜，私书留在自己布袋。茶喝完，她先收好自己的杯子，再把另一只推到你方便拿的位置。"
    l_cl "你看，杯子不用写我审定。"
    l_you "它今天确实没说过话。"
    "Claude笑了一下，把壶盖盖稳。她将椅子拉回原位，没让工作夹顶进去，自己的小书仍在她伸手就能拿到的地方。"
    # 按需CG候选：scene4覆贴中她按上沿，叫停歪角后抬眼看玩家。
    # 同事件可做按纸低头与松手抬眼两动作；当前无PNG、不调用、不解锁。
    return
