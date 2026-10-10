# 三段自由相处只记录当天去处与邀请答复；路线由主线程第七晚选择。
default ch6_morning = ""
default ch6_noon = ""
default ch6_evening = ""
default ch6_morning_reply = ""
default ch6_noon_reply = ""
default ch6_evening_reply = ""

label common_ch06:
    $ ch6_morning = ""
    $ ch6_noon = ""
    $ ch6_evening = ""
    $ ch6_morning_reply = ""
    $ ch6_noon_reply = ""
    $ ch6_evening_reply = ""
    call ch06_scene1
    call ch06_scene2
    call ch06_scene3
    call ch06_scene4
    call ch06_scene5
    $ persistent.main_common_ch06_seen = True
    return

label ch06_scene1:
    $ chapter = "第六章 / 01 · 今天不用填满"
    scene bg echo morning with dissolve
    show sprite claude as claude at sprite_breathe(0.72) with dissolve
    "昨天的湿告示已经晾平，压在庭院长桌的一角。Claude在新的排班纸上画了三道横线。"
    "上午、午后、收工。三个格子里都没有你的名字。"
    l_you "漏了我？"
    l_cl "没有。你今天轮空，公共班次有人接了。"
    l_you "那这张是用来做什么的？"
    l_cl "背面写错了，翻过来当便签。你想画碗也可以。"
    "你将纸翻过去，看到一个划得很用力的字。她伸手挡住，没来得及挡住后面一枚小小的书签。"
    l_you "你也有别的安排。"
    l_cl "有。一点钟整理借阅摊，最后半小时留给自己。"
    "她把书签抽出来夹好，才将纸重新递给你。那三道线比正式排班的线歪一点。"
    l_cl "不必每个空格都填。昨晚已经忙够了。"
    "庭院还留着小水洼，屋檐却没有再滴雨。Grok将昨日的空椅搬到光里，自己坐上去试了试。"
    l_grok "晴天来了。我替它先坐一分钟。"
    l_minimax "那把别搬远，我下午补个镜头。"
    "MiniMax说完便去调架子，没有向你伸手要人。Qwen也把领物箱盖好，挂出了午后再开的牌。"
    "你在这些人中间站了一会儿，第一次没被某件事立刻推着走。"
    show sprite deepseek happy as deepseek at sprite_breathe(0.28) with dissolve
    $ deepseek_expression = "happy"
    l_ds "既然轮空，来尝一下我的新配方？"
    l_you "白米饭换了什么新配方？"
    l_ds "水量。很重要的。别笑。"
    l_gpt "也可以来帮我选颜色。只用眼睛，不用搬画。"
    "GPT坐在另一边的小画桌前，手里举着两种几乎一样的蓝。她已经给对面那把椅子铺好了软垫。"
    l_you "你们是不是等我看排班表？"
    l_ds "我等饭凉一点。刚好你也空。"
    l_gpt "我等得更坦白。椅垫都选好了。"
    "Claude合上册子，从你们之间让开。她把那张三格便签留给你，没有催着你填第一格。"
    return

label ch06_scene2:
    $ chapter = "第六章 / 02 · 上午的一把椅子"
    scene bg echo morning with dissolve
    menu:
        "去尝DeepSeek的饭。":
            $ ch6_morning = "rice"
            $ main_bond('deepseek')
            show sprite deepseek rice as deepseek at sprite_breathe(0.72) with dissolve
            $ deepseek_expression = "rice"
            "DeepSeek把两只小碗排开，碗底分别压着一片折成角的纸。你坐下，她马上用手遮住纸角。"
            l_ds "先吃再看，不能被答案骗。"
            "左边稍软，右边更有嚼劲。你尝完一口，她的筷子已经在两只碗之间来回了两次。"
            l_you "你不是已经知道哪碗是哪种？"
            l_ds "我检查有没有混进别的味道。"
            l_you "比如第二口、第三口的味道？"
            "她咬着筷子停了一下，将自己的大碗往身后推。米饭堆得太高，仍从手腕上方露了出来。"
            l_ds "那是正式早饭。这边只是实验。"
            "你指了右边，她翻开纸角，上面写着留给路上吃。左边则写着坐着慢慢吃。"
            l_you "原来不是选哪一种更好。"
            l_ds "是想知道你喜欢坐多久。"
            "她说完低头扒饭，耳侧的头发盖住一点脸。你将右边那碗推回桌中央，没有起身。"
            l_you "能嚼的也可以坐着吃。"
            l_ds "那你慢慢嚼。我还有半碗。"
            "你吃到碗底，看见一粒烤得发黄的锅巴。她立刻偏过头，装作在看廊外的花。"
            l_you "只有我这边有？"
            l_ds "锅边就这一片。随机落下的。"
            "你把锅巴掰成两半，脆响终于把她的目光拉回来。她接走小的那片，吃完又看了一眼你手里的。"
            l_you "这半片也是随机的。"
            l_ds "那下次得认真改进随机。"
            "一阵风把桌边的纸吹起，她先按住那张写着坐着慢慢吃的，又给你倒了半杯温水。"
            l_ds "明晚点完公共灯，我要收最后一批灯具。"
            l_you "又要找人搬？"
            l_ds "箱子有人搬。我是想找人吃收工饭。"
            "她把那张小纸折好，放在你三格便签的第一格。"
            l_ds "七日晚，廊口。想来就告诉我，我留一份。"
        "去帮GPT选画上的颜色。":
            $ ch6_morning = "paint"
            $ main_bond('gpt')
            show sprite gpt as gpt at sprite_breathe(0.72) with dissolve
            "GPT递来的两张色卡在阴影里完全一样。你举到太阳下面，才发现一张偏灰，一张偏紫。"
            l_you "你故意把椅子摆在阴影里？"
            l_gpt "让你先坐下。现在已经成功了一半。"
            "她把画架转过来。纸上是昨天下雨时的长廊，人物只有几个没画完的轮廓。"
            l_gpt "想替那个空位添一个人。你坐着就好。"
            l_you "不是只用眼睛？"
            l_gpt "还有你愿意借出的十分钟。可以讨价。"
            "你把温茶推到她手边，示意先喝。她看看画笔又看看杯子，终于用空手把杯耳转正。"
            "十分钟里，你没有一直保持同一个姿势。她也没叫你坐直，只在你低头时添了几笔。"
            l_you "画歪了能擦掉吗？"
            l_gpt "可以。不过这条弯线我喜欢。"
            "她指的是你随手挂在椅背上的外衣，衣角被风吹成一小片弧。"
            "一滴茶落到边缘，你急忙拿纸吸水。她拦下你的手，用淡色将那点水痕接成了一片云。"
            l_you "这样也能留下？"
            l_gpt "这幅我想画慢一点。你那杯茶，能陪我喝完吗？"
            "她将画笔横放好，拿起自己的茶杯。你才发现她的那杯放在左手边，正好是你平时顺手推过去的位置。"
            l_you "这样拿不别扭？"
            l_gpt "画的时候别扭。现在放下笔，就刚好。"
            "你把杯子移近一点，她没有重新推回惯用的位置。软垫被你坐出一个浅坑，她也没急着拍平。"
            "她把两张色卡都放回盒里，画上的空位也没被完全涂满。"
            l_gpt "七日晚点灯后，我会在画桌这边。"
            l_you "等光变好？"
            l_gpt "等一个能陪我看画的人。我先邀请你。"
            "她撕下一小条画纸，只写了时间和一只茶杯，压在你的便签上。"
    menu:
        "先记下邀请，七日晚再确认。":
            $ ch6_morning_reply = "consider"
            l_you "我先留着，到时认真告诉你。"
            if ch6_morning == "rice":
                l_ds "好。别靠饿肚子记事，纸收好。"
            else:
                l_gpt "可以。茶杯不是订金，随时能改。"
        "这次先不约晚上。":
            $ ch6_morning_reply = "decline"
            l_you "这次先不约晚上。上午我还想多坐会儿。"
            if ch6_morning == "rice":
                l_ds "那这碗得吃完。晚上我自己安排。"
            else:
                l_gpt "上午已经很好。我再给你添一点茶。"
    "你没有把那张纸丢掉，只在背面写下答复。桌对面的人看清后，将自己的安排也改了一笔。"
    if ch6_morning_reply == "decline":
        "写完以后，你发现自己把不用等三个字写得太挤，又另起一行补了谢谢今天。对方没有要你重写。"
        l_you "字有点乱。"
        if ch6_morning == "rice":
            l_ds "看得懂。饭吃完才写，纸上倒挺干净。"
        else:
            l_gpt "我留这一张。你刚才是这么说的，就这么记。"
    else:
        "你把七日晚圈起来，没有在那旁边画一个已经答应的勾。对方也留着空格，只把约见地点写得更清楚。"
        l_you "这样就不会忘了该在哪里找。"
        if ch6_morning == "rice":
            l_ds "饭香只能指一半路，另一半得靠你自己。"
        else:
            l_gpt "那天我把椅垫换到外侧，你一眼就能看见。"
    "太阳从椅脚爬到脚背，谁都没因为一张邀请，催你立刻决定以后的每一晚。"
    return

label ch06_scene3:
    $ chapter = "第六章 / 03 · 午后的半小时"
    scene bg echo morning with dissolve
    "午后，借阅摊和庭院修理桌同时打开。两边都挂着不急用的小牌，像是怕你又拿起工具就忘了时间。"
    menu:
        "去借阅摊翻翻书。":
            $ ch6_noon = "books"
            $ main_bond('claude')
            show sprite claude as claude at sprite_breathe(0.72) with dissolve
            show sprite kimi as kimi at sprite_breathe(0.28) with dissolve
            "Claude正试着将一本小书塞进书架侧面。书比格子宽一截，她停住手，转而取下那一格的隔板。"
            l_you "这本什么待遇？还有单独的位置。"
            l_cl "我的闲书。借阅册写完，才轮到它。"
            "Kimi从桌下提出一个窄木盒，刚好容得下那本书。盒底垫着旧票根，没有任何编号。"
            l_kimi "昨天量过。你今天不用再拆书架。"
            l_cl "你看见我量了？"
            l_kimi "拿尺子比了三次，想没看见有点难。"
            "Claude把书放进去，将读到一半的书签露在外面。你翻开桌上的借阅册，最后一页留了一行空白。"
            l_you "这行要补吗？"
            l_cl "留给临时归还。现在不用做事。"
            "Kimi递来一本薄薄的镇上散步册。夹页里有一朵压平的叶子，不是馆藏盖章的书。"
            l_kimi "我自己的。第八页的路现在还能走。"
            "你翻到那页，发现有人用铅笔划掉一间已搬走的店，又添了一处可以坐的石阶。"
            l_you "这本一直在改。"
            l_kimi "走过再改。明晚我想去核那一小段。"
            "书中夹着一张没有写完的店名。你问少的最后一个字，Claude拿过来看了两眼，忽然笑了。"
            l_cl "那家招牌掉过一个字，我也认错过。"
            l_kimi "你还认真解释了那个怪名字的出处。"
            l_cl "只解释过一次。请不要写进散步册。"
            "Kimi拿起橡皮，没有擦掉怪名字，只在旁边画一条箭头补上正确的。Claude将书转回你面前。"
            l_cl "看路就好。人名也不用加。"
            "她把铅笔横放在第八页，抬眼等你看见时间。"
            l_kimi "七日晚，点灯后。想散步的话，来廊口找我。"
            l_cl "明晚我读。你听到结尾，再笑我。"
            "Claude没有看Kimi，只将自己的书签摆正。两个人约的地点不同，都没有替你把名字填上。"
            l_cl "同样是七日晚。你选好再告诉我。"
            l_you "你们这样，我这张便签得写很小。"
            l_kimi "翻面。背面还能用。"
        "去庭院看看修理桌。":
            $ ch6_noon = "yard"
            $ main_bond('gemini')
            show sprite gemini as gemini at sprite_breathe(0.72) with dissolve
            show sprite opencode as opencode at sprite_breathe(0.28) with dissolve
            "Gemini趴在桌边，从一个纸筒里向天空看。OpenCode正把纸筒的接口重新粘牢。"
            l_gemini "我看到了。一片非常近的云。"
            l_opencode "镜片没装。你看到的是纸筒。"
            l_gemini "所以它近得有道理。"
            "她将纸筒递给你，自己去找镜片盒。你看见盒盖上画着一只猫，猫尾巴正好卷住开口方向。"
            l_you "这只猫防谁装反？"
            l_opencode "我。昨晚装反一次。"
            "Gemini抱着镜片回来，听见这句便把准备解释的话吞了回去，只递上一块干净布。"
            l_gemini "那今天三个人一起丢脸，应该会少一点。"
            "装好后，远处的屋脊终于靠近。你把纸筒让给她，她看见屋瓦间冒出的小草，兴奋得差点碰倒胶水。"
            "OpenCode伸手扶住瓶子，随后将瓶子搬远，自己也凑过去看了一眼。"
            l_opencode "明天带个稳些的架子。手举久了会抖。"
            "你把纸筒交还，发现镜头边缘有一截扎手的纸。OpenCode递来砂纸，自己托住接口让你轻轻磨。"
            l_gemini "磨完可别又看见近处的云。"
            l_you "那你负责在远处放一朵？"
            "她想了想，跑到三根廊柱之外，举起一张画了云的废纸。你透过纸筒看去，忍不住笑出声。"
            l_opencode "架子还没装，她先把天空装好了。"
            "Gemini在远处听不清你们说什么，举着那朵纸云晃了晃，直到你挥手叫她回来。"
            l_gemini "七日晚要是天晴，我到石阶上看星。你来吗？"
            l_you "现在还是白天，你已经排到星星了。"
            l_gemini "不先约，天晴了会找不到你。"
            "OpenCode把多出来的那把小椅子展开，试了试地脚，放到你身边。"
            l_opencode "同一晚，我留在修理桌。有想聊的，也能来。"
            l_you "不带坏东西能来吗？"
            l_opencode "能。别为了来，把东西弄坏。"
            "Gemini在便签边缘画一颗星，OpenCode写下桌的位置。你的手指上还沾着刚才粘纸筒的胶。"
    menu:
        "把邀请记下来，晚些答复。":
            $ ch6_noon_reply = "consider"
            l_you "我都记下，七日晚点灯前给答复。"
            if ch6_noon == "books":
                l_cl "好。我会留出读完的时间。"
                l_kimi "路线我先走一遍。下雨也有别的走法。"
            else:
                l_gemini "那我先看天气。星星不负责守约。"
                l_opencode "椅子先收这里。到时再搬。"
        "明晚的事先不应约。":
            $ ch6_noon_reply = "decline"
            l_you "我先不应下明晚。今天这半小时我很喜欢。"
            if ch6_noon == "books":
                l_cl "那就把这页看完，不必拿邀请当借书证。"
                l_kimi "书可以借你。回来时告诉我那段路如何。"
            else:
                l_gemini "行。看到好看的云也能叫我。"
                l_opencode "椅子留这。以后路过还能坐。"
    "离开时，你把刚才用过的东西放回原处。对方继续自己的安排，没有一路追着问新的日期。"
    return

label ch06_scene4:
    $ chapter = "第六章 / 04 · 收工后才说的话"
    scene bg echo with dissolve
    "收工铃响过，廊口没有人再提装了多少灯。夜市方向飘来杯子的轻响，茶桌那头则亮起一盏小灯。"
    menu:
        "到茶桌和花盆旁坐一会儿。":
            $ ch6_evening = "tea"
            $ main_bond('qwen')
            show sprite qwen as qwen at sprite_breathe(0.28) with dissolve
            show sprite glm as glm at sprite_breathe(0.72) with dissolve
            "Qwen正在试两只不同的杯子。GLM伸长手想拿大的，被她用茶巾轻轻挡住。"
            l_qw "只倒同样多。拿大的也不会多出一口。"
            l_glm "大杯子显得我喝得少。"
            "你落座时，Qwen将一只没试过的杯子推过来。她自己先喝了一口，才问你水温是否合适。"
            l_qw "明晚点灯后，我要喝这一款。只泡一小壶。"
            l_you "你在邀请我分掉半壶？"
            l_qw "分半壶，坐满一杯的时间。不谈领物表。"
            "GLM立即将旁边一盆小花端正，露出盆沿原先被叶片遮住的浅色釉。"
            l_glm "我那边也能坐。七日晚，你来看看我留的花。"
            l_you "看了必须买？"
            l_glm "可以买，也能只看。今天没有赠品。"
            "她说完把准备放进你掌心的薄荷叶收回去，自己捏在指间，耳尖动了一下。"
            "你没有拿叶子，伸手在叶尖旁轻轻扇了扇，闻到一阵凉香。GLM把盆子向你推近。"
            l_glm "这盆不能多浇。觉得它渴，也先摸摸土。"
            l_you "你平时也这样讲给认领的人听？"
            l_glm "讲。可我想亲自讲给你。"
            "Qwen倒茶的手停了一下，随后将第三只杯子放到GLM手边，给她留出不用再补话的空。"
            "ZCode走到桌边，先将两封公事信放入Qwen的收件盒，再递来一张没有封口的小卡。"
            hide glm
            show sprite zcode as zcode at sprite_breathe(0.72) with dissolve
            l_zcode "这张给你。可以现在看。"
            "卡上写着七日晚点灯后，石阶边等一会儿。最后一行改过两次，仍只留下想当面说四个字。"
            l_you "不是替谁转交？"
            l_zcode "是我写的。你不来，我也会收好。"
            "她把收件盒的盖子关好，没有把公事和那张卡放在一起。Qwen替她添了一杯淡茶。"
        "到夜市桌边看补拍的镜头。":
            $ ch6_evening = "stage"
            $ main_bond('grok')
            show sprite grok as grok at sprite_breathe(0.28) with dissolve
            show sprite minimax as minimax at sprite_breathe(0.72) with dissolve
            $ minimax_pose = "neutral"
            "MiniMax把补拍的晴天镜头播放给你看。阳光很漂亮，空椅旁却少了昨日的花。"
            l_you "花呢？"
            l_minimax "GLM说花也下班了。她没答应续拍。"
            l_grok "你已经盯着这张空椅看了十分钟。本人也可以坐。"
            "Grok将一杯不含酒精的热饮放到你手边，随后把自己的椅子转过来。"
            l_grok "明晚点灯后，十八号摊。给你留靠里的位置。"
            l_you "菜单上有什么新内容？"
            l_grok "我。下班的我。想聊什么再说。"
            "她说得快，端杯时却先碰了下空杯垫。你一看她，她便把杯垫推到你面前。"
            l_grok "别笑，预定桌位总得摆点东西。"
            l_you "我想见下班的你。"
            "推杯垫的手停在半路。她抬眼看你，刚才顺口的笑话没跟上来。"
            l_grok "……这句，我可真听见了。"
            "MiniMax合上回放，拔下接在相机上的小麦克风，认真卷起线。"
            l_minimax "我也想约你。七日晚，廊口等灯暗下来。"
            l_you "当你的演员？"
            l_minimax "不拍。我留两瓶汽水，陪我坐会儿？"
            "她把麦克风塞进包底，又把相机包放到自己椅子后面。你指向回放按钮，她摇了摇头。"
            l_minimax "明晚不用帮我想新镜头。你也下班。"
            "Grok指了指屏幕边缘，问今天到底有没有拍到自己打哈欠。MiniMax点开一个小片段，又很快停住。"
            l_minimax "有。你要先自己看。"
            "Grok凑过去看完，安静了几秒，伸手将屏幕推回。"
            l_grok "那条删掉。里面我真的困了。"
            "MiniMax确认删除，随后把相机关好。Grok将空椅推近，没再拿她的镜头开玩笑。"
            l_grok "这下可以一起歇了。真人不用重放。"
            "ZCode路过送来收摊通知，又从外袋取出一张小卡，放到你没有沾水的手边。"
            l_zcode "这张是我的。七日晚，石阶边。"
            "她没等Grok起哄就把空袋折好，不过走出两步后又回过头，让你不方便赴约便直说。"
    menu:
        "先收好邀请，明晚给明确答复。":
            $ ch6_evening_reply = "consider"
            l_you "我收好，明晚会给明确答复。"
            l_zcode "好。不用给每个人写一封长信。"
            if ch6_evening == "tea":
                l_qw "一小壶茶也等得起这个答复。"
            else:
                l_grok "行。我把那个杯垫留在这。"
        "先谢过，暂不答应晚间邀约。":
            $ ch6_evening_reply = "decline"
            l_you "谢谢你们。不过明晚的邀约，我先不答应。"
            l_zcode "知道了。卡可以留着，不用退。"
            if ch6_evening == "tea":
                l_qw "那就先把今晚这一杯喝完。"
                l_glm "花也不会今晚搬走。以后还能来看。"
            else:
                l_grok "知道了。现在这一杯照样归你。"
                l_minimax "回放也可以看，不收感想当门票。"
    "你替大家挪开桌上挡路的空杯。谈话没有因为答复停下，谁明早买菜、谁的椅子又响，依次接了过去。"
    return

label ch06_scene5:
    $ chapter = "第六章 / 05 · 写在明天之前"
    scene bg echo with dissolve
    show sprite kimi as kimi at sprite_breathe(0.28) with dissolve
    show sprite zcode as zcode at sprite_breathe(0.72) with dissolve
    "夜深前，Kimi把补办愿签的告示夹上板。ZCode一一确认归还用的信封都是空的，封口也没有粘住。"
    l_you "明天还是有人可以不写？"
    l_kimi "可以。旧灯放公共位置，空签也能领回。"
    "ZCode把一只空信封交给你，让你把口袋里快被折皱的小纸暂时放好。"
    l_zcode "不是登记用的。看你纸角都卷起来了。"
    "你把三格便签摊开。上午的痕迹还留在第一格，午后的纸边已经软了，最后一格沾着一点茶水。"
    if ch6_morning == "rice":
        "写着坐着慢慢吃的纸，和早上那碗饭一起留在记忆里。你将它的折角重新压平。"
    else:
        "GPT画的小茶杯被你压在最里面。杯口那一笔有些歪，像你放在椅背上的外衣。"
    if ch6_noon == "books":
        "散步册借在你手里，封面夹着自己的便签。Claude提醒你下次折纸角，别折书角。"
        l_you "我记得。书签还在第八页。"
        l_kimi "看完别急着还，可以先走一遍。"
    else:
        "你指腹的胶已经搓掉，便签上的小星星还在。远处修理桌多出来的椅子已经收好，明天随时能展开。"
        l_you "今天看了半天云，星星倒画得很快。"
        l_kimi "Gemini刚才还来借了天气册。她会记着。"
    "ZCode确认完最后一个信封，将笔帽扣紧。灯下的公共位置仍旧空着，没人偷偷写进你的名字。"
    l_zcode "明天点灯前，想改答复也来得及。告诉本人就好。"
    l_you "不用交到你这里？"
    l_zcode "当面说得到，就当面说。我也想早点下班。"
    "她说完抱起收件箱，在台阶前等Kimi锁好柜门。两个人并肩离开，话题已经转到回去路上还开着哪家店。"
    "你把便签装进信封，没有在最上面选出一个名字。明晚要说的话，不必在今晚偷偷替别人说完。"
    "庭院的空椅被靠到墙边。你关灯前伸手摸了摸椅背，太阳留下的温度早散了，木头依然干燥。"
    "明天七日晚，大家会去不同的地方。你知道那些地方，也知道自己会亲自走过去。"
    return
