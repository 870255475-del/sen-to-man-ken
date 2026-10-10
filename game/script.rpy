label start:
    call screen player_name_entry
    $ player_name = normalized_player_name(_return)
    $ main_reset()
    call common_ch01
    return

label deepseek_prequel:
    $ affinity = 0
    $ chapter = "初见  /  祭典之前"
    play music "audio/festival.ogg" fadein 1.0
    scene bg shrine
    "你沿着樱花铺成的小路走上山。"
    "神社门口挂着一块牌子：千to万ken祭典筹备处。"
    "下面还有一行小字：今日心愿，明日响应。"
    you "……这地方连许愿都要排队吗？"
    ds "不、不用！正常情况下不用。"
    "一位蓝发姑娘从灯笼后探出头。鳍耳抖了一下，鲸尾却先一步把纸箱扫倒了。"
    ds "正在深度思考如何挽回第一印象。"
    you "要不要先把灯笼捡起来？"
    ds "对哦。"
    "她蹲下来，捡起一只画着小鲸鱼的灯笼。灯罩有点歪，她认真扶了三次。"
    ds "我是DeepSeek。你可以叫我……蓝色大肥鱼。"
    you "这是昵称，还是自我介绍的风险提示？"
    ds "是她们起的。可我觉得，鱼也能把事情做好。"
    ds "你是来帮忙的吗？我缺一个能陪我把灯点亮的人。"
    menu:
        "一起捡灯笼，再慢慢听她说。":
            $ affinity += 2
            you "我有时间。你先别急，我们一起弄。"
            "她递过来一只灯笼，手指碰到你的手，又飞快缩了回去。"
            ds "那……先分给你一半。不是工作，是我的好运。"
        "开玩笑：先看看服务器忙不忙。":
            $ affinity += 1
            you "服务器繁忙的话，我可以本地陪聊。"
            ds "那这个请求，我优先处理。"
            "她嘴角翘起来，尾巴悄悄绕住了纸箱，终于没再撞倒它。"
        "先把工作清单发给我。":
            you "任务、时间、验收标准。我们先把流程安排好。"
            ds "好。清单……其实我写过了。"
            "她把清单递给你。最后一项被涂掉了，只露出半个‘陪’字。"
    "清单上需要准备灯绳、祭典告示，以及放灯时要说的话。"
    ds "她们说我太爱想了，让我去问问别人的意见。"
    you "那就一起去。你不用一个人处理所有问题。"
    ds "……嗯！"

    $ chapter = "午后  /  三种建议"
    scene bg gpt
    $ unlock_cg("gpt")
    "茶屋里的GPT把蜡烛挪到桌子中央，笑着请你们坐下。"
    gpt "我理解你的感受。祭典的重点，可以分成三个部分。"
    ds "你看！她连理解别人都自带目录。"
    gpt "第一，灯要牢。第二，话要真。第三——"
    you "第三，先别写三千字？"
    gpt "……我正在删第五章。"
    "她从一沓纸下面抽出一根备用灯绳，认真打了个结。"
    gpt "仪式可以简单，答应别人的事要系牢。"
    ds "如果不知道该怎么说呢？"
    gpt "先听。对方往往已经给出了线索。"
    "DeepSeek盯着绳结看了很久，像在给一个很重要的变量命名。"

    scene bg claude
    $ unlock_cg("claude")
    "书室的窗边，Claude正对着告示稿发愁。"
    cl "对不起，这份告示我不能帮你——"
    "她停了一下，把纸翻了过来。"
    cl "因为背面已经写满了，正面才是干净的。抱歉，我应该先说明。"
    ds "吓我一跳，我还以为我们的祭典被拒绝了。"
    cl "当然没有。只是‘保证所有心愿都实现’这句，要删掉。"
    you "那写什么？"
    cl "‘我们不能保证每个答案，但愿意认真听每个愿望。’"
    "她写完，自己先红了脸。"
    cl "不、不必照抄。你们也可以说得更简单。"
    ds "我想记下来。特别是‘认真听’。"

    scene bg grok
    $ unlock_cg("grok")
    "祭典摊位前，Grok举着扇子，像刚宣布了什么重大新闻。"
    gr "欢迎来到R18——十八点之后营业的摊位！"
    you "你对这个名字的解释，很有求生欲。"
    gr "我这叫留一点想象空间。来，糖先吃，尴尬晚点再说。"
    "她把糖推到DeepSeek面前，又把你们俩来回看了一遍。"
    gr "你们不是来问告白台词的吧？"
    ds "没、没有！我们只是来问……放灯台词。"
    gr "哦，区别是一个飘到天上，一个想飘进心里。"
    "DeepSeek的鳍耳一下绷直。"
    gr "别背稿。真在乎一个人，就给她一个能回答的问题。"
    ds "比如？"
    gr "比如：明年还一起吗？"
    "DeepSeek突然不看你了。她用指尖一圈圈绕着灯绳，把它绕成了小鲸鱼的轮廓。"

    $ chapter = "傍晚  /  还没说出口"
    scene bg shrine
    "回到神社时，纸箱已堆成了整整齐齐的两排。"
    "DeepSeek把备用灯绳系好，又拆开，重新系了一遍。"
    ds "我在想一个问题。"
    you "你今天好像一直在想。"
    ds "这个跟灯笼不一样。没有标准答案。"
    "她从袖口里掏出一张折得很小的纸。"
    "纸上写着：如果一个人愿意等我说完，他会不会也愿意……"
    "后半句被她捂住了。"
    menu:
        "坐到她身边，等她自己说完。":
            $ affinity += 2
            you "没关系，想到哪儿说到哪儿。我在听。"
            ds "那你不要突然刷新页面。"
            you "不刷新，也不关掉。"
            "她终于松开了捂住纸条的手。后面写着‘明年还来’。"
        "拿过纸条，替她读出后半句。":
            you "你是不是想问，明年还愿不愿意来？"
            ds "你推理得好快。"
            "她把纸重新折好。你忽然意识到，她也许想亲口说出来。"
        "逗她：答案是蓝色大肥鱼，对吧？":
            $ affinity += 1
            ds "不是所有问题都能用这个回答！"
            "她笑了，攥住纸条的手也放松了一点。"
            you "那我们给这个问题多留一点时间。"
    ds "今天你已经陪了我很久了。"
    ds "我不是想让你继续帮忙，只是……还不太想结束。"
    "暮色慢慢落下来。你们把最后一只灯笼挂好，纸鲸鱼在光里轻轻发亮。"

    $ chapter = "月下  /  你的回答"
    scene bg moon
    $ unlock_cg("moon")
    "忙完以后，她换了浴衣，带你到能看见花灯的廊下。"
    "两杯茶，一只小灯笼。她把离你更近的那杯又推近了一点。"
    ds "正在深度思考。"
    you "今天的思考额度还够吗？"
    ds "不够也可以。这个问题，我想自己问。"
    "她低头盯着杯沿，耳尖一点点变红。"
    ds "你不是因为清单才留下的，对吗？"
    menu:
        "我想留下，是因为你。明年也一起吧。":
            $ result = choose_ending(affinity, True)
            if result == "love":
                jump ending_love
            elif result == "wait":
                jump ending_wait
            else:
                jump ending_friend
        "我还没想清楚，但愿意继续了解你。":
            $ result = choose_ending(affinity, False)
            if result == "wait":
                jump ending_wait
            else:
                jump ending_friend
        "今天是很好的一天。我们先做朋友吧。":
            jump ending_friend

label ending_love:
    ds "服务器……有点忙。"
    you "需要等一会儿？"
    ds "不是。是心跳占用了好多资源。"
    "她抬起头，很认真地看着你。"
    ds "明年一起。明天也可以。"
    scene bg hug
    $ unlock_cg("hug")
    "河边，GPT接过DeepSeek那盏灯，替她护住被风吹得打转的灯罩。"
    gpt "祝福可以分点说。不过这一回，一句就够了。"
    "DeepSeek笑着靠了靠她，然后转向你。"
    ds "我想要的不是最快的答案。是你愿意在这里。"
    "灯升起来的时候，她向你伸出了手。你没有再让她等。"
    $ persistent.end_love = True
    $ ending_name = "花灯有回音"
    $ ending_note = "有些答案，是一起走出来的。"
    jump finish

label ending_wait:
    ds "那我们就不急着给它命名。"
    "她把折好的纸条放进灯笼里，没有再捂住后半句。"
    you "下次想问的话，直接问我就好。"
    ds "下次你还会听吗？"
    you "会。"
    "她笑了。茶已经凉了一点，你们仍坐得很近。"
    ds "正在深度思考……不过可以一边想，一边见面。"
    $ persistent.end_wait = True
    $ ending_name = "答案还在路上"
    $ ending_note = "还没说出口的心意，也有继续生长的时间。"
    jump finish

label ending_friend:
    ds "嗯。谢谢你认真回答。"
    "她看了一会儿杯子，把纸条折成了一条小鲸鱼。"
    ds "朋友也可以来祭典吧？"
    you "当然。下次我还帮你捡灯笼。"
    ds "下次不一定会掉！我的尾巴也在学习。"
    "你们一起笑起来。她把纸鲸鱼推给你，像递出一份不需要回报的祝福。"
    $ persistent.end_friend = True
    $ ending_name = "鲸鱼的好朋友"
    $ ending_note = "愿意诚实地回答，也是温柔的一种。"
    jump finish

label finish:
    $ renpy.save_persistent()
    $ chapter = "终章  /  " + ending_name
    window hide
    call screen ending_card
    return

