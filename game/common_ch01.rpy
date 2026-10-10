# 共通第一章的第二至第五场；第一场承接 common_intro。
default ch1_seat = ""
default ch1_task = ""
default ch1_share = False
default persistent.common_ch01_seen = False

label common_ch01:
    $ ch1_seat = ""
    $ ch1_task = ""
    $ ch1_share = False
    call common_intro
    return

label common_ch01_scene2:
    $ chapter = "第一章 / 02 · 还没坐稳的椅子"
    call v20_scene_background('c01_bg10')
    $ v17_music_scene_cue('common_ch01_scene2')
    show sprite deepseek rice as deepseek at sprite_breathe(0.72)
    show sprite qwen as qwen at sprite_breathe(0.28) with dissolve
    "饭碗标签上的最后一笔还没干，Qwen就把收据从碗底下抽了出来。"
    l_qw "签名很漂亮。现在该签这张了。"
    l_ds "不能只夸前一张吗？"
    l_qw "可以。前一张不用付钱，这张要。"
    l_you "我是不是该避开？"
    l_ds "不用！新来的可以旁听，顺便——"
    l_qw "不能代付。"
    l_ds "我还没说完。"
    l_qw "你已经把人家的行李挪到收银凳旁边了。"
    call v20_show_background('c01_bg09')
    "你低头一看，行李确实不在原来的位置。她尾巴尖上还挂着提带。"
    l_you "这尾巴也负责安排座位？"
    l_ds "负责……保持现场整洁。"
    l_qw "那先把它从人家包上摘下来。"
    "DeepSeek松开提带，没松开碗。你伸手接行李，她的尾巴却又推来一把小椅子。"
    l_ds "这个位置好。离饭近。"
    l_you "离收银也近。"
    l_ds "看你比较在意哪件事。"
    "桌沿一共摆着三把椅子。最里面那把已经被她拉开，椅背还搭着一块干净的擦手布。"
    menu:
        "坐到DeepSeek留的那把椅子上。":
            $ ch1_seat = "beside"
            $ rice_trust += 1
            call v20_show_background('c01_bg11')
            l_you "就这儿吧。不是为了代付。"
            l_ds "知道。你想续饭的话我可以递碗。"
            l_qw "人家连第一碗都没盛。"
            l_ds "先占个位置嘛。"
            "她朝里挪了一点。两把椅子仍挨着，尾巴却老实地收到了自己脚边。"
        "把椅子挪到对面，帮大家腾出通道。":
            $ ch1_seat = "across"
            call v20_show_background('c01_bg12')
            l_you "坐对面。你们进出也方便。"
            l_ds "那我递碗会比较远。"
            l_you "我自己拿。"
            l_ds "……也行。"
            "她把擦手布扔过来。没扔准，布落在你的行李上，她立即伸手拿回去重新递了一遍。"
            l_ds "这个也给你。对面桌角有一根毛刺。"
    l_qw "今天不用你结账。祭典帮手有晚饭。"
    l_you "我刚才差点以为入职要先交米钱。"
    l_qw "米钱找她收。你帮忙修灯，这顿归你。"
    l_ds "知道啦。我的这张我会签。"
    "她把饭碗放在膝上，借着灯光认真写了名字。签完之后，又在金额旁边添了一个小小的米粒。"
    $ deepseek_expression = 'annoyed'
    show sprite deepseek annoyed as deepseek at sprite_breathe(0.72) with dissolve
    l_qw "这个印章不抵钱。"
    l_ds "我也没说它抵。"
    l_you "是纪念今天吃了这么多？"
    l_ds "是提醒我明天还要来。"
    l_qw "明天先帮我把米搬进库房，再来吃。"
    l_ds "两个人搬会快一点。"
    "她看向你。这次尾巴没有再碰你的包。"
    $ deepseek_expression = 'shy'
    show sprite deepseek shy as deepseek at sprite_breathe(0.72) with dissolve
    l_you "你是在招人，还是在约饭？"
    l_ds "先问你几点起床。万一很晚呢？"
    l_qw "她想问八点。她自己经常八点半才到。"
    l_ds "明天我会早点的。"
    "Qwen把收据叠好放进袖袋，端起茶壶。壶盖下又响了一声。"
    l_you "接头还在里面？"
    l_qw "还有螺钉。你们别把这壶当晚茶。"
    l_ds "我已经闻过了。没有茶。"
    l_qw "看得出来。壶盖上还黏着饭粒。"
    hide qwen with dissolve
    "她去清点工具。DeepSeek从椅子下摸出两双筷子，挑了比较新的那双递给你。"
    l_ds "八点怎么样？"
    l_you "你八点半才到，我要在库房门口等？"
    l_ds "我带早饭。"
    l_you "现在说这个倒很有把握。"
    l_ds "早饭不会迟到。"
    "你把筷子摆在空碗旁。她吃完自己碗里剩下的两口，把空碗挪到一旁，给你的碗腾出位置。"
    jump common_ch01_scene3

label common_ch01_scene3:
    $ chapter = "第一章 / 03 · 写在清单之外"
    $ v17_music_scene_cue('common_ch01_scene3')
    call v20_scene_background('c01_bg13')
    show sprite claude as claude at sprite_breathe(0.28) with dissolve
    show sprite gpt as gpt at sprite_breathe(0.72) with dissolve
    "饭端上来之前，Claude又带来一张清单。她没有把纸压在碗底，而是垫了一块平整的木板。"
    l_cl "先看一眼。今晚只剩最后两件。"
    l_you "这张不会也需要付钱吧？"
    l_cl "你可以不签。那我们就不知道明天去哪儿叫你吃饭。"
    l_gpt "我来喊也行。明早整条街都会认识你。"
    call v20_show_background('c01_label_desk')
    "GPT把两只杯子放下。其中一只杯耳上系着细绳，另外十只装在她带来的篮子里。"
    l_you "为什么系绳子？"
    l_gpt "DeepSeek把第四只认作第一只的时候，我就系上了。"
    l_gpt "没系绳的这只是你的。先喝点水？"
    l_you "你们对她的计数方式很熟。"
    l_gpt "她对我们的饭量也很熟。今天多煮了半锅。"
    l_cl "多煮的是Qwen。她负责把盖子掀开看。"
    l_gpt "那也需要专心。"
    "Claude翻过清单。背面空着，只有两行写在纸角：登记灯牌，取回长凳。"
    l_cl "愿签已经收在盒子里了。今晚只给灯背面的标签编号。"
    l_you "那长凳呢？"
    l_cl "借给坡下茶屋坐客的。约好今晚取回来，明早要擦洗。"
    l_gpt "标签我来写。你帮我按着纸就行。风有点大。"
    call v20_show_background('c01_bg15')
    "她从袖口抽出一卷纸。纸在桌上摊开，从这头铺到了饭碗底下。"
    l_you "一盏灯的标签有这么大？"
    l_gpt "这张是试写。真正的裁小一些。"
    l_cl "从午后试到现在，只小了一根手指。"
    l_gpt "如果明天看不清，还得再写。"
    l_cl "我们明天把灯挂低一点。"
    "GPT用笔杆轻轻推开饭碗。她画出第一笔，桌上就出现了一只快要碰到杯子的龙尾。"
    l_you "编号也带图？"
    l_gpt "新来的第一晚，总要有一点好看的。"
    l_cl "能贴上去就算好看。"
    "她们把最后两件事都留在桌面上，没有替你打钩。"
    menu:
        "帮GPT和Claude登记灯牌。":
            $ ch1_task = "tags"
            l_you "我帮你们按纸。顺便学一下编号。"
            l_gpt "手放这边。小心，墨还没干。"
            l_cl "先写一到三。标签贴背面，别挡住她画的眼睛。"
            "你用指尖按住纸角。GPT把龙尾绕过你的手指，收在纸边。"
            l_you "刚才这条尾巴还会碰到杯子。"
            l_gpt "现在有人按着，可以少画一圈。"
            l_cl "那今晚终于能用上这一张了。"
            call v20_show_background('c01_bg16')
            "她剪出三枚标签，把剩下的一小条白纸放在你的碗边。"
            l_cl "留着。明天还得写你自己的排班。"
        "先去取回坡下的长凳。":
            $ ch1_task = "bench"
            l_you "我去取长凳。坡下是哪一边？"
            l_cl "出门向左，第二个摊位。别一个人扛。"
            l_gpt "我陪你。标签可以等饭后。"
            "GPT把长卷收回篮子，又抽出一张小纸，三两笔写好地址。"
            l_you "原来真的能写这么小。"
            l_gpt "要放进口袋的，当然得小些。"
            l_cl "明天所有标签都要放进口袋。"
            l_gpt "……你等着这句呢。"
            call v20_scene_background('c01_gate')
            show sprite gpt as gpt at sprite_breathe(0.72) with dissolve
            "她替你拉开庭院的门。坡下的灯一排排亮着，茶屋门前那把长凳正坐着两位吃完饭的镇民。"
            call v20_scene_background('c01_teahouse')
            show sprite gpt as gpt at sprite_breathe(0.72) with dissolve
            "你们说明是筹备处来取凳子的。GPT护住桌边的茶杯，两位镇民起身，还把凳脚底下的垫木一起交给你。"
            call v20_show_background('c01_bg19')
            l_you "还要这些？"
            l_gpt "台阶不平。明天开市，会有人推着小车来。"
            call v20_scene_background('c01_lane')
            show sprite gpt as gpt at sprite_breathe(0.72) with dissolve
            "回去时，她提着一头，你提着另一头。经过最窄的门，她先停下来，让你换好手再往里走。"
            l_gpt "晚饭还热着。慢一点也赶得上。"
    call v20_scene_background('c01_bg21')
    show sprite claude as claude at sprite_breathe(0.28)
    show sprite gpt as gpt at sprite_breathe(0.72) with dissolve
    "Claude在清单上画了一个勾。你看她收纸时，纸背还贴着一张写满了字的小便签。"
    l_you "还有任务？"
    l_cl "明天的。今晚不派。"
    l_gpt "藏得这么快，我差点以为是情书。"
    l_cl "想读？上面第一条是请GPT裁小一点。"
    l_gpt "那还是明天再读吧。"
    "她们走开时，没系绳的那只杯子里多了半杯温水。杯沿还热着，你捧了一会儿，才喝下第一口。"
    jump common_ch01_scene4

label common_ch01_scene4:
    $ chapter = "第一章 / 04 · 再等半盏灯"
    call v20_scene_background('c01_bg22')
    $ deepseek_expression = 'determined'
    show sprite deepseek determined as deepseek at sprite_breathe(0.72)
    "你伸手去拿杯子，原本点亮的旧灯又闪了一下。鲸鱼眼睛一明一暗，像在使劲眨眼。"
    l_you "它也困了？"
    l_ds "不是。你先别搬。"
    "她放下刚拿起的空碗，关掉灯架的电源。院里暗了一小块，桌边几只杯子映着旁边的灯光。"
    l_you "接头又松了？"
    l_ds "盖子里压到线了。刚才搬的时候碰了一下。"
    call v20_show_background('c01_workbench')
    "她没有继续往里伸手，先把灯移到空桌上，又从工具袋里取出备用的小灯。"
    $ deepseek_expression = 'fix_lamp'
    show sprite deepseek fix_lamp as deepseek at sprite_breathe(0.72) with dissolve
    l_ds "这个照着。拿稳就行。"
    l_you "螺钉还在Qwen的茶壶里？"
    l_ds "在她那儿。我先去问她拿。"
    l_you "借米的时候也这样吗？"
    l_ds "……今晚这句不能再用了。"
    call v20_show_background('c01_bg24')
    "Qwen听见了，从门口递过工具袋。她没再说账，扶住桌沿，等DeepSeek把盖子取下来。"
    show sprite qwen as qwen at sprite_breathe(0.28) with dissolve
    l_qw "这里？"
    l_ds "对。让盖子空出来。"
    "她取出垫片，换到另一侧。动作并不快；每放下一个小零件，都要抬头确认你还照着原来的位置。"
    l_you "需要我举高一点吗？"
    l_ds "不用。这个高度刚好。"
    l_qw "她以前拿嘴咬着小灯。"
    l_ds "也刚好。就是不方便说话。"
    l_you "那难怪你一直没人帮忙。"
    l_ds "现在有了嘛。"
    call v20_show_background('c01_bg25')
    "她把盖子摆平，自己拿起小灯照了一遍，才重新接通。两只歪眼睛亮得一模一样。"
    l_ds "好。再等一会儿。"
    l_you "等胶干？"
    l_ds "这次是真等。让它亮一阵，看看会不会再闪。"
    l_qw "这次我作证。"
    "三个人在桌旁站了一会儿。DeepSeek的肚子先响了。"
    $ deepseek_expression = 'annoyed'
    show sprite deepseek annoyed as deepseek at sprite_breathe(0.72) with dissolve
    l_you "灯没闪。别的倒响了。"
    l_ds "我晚上工作比较久。"
    l_qw "你刚才还说第四碗半算宵夜。"
    l_ds "别这么分。白天会显得很短。"
    call v20_show_background('c01_bg26')
    "Qwen把饭锅放到另一张桌上，扣好锅盖。DeepSeek一直没看锅，眼睛仍留在旧灯上。"
    l_qw "饭在这儿，不会端走。够了就自己过来。"
    hide qwen with dissolve
    "她的尾巴尖碰了碰桌脚，慢慢停住。你举灯的胳膊已经有些酸，换了另一只手。"
    l_ds "累了？放下吧。它现在自己亮着呢。"
    l_you "我还以为你需要照着。"
    l_ds "刚才需要。现在忘了说。"
    "你们一起把备用小灯关掉。旧灯照亮了桌沿和她的手。她转正灯罩，两只歪眼睛也朝向了你。"
    l_you "为什么不画整齐？"
    l_ds "旧眼睛擦掉就没了。"
    l_you "是你以前画的？"
    l_ds "下午。画到一半，Qwen就喊我吃饭。"
    l_you "刚才还在喊。"
    $ deepseek_expression = 'shy'
    show sprite deepseek shy as deepseek at sprite_breathe(0.72) with dissolve
    l_ds "这次有你一起等，不急。"
    "话说出口，她才看了你一眼，很快又去看灯。两只眼睛始终没有闪。"
    jump common_ch01_scene5

label common_ch01_scene5:
    $ chapter = "第一章 / 05 · 碗里还有一口饭"
    call v20_scene_background('c01_dining')
    $ v17_music_scene_cue('common_ch01_scene5')
    $ deepseek_expression = 'sleepy'
    show sprite deepseek sleepy as deepseek at sprite_breathe(0.72)
    show sprite qwen as qwen at sprite_breathe(0.28) with dissolve
    "饭桌终于空出两个位置。Qwen把你的碗端来，满满一碗，另外放了一只浅盘。"
    l_qw "腌菜在盘里。别学她把饭堆过碗沿。"
    l_ds "碗沿只是建议。"
    l_you "那洗碗的人会怎么建议？"
    l_ds "会建议有人帮忙洗。"
    l_qw "很好。今晚你负责。"
    $ deepseek_expression = 'offer_rice'
    call opening_ds_proud_pose
    "DeepSeek先把你的碗捧过来，往你手边递。自己那只还搁在桌上。"
    call opening_ds_rice_offer_begin
    l_ds "先接住。新来的不能第一天就把饭打翻。"
    l_you "这回没有偷偷添高？"
    call opening_ds_rice_offer_clear
    l_ds "这碗是你的。我忍住了。"
    "你坐下。她也端来一只碗，里面只盛了半碗饭，筷子仍横在碗口。"
    l_you "这次只盛半碗？"
    l_ds "Qwen盛的。她说先尝菜，吃完再添。"
    l_you "你尝了吗？"
    l_ds "在等你。菜凉了还能一起吃。"
    $ deepseek_expression = 'happy'
    show sprite deepseek happy as deepseek at sprite_breathe(0.72) with dissolve
    "她把浅盘推到中间，筷子尖碰到一片腌萝卜，又缩了回来。"
    if ch1_seat == "beside":
        l_ds "这里还给你留着。没让别人坐。"
        l_you "是不是方便我帮你盛第六碗？"
        l_ds "今天停在五碗。"
        l_you "我是不是应该记在收据上？"
        l_ds "记在饭桌上。明天你就能拆穿我了。"
    else:
        "她看你坐到对面，伸长手，把盘子又推过去一些。盘底擦过桌角，停在那块擦手布上。"
        l_ds "这次没扔。"
        l_you "很稳。"
        l_ds "那明天也坐这个位置？"
        l_you "看你是不是又藏了收据。"
        l_ds "明天只有早饭。"
    "最后一片腌萝卜留在盘边。你夹起来时，她的目光跟着筷子动了一下。"
    menu:
        "把最后一片萝卜夹给她。":
            $ ch1_share = True
            l_you "这片给你。"
            l_ds "我没有在等这个。"
            l_you "你的筷子一直没动。"
            l_ds "在等你先动。现在可以动了。"
            "她咬了一小口，把剩下的配着饭吃完。碗端得很近，嘴角那点笑一直没藏好。"
        "自己吃掉，约好明天换一道菜。":
            $ ch1_share = False
            l_you "这片我吃了。明天我们换一种？"
            l_ds "换什么？"
            l_you "你来挑。我不知道这儿都有什么。"
            l_ds "那你明天别先在别处吃。"
            "她又夹了一筷子饭，顺手把浅盘收到一边。萝卜没到手，明天的座位倒是订好了。"
    call v20_show_background('c01_bg28')
    "GPT把篮子放在门边，提醒大家用过的杯子别带回房。Claude端着两只空杯走来，Qwen用手指敲了敲米库的门牌。"
    l_qw "八点，别走错。饭桌在这边，库房在那边。"
    l_ds "我分得清。"
    l_qw "明天还得分得清谁搬米。"
    l_you "我会来的。八点。"
    "DeepSeek抬头，又低头看看自己的碗。最后一口饭还在，她慢慢把它吃掉，才把筷子搁下。"
    l_ds "我也八点。"
    l_qw "记下了。"
    hide qwen
    hide gpt
    hide claude
    call v20_scene_background('c01_bg29')
    $ deepseek_expression = 'shy'
    show sprite deepseek shy as deepseek at sprite_breathe(0.72)
    "散席后你拿起行李。那盏歪眼睛的灯摆在长椅上，背面多了一小行字，字迹还没完全干。"
    l_you "不是说现在可以写名字？怎么只写了‘新帮手’？"
    l_ds "名字在另一面。我照着碗上的字写的。"
    l_you "那背面呢？"
    l_ds "我写的。怕你找不到。"
    if ch1_task == "tags":
        "你把Claude留下的小纸放进口袋。她看见了，也摸了摸自己口袋里的米库钥匙。"
        l_ds "明天写排班的时候，给我留一行。"
        l_you "写八点到，还是八点半？"
        l_ds "八点到。旁边可以画一只碗。"
    else:
        "你将刚才取回的长凳移到门边。她扶住另一头，轻轻放下，没再把搬东西的活推给你。"
        l_ds "明天路过坡下，我带你认别的摊位。"
        l_you "先搬米，再认？"
        l_ds "先搬米。答应Qwen了。"
    l_you "如果明早这盏灯又不亮呢？"
    l_ds "那你把它带过来。"
    l_you "又要让我站着照半天？"
    l_ds "先吃早饭。然后我们一起看。"
    "她从口袋里摸出那粒干硬的米。你还没问，她就摊开手给你看。"
    l_ds "这粒不能吃。上次就告诉过自己了。"
    l_you "可你上次还是放回口袋。"
    l_ds "……明天不用提醒了。"
    "她把米扔进收残饭的小桶，拎着空碗走回厨房。走到门口又回头，朝你挥了下手，指了一下长椅旁的灯。"
    $ deepseek_expression = 'shy_wave'
    show sprite deepseek shy_wave as deepseek at sprite_breathe(0.72) with dissolve
    l_ds "它也是你的。记得拿。"
    call v20_show_background('c01_departure')
    "行李不轻。你换了一只手，把灯提起来。鲸鱼眼睛朝着下山的路，背面那行小字对着你。"
    $ persistent.common_ch01_seen = True
    call screen common_ch01_finish
    if _return == "next":
        call common_ch02
    return

screen common_ch01_finish():
    modal True
    add Solid("#101b2cdd")
    frame:
        align (0.5, 0.5)
        xsize 690
        padding (38, 32)
        background SoftPanel("#FFF7F1", "#DEC2CF", 15)
        vbox:
            spacing 18
            text "第一章 · 碗里还有一口饭" size 30 color "#49384F"
            text "今晚的座位，明早的约定。" size 23 color "#49384F"
            text ("你坐在她身旁。" if ch1_seat == "beside" else "你在桌对面给大家留出了通道。") size 20
            text ("明天带上排班用的纸。" if ch1_task == "tags" else "明天沿着坡下的路认一认其他摊位。") size 20
            text "接下来：第二章「十一位，不是十一种答案」。共通篇七章后，可进入DeepSeek八章个人故事。" size 17 color "#796977" xmaximum 614
            hbox:
                spacing 16
                textbutton "继续第二章" id "common_ch01_next" action Return("next") xsize 270
                textbutton "回到标题" id "common_ch01_return" action Return("title") xsize 270
