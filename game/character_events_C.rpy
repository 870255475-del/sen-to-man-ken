# v17 C组候选：九个主动选择的独立恋人IF，全员30岁。
# 未接入/未原生。root提供guard、CGregistry和character_event_restore_scene label。
# 仅event_C_*选择变量；不写主线前史、关系、UUID、好感、周目或95/220。
# 不show旧常服立绘冒泳装。CG后与亲吻黑场后调用root场景恢复。
default event_C_glm_swim_join = ''
default event_C_glm_swim_order = ''
default event_C_glm_mishap_help = ''
default event_C_glm_mishap_finish = ''
default event_C_glm_kiss_invite = ''
default event_C_glm_kiss_answer = ''
default event_C_opencode_swim_join = ''
default event_C_opencode_swim_rest = ''
default event_C_opencode_mishap_help = ''
default event_C_opencode_mishap_table = ''
default event_C_opencode_kiss_invite = ''
default event_C_opencode_kiss_answer = ''
default event_C_zcode_swim_join = ''
default event_C_zcode_swim_card = ''
default event_C_zcode_mishap_help = ''
default event_C_zcode_mishap_message = ''
default event_C_zcode_kiss_invite = ''
default event_C_zcode_kiss_answer = ''

label event_story_glm_swim:
    if not character_event_story_allowed('glm','swim'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_C_glm_swim_join = ''
    $ event_C_glm_swim_order = ''
    "独立恋人邀约的休息日，三十岁的GLM将一只酸杏篮放到成人泳场的干台上。篮旁还有她自留的小白花，已经养好，没有挂价牌。"
    "她换好暖杏色不透明泳裙，长黑发束到肩后，黑白狐耳旁的饰夹扣稳。大尾巴留在干台后侧，没有垂进水道。"
    l_glm "花今天只坐船，不卖。"
    l_you "它买票了吗？"
    l_glm "我买的。泳场允许用这块小浮托，盆底也套好了。"
    "她把借来的空浮托移到低台旁，自己先看了一圈水道。水只到台阶下，远处的泳道和这一小块分开。"
    "小浮托还搭在干台边，她试着将盆放到偏角，另一边就翘了。她赶紧将盆抱回干台，尾梢在身后抖一下，恰好扫过自己的泳巾。"
    l_glm "你先别笑。我还没宣布出发。"
    l_you "花已经转了半圈。"
    l_glm "那是它看码头。"
    menu:
        "帮她将浮托稳住，陪她试这一小段":
            $ event_C_glm_swim_join = 'water'
            "你扶稳岸边的空托。她沿台阶坐到低台上，将盆移到托板中间。等你松手，她自己用双手护住托缘和盆底。"
            "她的双膝自然朝水道侧弯，右手扶托板近缘，左手护盆，抬头时仍想把刚才那半圈说得很有计划。"
            call show_main_cg('fan_glm_swim')
            l_glm "先看这边。它现在坐正了。"
            "她仍扶住托缘与盆底，狐耳轻轻向前转，嘴角那点硬气还没有收回。"
            call character_event_restore_scene
            "小托顺着水纹走出一小段，她跟到近端取回，将盆和空托放稳在干台。白花只晃两下。她擦干小腿，罩好薄外衫，坐到凳旁。"
            l_glm "回来也不加价。今天真不卖。"
        "今天只想陪聊，留在干台上":
            $ event_C_glm_swim_join = 'dry'
            l_you "我今天不试水。想陪你坐会儿。"
            l_glm "好。那盆花也先歇着。"
            "她将干台上的盆挪到凳旁，收起空托，罩上备好的薄外衫。你坐到她让出的半张凳子，尾巴挪回她自己这侧。"
            l_you "你自己玩也可以。"
            l_glm "可以。现在先坐。我连杏都还没挑。"
    "GLM揭篮盖，认真将一颗有小斑的杏拨到自己这边，另把普通的放在中间，等你自己拿。她把泳巾压在干处，掏出小水瓶。瓶底碰到篮扣，盖子又合回去，她低头看了一眼，好像篮子也在和她抢休息。"
    l_glm "先别关。我还没选完。"
    l_you "有小斑的更酸？"
    l_glm "不知道。想试这个，所以留给我。"
    "一只白蝶绕到盆边，她刚把篮盖开宽，又赶紧合回半边。蝶停在花叶上，没有来抢那颗酸杏。"
    l_glm "它比我会挑。酸的留我，花归它看一会儿。"
    "她压住篮扣，终于坐稳，问你接下来想怎样待这一会儿。"
    menu:
        "先把花放到凳旁，再慢慢开杏篮":
            $ event_C_glm_swim_order = 'flower_first'
            "她将小盆搬到不挡脚的干台内侧，拿泳巾垫住盆底，才重新开篮。你将空托移到干台空处，她拿起自己选的杏咬一口，狐耳悄悄向后压。"
            l_glm "现在能看花，也能吃。座位算好了。"
        "先吃自己的那一份，花等收篮时再搬":
            $ event_C_glm_swim_order = 'apricot_first'
            "她先取自己选的酸杏，花仍留干台外侧。刚咬一口，狐耳便向后压了一点。她把剩下半颗握稳，没有塞给你证明不酸。"
            l_glm "很酸。你可以挑别的，别跟我比这个。"
    "你从中间选了一颗，自己吃完，把核放进篮边的小纸碟。她慢慢吃完自己那颗，也将核放好，抿口水，才把刚才想说的那句补上。"
    l_glm "这花我挑了好久。你看它那两片朝里面的叶。"
    "那两片叶朝里卷着，一片比另一片浅。你凑近看，她把挡叶的泳巾边收开，给你留出盆旁的位置。"
    if event_C_glm_swim_join == 'water':
        l_you "看到了。刚才它坐船时也在转。"
        l_glm "嗯。转得比我镇定，回来还没掉一片。"
    else:
        l_you "看到了。坐在这儿，叶片的颜色很清楚。"
        l_glm "今天先在岸上看。下次想玩，我自己再带它来。"
    "临走时她把空托送回泳场借用处，盖好杏篮，花盆端在自己手里。那颗最酸的已经吃完，她嘴角还留着一点被酸住的笑。"
    l_glm "走慢点。花不赶路，我也不赶。"
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_glm_mishap:
    if not character_event_story_allowed('glm','mishap'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_C_glm_mishap_help = ''
    $ event_C_glm_mishap_finish = ''
    "这是独立恋人IF里一场打烊后的看花约。三十岁的GLM把两盆自留花搬到私人花架，白花在左，紫花在右。两盆都已养好，不是刚播的种子。"
    "她穿暖杏色露肩上衣和绿色长裙，长黑发绕开花架。黑白狐耳轻轻朝你这边转，尾巴已经替她挪出了半张点心凳。"
    l_glm "今天先看花。篮子还盖着。"
    l_you "你给它们挂了新牌？"
    l_glm "我自己取的名字。等一下，不许先猜价钱。"
    "她将左盆的小木牌提起来，视线停在正面。刚才还翘着的尾梢慢慢低下去，她又看了眼右盆。"
    l_glm "怎么两个都卖杏。"
    l_you "这就是杏篮旁那叠牌吧。"
    l_glm "同一个抽屉。我还特意把字写得很清楚。"
    "她没有将错误木牌塞给你掩饰，自己举起来，背面朝你。蓝绳仍系在盆边，没有拖住花枝。"
    menu:
        "帮她扶盆，换下这两张错牌":
            $ event_C_glm_mishap_help = 'cards'
            "你先扶稳花架，再将手收开。她蹲到盆前，右手提起错误木牌，左手扶着白花盆外沿，抬眼时一半窘、一半不肯认输。"
            call show_main_cg('fan_glm_mishap')
            l_glm "花没有打折。是我拿错牌。"
            "她右手的错牌还停在盆边，左手扶稳白花盆，尾梢悄悄绕回自己身侧。"
            call character_event_restore_scene
            "她解开两根蓝绳，把错误牌叠到抽屉外的小碟，不再混回原来的那一叠。两盆仍一左一右。"
            l_glm "这次看背面也分得清。"
        "今天不动花架，陪她坐着聊花":
            $ event_C_glm_mishap_help = 'chat'
            l_you "我今天想坐着听，不帮你换牌。"
            l_glm "好，坐。牌是我挂错的，本来就得我取。"
            "她自己将两枚木牌解下，放进抽屉外的小碟，才回点心凳。你让她把话讲完，她说白花那盆早上转了一点。"
            l_you "是你转的？"
            l_glm "我转的。它没趁我忙自己跑。"
            "她终于笑出声，指尖仍捏着蓝绳的尾端，慢慢绕成一小圈。"
    "GLM从袋里找出一支铅笔，先把笔尖搁到自己膝前的垫板。她想了两个名字，又划掉一个，不给你看被划掉的那行。"
    l_glm "白花叫小慢。紫的叫门边。"
    l_you "紫花现在在右边。"
    l_glm "它原来在门边。我取的是名字，不是催它回去。"
    "她把两个名字念第二遍，像要确认自己喜欢，念完才问你今晚怎么摆。花架不营业，改名也不用公示给一排客人。"
    menu:
        "把木牌翻背重新写，仍用蓝绳挂好":
            $ event_C_glm_mishap_finish = 'wood'
            "她翻到空白背面亲手写好，再系回两盆。蓝绳一个短些、一个长些，她调过一遍，免得牌碰叶。"
            l_glm "这次就是名字。杏价回杏篮那边。"
        "另画两张小卡，木牌收回抽屉":
            $ event_C_glm_mishap_finish = 'paper'
            "她选两张自己的小卡，画下白花和紫花的样子，名字留卡下。旧木牌另袋收好，放回抽屉，蓝绳绕回垫板边。"
            l_glm "卡放这儿。看见谁，就知道在说谁。"
    "她把铅笔放回袋里，才开酸杏篮。里面只有她买的那一份，不含替你准备的赠品。她让你自己选愿不愿尝，自己先挑一颗。"
    l_you "小慢今天没去门边。"
    l_glm "你叫对了。它在左边，别又给我换盆。"
    "你们边吃边看。她把花盆转一点，露出方才被叶挡住的那一面。你刚看清，她又转了回来，紫花的叶恰好碰到她的指尖。"
    if event_C_glm_mishap_finish == 'wood':
        "临收架时，两张翻背木牌仍挂在盆边。她先将蓝绳理到里面，再盖杏篮。"
    else:
        "临收架时，她将两张新小卡收入自己的薄袋。盆上没有木牌，名字却已经被她当面说过。"
    l_glm "明天还认得吗？认不出也能问。我不换名字收你两次钱。"
    "她先抱白花进檐下，回来又抱紫的，在檐下按原来的左右放稳。她特意照新名字叫了一遍，才提起合盖的杏篮。"
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_glm_kiss:
    if not character_event_story_allowed('glm','kiss'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_C_glm_kiss_invite = ''
    $ event_C_glm_kiss_answer = ''
    "独立的恋人IF里，你们约在私人草坡看落日。GLM三十岁，今天没有售票、没有工作，杏篮里的那一份也只由她自己挑。"
    "她穿暖杏色露肩上衣和绿色长裙，长黑发落在肩后，黑白狐耳转向风来的地方。大尾巴在干铺布后轻弯，没有碰到你。"
    "她把小花盆放在远侧平处，揭篮盖，想将最后一颗杏推过来。手停到一半，她反而自己取回去，咬了很小一口。"
    l_glm "我又想拿杏开场。"
    l_you "现在也可以开。"
    l_glm "嗯，但这颗我还想吃完。"
    "她吃完，把核放小碟，喝口水，自己将篮盖扣稳。两手空下来，才终于看着你，不再忙着找能送出去的东西。"
    l_glm "我想亲你一下。你愿意吗？"
    menu:
        "我愿意。想亲你一下。":
            $ event_C_glm_kiss_invite = 'yes'
            l_you "愿意。想亲你一下。"
            "她听完，肩头往你这边转一点，却仍坐在原来的铺布上。右手回到合盖篮边，左手留在自己膝上。"
            l_glm "好。我先把篮放稳，不拿它挡脸。"
        "今天先不亲，想陪你坐着。":
            $ event_C_glm_kiss_invite = 'defer'
            l_you "今天先不亲。我想陪你坐着。"
            l_glm "好。那就坐，篮盖也不用再开给你看。"
            "她没有靠过来，将小碟移到自己身侧。你们仍各坐原来的地方，风把她刚才压住的铺布角抬起一点。"
    "GLM用水瓶压住布角，先看远侧花盆，确认没有被影子挡住。她想挪盆，手伸到一半，又觉得此刻的位置也很好。"
    l_glm "以前我老想把每个位置都摆给人看。"
    l_you "今天只摆了这几样。"
    l_glm "还有我。不是摆的，我自己坐过来的。"
    "她说完自己先笑，尾梢在布后轻轻折了一下。她又把杏篮转过来，让你看见背面一截歪了的编边。"
    l_glm "这一面刚才朝草丛。买的时候顾着挑杏，回去才看见。"
    l_you "要藏一下午？"
    l_glm "本来想藏。现在看久了，也挺好认。我的那只歪篮。"
    "她用指腹顶了顶翘起的小结，结没松，篮扣也好好的。她干脆让它朝着你，自己扯平铺布，才发现另一端压在尾巴下。"
    l_glm "等一下。我给自己坐住了。"
    "她把尾梢移开，布角一下滑远，又连忙用水瓶压回去。做完两步，她低头笑得肩头轻抖，小花盆在远侧安安稳稳。"
    l_you "篮子倒没跑。"
    l_glm "它知道杏吃完了，跑也没用。你别把这句告诉花。"
    "她笑够了才看你。日光从花盆挪到篮边，她没有追着那一小块亮处继续搬东西，两人面前留着原来的距离。"
    if event_C_glm_kiss_invite == 'yes':
        l_glm "现在轻吻一次，好吗？"
    else:
        l_glm "你想再坐一会儿，还是一起走回去？"
    menu:
        "现在可以。我也愿意。" if event_C_glm_kiss_invite == 'yes':
            $ event_C_glm_kiss_answer = 'yes'
            l_you "现在可以，我也愿意。"
            "她双膝自然向一侧收，右手轻按已合杏篮，左手回自己膝上。黑发留在肩后，她闭眼向画外近前一点，唇仍轻合。"
            call show_main_cg('fan_glm_kiss')
            l_glm "嗯。"
            "她闭着眼，右手仍轻按合盖杏篮，唇边的笑停了一小拍。"
            scene black
            "你们轻轻吻了一下。"
            call character_event_restore_scene
            "再睁眼时，她已经自己坐回铺布中央，脸有些热，先去摸篮扣有没有碰倒，又自己笑了。"
            l_glm "这个没附赠东西。别替我查篮子。"
        "先停在这里，今天不亲。" if event_C_glm_kiss_invite == 'yes':
            $ event_C_glm_kiss_answer = 'stop'
            l_you "先停在这里，今天不亲。"
            l_glm "好，停。那我把花挪一点。"
            "她的肩退回原来的方向，没有触碰，也没有向你递出换答复的杏。她将花搬到另一块平地，给收铺布留出位置。"
        "再坐一小会儿，看花的影子。" if event_C_glm_kiss_invite == 'defer':
            $ event_C_glm_kiss_answer = 'stay'
            "你们继续看影子沿草坡变长。她捏住铺布的小褶，拿花盆边缘去比，发现自己刚才比反，便把手放下。"
            l_glm "影子长了，花没长这么快。你别笑出整盆来。"
        "一起收好东西，慢慢回去。" if event_C_glm_kiss_invite == 'defer':
            $ event_C_glm_kiss_answer = 'walk'
            "她先将花盆抱起，杏篮留给自己下一趟拿。你提自己的东西，没有把她的私物全揽到你怀里。"
            l_glm "先到坡口。回来拿篮，不需要再买一次票。"
    "最后那段日光移出铺布。GLM亲手收起水瓶和小碟，篮盖一直扣着，花盆依旧好好的。"
    l_glm "下次我还想来。杏我自己挑，地方也自己选。"
    "你们按刚才选的节奏离开。她卷铺布时又让尾梢勾散一角，停半拍，自己低头笑出来，重新卷了一次。"
    call character_event_restore_scene
    if _return is not True:
        return False
    return True
label event_story_opencode_swim:
    if not character_event_story_allowed('opencode','swim'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_C_opencode_swim_join = ''
    $ event_C_opencode_swim_rest = ''
    "这场独立恋人IF的休息日上午，三十岁的OpenCode带你到南镇公共泳池。她已经吃过自己的早餐，工具箱锁在寄物柜，没有带到池边。"
    "她穿灰蓝色不透明连体运动泳衣，深紫长发束好，黑色机械双耳架保留原来的形状。泳镜却被她戴反，鼻梁那一段朝上。"
    l_opencode "压歪了。等半分钟。"
    l_you "要我看一下？"
    l_opencode "能调。你先放自己的东西。"
    "她站在干台上摘下泳镜，对着内侧看一遍，再将镜带理平。调整后的泳镜暂放额前，她眨眨眼，确认不再压住眉。"
    l_opencode "现在能下去。刚才不是水的问题。"
    l_you "还没有碰水。"
    l_opencode "嗯，所以先怪我。"
    "她看向短侧道的终点，手往池沿伸了一下，又收回。这里没有要修的器材，她今天只想知道自己能不能一口气游完这一小段。"
    menu:
        "陪她进入侧道，各游一小趟":
            $ event_C_opencode_swim_join = 'water'
            "你答应，她沿固定台阶下水，先在浅侧道站稳。泳镜落到眼前，镜带没有翻转。她双手扶着固定池沿，身体稍侧转。"
            "深紫长发束在肩后，机械双耳架左右都清楚。她将额头抬向画外，短短笑一下，正要从池沿松手开始游。"
            call show_main_cg('fan_opencode_swim')
            l_opencode "这一道。我先走。"
            "她的双手仍贴着池沿，泳镜下的笑没有被镜带挤歪，肩头先松了一点。"
            call character_event_restore_scene
            "她轻轻离开池沿，游到自己选的终点再回头。你完成自己的那一趟，她沿台阶回干岸，擦干身上的水，将泳镜收入干袋，罩上薄外衫，穿好便鞋。"
            l_opencode "没有戴反。第二次也没有。"
        "今天留在干处，陪她坐着休息":
            $ event_C_opencode_swim_join = 'dry'
            l_you "今天不下水。想坐一会儿。"
            l_opencode "好。凳子在那边。"
            "她退回干台，擦干试水的指尖，罩上自己的薄外衫，穿好便鞋，再把泳镜放回干袋。侧道没人催她必须游完。"
            l_you "你可以自己游。"
            l_opencode "可以。等我把这口水喝完。"
            "她坐到凳中间，给你留另一端，先拧开自己的水瓶。瓶盖没对准，转了半圈才落下，她看一眼，又短短笑了。"
    "你们坐到干岸的休息桌边，桌上只有两只各自的水瓶。她摸了摸袋里的柜匙，拿出时带出一张小纸票，票背还画着本人想去的午饭店。"
    l_you "这张不是车票？"
    l_opencode "柜匙的编号。后面我画的路。"
    "她让票翻面，路线很短，却把店门画得比桥大。她说怕回程只记得桥，忘了自己到底想吃什么。"
    l_opencode "想吃面。有笋的那碗。"
    l_you "现在出发？"
    l_opencode "先把这一段歇完。"
    "她将自己的水瓶挪进阴凉，掌心还贴着瓶身，先舒舒服服地靠住凳背。"
    l_opencode "水慢慢喝。面还在店里，不会自己跑来。"
    menu:
        "留在凳上喝完水，再去找面店":
            $ event_C_opencode_swim_rest = 'bench'
            "她将编号牌放到干袋内侧，自己喝完剩下的水。你们不赶着起身，等她确认镜袋拉好，才一起到寄物柜。"
            l_opencode "等这个没耽误。店十二点才收午档。"
        "到遮阳棚下慢慢走，再去面店":
            $ event_C_opencode_swim_rest = 'shade'
            "你们提着各自的瓶和袋，沿干台走到遮阳棚。她在阴影里停一下，将瓶盖重新拧稳，不拿太阳热当必须快跑的理由。"
            l_opencode "这边凉。路也能从这里接过去。"
    "到了寄物柜，她先取出自己的干衣，进更衣处换好，再回来拿工具箱。提手扣稳，箱盖保持合着。泳镜另装干袋，没被塞进零件格。"
    if event_C_opencode_swim_join == 'water':
        l_you "今天还想再游一趟吗？"
        l_opencode "下次。今天这趟有了，还想吃面。"
    else:
        l_you "今天没游到，改天还来吗？"
        l_opencode "来。这个柜号不用记，下一次另租。"
    "她将背面的小路线收好，走到门口时先等你拿稳自己的东西。没有把你当拎箱助手，也没给午饭添一项顺路维修。"
    l_opencode "走吧。我看着店门，你看路。"
    "你们离开泳池，往她实际想去的面店走。泳道留在身后，这个休息日上午没有欠谁一趟没游的距离。"
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_opencode_mishap:
    if not character_event_story_allowed('opencode','mishap'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_C_opencode_mishap_help = ''
    $ event_C_opencode_mishap_table = ''
    "这场独立恋人IF里，三十岁的OpenCode自己买了早班车票，约你在南镇吃早餐。她穿灰蓝色露肩休闲上衣和完整裤装，工具箱合闭放在脚边。"
    "她想点两个不同馅的包子，在自己那张点单条旁写下取餐号。店主照着条子递来两个鼓鼓的纸袋，问剩下的八个要不要继续装。"
    l_opencode "我写的是两个。"
    l_you "旁边还有一个一。"
    l_opencode "那是号。写到份数栏了。"
    "纸袋里各装好两只，其余还在店主那边。她没动食物，先把袋子放稳，低头看自己的条子。工具箱仍在脚边，没有被开成解决所有问题的办法。"
    l_opencode "这张得重写。"
    l_you "早餐先别变成十二个。"
    l_opencode "嗯。吃完会赶不上下午。"
    menu:
        "陪她核对单子，帮她把份数指清":
            $ event_C_opencode_mishap_help = 'confirm'
            "你把点单条铺到柜台，她亲自向店主说明取号和份数。店主暂停装袋，让她先看已经装好的那四只。"
            "她双手托起两个纸袋，袋口只露出几只包子的顶端。深紫长发落在肩后，机械双耳架不变，抬眼时自己先露出一个干笑。"
            call show_main_cg('fan_opencode_mishap')
            l_opencode "这个数，现在看得清。"
            "她仍托着两只纸袋，袋口露出包子的圆顶，干笑里终于多一点想吃的意思。"
            call character_event_restore_scene
            "她确认留下四只，取消还没装的八只，亲手改条子，付了四只的钱。额外两只装另袋，留作自己的下午点心，不往你那份里塞。"
        "今天不帮改单，想陪她吃顿早餐":
            $ event_C_opencode_mishap_help = 'chat'
            l_you "我今天不帮你改单。想坐着陪你吃早餐。"
            l_opencode "好。你先看看座位，我自己说。"
            "她独自同店主核对，留下已经装好的四只，取消没装的八只。出来时条子已改，额外两只装到另袋，由她自己付钱、自己带。"
            l_you "多那两个怎么办？"
            l_opencode "下午我吃。刚才点的时候，本来就想再看另一种馅。"
            "她把另袋压好口，没有拿多买了的份量来催你吃。你自己的早餐仍由你自己选择。"
    "店门前的风掀起纸袋边。她将另袋放工具箱上，发现提手压不住，便拎回手里，指尖按住折低的袋口。"
    l_opencode "箱子合得住。袋子不吃这一套。"
    l_you "有靠窗的桌，外面也有石凳。"
    "她看看店内，又看门边那块干石凳。今天还早，纸袋还暖着。"
    l_opencode "先吃咸的。甜的留最后。"
    l_you "已经挑好顺序了？"
    l_opencode "只挑我的。你的别让我顺手排了。"
    "她把袋口折低一点，终于露出自己最想吃的那只。原先急着买票的手，此刻停下来，托了托暖纸袋。"
    menu:
        "进店坐靠窗桌，慢慢吃完":
            $ event_C_opencode_mishap_table = 'inside'
            "你们选了靠窗桌，各放自己的早餐。她将额外两只放远侧，只打开正餐那袋。工具箱留脚边，没占桌面。"
            call character_event_restore_scene('window_table')
            if _return is not True:
                return False
            l_opencode "窗边能看见车站。还早，吃完再走。"
        "坐门边石凳，把袋口折好":
            $ event_C_opencode_mishap_table = 'outside'
            "她在石凳上铺自己的小垫，将额外那袋折两次放进随身布袋。正餐袋留膝上，风吹过也没有再掀口。"
            call character_event_restore_scene('outside')
            if _return is not True:
                return False
            l_opencode "这次它坐稳了。别拿箱子压。"
    "她吃第一只时停了一下，原来两种馅被店主交叉装着。她重新看袋内的包纸，这次真找到自己先想吃的那一个。"
    l_you "又认错？"
    l_opencode "还没有。停住看了。"
    "她将自己的包纸收进空袋，喝完水，才问你要不要按原计划去河边。她没有把错误藏成没发生，也没让早餐只剩下处理单子。"
    if event_C_opencode_mishap_help == 'confirm':
        l_opencode "刚才那一栏，谢谢你指给我。下一张我自己分开写。"
    else:
        if event_C_opencode_mishap_table == 'inside':
            l_opencode "窗边选得好。我想慢慢吃。"
        else:
            l_opencode "石凳选得好。刚才那阵风也过去了。"
    "她提起仍合闭的工具箱，另袋进本人布袋。额外两只留给她下午，柜台没有十二份等着你们背走。"
    l_opencode "去河边。走慢点，现在想做那个。"
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_opencode_kiss:
    if not character_event_story_allowed('opencode','kiss'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_C_opencode_kiss_invite = ''
    $ event_C_opencode_kiss_answer = ''
    "这场独立恋人IF的清醒早晨，你和三十岁的OpenCode在南镇候车木棚旁见面。双方各自买好了票，离出发还有半小时，今天没有维修委托。"
    "她穿灰蓝色露肩上衣和完整裤装，薄外套搭在本人袋口。深紫长发留在肩后，黑色机械双耳架没有换成别的形状。"
    "她把合闭工具箱放到自己脚边，手指沿锁扣摸了一次。扣子本来就合着，她又看一眼，自己先松开手。"
    l_opencode "不是没扣好。习惯摸一下。"
    l_you "还有什么没拿？"
    l_opencode "水、票、袋。都有。"
    "她把自己的票夹回自己的袋，不把你的也收进去。手空下来，才抬眼看你，嘴边那一点笑停得比平时久。"
    l_opencode "我想亲你一下。可以？"
    menu:
        "我愿意。想亲你一下。":
            $ event_C_opencode_kiss_invite = 'yes'
            l_you "愿意，想亲你一下。"
            "她点头，仍站在木棚柱旁，没有伸手把你拉过去。左手轻扶柱，右手收回本人袋侧。"
            l_opencode "好。站这边，风小一点。"
        "今天先不亲，陪你等车就好。":
            $ event_C_opencode_kiss_invite = 'defer'
            l_you "今天先不亲。陪你等车就好。"
            l_opencode "好。凳子还能坐。"
            "她退到原来的柱旁，将自己的外套铺到本人那端凳面。另一端留给你。她坐下时差点坐住发尾，侧头拢过来，重新理到肩后。"
    "远处有车经过，轮胎声沿路面滚了一小段。她看向站牌，又低头看自己的票，确认是下一班，不跟着别人提箱子。"
    l_you "这次不急着上？"
    l_opencode "不是那班。还要一会儿。"
    "她将水瓶拿出来，盖上那根小带绕到了瓶身。她顺着解开，再放回木棚小台，手没有停成给你修东西的开场。"
    l_opencode "今天想先坐车，再吃我选的那家面。"
    l_you "那家已经开门了？"
    l_opencode "开。出门前问过店主，九点开，今天不休。"
    "她把票往袋里压好，自己的肚子却响了一声。她停住，先笑了一下。"
    l_opencode "问好了。你饿就说。"
    "水瓶侧面贴着一颗剪歪的小纸星。她按回翘起的一角，木台还留着一点水印，纸尖倒没有湿。"
    l_you "这也是出门前做的？"
    l_opencode "嗯。剪了三颗。这颗留下。"
    l_you "为什么选最歪的？"
    l_opencode "像我的手。剪完就长这样。"
    "她说完伸出空着的手，五指展开给自己看，又拢回去。瓶上那颗只有四个尖，她看了两眼，终于笑出声。"
    l_opencode "少一根。剪过头了。"
    "她没有撕掉重剪，捏着瓶盖将水瓶挪到阴凉里。那点歪边仍朝外，来候车的人走过时，她也没用袋子挡。"
    l_you "回去还剪吗？"
    l_opencode "想剪。先吃面。纸留在家，今天不带来做。"
    if event_C_opencode_kiss_invite == 'yes':
        l_opencode "现在亲一下，还愿意吗？"
    else:
        l_opencode "想坐着等，还是到棚边走两步？"
    menu:
        "现在可以。我也愿意。" if event_C_opencode_kiss_invite == 'yes':
            $ event_C_opencode_kiss_answer = 'yes'
            l_you "现在可以，我也愿意。"
            "她站在柱旁，左手轻扶木柱，右手停在本人袋侧，肩稍转向画外。深紫发留在肩后，她闭眼近前一点，唇仍轻合。"
            call show_main_cg('fan_opencode_kiss')
            l_opencode "嗯。"
            "她闭着眼停了一拍，左手轻扶木柱，嘴角的笑没有被风吹散。"
            scene black
            "你们轻轻吻了一下。"
            call character_event_restore_scene
            "她自己退回原站位，睁眼后先摸到袋带，没有又去检查箱扣。嘴角刚扬起便被风吹开的发尾挡一点。"
            l_opencode "头发挡了。下次先理好。"
        "先停在这里，今天不亲。" if event_C_opencode_kiss_invite == 'yes':
            $ event_C_opencode_kiss_answer = 'stop'
            l_you "先停在这里，今天不亲。"
            l_opencode "停了。来，坐会儿。"
            "她收回向前的肩，退到本人那一端凳旁。箱子位置没动，票也照原来的班次留着，没有将错过什么算到你身上。"
        "坐着等，喝一口自己的水。" if event_C_opencode_kiss_invite == 'defer':
            $ event_C_opencode_kiss_answer = 'sit'
            "你们坐到凳上，她把水瓶放在本人手边。等你自己取水，她才拧开自己的瓶，不忙着替你作决定。"
            l_opencode "这里能看见车头。不用一直站。"
        "到木棚边走两步，再回来。" if event_C_opencode_kiss_invite == 'defer':
            $ event_C_opencode_kiss_answer = 'walk'
            "箱子留她目光看得到的柱边，你们只沿棚内走一小段。她用鞋边拨开一粒挡路的小石，顺势站稳，没蹲下开工。"
            l_opencode "两步够了。回来等。"
    "真正那一班车还没进站。她自己收回水瓶，理好外套，再提起工具箱。你带你的票，仍有时间决定要不要同行。"
    l_opencode "不坐这班也行。到了给我留句消息。"
    "她走出木棚又回头，记起水瓶已经在袋里，摸到那颗翘起的纸星才笑着转回来。真正的班车从路口露出车头。"
    call character_event_restore_scene
    if _return is not True:
        return False
    return True
label event_story_zcode_swim:
    if not character_event_story_allowed('zcode','swim'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_C_zcode_swim_join = ''
    $ event_C_zcode_swim_card = ''
    "独立恋人邀约的休息日上午，三十岁的ZCode约你到新街外的成人海滨泳场。她出门前已交接工作件，这次带的是自己的泳巾和一只空白小卡盒。"
    "她换好暖橙色不透明连体泳衣，将蓝边眼罩抬到发顶，清醒地看岸线。银白长发束好，白狐耳旁的蓝饰带留稳，白蓝尾收在自己身后。"
    l_zcode "这趟没有收件地址。"
    l_you "那选哪条？"
    l_zcode "短的。走到岸边那块圆牌。"
    "她指了泳道色带，再看远处岸牌，才发现两者并不在同一边。手收回来，嘴边那句长解释也一起收住。"
    l_zcode "认错线了。改这条。"
    l_you "还可以先站着看清。"
    l_zcode "嗯。不是到了就得马上游。"
    "她把小卡盒放进干袋，泳巾搭在干扶栏上，尾梢没有扫到旁人的用品。确认成人浅水线的入口后，她转身问你。"
    menu:
        "陪她进入浅水线，各游自己那一小段":
            $ event_C_zcode_swim_join = 'water'
            "你答应同行这段，她先沿台阶下到浅水处。右手平伸，指向这次看清的短弧，左手已离开干扶栏，没有拿着卡盒。"
            "她身体稍侧转，银白发束在身后，白狐耳与蓝饰带清楚。抬眼望向画外时，她把刚才那一点窘收成很轻的笑。"
            call show_main_cg('fan_zcode_swim')
            l_zcode "这次看对了。到近岸见。"
            "她右手仍指着短弧，左手自然落在身侧，白狐耳尖轻轻朝近岸转。"
            call character_event_restore_scene
            "你们各游自己的短线，回到同一干岸。她用泳巾擦干，罩上薄外衫，穿好便鞋，不急着把所见写成共同走过的整个海湾。"
            l_zcode "我的线短一点。你那边看见什么？"
        "今天只想坐在干岸陪她聊聊":
            $ event_C_zcode_swim_join = 'dry'
            l_you "今天不游。想坐这儿陪你聊聊。"
            l_zcode "好。那先把东西放稳。"
            "她回到干岸，罩上自己的薄外衫，穿好便鞋，泳巾收在本人袋旁。你们找了阴凉的小凳，岸牌仍能从这里看到。"
            l_you "那条线留给下次？"
            l_zcode "嗯。今天到了这里，也是真的。"
            "她将水瓶放到自己那一端，不把你没下水写成错过一整日。远处有人收泳道带，她看一眼，便转回你这边。"
    "小卡盒里有两张普通白卡和一支短铅笔。她抽出一张，却先把另一张压住，免得风替她选走。"
    l_zcode "本来想写很长。现在只想写三行。"
    l_you "哪三行？"
    l_zcode "在哪儿。做了什么。还想来。"
    "她将最后一行的位置留出来，铅笔先停在自己指间。你看着她重新检查干袋，原来写字那面并没有潮湿。"
    "她用笔比了比卡宽，还没落笔，便觉得三行也可能挤满。她把笔平放在盒槽，先将压住盒角的袋带挪开。"
    l_zcode "不能拿最小的卡，再怪它装不下我。"
    l_you "那换大的？"
    l_zcode "不换。今天想说短一点。"
    menu:
        "请她写一张只记今天的短卡":
            $ event_C_zcode_swim_card = 'write'
            if event_C_zcode_swim_join == 'water':
                "她写自己的短弧和亲眼见的近岸。提到你时只记你真的说过的一件所见，问清愿不愿留这句，没代写你整条路线。"
            else:
                "她写阴凉小凳、看清了却没游的短线。纸上没有两人下水，她自己把这个没做的事留到未来。"
            l_zcode "第三行是我还想来。先不替你写。"
        "先不写，让她当面讲一个小发现":
            $ event_C_zcode_swim_card = 'tell'
            "她把白卡收回盒。原来近岸圆牌背后还有一个旧挂钩，只有从你们站过的入口才看见，她用手指朝那边比了一下。"
            l_zcode "这一句当面够了。卡可以空着带回去。"
    "她将铅笔插回盒内短槽，合盖时又开一次，确认没有压住多余的白卡。你自己的东西仍在你手里，她没有拿走保管。"
    if event_C_zcode_swim_card == 'write':
        "新卡留在本人盒里，寄不寄由她再决定。上面只写本次发生的事，不含任何工作收件地址。"
    else:
        "两张卡仍是空白。她把讲过的小发现留在今天，没说下次一定补一封长信。"
    l_you "回去先做什么？"
    l_zcode "吃自己的午饭。今天不用等最后一趟送完。"
    "她收好泳巾，带自己的袋去更衣处换回干衣。出来时提稳小卡盒和袋子，与你离开岸边。路过旧挂钩，她指给你看，又收回手握住袋带。"
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_zcode_mishap:
    if not character_event_story_allowed('zcode','mishap'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_C_zcode_mishap_help = ''
    $ event_C_zcode_mishap_message = ''
    "这是独立恋人IF里一次写卡约。三十岁的ZCode约你到新街小文具铺门前，她想选一张自己的卡，写完再一起吃晚饭。工作件早已交接，没有带进这只私人袋。"
    "她穿暖棕色长裙和浅色轻披层，蓝边眼罩已抬到额前。银白长发两侧的蓝饰带留好，白狐耳尖转向小铺开门的铃声。"
    "她在写卡桌上打开小铁盒，准备好的句子却停住。盒里只有线轴和合拢的备用别针，连半张白卡都没有。"
    l_zcode "带错了。这个装工具。"
    l_you "卡盒呢？"
    l_zcode "在住处。同样的盖，我拿快了。"
    "她将别针留在盒内，指尖只拨了拨线轴。补纸边的东西都有，偏偏没有要补的那张纸，她终于自己笑一点。"
    l_zcode "今天准备得很全。全错一盒。"
    menu:
        "陪她买一张朴素空卡，重新写这次":
            $ event_C_zcode_mishap_help = 'buy'
            "你陪她进铺，她自己挑普通白卡、自己付钱。回到桌边，她先合上工具盒，再用左手稳盒盖，右手拿起新买的小卡。"
            "银白长发留在披层外，白狐耳与蓝饰带仍在。她抬眼望画外，嘴角已经松开，卡面还是空白。"
            call show_main_cg('fan_zcode_mishap')
            l_zcode "这次有卡了。话不用全写满。"
            "她左手仍稳着闭盒，右手的白卡没有递出，狐耳旁的小铃留在肩边。"
            call character_event_restore_scene
            "她将空卡放平，扣好的工具盒收入本人袋，再取出自己的短铅笔，在卡角试一小笔。新卡没有别人的地址。"
        "今天先不买卡，听她当面讲就好":
            $ event_C_zcode_mishap_help = 'talk'
            l_you "今天不帮你买卡。我想听你当面说。"
            l_zcode "好。我把盒收起来。"
            "她扣上工具盒，放回本人袋内，桌面空下来。你坐在她对面，她看了一眼空桌，却没再急着找能抄一句的纸。"
            l_zcode "本来写了三种开头。在脑子里。"
            l_you "现在用哪一种？"
            l_zcode "短的。想请你留下吃饭。"
    "门边的小铃又响一次，另一位成年客人进去取自己的文具。她往旁边挪一点，让出过路的位置，不将私人约会摆在店门正中。"
    l_zcode "里面有红边卡。我没买那张。"
    l_you "不喜欢？"
    l_zcode "喜欢边。今天的话不需要那么多边。"
    "她指了一下自己披层上的小折线，又将手收回来。晚饭店就在街的另一头，她还想亲口说想同你怎么待。"
    "袋里小铁盒碰出一声，她隔着布按住盒盖，忽然又笑了。工具一件没漏，偏偏拿来赴写卡约。"
    l_zcode "早晨还觉得它好看。挑了半天，里面没看。"
    l_you "现在还好看吗？"
    l_zcode "好看。就是不负责装我想写的话。"
    "她把袋放到自己脚边，盒子平稳了，不再响。铺内有一排同样的小盒，她看过一眼，没有急着再买一只。"
    l_zcode "回去先开盖。别先夸盖子。"
    menu:
        "让她先说完今晚想一起做的事":
            $ event_C_zcode_mishap_message = 'dinner'
            l_zcode "先吃饭。再到门边小巷走一段，九点以前回来。"
            l_you "晚饭愿意。小巷等吃完再看。"
            if event_C_zcode_mishap_help == 'buy':
                "她将三个小安排写到新卡，自己署名，问你要不要收。你说先听她讲完，她便将卡留在自己的薄套，散步仍等吃完再看。"
            else:
                "她直接将三件小事说完。没有卡也没有回执，你能当面答愿意哪一段，不必补一整封信。"
        "先选一个今晚想吃的菜，再决定走不走":
            $ event_C_zcode_mishap_message = 'dish'
            "她选了自己想吃的藕片，又问你想吃什么。散步暂不定，街口还亮着，你们先闻见了饭店的香气。"
            l_you "晚饭愿意。走路等吃完再看。"
            if event_C_zcode_mishap_help == 'buy':
                "新卡只写今晚吃饭和她的署名，余下的地方空着。她自己决定保留，不突然写满未答的行程。"
            else:
                "她把手从空桌收回，藕片的名字已经说出来。她念着店招，轻点自己掌心，像怕这一次又拿错。"
    "小铺门上的影子往街里移。她提起自己的袋，工具盒在内，新卡若买过就夹在本人薄套里，没买便没有。"
    l_you "下次会把两盒分开吗？"
    l_zcode "会。一个留线，一个留卡。也可能先开盖看。"
    "她说完朝饭店走了两步，又停住，等你把东西收好。你们先去吃答应的晚饭，店里那张小桌还空着。"
    l_zcode "这一段顺路。我选的店就在前面。"
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_zcode_kiss:
    if not character_event_story_allowed('zcode','kiss'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_C_zcode_kiss_invite = ''
    $ event_C_zcode_kiss_answer = ''
    "这场独立恋人IF中，三十岁的ZCode在新街租了一间自己的写信小间。门边信箱是她这个休息日亲手装好的，工作信件不用这里收。"
    "你们按本人当面邀请来吃晚饭。她穿暖棕长裙和浅色轻披层，银白长发落在肩后。蓝边眼罩抬到发顶，她此刻清醒，白狐耳边的小铃静静停着。"
    "她从私人小卡盒取出一张新邀请，已经写好自己的名字。看见你就在面前，她念了开头三个字，却停下来笑一点。"
    l_zcode "写得很长。现在不想念全。"
    l_you "想先说哪一句？"
    "她把卡放回本人盒，合上盖，让盒底平平落在小木台上。右手仍轻压盒盖，左手理住自己的披层边。"
    l_zcode "我想亲你。现在愿意吗？"
    menu:
        "我愿意。想亲你一下。":
            $ event_C_zcode_kiss_invite = 'yes'
            l_you "愿意。想亲你一下。"
            "她听完，仍站在自己门边，没有借递卡先碰过来。唇边很浅的笑放出来，手指却还压着盖，像怕自己漏放了什么。"
            l_zcode "盒子合好了。我再问一句。"
        "今天先不亲，想和你吃晚饭。":
            $ event_C_zcode_kiss_invite = 'defer'
            l_you "今天先不亲。我想和你吃晚饭。"
            l_zcode "好。饭照刚才说的。"
            "她保持原来距离，自己把卡盒推到小木台内侧。信箱没有因此关起来，邀请也没有被撕掉，只是卡仍由她自己留着。"
    "小木台的边角轻轻翘着一片旧漆。她指尖停在边上，想到这会儿并不需要修，便将手收回披层下。"
    l_you "这间先住几天？"
    l_zcode "先住到这周末。之后自己再选。"
    "她没有替你留下一把未经说好的钥匙，只说晚饭从窗里那张小桌开始。你能看见桌上两只普通碗，还没有盛饭。"
    l_zcode "想先问你要不要来。饭等人到了再盛。"
    "她说完看了一眼合着的卡盒，又转回你。窗内的小灯正照着门边信箱，饭桌倒暗了一角。"
    l_zcode "灯放反了。信箱像在等客，碗看不清。"
    "她腾出左手，从窗边将小灯转了半圈，暖光落到两只空碗上。她站回门边，披层被灯架轻轻勾住，自己抬手解开。"
    call character_event_restore_scene('lamp_turn')
    if _return is not True:
        return False
    l_you "饭还在锅里？"
    l_zcode "嗯。第一勺我尝过了。"
    l_you "尝饭也要写长句？"
    l_zcode "想了三句。尝第二次，只剩一个字。咸。"
    "她抿住嘴，却没忍住笑。窗内盖着的锅仍在，她侧头看了一眼，重新把披层边理好，手没有朝你伸来。"
    l_zcode "还好只咸一点。水在桌上，饭也够。"
    if event_C_zcode_kiss_invite == 'yes':
        l_zcode "让我近一点，现在轻吻一次，好吗？"
    else:
        l_zcode "先进去，还是在门边说完这句？"
    menu:
        "现在可以。我也愿意。" if event_C_zcode_kiss_invite == 'yes':
            $ event_C_zcode_kiss_answer = 'yes'
            l_you "现在可以，我也愿意。"
            "她站在本人信箱内侧，右手轻压合着的小卡盒，左手理住自己披层边。蓝边眼罩在发顶，银白发留在肩后，她闭眼向画外近前，唇仍轻合。"
            call show_main_cg('fan_zcode_kiss')
            l_zcode "嗯。"
            "她闭眼停了一拍，右手仍按台上的盒盖，左手轻理披层边。"
            scene black
            "你们轻轻吻了一下。"
            call character_event_restore_scene
            "她自己退回原站位，睁眼后看了看盒盖，终于将按盖的右手收回。盒底仍稳稳落在木台，她的笑没藏进披层。"
            l_zcode "信比这句长。下回还想当面问。"
        "先停在这里，今天不亲。" if event_C_zcode_kiss_invite == 'yes':
            $ event_C_zcode_kiss_answer = 'stop'
            l_you "先停在这里，今天不亲。"
            l_zcode "好。停在这里。"
            "她退回原距离，将台上的卡盒推到内侧，手收回身边。你们没有触碰，她也没继续拿另一句漂亮话等你改答案。"
            l_zcode "要进来吃饭吗？今天也可以改日。"
        "先进去吃饭，话可以坐着说。" if event_C_zcode_kiss_invite == 'defer':
            $ event_C_zcode_kiss_answer = 'inside'
            "她将卡盒留木台内侧，亲自推开门。你带自己的东西进来，两只空碗待在桌上，她先问你愿意吃多少。"
            call character_event_restore_scene('home_inside')
            if _return is not True:
                return False
            l_zcode "少一点也行。剩的我自己留。"
        "在门边说一会儿，再决定进不进。" if event_C_zcode_kiss_invite == 'defer':
            $ event_C_zcode_kiss_answer = 'door'
            "她站回本人门边，讲起今天安装信箱时螺帽掉进空盒的事。她自己倒出来，最后并没借工作信件填住那个空隙。"
            l_zcode "声响很大。我还以为有人寄了第一封。"
    if event_C_zcode_kiss_answer == 'inside':
        "夜色慢慢落到新街。她先盛好各自的饭，坐回窗内小桌边，小灯仍照着碗。门边的卡盒留在木台内侧，信箱的盖响了一声，她只朝窗外看一眼。"
        "ZCode理好披层，将水放到自己碗旁，听你把话说完。她尝了自己那口饭，又笑着多喝一口水。"
    else:
        "夜色慢慢落到新街。她把自己的卡盒留在木台内侧，信箱盖被风掀起，又自己落下。没有新信，她却抬头看了一眼。"
        "ZCode理好自己的披层，把小灯的光挪到门槛上。你按愿意的方式停留或离开，她就站在原处，等你把话说完。"
    call character_event_restore_scene
    if _return is not True:
        return False
    return True
