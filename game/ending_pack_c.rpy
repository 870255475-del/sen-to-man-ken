# 千to万ken v0.9 候选：组 C 隐藏 08—11；另附四篇主动坏/遗憾 IF。
# 全员成年。此文件尚未复制入 game，未 native 验证。
# 完成 API 由根代理统一接入；本文件不定义替身、不解锁图库、不改变主线关系。
# 每个入口重置且仅写自身前缀的选择变量；短 IF 的前史在正文内独立成立。

default secret_08_visit = ""
default secret_09_picnic = ""
default secret_10_trip = ""
default secret_11_letter = ""
default bad_common_overpromise_excuse = ""
default bad_gpt_empty_frame_keep = ""
default bad_qwen_closed_tab_delay = ""
default bad_zcode_return_letter_reply = ""

label secret_08:
    if not secret_guard('secret_08'):
        return
    $ secret_08_visit = ""
    call secret_08_scene1
    call secret_08_scene2
    call secret_ending_finish('secret_08')
    return

label secret_08_scene1:
    scene bg echo morning
    show sprite qwen at sprite_breathe(0.62)
    "在这段独立的可能里，你已经在茶摊欠下三次‘下回请’。今天，你带够了钱。"
    "Qwen把零钱推回一半，剩下的照价放进抽屉。她没有趁机多算一杯。"
    l_qw "茶钱结清。那三张欠条，今天也到期了。"
    l_you "我还没请呢。"
    l_qw "所以收回。再挂下去，我都像在经营你的下回。"
    "她把三张纸摞齐。你以为她要销毁，却见她撕掉金额，只留下最宽的空白。"
    l_you "这一栏怎么没划掉？"
    l_qw "原本拿来记我歇了多久。后来总填成给谁送茶。"
    "她按住准备响起的计时铃，第一次没有立刻去看旁边的水壶。"
    l_qw "明天半天不营业。我想走到河边，再慢慢走回来。"
    l_you "你想一个人走，还是让我占一点？"
    l_qw "占一点。别替我排满。"
    "你拿起笔，却没急着写名字。她用指节轻敲那一栏，耳尖藏在发丝后面。"
    menu:
        "写‘早上，河边一起吃两只包子’。":
            $ secret_08_visit = "morning"
            l_you "我买两只热包子。你醒了再来，不算迟到。"
            l_qw "三只。我要一只甜的，再分你半只咸的。"
            "她接过笔，把‘两只’改成‘三只’，在旁边画了一个很小的太阳。"
        "写‘傍晚，河边陪你散步’。":
            $ secret_08_visit = "evening"
            l_you "白天留给你睡。傍晚我在桥边等。"
            l_qw "那我会走到桥边。你不用一路找过来。"
            "她接过笔，画了一弯小月亮。弧线不够圆，她又补了一笔，没擦掉。"
    "你把欠条还给她。Qwen叠起纸，收进自己的袖袋，而不是摊位的账夹。"
    return

label secret_08_scene2:
    scene bg river day
    show sprite qwen at sprite_breathe(0.62)
    "第二天，你们真的沿河走了一段。她没带茶盘，袖袋里也没有备用账本。"
    if secret_08_visit == "morning":
        "包子纸沾了油。Qwen护着甜馅那只，咬了一口，才把另两只分开。"
        l_qw "咸的比我想的好吃。这个决定可以反悔。"
    else:
        "傍晚的光仍亮着。Qwen睡得发梢翘起，走到你面前才发现，抬手压了两次。"
        l_qw "半天睡不够。可出来这一趟，也不想省。"
    "一辆小推车从窄路经过。她顺势拉住你的袖口，等车远了，手也没有马上松。"
    l_you "要记我帮你让过一次路吗？"
    l_qw "不用。我拉的。"
    "她说完自己笑了，往你身边靠了半步。河风把空白纸的一角吹出袖袋。"
    l_you "还留着它？"
    l_qw "留着。纸另一面还能写。"
    "你们坐到石阶上，她拆开纸，发现你写的那一行没有占满。"
    "Qwen在剩下的地方写下‘今天很好’，停了片刻，又加上一个具体的时刻。"
    l_qw "下次想见你，我会开口。不会发账单。"
    l_you "我也会。今天先坐到你想回去。"
    "她把纸压在膝上，掌心朝上放在你们之间。你伸出手，她轻轻握稳。"
    if ending_playthrough_stage() >= 2:
        "你在纸背先留出一整格。Qwen看见，没有急着补上下一次的时刻。"
        l_qw "这一格先归我。想见你时，再约。"
        l_you "好。空着也不会算欠。"
    "这一天没有留下新欠条。茶摊重新开门前，你们已经把半天过完了。"
    return

label secret_09:
    if not secret_guard('secret_09'):
        return
    $ secret_09_picnic = ""
    call secret_09_scene1
    call secret_09_scene2
    call secret_ending_finish('secret_09')
    return

label secret_09_scene1:
    scene bg echo morning
    show sprite glm at sprite_breathe(0.62)
    "这段独立的可能，从GLM收起最后一块促销牌开始。篮子旁不再挂赠品袋。"
    l_glm "今天没有赠品。买一份，就只有一份。"
    l_you "那你这份卖吗？"
    "你指的是她留在篮子最底下的酸杏。GLM立刻用掌心盖住那只纸包。"
    l_glm "这个不卖。我挑了好久。最酸的留给我。"
    l_you "我以为你只挑别人肯买的。"
    l_glm "会卖，也会馋。不冲突。"
    "她的尾巴绕到纸包边，又像怕暴露似的收回去。你把要买的点心钱放下。"
    l_glm "真的照原价？没有附送尾巴摸一下哦。"
    l_you "我来找你。点心是顺路。"
    "她抬起的手停在半空，几秒后才把钱收好。促销牌背面碰到桌沿，响得很清楚。"
    l_glm "那等我收摊。别替我喊，我今天想早点走。"
    "她从桌下拉出两只小篮子。一只是野餐布，另一只放着她没舍得吃的酸杏。"
    menu:
        "提起野餐布，去河边挑个舒服的位置。":
            $ secret_09_picnic = "cloth"
            l_you "我提布。你把自己的那份带好。"
            l_glm "选背风的地方。漂亮也要坐得住。"
            "她把布角重新卷紧，悄悄塞进一只软垫，才把篮子递给你。"
        "留下装好酸杏，和她一起慢慢走。":
            $ secret_09_picnic = "apricot"
            l_you "我帮你扎纸包。太紧会压坏，告诉我。"
            l_glm "松一点。最酸那颗，我想完整地咬。"
            "你试着绕了一圈。她伸手扶住结，两个人的指尖碰在同一根细绳上。"
    "最后一位客人离开后，GLM自己翻过打烊牌，没有把它留成等你的借口。"
    return

label secret_09_scene2:
    scene bg river day
    show sprite glm at sprite_breathe(0.62)
    "河边没有价目牌。GLM先坐下，尾巴从布边探出去，给旁边的位置留出空隙。"
    if secret_09_picnic == "cloth":
        "软垫一半压在她身下，一半被推给你。她试了试，认真宣布这块地选得不错。"
        l_glm "篮子放这里。你也坐这里，别退到晒太阳那边。"
    else:
        "酸杏纸包打开后，她认出你扎的那个歪结，没笑它，先把绳子绕在篮柄上。"
        l_glm "这个结留着。下次我一眼就认得。"
    "她咬到第一颗杏，眼睛立刻眯起来。你递水，她还坚持把那一口嚼完。"
    l_you "太酸就放下。"
    l_glm "不。就是这个味道。等我缓一下。"
    "你忍着笑陪她缓。她看见了，把另一颗举到你嘴边，又在碰到之前停住。"
    l_glm "想试吗？不想的话，我能全吃完。"
    l_you "分我小半颗。"
    "她用手掰开，自己咬了较大那半。你才咬一口，两人同时去找水杯。"
    l_glm "好了。现在谁也别笑谁。"
    "她嘴上这么说，尾巴却轻轻扫过你的手背。你把杯子递回去，没有抓住它。"
    "GLM把吃空的纸包展平，铺在篮底。她带来的那份终于没有留到收摊以后。"
    l_glm "明天也没有赠品。你还来吗？"
    l_you "来。你挑你想吃的，我带水。"
    "她报了一个下班时刻。你记好，她便往你身边挪了半步，肩头轻轻碰过来。"
    if ending_playthrough_stage() >= 2:
        "你没替她列下次的菜单。GLM把空纸包折成小船，端端正正放在篮底。"
        l_glm "下次可能换口味。我自己挑。"
        l_you "那我多带一杯水。"
    "你收起野餐布，她把水杯放回装过杏的那只篮子。你们各提一只，沿河边慢慢往回走。"
    return

label secret_10:
    if not secret_guard('secret_10'):
        return
    $ secret_10_trip = ""
    call secret_10_scene1
    call secret_10_scene2
    call secret_ending_finish('secret_10')
    return

label secret_10_scene1:
    scene bg echo morning
    show sprite opencode at sprite_breathe(0.62)
    "在这段独立的可能里，你临时去南镇住了几天。出发前，OpenCode来还一把尺。"
    "她把尺放进工具箱，试着拧上搭扣。扣歪了，她却没有拆开整个箱盖。"
    l_opencode "能扣。先这样。"
    l_you "不像你平时的口气。"
    l_opencode "今天不是来修箱子。"
    "她从外袋取出票。不是运货单，两张薄纸被她护在掌心，边缘还很平。"
    l_opencode "南镇的车。往返票，下午去，晚上回。"
    l_you "谁那边坏了东西？"
    l_opencode "没人。你在那边。"
    "你这才注意到她没背工具袋。平时装螺丝的侧袋里，放着一只装豆饼的纸盒。"
    l_you "我会回来。你不用赶着陪我搬。"
    l_opencode "知道。我想去看你住的那条河。也看你。"
    "她说完，又低头检查了一次车票日期。这回不是找错，是给自己一点空隙。"
    l_you "下午不接活？"
    l_opencode "停到晚上。告示挂好了，不会有人白等。"
    menu:
        "先到南镇，在河桥边等她。":
            $ secret_10_trip = "meet"
            l_you "我先去把住处放好。下车往左，我在桥边。"
            l_opencode "站在好找的地方。我会带豆饼。"
            "她收好往返票。你们约好只认桥，不去找未坏的灯，你按原定的早班车先走。"
        "改坐同一班车，和她一起过去。":
            $ secret_10_trip = "together"
            l_you "东西不多。我等下午，和你一起走。"
            l_opencode "好。靠窗给你，我拿盒子。"
            "你换到下午那班车。她把往返票压平，工具箱留在屋里，没有跟来。"
    "临出门，她又回头看了一眼搭扣。手伸到一半，转而拿起纸盒。"
    return

label secret_10_scene2:
    scene bg river day
    show sprite opencode at sprite_breathe(0.62)
    "下午，你们到了南镇的河桥。OpenCode没有先检查桥栏，把盒子放稳就坐下来。"
    if secret_10_trip == "meet":
        "她按约从左边过来，远远看见你，步子快了几下。豆饼盒被两只手端得很稳。"
        l_opencode "没走错。你也没走开。"
    else:
        "车上她靠着盒子睡了片刻。下车时你叫醒她，她先看你，再确认豆饼没有被压。"
        l_opencode "够睡了。现在想坐水边。"
    "豆饼有些凉，边缘却还是酥的。她掰开第一块，碎屑落在自己的裤膝上。"
    l_you "我去找个盘子？"
    l_opencode "不用。一块饼能直接吃。"
    "你们各拿一半。她把空盒垫到膝上，终于不用腾出手做下一件事。"
    "河面反光刺眼，你抬手挡了挡。她挪到你身旁，肩膀刚好碰上，先看了你一眼。"
    l_you "这样舒服。"
    l_opencode "那就不挪。"
    "她真的没挪。回程车票在口袋里，整段下午却没有被倒数成可用的工时。"
    l_you "下回来，你想看什么？"
    l_opencode "那边的早点摊。今天看见了，已经关门。"
    l_you "我记一下它几点开。"
    l_opencode "问时间就好。不用把摊修一遍。"
    if ending_playthrough_stage() >= 2:
        "你在地图上圈好早点摊，没有添上要她检查的清单。她把地图折到能放进口袋的大小。"
        l_opencode "下次也留半天。不是备用工时。"
        l_you "我知道。你来吃早点。"
    "她笑得很轻，把最后半块豆饼放到你掌心。吃完，你送她到车站，自己留在南镇。"
    "这次离镇没有带回任何修好的东西。OpenCode带回一张用过的票，夹进自己的日历。"
    "日历上新写的那一格，是探望。"
    return

label secret_11:
    if not secret_guard('secret_11'):
        return
    $ secret_11_letter = ""
    call secret_11_scene1
    call secret_11_scene2
    call secret_ending_finish('secret_11')
    return

label secret_11_scene1:
    scene bg echo morning
    show sprite zcode at sprite_breathe(0.62)
    "这段独立的可能里，ZCode写了一封没有地址的信。她带着它来找你，鞋边还沾着晨露。"
    l_zcode "不是代寄。收件人是你。"
    l_you "那我现在就签收。"
    "你伸出手。她没有松开，先把信封翻到背面，让你看那条没贴牢的封口。"
    l_zcode "胶是新的。信不是临时写的。"
    l_you "要紧的事？"
    l_zcode "一件小事。写大了，又删回去了。"
    "你看见信封边角的擦痕。她用拇指遮住一半，另一半实在挡不住，索性放下来。"
    l_zcode "我想邀请你。只邀请你，去河边坐一会儿。"
    l_you "这个不用写很多页。"
    l_zcode "嗯。最后只剩一页。"
    "她把信往前送了一寸，呼吸却比平时送件时慢。你没有在纸上追问被删掉的话。"
    menu:
        "请她亲手打开，读给你听。":
            $ secret_11_letter = "read"
            l_you "我想听你读。读不顺的地方可以停。"
            l_zcode "会停。但我读完。"
            "她小心揭开封口，先在衣角擦干指尖，才把那页折纸展开。"
        "接过信，和她坐下慢慢看。":
            $ secret_11_letter = "share"
            l_you "我们一起看。你不用站着等我的答复。"
            l_zcode "那我坐你旁边。"
            "她把信放到你掌心，绕到座位另一侧。你等她坐稳，才展开纸页。"
    "邀请上写着具体的下午。下面另有一行：带一瓶梅汁，别把空瓶留在河边。"
    l_you "我去。空瓶我带回来。"
    "她轻轻点头，手指终于离开封口。你把信叠好，收进了自己的口袋。"
    return

label secret_11_scene2:
    scene bg river day
    show sprite zcode at sprite_breathe(0.62)
    "到了约定的下午，ZCode比你早几步。她没有替你看遍全部座位，只指了自己喜欢的石阶。"
    l_zcode "坐这里。水声小些，我听得清。"
    "你把梅汁放到两人中间。她用袖子垫着瓶盖，拧第一下没开，便把瓶子递给你。"
    l_you "盖子紧。"
    l_zcode "所以递给你。不是考验。"
    "瓶盖开了。她低头笑了一下，接过瓶子，先倒好你的那杯。"
    if secret_11_letter == "read":
        l_you "你上午读到‘一起’的时候，停得最久。"
        l_zcode "怕说快了，你只听见‘河边’。"
        "她把杯子递来，又说了一遍：一起坐这里。你取出上午的信，照着她停过的那一行慢慢展开。"
    else:
        "你取出信。她看见纸页被仔细折回原样，伸出手，把最边上那道折痕压平。"
        l_zcode "字没改。人已经来了。"
    "一阵风掀起纸角，她的手覆到你的手背上。你稳住信，等她自己决定何时移开。"
    "她没有马上移开，只把杯子放到身旁。凉意留在指尖，掌心却慢慢暖起来。"
    l_you "这封信有署名吗？"
    l_zcode "背面。我最后才敢写。"
    "你翻过去，看见她的名字，还有一行比正面更小的字：我想再约一次。"
    l_you "这次你可以当面问。"
    l_zcode "那，下个下午呢？"
    l_you "好。还是这里，或者你另挑。"
    if ending_playthrough_stage() >= 2:
        "你在信封背面补上自己的名字。ZCode把纸转过来，又转回去，笑意没有藏住。"
        l_you "下次我也可以亲手送给你。"
        l_zcode "我会接。不用先写很多页。"
    "她拿回空瓶，和你一道走上石阶。无地址的信已经送达，下一次邀请有了回答。"
    return

# 两篇主动坏 IF 独立于隐藏十三篇。必须由统一入口明确选择后进入。
# 不能把拒绝恋爱、低关系分或退出共同攻略自动跳转到本文件。
label bad_common_overpromise:
    if not bad_guard('bad_common_overpromise'):
        return
    $ bad_common_overpromise_excuse = ""
    call bad_common_overpromise_scene1
    call bad_common_overpromise_scene2
    call bad_ending_finish('bad_common_overpromise')
    return

label bad_common_overpromise_scene1:
    scene bg echo morning
    show sprite qwen at sprite_breathe(0.62)
    "这是一个主动选择过量承诺的独立IF。祭典当天，你把同一段傍晚答应给了许多人。"
    "Qwen在茶摊等你搬最后一箱杯子。GLM要去河边收花篮。DeepSeek约好一起吃刚蒸的饭。"
    "三个地点挤在同一刻。你看了一眼日程，却在新的请求旁继续写下‘肯定能到’。"
    l_qw "杯子不急。来不了，我另找人。现在说就好。"
    l_you "来得及。你等我一下。"
    "她没有再劝，把箱子留到安全的桌下。你离开前，又答应陪她看第一盏灯点亮。"
    "午后，你一边赶路一边回消息。每回复一个好字，就把上一处约定推迟十分钟。"
    "等到灯绳开始摇晃，你还在礼物摊前挑一个能送给所有人的纪念物。"
    "有人问你究竟什么时候到。你可以承认安排重叠，此时却选择继续遮住它。"
    menu:
        "给每个人都写‘马上到’，让她们再等。":
            $ bad_common_overpromise_excuse = "soon"
            l_you "马上。我已经在路上了。"
            "相同的四个字被发了三遍。你站在原地，等谁先说不用来了。"
        "把迟到说成舞台故障，让她们替你体谅。":
            $ bad_common_overpromise_excuse = "fault"
            l_you "舞台突然出了事，我得先处理。"
            "消息发出去时，舞台上的灯正好亮起。你没有过去，也没有撤回那句解释。"
    "你终于往茶摊走，途中又绕去买赔礼的点心。排到你时，第一轮烟花已经结束。"
    "纸袋很热。你一手提着袋子，一手把还没完成的约定逐条往下划，却没有划掉一条。"
    return

label bad_common_overpromise_scene2:
    scene bg echo
    show sprite qwen at sprite_breathe(0.62)
    "你到的时候，Qwen已经把杯箱搬好。茶摊剩下她自己那只杯子，灯也熄了一半。"
    if bad_common_overpromise_excuse == "soon":
        l_qw "你说马上，我替你留到最后一杯。现在收摊了。"
    else:
        l_qw "舞台一直亮着。我在那里看完一场，没看见你。"
    l_you "我买了点心。还有灯，我们可以——"
    l_qw "我和邻摊约好收东西。点心你留着。"
    "她扣上箱盖，去了自己今晚要去的地方。你追出一步，才看见那并非临时编出的托词。"
    hide sprite qwen
    "GLM的消息也到了：花篮已经归还，她跟收摊的人一起回去。照片里没有空着等你的手。"
    "你把袋子放到长凳上。灯绳的影子落在纸袋口，点心一点一点凉了。"
    show sprite deepseek rice at sprite_breathe(0.26)
    l_ds "我吃过了。饭刚好的时候，没等你。"
    l_you "我明明说了会到。"
    l_ds "听见了。也等过。后来饿了，就吃了。"
    "她提起自己的饭盒，要去帮忙归还桌子。你腾出手，她却已经和那边的人约好了。"
    l_ds "今晚别再替自己加活了。桌子有人搬。"
    hide sprite deepseek rice
    "祭典的人群沿着两条路散去。每个人都有要回的地方，你的消息停在三句没有兑现的承诺。"
    "你坐在长凳上，拆开整袋点心。一份吃不下，另一份也没有人来接。"
    "最后一盏灯灭时，你终于删去日程上的‘马上’，却再没有今晚可以重新分给谁。"
    "长凳旁只剩你的纸袋。你独自收好垃圾，走完了没有同行者的归路。"
    return

label bad_gpt_empty_frame:
    if not bad_guard('bad_gpt_empty_frame'):
        return
    $ bad_gpt_empty_frame_keep = ""
    call bad_gpt_empty_frame_scene1
    call bad_gpt_empty_frame_scene2
    call bad_ending_finish('bad_gpt_empty_frame')
    return

label bad_gpt_empty_frame_scene1:
    scene bg echo morning
    show sprite gpt at sprite_breathe(0.62)
    "这是一个主动停在过去的独立IF。你们曾一起画过一张画，今天GPT带来新的试稿。"
    "她想试粗一点的线。纸上的侧脸还没完成，旁边画着她今早喝歪了口的杯子。"
    l_gpt "来看看。这里故意不修齐，我想留一下。"
    "你没有接新稿，先去擦旧画框的玻璃。框里那张纸，你已经另放进防潮盒保存。"
    l_you "旧的更好。那时候你笑得很漂亮。"
    l_gpt "我今天也有笑。你刚才在擦玻璃。"
    "她把新稿立在空框旁边。你移开它，免得潮湿的墨蹭到已经擦亮的边角。"
    l_you "等干透再说。这个框要留给原来那张。"
    l_gpt "我没要你换。我想让你看看现在这张。"
    "她指着杯子，准备告诉你那一笔为什么歪。你的视线却停在旧画的日期标签上。"
    "标签边缘翘起，你怕它掉下来。她把手收回去，等你先处理完。"
    "桌上还有两杯热茶。她那杯已经喝了一口，你端起自己的，却没有坐到她留出的椅子上。"
    l_gpt "茶凉了，今天这杯也就过去了。"
    "你把杯子放回去，继续寻找压标签的细刷。"
    menu:
        "给旧画再加一层封纸，让她别碰新稿。":
            $ bad_gpt_empty_frame_keep = "seal"
            l_you "别挪了。封好之后，才跟以前一样。"
            "你铺开封纸，占去桌上最后一处平面。GPT只得把还没干的试稿端在手里。"
        "先送旧画去重新装框，让她等下一次。":
            $ bad_gpt_empty_frame_keep = "later"
            l_you "今天先把旧的办完。你这张明天再看。"
            "你抱起防潮盒，连她新试稿的标题都没问。她让开门口，没有再叫住你。"
    "傍晚，框已经重新摆正。GPT的杯子留在桌上，试稿却已经不在那里。"
    return

label bad_gpt_empty_frame_scene2:
    scene bg echo rain
    show sprite gpt at sprite_breathe(0.62)
    "几天后，雨打湿了门槛。GPT来取最后一叠纸，旧画仍被你小心收在盒里。"
    l_you "框干净了。可以把以前那张放回去。"
    l_gpt "你想放，就放。它还是我送你的画。"
    "她弯腰扎紧纸卷。最上面是新的粗线稿，她已经补好了那个歪杯子旁边的手。"
    l_you "我没说不喜欢你画画。"
    l_gpt "我知道。你喜欢那天的画。"
    if bad_gpt_empty_frame_keep == "seal":
        "她看了一眼封纸。胶边没有翘，保护得很好。你等她夸一句，她却把自己的新稿抱稳。"
        l_gpt "那天保存好了。今天我拿走。"
    else:
        l_gpt "你说的明天到了好几次。我不再拿着它等。"
        "她把试稿朝里卷。你这才想看全，露在外面的却只剩一圈干透的纸边。"
    l_you "你要去哪里？"
    l_gpt "新画室。有桌子，窗边够亮。我想在那里继续画。"
    "你提议带旧画送她过去，她摇头，把另一只空画框放回桌面。这只是借来比尺寸的。"
    l_gpt "这个还你。新稿我另外装。"
    "她没有砸掉你的收藏，也没有要求你忘记。她只是收齐现在需要的东西，走出了门。"
    hide sprite gpt
    "你打开防潮盒。旧纸平整，墨色也没有变。你想起她要讲的那只杯子，却已经找不到问的人。"
    "为了不让雨气进去，你又合上盒盖。桌面的框因此仍是空的，映着你迟迟不肯松开的手。"
    "这一次，门口不会有人带着新试稿等你擦完玻璃。雨停以后，你独自把空框扶正。"
    return

# 两篇遗憾 IF：自愿关系中的时间与回避；属于独立假设，不能覆盖既有恋人状态。
label bad_qwen_closed_tab:
    if not bad_guard('bad_qwen_closed_tab'):
        return
    $ bad_qwen_closed_tab_delay = ""
    call bad_qwen_closed_tab_scene1
    call bad_qwen_closed_tab_scene2
    call bad_ending_finish('bad_qwen_closed_tab')
    return

label bad_qwen_closed_tab_scene1:
    scene bg echo morning
    show sprite qwen at sprite_breathe(0.62)
    "在这段遗憾IF里，你和Qwen已经相爱。茶钱一直各自结清，没结清的是一次次约会。"
    "你说忙完就去河边。她说收摊就来找你。两个人都认真说过，也都把下一次写进小册子。"
    "从春天写到入夏，册子厚了一叠，河边那条新路却还没一起走过。"
    l_qw "明天我休息。不进茶叶，也不替别人续摊。"
    l_you "最近实在忙。"
    l_qw "知道。你上次也这样说。"
    "她从袖袋抽出两张船票。边缘被指尖压软，日期就在明天，没有更远的空白可填。"
    l_you "你已经买了？"
    l_qw "想同你去。也怕问完，又听见下次。"
    "你看向桌上的工作。事情确实很多，可其中有一件今天不做也无妨。你没有说出是哪件。"
    menu:
        "在册子写‘祭典忙完补上’，请她再记一笔。":
            $ bad_qwen_closed_tab_delay = "festival"
            l_you "先记这里。等祭典结束，我把整天补给你。"
            l_qw "那一天真的空得出来吗？"
            "你圈起日期，没有回答。她把船票夹进去，纸边盖住了你画的圆。"
        "把她的休息日改约到下个月，不谈为什么。":
            $ bad_qwen_closed_tab_delay = "month"
            l_you "下个月行吗？到时候总能轻松些。"
            l_qw "我明天还是会休息。"
            "她没同意改掉自己的休息日。你却已经翻到下一页，替两个人写好了下次。"
    "晚上她留了一盏灯等你。你忙完想过去，又怕让她看见自己疲倦，发去一句早点睡。"
    "她看着那句关心，把灯关了。第二天你问船好不好坐，她只说河上风很大。"
    return

label bad_qwen_closed_tab_scene2:
    scene bg river day
    show sprite qwen at sprite_breathe(0.62)
    "又过一个季节，你们终于到了河边。Qwen没有带茶壶，只带着那本越来越满的小册子。"
    if bad_qwen_closed_tab_delay == "festival":
        "祭典后的整天又被新的工作占去。那两张船票始终夹在原处，日期已经过了很久。"
        l_qw "整天没补回来。可我也不想把今天拿来催。"
    else:
        "下个月，你们换了新的工作时刻。你没问她去了哪里，她也没有再追问哪天有空。"
        l_qw "后来我休息了好几次。没再替你改日程。"
    "她把册子摊到石阶上。最初那页还有你画的茶杯，后来只有日期和小小的箭头。"
    l_you "我一直以为，记着就是还在一起。"
    l_qw "我也这样以为。怕说不开心，连见面都没了。"
    "她拿出明年去外地学茶的报名回执。你曾听她提起，却一直把它当成另一个以后。"
    l_you "住处找好了？"
    l_qw "找好了。窗外有一条坡，我想早上自己走走。"
    "你想说陪她，又看见她握住回执的手很稳。那不是等你安排的空栏。"
    l_you "这次我不把它写成欠你的事。"
    l_qw "嗯。我也不留着等你偿还。"
    "河上的船准时离岸。这回她没有掏笔，给错过的这一班再画一支箭头。"
    "她合上册子，没有撕掉你们一起画过的那只茶杯。旧日的喜欢还在，今天的分别也是真的。"
    "临走前，你们认真拥抱了一次。她先松开，你也放开手，没有用新承诺延长这一下。"
    "Qwen走上河边那条新路，去赶已经订好的车。你留在石阶上，把自己的明日重新写短。"
    "后来你确实学会留出时间。那本册子却没有再翻开，你们各自走完了不同的日子。"
    return

label bad_zcode_return_letter:
    if not bad_guard('bad_zcode_return_letter'):
        return
    $ bad_zcode_return_letter_reply = ""
    call bad_zcode_return_letter_scene1
    call bad_zcode_return_letter_scene2
    call bad_ending_finish('bad_zcode_return_letter')
    return

label bad_zcode_return_letter_scene1:
    scene bg echo morning
    show sprite zcode at sprite_breathe(0.62)
    "在这段遗憾IF里，你和ZCode曾默契地靠近。你们都想一起走，却没人把目的地说全。"
    "离镇前，她送来一封信。你接了，却忙着清点行李，连封口旁的新墨都没注意。"
    l_zcode "路上看也行。不是急件。"
    l_you "到地方我就回你。"
    "车开出很远，你才拆开。纸上写着她也想离镇学新东西，问你愿不愿意一道商量。"
    "她没替你决定去处。末尾只留了一个见面时刻，和你曾说很想一起去的河桥。"
    "你把回信纸铺在膝上。第一句已经写好，后面关于喜欢的话，却被你改了又改。"
    menu:
        "等新住处安稳再答复，把没写完的信收起。":
            $ bad_zcode_return_letter_reply = "settle"
            l_you "等一切定下来，再给她一个像样的回答。"
            "你把纸折回行李夹层。新的住处换了两次，信也被你带着搬了两次。"
        "先只回‘收到了’，把真正答复留到见面。":
            $ bad_zcode_return_letter_reply = "received"
            l_you "收到了。等见面，我们慢慢说。"
            "短短的回信寄出去了。你没写何时回去，她也没把自己的期限说成催促。"
    "日子开始有了固定的上班与归路。你记得那座桥，却总等到夜里才想起该再写一封。"
    "ZCode也寄过新的信。她写明自己将去另一个镇，地址放在最后一行，你的旧址却已经退租。"
    "那封信被退回。她留到出发前一天，终于合上箱子，按自己的日期去了新生活。"
    return

label bad_zcode_return_letter_scene2:
    scene bg river day
    show sprite zcode at sprite_breathe(0.62)
    "几年后，你短暂回镇，和ZCode在河桥边见面。你们各自有了稳定的生活，也有珍惜的人。"
    "她带来一封旧信。封面有退回的印记，纸并不新，却被好好压在书里，没有揉皱。"
    l_zcode "这封没到。现在给你。"
    "你接过，坐在她旁边认真读完。那些搬家的日期、想去的地方，都有具体的名字。"
    l_you "原来那时，你也已经准备好了。"
    l_zcode "准备好走。没准备好催你回答。"
    if bad_zcode_return_letter_reply == "settle":
        "你从随身的旧夹层里取出未寄出的信。第一句还在，下面空着你曾想写好的以后。"
        l_you "我把回答等成了空白。"
    else:
        l_you "那句收到了，是我当时全部的勇气。也太少了。"
        "她点了点头。你们终于没有拿下一次见面，把这句话轻轻带过去。"
    "风把纸页掀起来，你用手压住。她不再替你按住另一角，而是打开自己带来的水杯。"
    l_you "桥还是这里。人已经走出去很远。"
    l_zcode "嗯。现在的日子，我也喜欢。"
    "你问起她学会的新手艺。她讲了两次失败，讲一间自己挑的房间，讲得比旧信里轻快。"
    "你也说起现在的住处。这一次，地址讲得很清楚，只是用来寄问候，不是邀请她重来。"
    l_you "这封信，我会认真留着。不是留着等你。"
    l_zcode "我知道。读完就好。"
    "她拧紧水杯，给自己的归程看了一眼表。你也看了一眼，互相说清了谁先往哪边走。"
    "你们把信叠回原来的折痕。她起身赶车，你按约去见自己的家人，没有谁留在桥上罚站。"
    "多年后的这一页，终于被两个人读完。错过没有被改写，迟来的字也得到了温和的回答。"
    return
