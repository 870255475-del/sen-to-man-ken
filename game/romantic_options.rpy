# 三十岁成年角色的非露骨可选日常。玩家沿用可自定义姓名的 l_you。
# warm / quiet 只记录此处互动方式，不改变既有关系或结局。
default ds_romance_style = {}

label ds_optional_outerwear:
    $ chapter = "DeepSeek 第七章 / 可选 · 外带又打结了"
    scene bg echo morning with dissolve
    $ deepseek_expression = "shy"
    show sprite deepseek shy as deepseek at sprite_breathe(0.72) with dissolve
    "试完浴衣，DeepSeek把衣袋抱回房里，出来时仍穿完整的蓝白女仆裙，白围裙外披着深蓝羽织。"
    l_ds "廊下有点凉。我就披一小会儿。"
    "她将饭盒放稳，想脱下羽织，却发现外带绕成两个结。刚才系得太顺手，现在反而找不着先解哪头。"
    l_you "你是不是把它当成了饭盒提绳？"
    l_ds "饭盒也值得系牢。它们又没写不能用同一种结。"
    "她拉了一下长的那头，结变得更紧，立刻收手，把带头摊在掌心给你看。"
    l_ds "这个只绑外衣。里面已经穿好了。"
    l_you "看到了。需要我帮忙吗？"
    l_ds "可以帮我解外带。也可以在旁边，提醒我别越拉越紧。"
    menu:
        "帮她解外带":
            $ ds_romance_style["outerwear"] = "warm"
            l_you "我先碰这两个带头，可以吗？"
            l_ds "可以。别把它的成绩越解越好。"
            $ hide_speaker_portrait = True
            call show_main_cg('ds_outerwear_worn')
            "她先将羽织下摆抚平，把外带往前递一点，给你看清被压住的小环。"
            l_ds "就是这里。刚才拉错了，不给它第二次机会。"
            "你托住外带的一侧，慢慢松开小环。她接过两截带头，各拿在一只手里，确认这次能轻松分开。"
            call show_main_cg('ds_outerwear')
            l_ds "好了。你看，两头都听话。"
            "她自己将羽织挪到手臂上，转身时又回头看你。蓝白女仆裙和白围裙仍完整留在内层。"
            call show_main_cg('ds_outerwear_turn')
            "你给衣袋让出位置。她将羽织折整齐，才把胳膊上那一点重量放进去。"
            l_ds "谢了。下次我先学一种好拆的。"
            l_you "你今晚还能拿饭盒练。"
            l_ds "今晚的饭不参加练习。它有别的安排。"
        "让她自己整理":
            $ ds_romance_style["outerwear"] = "quiet"
            l_you "先别拉长的。松中间那个小环。"
            "她照着试，第一下没动，第二下终于把环挑开。她立即举起解开的带头，给你看两头都还完整。"
            l_ds "好了。没有剪掉。"
            l_you "你原本想到剪刀了？"
            l_ds "只想了一秒。你来得很及时。"
            "她自己脱下羽织，慢慢折好，把袖子朝里面收。你帮她腾开衣袋的位置，她将外衣放进去。"
            l_ds "不用颁奖。晚饭给我留点菜就行。"
    $ hide_speaker_portrait = False
    scene bg echo morning with dissolve
    $ deepseek_expression = "happy"
    show sprite deepseek happy as deepseek at sprite_breathe(0.72) with dissolve
    "她把外带收在羽织里，才重新提起饭盒。你见她又要打结，忍不住看一眼，她马上抬起空着的手。"
    l_ds "这次只是提着走。没有现场返工。"
    "走到廊口，她回头等你，给自己刚才的手忙脚乱补了最后一句。"
    l_ds "你可以记住好看的那套。这个结少记一点。"
    return

label ds_optional_hug:
    if ds_reply != "love":
        return
    $ chapter = "DeepSeek 第八章 / 恋人可选 · 这一步轮到我"
    scene bg echo with dissolve
    $ deepseek_expression = "happy"
    $ hide_speaker_portrait = True
    "第六周泳池回来，DeepSeek已换上完整短袖蓝裙，领边是白色圆荷叶边。她把毛巾袋放到椅边，忽然站到离你两步远的位置。"
    l_you "还有东西没还？"
    l_ds "还完了。现在不检查东西。"
    "她看一眼脚下，确认衣摆与尾巴都不会绊住，朝你张开两只手，又在迈步前停下。"
    l_ds "我想主动过来抱你一下。你愿意吗？"
    l_you "愿意。也可以坐下来，让你先把想说的说完。"
    "她望着你笑，刚摆好的架势有点端不住，索性将手先放回身侧。"
    l_ds "好。今天不抢跑，等你选。"
    "她把毛巾袋又推远一些，认真给自己清出那两步。你看着她忙完，她才重新抬头。"
    l_ds "这回不会半路停下来，先问你毛巾放哪儿。"
    menu:
        "张开手接住她":
            $ ds_romance_style["hug"] = "warm"
            "你站稳，张开手。她又确认了一眼，快快走过最后一步，带着笑朝你靠过来。"
            $ hide_speaker_portrait = True
            call show_main_cg('ds_hug_pov')
            "你接住她的轻抱，手只落在完整衣料外。她没有撞得很猛，倒是尾巴高兴地绕了一小圈。"
            l_ds "接住了。没有把你当浮板。"
            l_you "幸好。我今天已经看过浮板的路程。"
            "她笑着将手臂收紧一点，随后抬眼看你。"
            l_ds "能再抱一小会儿吗？我还不想退回那两步。"
            l_you "可以。我也想抱着你。"
        "坐近一点说话":
            $ ds_romance_style["hug"] = "quiet"
            "你拉出相邻的椅子。她先把尾巴放到空处，挨着你坐下，将刚才张开的手搁在自己膝上。"
            l_ds "其实只想告诉你，今天很开心。"
            l_you "我看见了。你走回来一直在笑。"
            l_ds "还想让你再看一会儿，不用隔两步。"
            "你转向她，认真看完她的笑。她反而先眨了眨眼，把原本想好的下半句忘了。"
            l_ds "等一下。我坐过来之前，明明挺会说的。"
            l_you "那就先一起坐着。"
    "她拿起毛巾袋回到房间，放好后换回完整女仆装。再出来时，她顺手将你身旁的椅子往内侧挪齐。"
    $ hide_speaker_portrait = False
    scene bg echo with dissolve
    $ deepseek_expression = "shy"
    show sprite deepseek shy as deepseek at sprite_breathe(0.72) with dissolve
    "刚才腾出的那一点位置，仍留在两个人之间。"
    l_ds "晚点喝水，还坐这里吧。"
    l_you "好。杯子先放稳。"
    "她点头走了两步，又回头对你笑。这一回脚下没要检查的东西，她只是还想看你。"
    return

label ds_optional_bath:
    if ds_reply != "love":
        return
    $ chapter = "DeepSeek 第八章 / 恋人可选 · 两杯温水"
    scene bg echo with dissolve
    $ deepseek_expression = "happy"
    show sprite deepseek happy as deepseek at sprite_breathe(0.72) with dissolve
    "又过了一个星期，第一次留宿的周末。你放好自己的过夜包，DeepSeek将两条干毛巾摆到廊边。"
    l_ds "你的这条。洗过，晒干了。"
    hide deepseek with dissolve
    $ hide_speaker_portrait = True
    "你们分别去洗澡。轮到她时，她将浴室门关好，你在廊下看书；轮到你时，你也关好门，她去准备温水，没有开门探看。"
    "两个人都洗好后，她换上浅蓝高领长袖家居裙。整齐的裙摆一直盖到脚踝，她理好袖口，端来温茶。"
    "她将两只白色鲸鱼图案茶杯放到桌上，先试杯壁的温度，给你挑了没那么烫的一只。"
    "刚才那本书已经合上。米饭小点心摆在旁边，窗外的月亮悬在镇灯上方。"
    l_ds "今晚不赌谁比较能忍烫。"
    l_you "那个比赛的奖品也只是再喝一杯。"
    "她笑着站到你身旁，背对你半转过来，却没有直接往后靠。"
    l_ds "如果你愿意，可以从后面轻轻抱我一下。"
    l_you "可以。或者坐下来，我们把水喝完。"
    menu:
        "她邀请时从后轻抱":
            $ ds_romance_style["bath"] = "warm"
            l_you "我过来了。这样抱，可以吗？"
            l_ds "可以。松一点，我还得够到水杯。"
            "你从身后短短地轻抱她一下，手落在完整家居裙外。你们松开后，她坐到桌边，端起两只鲸鱼茶杯，把其中一只递向你。"
            call show_main_cg('ds_evening_tea')
            l_ds "你那杯我试过了。这个温度，可以喝。"
            l_you "先吹一下，别急着喝。"
            "她拿好自己的那杯，慢慢吹过茶面。你们并排坐着，两只杯子轻碰一下，热气从杯沿升起来。"
            l_ds "这样也近。还能腾出手喝水。"
        "并排喝温水":
            $ ds_romance_style["bath"] = "quiet"
            "她给你换一杯温水，自己的杯子仍是淡茶。两只杯子都先留在桌上。"
            "你将两只椅子摆到桌边。她坐下，给尾巴留好地方，抱住杯子轻轻吹了一口。"
            l_ds "刚才准备了半杯。又怕聊完就喝空了。"
            l_you "原来你给聊天也备了续杯。"
            l_ds "嗯。今天想听你说点不用记在册里的事。"
            "你讲起下午走错的小巷。她听到那家面店，立即认出路口，说自己也绕过同一个弯。"
            l_ds "下次我带你走。顺便尝汤，不算白绕。"
    "两只杯子慢慢见底，你们将它们放好，约了明早的饭。各自休息前，她在门口回头，认真补上晚安。"
    $ hide_speaker_portrait = False
    scene bg echo morning with dissolve
    $ deepseek_expression = "happy"
    show sprite deepseek happy as deepseek at sprite_breathe(0.72) with dissolve
    "第二天，她换回干净的女仆装。两只昨夜的茶杯晾在一起，旁边多了新煮的白饭。"
    l_ds "早上这一碗，不用先吹半天。"
    return
