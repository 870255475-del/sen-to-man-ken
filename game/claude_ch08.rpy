# 千to万ken / Claude 第八章候选 / 留下整页的空白。
# 第十五日。全员成年三十岁，玩家无立绘；仅本章状态与局部结尾。
# 未原生验收。外层 runner/正式结局/来源戳接入见同目录接力，不在本文伪造。

default persistent.main_claude_ch08_seen = False
default claude8_has_ch07 = False
default claude8_source_run_id = None
default claude8_previous_snack = ""
default claude8_reply = ""
default claude8_reply_inherited = False
default claude8_reply_confirmed = False
default claude8_club_part = ""
default claude8_tea_order = ""
default claude8_frame_returned = False
default claude8_club_opened = False
default claude8_club_finished = False
default claude8_turn_kept = False
default claude8_bookmark_written = False
default claude8_private_reading_kept = False
default claude8_close_asked = False
default claude8_close_agreed = False
default claude8_wait_revisable = False
default claude8_friend_turn_set = False
default claude8_novel_chapter = 2
default claude8_ending = ""
default claude8_complete = False

label claude_ch08:
    # 公开回看、旧 seen、跨角色或更换 UUID 均不能补出昨日关系。
    $ claude8_has_ch07 = getattr(persistent, "main_claude_ch07_seen", False) is True and getattr(renpy.store, "main_last_chapter", "") == "claude_ch07"
    $ claude8_has_ch07 = claude8_has_ch07 and all(getattr(renpy.store, "claude7_" + k, False) is True for k in ("invitation_written", "invitation_received", "snack_saved", "private_time_kept", "arrived", "invitation_spoken", "answer_heard", "snack_shared", "paper_kept", "day_closed")) and getattr(renpy.store, "claude7_novel_chapter", 0) == 2 and getattr(renpy.store, "claude7_snack_help", "") in ("tray", "plate")
    $ claude8_has_ch07 = claude8_has_ch07 and ((getattr(renpy.store, "claude7_answer", "") == "love" and getattr(renpy.store, "claude7_close_asked", None) is True and getattr(renpy.store, "claude7_close_agreed", None) is True and getattr(renpy.store, "claude7_wait_revisable", None) is False and getattr(renpy.store, "claude7_friend_plan", None) is False) or (getattr(renpy.store, "claude7_answer", "") == "wait" and getattr(renpy.store, "claude7_close_asked", None) is False and getattr(renpy.store, "claude7_close_agreed", None) is False and getattr(renpy.store, "claude7_wait_revisable", None) is True and getattr(renpy.store, "claude7_friend_plan", None) is False) or (getattr(renpy.store, "claude7_answer", "") == "friend" and getattr(renpy.store, "claude7_close_asked", None) is False and getattr(renpy.store, "claude7_close_agreed", None) is False and getattr(renpy.store, "claude7_wait_revisable", None) is False and getattr(renpy.store, "claude7_friend_plan", None) is True))
    $ claude8_has_ch07 = claude8_has_ch07 and getattr(renpy.store, "ending_route_run_role", "") == "claude" and getattr(renpy.store, "claude7_completed_run_id", None) is not None and getattr(renpy.store, "claude7_completed_run_id", None) == getattr(renpy.store, "claude7_answer_run_id", None) == getattr(renpy.store, "ending_route_run_id", "") and (not getattr(renpy.store, "ending_route_run_id", "") or 7 in getattr(renpy.store, "ending_route_run_chapters", ()))
    $ claude8_source_run_id = getattr(renpy.store, "claude7_completed_run_id", None) if claude8_has_ch07 else None
    $ claude8_previous_snack = getattr(renpy.store, "claude7_snack_help", "") if claude8_has_ch07 else ""
    $ claude8_reply = getattr(renpy.store, "claude7_answer", "") if claude8_has_ch07 else ""
    $ claude8_reply_inherited = claude8_has_ch07
    $ claude8_reply_confirmed = claude8_has_ch07
    $ claude8_club_part = ""
    $ claude8_tea_order = ""
    $ claude8_frame_returned = False
    $ claude8_club_opened = False
    $ claude8_club_finished = False
    $ claude8_turn_kept = False
    $ claude8_bookmark_written = False
    $ claude8_private_reading_kept = False
    $ claude8_close_asked = False
    $ claude8_close_agreed = False
    $ claude8_wait_revisable = False
    $ claude8_friend_turn_set = False
    $ claude8_novel_chapter = 2
    $ claude8_ending = ""
    $ claude8_complete = False
    call claude08_scene1
    call claude08_scene2
    call claude08_scene3
    call claude08_scene4
    call claude08_scene5
    $ claude8_ending = claude8_reply
    $ claude8_complete = True
    return claude8_complete

label claude08_scene1:
    $ chapter = "Claude 第八章 / 01 · 椅子先坐下"
    $ main_cg = None
    $ hide_speaker_portrait = False
    scene bg echo morning with dissolve
    show sprite claude as claude at sprite_breathe(0.65) with dissolve
    "第十五日九点二十五，东廊多摆了四只矮凳。Claude从最里面走出来，手里还抱着第五只。"
    l_you "你打算把自己摆在哪里？"
    l_cl "这只。"
    "她低头看看，凳面已经放了两叠薄纸。她把纸移到桌上，桌上的茶壶便没有地方落。"
    l_you "壶也报名了？"
    l_cl "它只供茶。让它占一张凳子，太抬举它。"
    "你把窗旁的窄木桌拉近一点。她放下壶，总算能把第五只凳子搬到有阳光的位置。"
    "蓝封小说收在她自己的布袋里，厚垫压着袋底。桌上的薄纸没有装订，封面只写了小读书会。"
    if claude8_has_ch07:
        l_cl "昨天的梨吃完了。今天不再带一锅东西。"
        l_you "我看见你柜里留着食盒。"
        l_cl "洗净了。下午装饼，不装那么多汁。"
        "她给你倒茶。你从口袋里取出那张句号偏胖的邀请，放在自己的杯边。"
        l_cl "今天没约四点十分。"
        l_you "我知道。只是没丢。"
        "她看了一眼自己的名字，将杯子往旁边移开，没有把茶水压在那张私人纸上。"
    else:
        l_cl "我想试一次有人来读，我也能坐着听的聚会。"
        l_you "你把自己的位置放在最里面了。"
        l_cl "怕站起来方便。现在才发现，进去也麻烦。"
        "她把那只凳子重新挪到门边，布袋挂在自己够得到的椅背上。私人小说没有混进两叠公用薄纸。"
    "九点半，阿澄抱着修好的门牌木框进来。边角重新固定了，原来的字仍在里面。"
    if claude8_has_ch07:
        l_you "按你昨天约的时刻来了。"
        l_cl "嗯。先把这件交给他，不占后面的朗读。"
    else:
        l_cl "我约他今天九点半带来再看一眼。你帮我扶一下桌边就好。"
    "她用指腹轻压四个角，将框交还。阿澄提起时，她又伸手，像是想追回一个尚未检查的地方。"
    "手停在半空，她自己收了回来。木框没有松，她只是忽然想起背面的绳结还没夸一句。"
    l_cl "能挂。别拿回去再拆。"
    "阿澄笑着答应，自己带走门牌。她将登记的小纸夹回公用盒，留下桌上干净的一角。"
    $ claude8_frame_returned = True
    "离十点还有一会儿。她坐上自己那只凳子，试了试厚垫，随后把茶壶的嘴转向外侧。"
    l_you "这回不会有人挤走你了。"
    l_cl "还会有人问水在哪里。"
    l_you "我坐壶旁边。"
    l_cl "你坐凳子上。壶不缺陪读。"
    "她指给你靠桌的空位，忽然又把自己那只杯子推近一点。两只杯子没有碰到，却都留在两人能拿到的地方。"
    l_cl "今天想让你也读一点。不是来替我端一上午茶。"
    "她拿起薄纸，只把前两页对齐。第三页歪着，她看了一眼，压住想继续整理的手。"
    return

label claude08_scene2:
    $ chapter = "Claude 第八章 / 02 · 雨伞没有第三条腿"
    scene bg echo morning with dissolve
    show sprite claude as claude at sprite_breathe(0.65)
    "十点，陶姐和另外两位成年镇民坐下来。阿澄送完木框，也回来占了门边的一只凳子。"
    "今天读的是镇民新写的短故事《会敲门的雨伞》。那把伞总在下雨前敲门，主人却一直以为门框歪了。"
    l_you "他先修了门框？"
    l_cl "修了两次。第二次把伞钉在外面。"
    l_you "你挑它，因为门牌刚修好？"
    l_cl "挑它的时候还没想到。现在不能替作者补这个用意。"
    "她将自己的蓝封小说压进布袋内侧。陶姐问那本好不好看，她先点头，随后想起封面上的大礼帽。"
    l_cl "好看。帽子有点大。今天不借它当教材。"
    "她拿着短故事的第一页坐下，才发现自己把小凳挪得离桌太远。杯子近，纸反而够不到。"
    "你给她递过去。她接住纸，顺手也想把你那一份拿来对齐，你轻轻按住自己的页角。"
    l_you "我这张还要用。"
    l_cl "看见它歪，就想顺一下。你按得对。"
    "她把手放回膝上，指尖在那里轻敲了一下。陶姐已经等着听雨伞，她却还在估摸第一段该由谁开始。"
    l_cl "我可以念开头。也想试试第一段先听别人念。"
    menu:
        "让她念开头，你接后一页。":
            $ claude8_club_part = "relay"
            l_you "你先开门，我接雨伞进来。"
            l_cl "先念。别替它添脚。"
            "她读主人第一次拆门的段落，声音起初很稳。读到主人把螺钉放进糖罐，她停了一瞬，看向自己的茶。"
            l_you "杯子里没有。你继续。"
            "她忍着笑把这一页念完，将纸转向你。你接住时，她只提醒页码，没替你先读下一句。"
            "你让那把雨伞咳嗽似的敲了一下门。陶姐笑出声，她也低下头，肩头轻轻动了两次。"
            l_cl "伞已经够倒霉了，别让它伤风。"
            l_you "它淋了一夜。"
            l_cl "是你刚才给它配的声音淋了一夜。"
            "她想接着纠正，下一行却已经由阿澄念出来。她把没说完的半句留住，专心听那把伞终于进屋。"
        "你先念，让她坐着听完开头。":
            $ claude8_club_part = "listen"
            l_you "第一段我来。轮到你，再把纸递给你。"
            l_cl "好。我先不握着第二页等。"
            "她将薄纸放回桌边，双手扶住自己的杯子。你念主人拆门，故意把藏螺钉的糖罐念得格外郑重。"
            "她刚喝一口，立即放下杯子。你停下来，她摆摆手，等嘴里的茶咽净才出声。"
            l_cl "你把糖罐念成了秘密墓穴。"
            l_you "里面埋着两次修门的希望。"
            l_cl "还有螺钉。下一行就在找它，别给它下葬。"
            "陶姐接着念第二段。Claude跟着看，却没有伸手抢走那张略歪的纸。"
            "到了第三段，纸才传到她手里。她把雨伞进屋那句念得很轻，随后用伞柄敲门的语气接下一句。"
            l_you "现在它没有伤风了。"
            l_cl "它刚进屋。你先让它晾干。"
    $ claude8_club_opened = True
    "故事走到一半，纸页传过四双手。她的水已喝掉半杯，厚垫一直留在自己身下，没有被拿去垫桌。"
    "阿澄念错一个字，自己改过来。她已经抬起的手变成拿杯子的动作，嘴角倒比刚才更明显。"
    l_you "你听见了。"
    l_cl "嗯。他也听见了。我不用替他抢第二次。"
    return

label claude08_scene3:
    $ chapter = "Claude 第八章 / 03 · 短一点的书签"
    scene bg echo morning with dissolve
    show sprite claude as claude at sprite_breathe(0.65)
    "十点四十，雨伞主人终于开门。屋里那只先前总失踪的狗，正叼着半截绳子等它。"
    "陶姐读完最后一句，翻了翻背面。没有另一段解释狗为什么喜欢雨伞，只有作者留的一整页空白。"
    "Claude先伸手摸笔，摸到以后又没拿起。她往后挪一点，坐稳在厚垫上。"
    l_you "你想写什么？"
    l_cl "为什么狗之前没有出声。"
    l_you "它咬着绳子。"
    l_cl "我看见了。所以现在想笑刚才那个问题。"
    "她真的笑了一下，没把这个小错藏在别人读错的字后面。陶姐拍着膝盖，说下次想听一篇主人更笨的。"
    "桌上原先备的六条窄纸还剩四条。Claude说可以当书签，阿澄便拿笔写雨伞应该早一点出声。"
    "她看着那句话，自己取另一条。第一行写了想把伞留下，后面又跟了几个字，越写越靠近纸边。"
    l_you "纸不打算再长。"
    l_cl "我知道。字还在往前走。"
    "她把笔停住，盯着末尾那三个字。过一会儿，她拿一条新的，写今天好笑。只有四个字。"
    l_you "没有解释是哪一段。"
    l_cl "我自己知道。以后忘了，也能再读。"
    "旧的长纸条收进废纸盒，新的放在她掌边。你拿另一条写伞没有第三条腿，她看过以后伸手盖住嘴。"
    l_cl "刚才不让你添脚，你还记着。"
    l_you "留着下次提醒我。"
    l_cl "留着。我下次可能先笑。"
    $ claude8_bookmark_written = True
    "十一点，人陆续离开。各人把用过的薄纸收回公用夹，镇民的短故事没有被装进她的蓝书。"
    if claude8_club_part == "relay":
        "她把你接读的那一页最后收起。页角被你压出一道小折，她用手掌压平，随后就将它夹好。"
        l_cl "你下次还想接在我后面吗？"
        l_you "可以。不过伞的声音换一个。"
        l_cl "那次轮到我听你淋雨。"
        "她收走自己的第一页，留一只杯子给你。你把其余杯子搬到洗盆边，她先坐着喝完那一口。"
    else:
        "她把开头那页交还给你去收，自己只拿第三段。你将薄纸夹好时，她还在看那句进屋。"
        l_cl "先听确实比先想怎么念慢一些。"
        l_you "下次也先听？"
        l_cl "换着来。今天听完，我又想念那只狗。"
        "你把杯子搬到洗盆边。她没来替你排队，先端着自己的杯子，将最后一点茶喝掉。"
    $ claude8_turn_kept = True
    "她洗好两只杯子，倒扣在干布上。厚垫没有跟着挂起，布袋和小说也仍是她自己的东西。"
    l_cl "下午我想去河边。从第三章开始。"
    l_you "短故事已经读完，还没读够？"
    l_cl "那是别人的伞。我自己的嫌疑人还在等。"
    l_you "我能去吗？"
    l_cl "能。三点十分，那时长凳边的石头不晒手。"
    "她把今天好笑的书签夹进蓝封小说，位置仍在第二章末。公用笔放回原盒，没跟着装进私人袋里。"
    "自己的短铅笔收进外袋，还有两条空窄纸和一张记柜格的便纸。她最后装好水壶，将薄垫叠在厚垫旁。"
    $ claude8_club_finished = True
    return

label claude08_scene4:
    $ chapter = "Claude 第八章 / 04 · 书在袋里，人在这里"
    scene bg river day with dissolve
    show sprite claude as claude at sprite_breathe(0.65) with dissolve
    "三点十分，河边长凳的半边落着树影。Claude把厚垫放好，先坐上去，才从袋里取出蓝封书。"
    "她递来薄垫，你铺在身旁，再把她刚取出的水壶放到平石上。她开袋时，一个纸包跟着滑出来，落在自己膝头。"
    if claude8_has_ch07:
        l_you "不是又煮梨？"
    else:
        l_you "今天还带了点心？"
    l_cl "芝麻饼。买的。我今天想吃自己没有守过锅的东西。"
    "她将饼放进一只干净小食盒。纸包的底折却跟着卡在扣边，她扣了两次，声音总比该有的轻。"
    l_you "你先看下面。"
    l_cl "看见了。纸在替我多占一个底。"
    "她把折角拉出来，重新盖好。这回扣边很响，她反倒被自己的力气吓了一下。"
    if claude8_previous_snack == "tray":
        l_you "今天不用我托住右边了。"
        l_cl "嗯。昨天的纸托用过一次就够了。饼不会往你袖口倒汁。"
    elif claude8_previous_snack == "plate":
        l_you "今天也不用再回去拿平盘。"
        l_cl "不用。昨天洗好的那只还在柜里，别为两块饼请它出门。"
    else:
        l_you "现在合上了。"
        l_cl "嗯。你别夸它。是我刚才夹错了。"
    "她把食盒放上平石，蓝封书留在自己腿上。你坐在另一只薄垫上，两人之间能放下合拢的书。"
    if not claude8_reply_inherited:
        "她看过今天的短书签，忽然将书合起来。指尖沿着封面的礼帽边走了一小段，停在书脊旁。"
        l_cl "读之前，还有一件想问你。"
        l_you "不是伞的第三条腿？"
        l_cl "不是。我今天想和你说，我喜欢你。"
        "她抬头看你，手仍停在书脊旁。拇指沿着布纹慢慢放平，等你听完。"
        l_cl "我想和你谈恋爱。你可以想等一等，也可以只想做朋友。告诉我你现在想选的。"
        menu:
            "我也喜欢你，想和你成为恋人。":
                $ claude8_reply = "love"
                l_you "我也喜欢你。今天想和你成为恋人。"
                l_cl "好。我听见的是这句。"
                "她呼出一口气，掌心在封面上停稳。没有立刻伸手过来，只把自己的厚垫向你转了一点。"
            "我还不能答应恋爱，想再相处看看。":
                $ claude8_reply = "wait"
                l_you "我还不能答应恋爱。愿意继续见你，也想再相处看看。"
                l_cl "好。今天先到这里。之后的见面也可以再商量。"
                "她点点头，松开捏紧的书角。你仍坐在自己的垫子上，她把合拢的书留在两人之间。"
            "我想和你做朋友。":
                $ claude8_reply = "friend"
                l_you "我想和你做朋友。今天这场读书会，我还想来下一次。"
                l_cl "听见了。下一次可以来，朋友也有份。"
                "她垂眼看了一会儿书签，随后抬头。笑容慢一点，却没有将你的薄垫收走。"
        $ claude8_reply_confirmed = True
    elif claude8_reply == "love":
        l_cl "今天想坐你旁边，不止是为了让你翻页。"
        l_you "我知道。昨天你已经说过喜欢我。"
        l_cl "嗯。今天也喜欢。只是今天的饼没有那么酸。"
        "她的嘴角抬起来。你没有抢着将书拿走，她便让它继续留在自己腿上。"
    elif claude8_reply == "wait":
        l_cl "今天不追问昨天那句。三点十分约的是一起看书。"
        l_you "我也只答应了这次见面。"
        l_cl "嗯。书先往后读，别跟着我们卡在同一页。"
        "她翻到第三章，让短书签留在已经读完的地方。你的杯子放在你手边，两只座垫仍各自铺着。"
    else:
        l_cl "朋友今天负责提醒我别把饼屑夹进书。"
        l_you "那我有一项实际工作了。"
        l_cl "还有想笑就笑。我不想请一个坐着替我点头的人。"
        "你指了指她食盒的扣边，她自己再检查一遍。没有把那张私人邀请拿来添上另一个名字。"
    "书翻到第三章。她从封里抽出旧猜纸，借勺人三个字还在上面，没被划掉。最后那位嫌疑人尚未露面。"
    l_you "第二章已经排除这位了？"
    l_cl "嗯。他当时在对岸补船，没偷那双鞋。纸留着，看后面再笑我一次。"
    "她看向石上的芝麻饼，又低头看了一眼新章第一行。你把水壶移稳，等她自己决定先拿哪样。"
    menu:
        "先读一段，读完再拆饼。":
            $ claude8_tea_order = "read"
            l_you "先看这一段。我把食盒留合着。"
            l_cl "好。要是又写一桌饭，你先别念得太香。"
            "第三章偏偏从厨房开场。你读主人去找盐，Claude跟着读柜门后掉下来的围裙，读到一半肚子响了一声。"
            "她按住自己腹前，书却没合上。你停了一下，她用指尖点住下一行。"
            l_cl "继续。响声不是最后那位的台词。"
            "你们读完这一小段，她才将书签移过来。她伸手开食盒时，先把蓝书交给你合好。"
            l_you "这一回没有饼屑进去。"
            l_cl "还没有。你别把话说完就替我拍手。"
        "先吃饼，洗净手再读。":
            $ claude8_tea_order = "eat"
            l_you "先吃。书放袋上，不用让它也尝。"
            l_cl "好。我今天确实想早点吃到这一块。"
            "她打开食盒，挑了边缘略焦的一块，随后将另一块推到你那边。咬第一口时，芝麻先掉进自己掌心。"
            l_you "你选的那块更脆。"
            l_cl "看出来了。不是每次都把最整齐的让你拿。"
            "你将饼屑留在食盒里，她端水让你洗手，自己也用少量清水冲净指尖，再擦干。"
            "她翻第三章时，拇指在封面外停了一下，确认没有油。你读厨房找盐，她把刚擦干的手举给你看。"
            l_cl "现在盐也不能叫我回去做饼。"
            "你们读完第一小段，她将书签移过来。两块饼已经吃完，空食盒盖好，留在平石上。"
    $ claude8_novel_chapter = 3
    $ claude8_private_reading_kept = True
    return

label claude08_scene5:
    $ chapter = "Claude 第八章 / 05 · 留下整页的空白"
    scene bg river day with dissolve
    show sprite claude as claude at sprite_breathe(0.65)
    "三点四十分，河面的亮光绕过桥墩。蓝封书停在第三章开始的几页，新的短书签露出一点角。"
    if claude8_tea_order == "read":
        "她吃掉那块边缘略焦的饼，将芝麻屑收在食盒里。你合着书等她擦净手，没继续往后读。"
        l_cl "刚才响得那么大，现在反而吃得慢。"
        l_you "它终于轮到你了。"
        l_cl "嗯。这块边我想留到最后。"
    else:
        "她给空食盒擦掉一滴水，放回袋内的外侧。书留在干着的布面上，没有贴着刚洗手的石角。"
        l_cl "先吃有一个坏处。现在没东西替我遮住想偷看的眼睛。"
        l_you "你要翻最后一页？"
        l_cl "想。今天不翻。我想看看那顶帽子还能惹多少事。"
    if claude8_reply == "love":
        "她把书接回去，合好，放进自己的布袋。动作没有急，等书脊落稳，才转过来看你。"
        l_cl "今天想先看你。"
        l_you "我坐在这里，没有躲到最后一页。"
        l_cl "知道。刚才一直看纸，有点亏。"
        "她往你这边挪厚垫，挪到一半，发现袋口绳子压在下面。她只好先站起来，让你看着她把自己解开。"
        l_you "你被袋子留住了。"
        l_cl "它今天比我谨慎。别替它答应。"
        "你把薄垫向她留出的方向挪近一点。她坐回来，裙摆理在自己膝上，双手暂时扶着垫边。"
        l_cl "我可以靠近吗？想牵一会儿。"
        $ claude8_close_asked = True
        l_you "可以。我也想牵。"
        $ claude8_close_agreed = True
        "你向她伸出手。她先看你，再将手放进你掌心。指尖合拢时，她的肩才轻轻靠向你的袖边。"
        "水杯和食盒都收稳了，没有一样东西需要她立刻腾出手。她低头看了一会儿，竟先笑起来。"
        l_you "我手里也有螺钉？"
        l_cl "没有。我想起早上把壶摆得比你舒服。"
        l_you "它不用翻页。"
        l_cl "你也不用一直翻。今天我想留这只手。"
        "你轻轻握稳。她把另一只手放回自己膝上，没有替两人的沉默找一段说明。河风将她脸旁的发丝吹乱一点。"
        "她想用空着的手理好，抬到一半又停了，先拿指背碰一下脸颊，笑着把发丝拨回耳边。"
        l_cl "明天我下午想自己读。"
        l_you "你不用等我才往后翻。"
        l_cl "嗯。傍晚想和你去挑一只更小的食盒。我买，不必每次带两份。"
        l_you "那次可以不带书。"
        l_cl "可以。我也想听你讲一点今天没来得及讲的事。"
        "你说起早上走错的那条廊路。她听着，不急着给你画另一张地点图，反而问那扇多绕的门有没有风。"
        "有风。你说得太像一条舒适的捷径，她便指出，既然如此，下次不要一边绕路一边抱怨她等。"
        l_you "你会等在门边？"
        l_cl "约好了才等。没约的时候，我可能已经买到饼。"
        "她说完，把握着的手轻轻抬一下。你看向她，她没有把眼睛藏回蓝色封面后面。"
        l_cl "不过今天还不走。再坐一会儿。"
        "你们坐到桥边的影子挨着长凳。离开时，她先松手收自己的厚垫，随后又主动等你伸手。"
        "后面的书页留给下次。她在你身旁走着，今天好笑的书签和写着借勺人的旧猜纸，都还在她自己的袋中。"
    elif claude8_reply == "wait":
        "她翻到夹书签的位置，确认第三章已经读了几页，随后合好书。你的薄垫没有往她那边挪。"
        l_cl "我今天想留一个下一次。你愿意吗？"
        l_you "愿意。还是来读？"
        l_cl "可以读，也可以逛书铺。下次我可能已经读到后面了。"
        "她说着翻出书后的价格小纸，发现那不是价格，是自己当时记的另一本书名。她看了两秒，先将纸放回去。"
        l_you "找到了什么？"
        l_cl "一个更难看的封面。刚才差点用它给你算多少钱。"
        l_you "你想买？"
        l_cl "想。上面那个人拿着三把钥匙，一扇门都没画。"
        "她举起三个手指，认真比了一下，自己也觉得太满。你说可以下次去看，她却先问你那天有没有空。"
        l_you "第十八日下午有空。"
        l_cl "那就下午三点在书铺门口。不约在最后一页上。"
        l_you "见面也不用给今天添一个恋爱答复。"
        l_cl "不用。到那时我们还能说想继续等，或者不想等了。"
        $ claude8_wait_revisable = True
        "她用自己的短铅笔，把约好的时刻记在一条窄纸上。你接过笔，在另一条空纸上记下同一时刻，两张没有夹成一张。"
        "写好后，她把笔收起来。河上有人撑过小船，你们各自看了一会儿，没有催船替谁先靠岸。"
        l_cl "我会惦记你。今天说过这一句，不等于以后不能改主意。"
        l_you "你也可以不再等我。"
        l_cl "嗯。我知道自己会失望，所以不想假装只是一次买书。"
        "她低头拂掉厚垫边的一粒芝麻，没把它推到你手边。过一会儿，她自己抬起脸，问你喜不喜欢那篇雨伞。"
        l_you "喜欢。尤其是你差点替那只狗解释的时候。"
        l_cl "那一段我自己也喜欢。你可以记住我先笑了，不必只记住我伸手摸笔。"
        "你说好。她把垫子收在自己袋里，留出你能站起的位置。小说也由她自己拿，没有交给你替她保管后半本。"
        l_cl "今晚我想继续读。读累了就停，读到凶手也不用留住他。"
        l_you "下次只别先告诉我名字。"
        l_cl "能答应。封面难看倒可以提前说。"
        "你们一起走到分路口。她往书铺那边先看了一眼，今天没去，转身走向自己想吃晚饭的小店。"
        "下一次的时刻留在各自纸上。今日的会面已经走完，她没有站在河边，把未来的每一天也交给你答。"
    else:
        "她把书合起来，手掌在蓝封面上放了一会儿。你没有靠过去，她抬眼时也没有将凳子转开。"
        l_cl "下次读书会，你想先念吗？"
        l_you "想。可以挑另一篇主人很笨的。"
        l_cl "你先挑。我不替你把笨的部分改聪明。"
        "她从外袋取出那张便纸，用自己的短铅笔写下收短故事的柜格。写到字旁，笔尖忽然停住。"
        l_you "还想补几个注意事项？"
        l_cl "想。现在先不给。柜门上已经有字。"
        "她只留了柜格名，递给你。纸上没有两个人的恋爱称呼，也没有让你代管她私读的那一个小时。"
        l_you "下次我先念，你坐下来听。再下次换你。"
        l_cl "可以。我想把那个主人念得比你更笨。"
        $ claude8_friend_turn_set = True
        "你们把下一次定在第十八日上午十点，地点仍是东廊。她另给自己留了下午，准备一个人把小说往后读。"
        "她想起书铺那本画了三把钥匙的书，给你描述了封面。你以为她不喜欢，她却说正想借它看看。"
        l_you "这回还猜借勺人？"
        l_cl "换一位。这张猜纸留着，我当时写得可笃定了。"
        l_you "我下次给你找一顶更大的帽子。"
        l_cl "拿书来，别拿真的。我柜子没有那种位置。"
        "你笑得肩头动起来，她也没忍住。笑过以后，她先收自己那张垫子，顺手把你的杯子递到你能接的位置。"
        "你问她今天想不想再逛一圈。她看着河边的小路，想了一会儿，摇头，说今天想独自去买晚饭。"
        l_cl "今天想自己挑晚饭。你不用把每条路都陪完。"
        l_you "那我从桥边回去。第十八日见。"
        l_cl "第十八日见。先挑故事，别让雨伞再替你顶一回。"
        "你们在分路口道别。她将公用夹的纸条另放外袋，蓝封小说抱在自己臂弯，没有用那张纸充当私人书签。"
        "走出几步，她忽然回头，叫住你，举起今天好笑的那条窄纸。你以为她要改下一次的时刻，先停下来等。"
        l_cl "第三条腿那句，下次带着。"
        l_you "这也算我挑的故事？"
        l_cl "算你先给我的一个笑话。别扩成一整篇。"
        "她挥一下手，转身走远。手里仍是自己的小说，明天仍有她想独自读的几页。朋友的那一场，则已经给你留好开头。"
    "河边的长凳空下来，杯底留下的两圈水痕慢慢晾干。她带走厚垫和蓝封书，那张短书签仍露出一点纸角。"
    return
