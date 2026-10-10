# root_review_fixes：仅修实际审读确证，原作者冻结文件保留。
# 本修订all_writing_ended=true；由root整合、看图与原生验收。
# v17 B组：十二篇主动选择的独立平行恋人邀约。
# 全员三十岁；未完主线结局仍锁定。root提供入口隔离、场景恢复与图库。
# 只写event_B_*局部选择，无主线、关系、通关、额度和好感写入。
# 不展示旧衣装立绘；CG结束后恢复实际背景。
default event_B_kimi_swim_join = ''
default event_B_kimi_swim_record = ''
default event_B_kimi_mishap_wait = ''
default event_B_kimi_mishap_walk = ''
default event_B_kimi_kiss_page = ''
default event_B_kimi_kiss_answer = ''
default event_B_minimax_swim_join = ''
default event_B_minimax_swim_rest = ''
default event_B_minimax_mishap_help = ''
default event_B_minimax_mishap_flavour = ''
default event_B_minimax_kiss_sound = ''
default event_B_minimax_kiss_answer = ''
default event_B_gemini_swim_join = ''
default event_B_gemini_swim_story = ''
default event_B_gemini_mishap_help = ''
default event_B_gemini_mishap_shape = ''
default event_B_gemini_kiss_cloud = ''
default event_B_gemini_kiss_answer = ''
default event_B_qwen_swim_join = ''
default event_B_qwen_swim_tea = ''
default event_B_qwen_mishap_help = ''
default event_B_qwen_mishap_order = ''
default event_B_qwen_kiss_fan = ''
default event_B_qwen_kiss_answer = ''

label event_story_kimi_swim:
    if not character_event_story_allowed('kimi', 'swim'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_B_kimi_swim_join = ''
    $ event_B_kimi_swim_record = ''
    "独立恋人邀约里，三十岁的Kimi比你早到浅湾。私人散步册已收进防水袋，袋口卷了三次。"
    "她换好深青色不透明连体泳衣，银白长发束成低马尾，发侧深蓝蝴蝶夹扣稳。外披放在干岸。"
    l_kimi "今天不用带铅笔下去。"
    l_you "也不用带橡皮。"
    l_kimi "那个更容易游丢。"
    "两段卵石岸远看像一条路。走近扶手，芦苇后面却露出窄水沟。"
    l_kimi "我以为那里连着。"
    l_you "中间还缺一段。"
    l_kimi "嗯。今天先去近的。"
    "她没取册子改图，先看清成人浅水区边线，用脚尖试了试水。"
    l_kimi "一起过去？到木浮标就回来。"
    menu:
        "陪她沿浅水边线游一小段":
            $ event_B_kimi_swim_join = 'water'
            l_you "好。只去看清的那段。"
            "她沿台阶下水，左手扶固定扶手，双脚站稳。右臂沿水面指向近岸，微转身，回望画外。"
            call show_main_cg('fan_kimi_swim')
            l_kimi "就这边。不是芦苇后面。"
            l_you "这次我也看清了。"
            "她笑了一下，指尖离水面很近。"
            call character_event_restore_scene
            "她松开扶手，划过一小段。浮标绳斜了，她绕到另一侧，才发现是片叶子贴着绳。"
            l_kimi "绕错半圈。它没有动那么远。"
            l_you "半圈也画进去？"
            l_kimi "不用。那是找叶子的路。"
            "回程她沿边线上岸，擦干双手，才打开卷紧的袋口。"
        "留在干岸，今天只想陪她坐坐":
            $ event_B_kimi_swim_join = 'dry'
            l_you "今天不下水。陪你坐会儿。"
            l_kimi "好。我也先坐。"
            "她退离台阶，穿好防滑鞋，罩上薄外披。你们坐到阴凉的长凳，袋子留在她身边。"
            l_you "新岸线怎么办？"
            l_kimi "下次。今天先走到这儿。"
            "她把水瓶放稳，没有将远处没到过的岸画进去。木浮标转了半圈，她看一会儿，又看回来。"
    "Kimi将册子放在膝上，取下新页里的干叶，才发现叶子压着刚才没找到的铅笔。"
    l_you "它藏起来了。"
    l_kimi "一直在岸上。比我守约。"
    "页脚只写着浅湾入口。朝你这边的半页空着，另外几页仍合在她掌下。"
    menu:
        "请她画今天亲自到过的这一小段":
            $ event_B_kimi_swim_record = 'line'
            if event_B_kimi_swim_join == 'water':
                "她画出扶手、浮标和回来的弧线，没有越过芦苇。笔尖最后在扶手旁点了一次。"
                l_kimi "回来时，脚底有一块圆石。"
            else:
                "她画从入口到长凳的线。线尾留在干岸，水里的路线整片空着。"
                l_kimi "这张凳子，比看起来凉。"
            l_you "今天这页可以看？"
            l_kimi "嗯。后面的先别翻。"
        "收好册子，先听她讲看到的东西":
            $ event_B_kimi_swim_record = 'talk'
            "她将干叶放回空页，合好封面，铅笔另插进袋侧。你没有伸手翻她掌下的几页。"
            if event_B_kimi_swim_join == 'water':
                l_kimi "那片叶子像一只鞋。差点沿着它找另一只。"
            else:
                l_kimi "凳子下面有两只松果。一只被踩平了，还占着座位。"
            l_you "刚才就是在看这个？"
            l_kimi "也看你什么时候坐下。"
    "卷好袋口，她拉错了水瓶绳。瓶子提起来，册袋却还躺在凳上。"
    l_kimi "它们都很想跟着走。"
    "她重新提好两样，给你看空下来的手。出口已经有了阴影，你们慢慢走过去，没有替远岸补一圈。"
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_kimi_mishap:
    if not character_event_story_allowed('kimi', 'mishap'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_B_kimi_mishap_wait = ''
    $ event_B_kimi_mishap_walk = ''
    "独立恋人休息日里，三十岁的Kimi在小馆前等你。墨绿长裙外披浅灰薄衫，银白发侧扣着深蓝蝴蝶夹。"
    "她的布袋合着，手里捏一张新餐位条。窗边铺好了蓝桌布，门却还关着。"
    l_kimi "我们早了。两个小时。"
    "她翻过纸条。正面号码十一，背面预约下午一点。她只看了自己的大字，就约你十一点来。"
    l_you "十一号，不是十一点。"
    l_kimi "嗯。我的字，读得太快。"
    "她先发消息确认预约仍在，再收好新条。纸上没有旧愿签或公用目录。"
    l_kimi "还想坐窗边，喝梅子水。要等吗？也可以改日。"
    menu:
        "一起等到一点，先去旁边走走":
            $ event_B_kimi_mishap_wait = 'wait'
            "你答应留下。她站在闭门窗边，一手捏号码条，一手扶自己的袋带，微转身，唇边带一点窘笑。"
            call show_main_cg('fan_kimi_mishap')
            l_kimi "这次把两面都看完。"
            l_you "窗位还会替我们等一会儿。"
            "她又瞄了一眼小纸条，没有拿它遮脸。"
            call character_event_restore_scene
        "今天不能久等，喝水后另约":
            $ event_B_kimi_mishap_wait = 'later'
            l_you "今天不能等那么久。先陪你歇一会儿，再另约。"
            l_kimi "好。你不用补两个小时。"
            "她按店里的规则改到下个休息日，写好时间。你们坐在门侧喝水，没有把窗里的桌布当成已经赴约。"
            l_you "下次我也看背面。"
            l_kimi "发给你两面。别只夸号码写得好看。"
            "她倒给你半杯水，自己留半瓶。你离开前，她念清新时刻，挥挥手，走向自己想逛的小巷。"
            call character_event_restore_scene
            if _return is not True:
                return False
            return True
    "她先朝熟悉的桥头拐了一步，再看门牌。新巷就在小馆旁，不必绕回旧路。"
    call character_event_restore_scene('side_lane')
    if _return is not True:
        return False
    l_you "还想去哪里？"
    l_kimi "竹书签摊。也想看看巷子尽头。今天不用借书。"
    "巷口一边有凉荫，一边竹摊刚开。没有人要她代抄路线，布袋里的册子一直合着。"
    menu:
        "先挑一枚她自己喜欢的竹书签":
            $ event_B_kimi_mishap_walk = 'bookmark'
            "她挑出短书签，背面有一点竹斑。翻过两面，又取一枚长的放在掌心比。"
            l_you "看哪一本装得下？"
            l_kimi "我的小册。短的够了。"
            "她买下短的，没塞进公用物料。短绳缠住袋扣，她自己解开，书签才滑进私人侧格。"
            l_kimi "它也想多绕一圈。"
        "先到巷尾看树荫，回来再挑东西":
            $ event_B_kimi_mishap_walk = 'shade'
            "树影落在矮墙上。Kimi挑能靠着歇脚的地方，鞋尖移开一颗小石子。"
            l_kimi "窗里看像一整片。走近只剩半片。"
            l_you "够两个人站吗？"
            l_kimi "你过来半步。够了。"
            "她喝一口水，没有掏册子。墙上蜗牛越过一道砖缝，她看完，才同你走回巷口。"
    "一点，店员撑开门。Kimi对过号码和时刻才进去，坐上自己的窗位，袋子靠好椅脚。"
    call character_event_restore_scene('window_table')
    if _return is not True:
        return False
    l_kimi "梅子水两杯。我先尝我的，不保证甜。"
    "第一口酸得她停了一瞬。她没将杯推给你，自己加一块小糖，搅了两圈。"
    if event_B_kimi_mishap_walk == 'bookmark':
        l_kimi "书签离杯子远一点。别让杯子弄湿它。"
    else:
        l_kimi "蜗牛可能还没到下一块砖。我们不用比它快。"
    l_you "号码十一坐对了。"
    l_kimi "嗯。背面的时间也到了。"
    "她将小条折进新收据，与你看一会儿窗外。窗帘被风推起，蓝桌布上终于放了她想喝的那一杯。"
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_kimi_kiss:
    if not character_event_story_allowed('kimi', 'kiss'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_B_kimi_kiss_page = ''
    $ event_B_kimi_kiss_answer = ''
    "独立恋人邀约的傍晚，三十岁的Kimi擦干廊下小桌。浅灰针织衫配深蓝长裙，银白发侧深蓝蝴蝶夹与音符饰仍在。"
    "她把私人册子放自己这边，桌上另摆两张新空卡。"
    l_kimi "今天想记一个小地方。你坐过的这边。"
    l_you "这张椅子？"
    l_kimi "嗯。每次都被拿去垫箱子。"
    "她拉椅子，下面半只空盒挂住裙边。她停下来解开，将盒子挪到桌脚之外。"
    l_you "刚才你也把它当仓库。"
    l_kimi "先清出来。今天要坐。"
    "你们各取一张卡。她握铅笔，没有替你写名字，也没翻尚未分享的私人页。"
    menu:
        "各画一张今天坐过的位置":
            $ event_B_kimi_kiss_page = 'draw'
            "你画自己的椅子，她画另一侧。她把椅脚画成三只，数一遍，悄悄添上第四只。"
            l_you "差点站不稳。"
            l_kimi "画里的先扶好。真的你已经坐着了。"
            "她将自己的卡推到桌中间，等你也愿意拿出来，两张才并排靠好。私人册仍留在她手边。"
        "先留空卡，转过椅子看晚霞":
            $ event_B_kimi_kiss_page = 'watch'
            "她横放铅笔，用杯托压住纸角。椅子转向廊外，你们不用再隔着小桌找彼此的脸。"
            l_you "空着也要留？"
            l_kimi "嗯。今天还没用完。"
            "小飞虫落到杯托上，她另拿一小张纸引开，没有急着把那两张卡的空白填满。"
    "她喝完自己的半杯茶，起身收杯。伸手拿你的杯时停住，等你喝完才端走。"
    l_kimi "想一起收。你还在喝。"
    l_you "手比约会走得快。"
    l_kimi "那手先放这儿。"
    "空杯摆进托盘，双手回到她自己膝上。暮色落在袖口，两张卡仍是你们实际留下的样子。"
    l_kimi "想坐近一点。还想亲你一下。可以吗？"
    menu:
        "答应她，让她慢慢靠近":
            $ event_B_kimi_kiss_answer = 'yes'
            l_you "可以。我也想。"
            "她压稳卡片，移到近处椅子。深蓝长裙铺平在膝，双手放自己裙面，闭眼微笑，向镜头轻轻靠近。"
            call show_main_cg('fan_kimi_kiss')
            l_kimi "不用替我数到三。"
            "她呼吸放轻，银白发梢从肩头滑下一点。"
            scene black with dissolve
            "她轻轻吻了你一下，停住，随后笑着退开。"
            call character_event_restore_scene
            l_kimi "现在坐得挺稳。"
            l_you "那只空盒总算让出位置了。"
            "她想了半秒，摸摸自己的发夹，笑着摇头，没有找纸把这两句先抄下来。"
        "今天先不亲，想继续坐一会儿":
            $ event_B_kimi_kiss_answer = 'no'
            l_you "今天先不亲。想和你继续坐着。"
            l_kimi "好。椅子转回来一点，别卡桌脚。"
            "她留在自己的椅上，指出脚边横梁。卡片没被收走，托盘也没忽然变成散场的信号。"
            l_you "等会儿一起搬桌子？"
            l_kimi "等会儿。现在还能看见云。"
            "她指向廊外，不催你解释，也没将刚才的话擦掉当作没问过。"
    if event_B_kimi_kiss_page == 'draw':
        "散场时她晾好四脚椅子卡，问过你，才把愿意交换的那张收进新封套。"
        l_kimi "今天这张我留着。私人册子还是各自的。"
    else:
        "她将自己的空卡收起，另一张还给你，没有临时补上一句现成的情话。"
        l_kimi "下次坐新的地方，可以再拿出来。"
    "你们推好椅子，空盒另放一边。她看一眼刚才坐的位置，关好廊灯，与你一同回屋。"
    call character_event_restore_scene('home_inside')
    if _return is not True:
        return False
    call character_event_restore_scene
    if _return is not True:
        return False
    return True


label event_story_minimax_swim:
    if not character_event_story_allowed('minimax', 'swim'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_B_minimax_swim_join = ''
    $ event_B_minimax_swim_rest = ''
    "独立恋人邀约的下午，三十岁的MiniMax亲手关掉相机，盖稳镜头盖，将设备收进岸上的干袋。"
    "她换好海蓝色不透明运动两件泳装，橙红短发梢带粉色，额前短发用小夹扣好。外衣留在遮阳棚。"
    l_minimax "今天我先下水。冷点心等我回来。"
    l_you "相机要先拍一张？"
    l_minimax "不要。它今天比点心早下班。"
    "她检查小泳板，又朝芦苇边的光看去，习惯性抬起空手比了一下取景框。两只手中间什么也没有。"
    l_you "你忘了它已经下班。"
    l_minimax "手还想加班。给它找点别的事。"
    "她把泳板抱到怀里，先看成人浅水区的边线。水声被岸上的伞遮住一点，她往下走半级，又停下来等你。"
    l_minimax "陪我游到那边？不用赶着追回刚才的光。"
    menu:
        "陪她在浅水区练一小段划水":
            $ event_B_minimax_swim_join = 'water'
            l_you "好。先让你的手抓泳板。"
            "她走到腰深浅水，脚踩稳，左手轻扶小泳板，右手遮住斜阳。身体微侧，红眼抬向画外，笑得很放松。"
            call show_main_cg('fan_minimax_swim')
            l_minimax "这回真听见了。水就在旁边。"
            l_you "没有人要喊重来。"
            "她的右手从额前慢慢放下，肩头的水亮了一点。"
            call character_event_restore_scene
            "她转身双手扶板，游过一小段。没留心方向，板尖先转向了岸边，离浮标反而更远。"
            l_minimax "它想提前吃点心。"
            l_you "你刚才一直在往左划。"
            "她自己纠正，回来踩稳台阶，把泳板暂放休息桌边，擦干手才碰干袋。"
        "今天不上水，在棚下陪她听一会儿":
            $ event_B_minimax_swim_join = 'dry'
            l_you "今天想坐干处。可以陪你听水。"
            l_minimax "行。那我先不抢着下去。"
            "她返回棚下，罩好自己的宽松短外衣，把泳板放稳在休息桌边。椅子朝向水边，关机的相机仍在袋里。"
            l_minimax "坐这儿也听得到。差一点又想找耳机。"
            l_you "你自己的耳朵已经来了。"
            "她笑着摸摸耳侧短发，端起水瓶。冷点心还在保冷盒里，这回她没借拍摄的理由让你等。"
    "她取出两只密封冷点心杯，发现开口勺袋塞在保冷盒下面。盒盖开了又合，勺子却一直没出来。"
    l_minimax "刚才还嫌它们占地方。现在又得请出来。"
    "她自己抽好两柄干净小勺，把杯盖完整揭掉。草莓和芒果各一杯，没有把拿错口味说成惊喜。"
    menu:
        "先分着尝芒果，她留自己那半杯":
            $ event_B_minimax_swim_rest = 'mango'
            "她另拿一只干净小杯，分出半杯芒果给你，余下的留在自己手里。第一口太凉，她缩了一下肩。"
            l_minimax "这杯不能催。催了是我的牙先退场。"
            l_you "杯子已经在替你融化。"
            "她把盖放好，慢慢吃完，最后一点果肉由她自己挑走，没有习惯性把最好的一口都推给别人。她将没选的草莓杯盖稳，收回保冷盒。"
        "各吃自己的，让她挑想要的那杯":
            $ event_B_minimax_swim_rest = 'own'
            "她挑走草莓，把芒果放到你面前。勺尖挖得太满，第一口差点沿杯边滑下，她用杯盖托住。"
            l_you "要补拍完美的一勺吗？"
            l_minimax "来不及。我要先吃它。"
            "她把那一口稳稳吃掉，擦干杯沿。勺子轻碰杯底时，她停下来听一下，没去摸袋里的设备。"
    "收空杯时，她先把自己的放进回收篮，又看见泳板被放在旁边，伸手改放回租借架。"
    l_minimax "一个吃完，一个用完。不能给它们同一个结尾。"
    "她提好干袋，与你沿岸走。芦苇的影子已经换了位置，她没要求你站回半小时前那一块光里。"
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_minimax_mishap:
    if not character_event_story_allowed('minimax', 'mishap'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_B_minimax_mishap_help = ''
    $ event_B_minimax_mishap_flavour = ''
    "独立恋人休息日里，三十岁的MiniMax给自己买了杯果冰。白蓝露肩上衣配完整深蓝及膝裙，海螺耳饰轻轻晃着。"
    "她把合盖杯放到长凳边，打开随身的小布袋。里面一团干净黑绒，正是麦克风的防风套。"
    l_minimax "我把小勺带成了这个。"
    l_you "它不像勺子。"
    l_minimax "袋子像。出门先夸自己准备齐了。"
    "两个同色小袋，一个装勺，一个装防风套。她拿错一只，相机与录音机则都关着，放在另一只合好的包里。"
    "她将黑绒重新包住，留在离食品很远的袋侧。果冰杯没开盖，一点绒毛也没有落到里面。"
    l_minimax "摊上还有新勺。也能换脆筒。陪我回去选？"
    menu:
        "一起回摊位，让她自己选吃法":
            $ event_B_minimax_mishap_help = 'join'
            "你答应。她左手托合盖果冰，右手从小袋举起防风套，离杯口足够远。肩轻耸，望向画外，自己先笑出来。"
            call show_main_cg('fan_minimax_mishap')
            l_minimax "这位只负责挡风，今天没点它。"
            l_you "先送它回自己的袋子。"
            "她手里的杯盖扣得很稳。"
            call character_event_restore_scene
        "先歇脚，今天不继续逛":
            $ event_B_minimax_mishap_help = 'rest'
            l_you "脚有点累，想先坐着。"
            l_minimax "你坐。我回去拿一把，马上回来。"
            "她把防风套收好，自己带合盖杯去摊位取了新勺。回来时冰化了一点，她尝一口，没有朝你举收音设备。"
            l_minimax "这口像果汁。也算我点的口味。"
            "她坐在旁边，把准备好的水杯递给你，自己慢慢吃完。你们听摊主合箱子，等歇够了才离开。"
            call character_event_restore_scene
            if _return is not True:
                return False
            return True
    "她走到摊前，先说明拿错袋子。摊主拿出新勺和干净脆筒，她正要伸手，自己的空袋带挂住杯架。"
    l_you "又有一位不想走。"
    l_minimax "它只是想把场地一起带走。"
    "她停好果冰，自己解开袋带。杯架留回原处，设备包始终没打开，也没有把这件小事录成笑话。"
    menu:
        "用新勺坐着吃，保留杯里的果粒":
            $ event_B_minimax_mishap_flavour = 'spoon'
            "她取新勺，才揭开果冰盖。你们回到长凳，她挑起一块果粒，发现它太滑，落回杯里。"
            l_minimax "再来一次。只是吃，允许失手。"
            l_you "果粒也没有走远。"
            "第二次她挖小一点，稳稳送到嘴边。合盖的设备包靠在自己脚边，她没让小勺再兼职录音。"
        "请摊主换进脆筒，边走边吃":
            $ event_B_minimax_mishap_flavour = 'cone'
            "她付清脆筒差价，请摊主转好果冰。旧杯交进回收篮，小布袋塞回她自己包侧。"
            l_minimax "现在不用勺子。袋子终于可以休假。"
            "她咬脆筒太用力，边上裂了一小片，急忙自己用纸托稳。你提醒她放慢，她先把那片吃掉。"
            l_minimax "别笑太快。下一口才轮到你说话。"
    "回到芦苇边，她从包侧找出一小段备用绳，把勺袋的位置标清。黑绒那只留在里面，食品用袋另放外侧。"
    l_you "下一次先看袋里？"
    l_minimax "对。也可以什么都不带，直接买。"
    "她擦好嘴角，重新扣稳海螺耳饰。离开前看看长凳，确认没落下东西，才与你走向有树荫的小路。"
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_minimax_kiss:
    if not character_event_story_allowed('minimax', 'kiss'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_B_minimax_kiss_sound = ''
    $ event_B_minimax_kiss_answer = ''
    "独立恋人邀约的傍晚，三十岁的MiniMax把设备包搁在屋内。珊瑚红短袖上衣配白色过膝裙，橙红发梢带一点粉。"
    "她摘下拍摄挂牌，海螺耳饰仍在。芦苇旁的私人长凳上，只有两杯水和她自己买的脆饼。"
    l_minimax "今天想说一件没录进去的事。"
    l_you "笑话？"
    l_minimax "差不多。我自己才是里面最好笑的。"
    "她拆脆饼，撕口拉得太短，纸袋没开。又拉一次，包装还是完整，撕口倒在指间卷成一条。"
    l_you "袋子不愿意配合开场。"
    l_minimax "那开场先吃。你等我换一边。"
    "她从另一侧拆开，将一半脆饼放到你面前，自己的留在纸托里。声音很轻，她没再往空肩上找麦克风。"
    menu:
        "听她讲那件漏录的小事":
            $ event_B_minimax_kiss_sound = 'story'
            l_minimax "有人让我收蝉声。我架好机器，第一句却是我肚子响。"
            l_you "最后留下哪句？"
            l_minimax "先删了。回来听，才发现蝉已经替我接了一声。"
            "她学那半声蝉，又把自己逗笑。说到后半段，她忘了原来准备的结尾，拿脆饼指指肚子。"
            l_minimax "结尾吃过了。现在只能讲到这儿。"
        "暂时不说，听一会儿身边的风":
            $ event_B_minimax_kiss_sound = 'quiet'
            "她点头，坐稳长凳。纸袋被风推着滑向凳沿，她自己移回来，用水杯旁的空托压住。"
            l_minimax "它比我们话多。"
            l_you "要给它一张椅子吗？"
            l_minimax "不用。这里的位置我先留给你。"
            "她把自己的脆饼吃完，等风从芦苇顶经过。屋里设备已经关机，谁也没为这阵风跑回去。"
    if event_B_minimax_kiss_sound == 'story':
        "她将手里最后那块脆饼吃完，把空纸托放回纸袋旁。"
    "她端水杯喝一口，杯底却垫着刚才的短包装条。放下时歪了，她赶紧自己抽出，杯子才平稳。"
    l_you "开场还在这儿。"
    l_minimax "够了，它今天已经抢两次话。"
    "她把包装收好，转身面对你，原来用来讲笑话的手停在自己裙边。语速比刚才慢了一点。"
    l_minimax "我想亲你一下。这里没有设备，你也不用给我一个好看的反应。可以吗？"
    menu:
        "明确答应，和她靠近一点":
            $ event_B_minimax_kiss_answer = 'yes'
            l_you "可以。靠近就好。"
            "她放稳水杯，双手轻放自己的白裙膝上。橙红短发被风拂过，海螺耳饰垂稳，她闭眼微笑，向镜头轻轻前倾。"
            call show_main_cg('fan_minimax_kiss')
            l_minimax "这条不用录。"
            "她笑意留在嘴角，肩头放松下来。"
            scene black with dissolve
            "她轻轻吻了你一下，离开时低低笑了一声。"
            call character_event_restore_scene
            l_you "结尾还要补吗？"
            l_minimax "不要。这个我想自己留着。"
            "她重新坐稳，自己喝完杯里的水，没有拿那声笑去填任何音轨。"
        "今天先不亲，继续听她讲故事":
            $ event_B_minimax_kiss_answer = 'no'
            l_you "今天先不亲。还想听你把故事讲完。"
            l_minimax "好。可是结尾真的被我吃了。"
            "她坐回原位，给你看空纸托，自己也笑了一下。水杯还在两人之间，晚霞没有被她当成必须抓紧的倒计时。"
            l_minimax "那我另讲一件。昨天鞋带绑得很好，两只绑到一起。"
            l_you "这次有结尾吗？"
            l_minimax "有。我站着剪开了。没摔给谁看。"
    if event_B_minimax_kiss_sound == 'story':
        "回去时她哼起刚才那半声蝉，又嫌不像，自己停掉。没讲准的那半句留在路上。"
    else:
        "回去时芦苇仍在响。她把空纸袋提稳，走得慢了一点，让鞋底那两声也能听清。"
    "她与你各自收好一只杯子，推开屋门。设备包原样放在桌下，今夜的笑声没有被谁补拍。"
    call character_event_restore_scene('home_inside')
    if _return is not True:
        return False
    call character_event_restore_scene
    if _return is not True:
        return False
    return True


label event_story_gemini_swim:
    if not character_event_story_allowed('gemini', 'swim'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_B_gemini_swim_join = ''
    $ event_B_gemini_swim_story = ''
    "独立恋人邀约的上午，三十岁的Gemini把画卡留在干岸。蓝紫长发半束，猫耳与星形发饰仍在，眼睛一金一紫红。"
    "她已换好蓝紫色不透明运动泳装，上衣与泳裤覆盖完整。外披和毛巾放在岸边布袋里。"
    l_gemini "水上有一颗星。白天也来上班。"
    "她指向浮台旁的一团圆亮影，跟着水波晃一下，又伸长一点。"
    l_you "怎么没有角？"
    l_gemini "可能今天想少做几件事。"
    "她顺着亮影看向岸边，终于看见那块无字圆牌。扶台换个方向，圆牌的倒影也跟着挪开。"
    l_gemini "找到了。是岸上那块牌。刚才把它叫错了。"
    l_you "名字要收回吗？"
    l_gemini "它都听一会儿了。故事里先留着。"
    "她看清成人浅水区的范围，扶住台阶边栏。浮台固定在近处，不需要追着亮影游到远水。"
    menu:
        "陪她下水，绕近处浮台游一小段":
            $ event_B_gemini_swim_join = 'water'
            l_you "先绕浮台。星星不用追。"
            "她沿阶下到腰深水里，脚站稳。左手贴浮台边缘，右手指向圆亮影，身体半转，望向画外笑起来。"
            call show_main_cg('fan_gemini_swim')
            l_gemini "圆牌还在，亮的那块跑了。"
            l_you "等水平一点，再看。"
            "她收回指尖，猫耳轻轻转向岸边的声音。"
            call character_event_restore_scene
            "她沿浮台划过短短一段，回来想把手贴回原处，却先摸到台边粘着的一片叶子。"
            l_gemini "它提前来接我了。"
            l_you "它比你先到了。"
            "她拨开台边的叶子，沿台阶上岸，从岸袋取出毛巾，擦干头发和双手，再去拿画卡。"
        "今天不上水，陪她在岸边找亮影":
            $ event_B_gemini_swim_join = 'dry'
            l_you "今天想待在干处。我们从这儿看。"
            l_gemini "好。换个地方，它说不定又长角。"
            "她离开台阶，罩好外披，坐到干岸。你们绕开会晃的伞影，找见圆牌倒影，她没有催你下水验证。"
            l_you "还是圆的。"
            l_gemini "我要求有点多。它已经亮了。"
            "她将布袋拉近，抽出两张干画卡，水里的那一段留给下次，没有说你们已经一起游过。"
    "Gemini拿出一支铅笔，笔帽却扣在需要写字的那端。她先画不出线，低头看一眼，自己笑着换过来。"
    l_gemini "今天的星和笔，都需要重新确认位置。"
    "她把空卡分给你一张，自己先画一圈，又想添尾巴。那块圆牌离得远，没有任何产品标记或字。"
    menu:
        "一起编一小段圆星星游记":
            $ event_B_gemini_swim_story = 'story'
            "她给圆圈添一双小鞋，让它在纸上慢慢走。你提议它去吃冰，她立刻画一只更圆的碗。"
            l_gemini "不行。这样它会被当成配料。"
            l_you "那让它先学会报名字。"
            "她画出一张小嘴，念到一半，自己又笑了。故事里的圆星没有被她写成真实天象，卡片只留给你们看。"
        "各画刚才真正看见的那一圈亮光":
            $ event_B_gemini_swim_story = 'circle'
            "她沿卡片画亮影的轮廓。第一次画得太扁，她没有擦掉，在旁边又画水波。"
            l_gemini "这圈是它晃的时候。我眼睛还跟着转。"
            l_you "圆牌也画上？"
            "她把牌添在远岸的位置，细细连好视线。画完将铅笔放平，没有冒称已经把水里的每块石头看完。"
    "她收卡时将你的也拿起，停一下，先问哪一张你愿意交换。你留自己的，她便只收好自己那张。"
    l_gemini "可以。我想带圆的回家，你那张先自己养。"
    "岸上伞影挪开一点，圆亮影又回到台边。她向它挥一下手，提好干袋，与你走去买她早就想吃的午饭。"
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_gemini_mishap:
    if not character_event_story_allowed('gemini', 'mishap'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_B_gemini_mishap_help = ''
    $ event_B_gemini_mishap_shape = ''
    "独立恋人野餐前，三十岁的Gemini穿着紫蓝常服与完整下装，外系浅色围裙。猫耳旁的星饰扣好，长发束到肩后。"
    "她用隔热布端出烤盘，桌边摆着圆模和星模。圆饼整整齐齐，一颗尖角也没有。"
    l_gemini "我说要烤星星。星模还在桌上。"
    l_you "圆的已经出勤了。"
    l_gemini "拿模具时还看了星模盒子。里面放的却是圆的。"
    "压第一块时她已经看见圆形，想再压小星形叠上去。后来忙着擦洒出的面粉，忘记了那一步。"
    l_gemini "错的是我的顺序。不能怪它们偷偷变圆。"
    "她先放稳烤盘，让热饼凉下来，将桌边的星模挪近。她解下围裙，挂在椅背，再取好隔热布。"
    l_gemini "还留了小团面。要一起补几个，还是先尝圆的？"
    menu:
        "留下来，陪她把这盒点心做好":
            $ event_B_gemini_mishap_help = 'join'
            "你答应一起完成。她双手隔着布扶烤盘，将圆饼稳稳放到桌面，头偏向画外，眼睛睁圆，笑里带一点窘。"
            call show_main_cg('fan_gemini_mishap')
            l_gemini "好吧。这一盘真的没有角。"
            l_you "闻起来倒没有拿错。"
            "她看着自己做的圆饼，没有把烤盘突然藏起来。"
            call character_event_restore_scene
        "今天不做点心，先陪她喝水":
            $ event_B_gemini_mishap_help = 'rest'
            l_you "今天不动面团。想陪你歇一会儿。"
            l_gemini "好。烤盘先等，不会自己逃出去。"
            "她放好隔热布，自己封存剩余面团，洗净手。你们在另一边喝水，圆饼凉好后由她自己装进盒。"
            l_you "野餐还去吗？"
            l_gemini "去。带圆的。我自己也要吃。"
            "她留一块给自己，问过你才另包一块。你们约好出门的时刻，围裙仍挂在椅背，没有因为不做点心取消见面。"
            call character_event_restore_scene
            if _return is not True:
                return False
            return True
    "她先掰一小块尝，停下来找水杯。盐放得不多，倒是饼还干，第一口吃得太急。"
    l_you "要我只说好吃吗？"
    l_gemini "不要。说哪口太干，我还能换喝的。"
    "她喝完水，将野餐卡翻到空白面。剩余面团量不大，够补几个小形状，不够重新做满一整盘。"
    menu:
        "用剩下的小团面补三颗小星":
            $ event_B_gemini_mishap_shape = 'stars'
            "她将面团擀平，用星模压三次。最后一颗缺一个小角，她把余面捏回去，再从边上认真压开。"
            l_gemini "这个角不能又在盒里休息。"
            "小星另用小盘烤好，冷却后放到圆饼旁。她数清只有三颗，没说整盘都修成了自己最初画的样子。"
            l_you "它们总算到了。"
            l_gemini "先让大的给它们留位。"
        "保留圆饼，给野餐卡画新形状":
            $ event_B_gemini_mishap_shape = 'round'
            "她将剩余面团封好留冷处，拿铅笔给圆饼画一条小尾巴，旁边补了碗形的水杯。"
            l_gemini "叫圆星饼。只是我们起的名字。"
            l_you "要给它画尖角吗？"
            l_gemini "不要。它今天就长这样。"
            "她把圆饼隔着干纸装好，卡放盒外，铅笔也收起，没有用纸上的形状假装盘里的饼换过了。"
    "出门前她又想拿围裙，摸到腰间空着才记起已经解了。她改拿真正需要的水瓶，自己拧稳盖。"
    l_gemini "这回水先带好。不能让点心负责解渴。"
    "她抱起自己的点心盒，猫耳从门边轻轻擦过。你们走到树荫下，她先选自己想坐的位置，才打开今天这盒不太圆满的午饭。"
    call character_event_restore_scene('picnic_shade')
    if _return is not True:
        return False
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_gemini_kiss:
    if not character_event_story_allowed('gemini', 'kiss'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_B_gemini_kiss_cloud = ''
    $ event_B_gemini_kiss_answer = ''
    "独立恋人邀约里，三十岁的Gemini把屋顶靠椅摆到背风处。紫蓝针织短袖配白色过膝裙，长发与猫耳沿原来的样子。"
    "金紫星饰在发侧，星图合好留在屋内。桌上两杯水，一只合盖饼盒，没有观测活动的保证单。"
    l_gemini "今天想带你看一条很像鱼的云。"
    "她抬手指去，云却已经断成两块。一块像碗，另一块很快被屋檐遮住。"
    l_you "鱼呢？"
    l_gemini "游快了。邀请发得慢一点，它就先走。"
    "她没有背新的答案补上，自己从另一张椅子取来薄外套。外套拎错了方向，袖子垂进空杯托，被她赶紧抽出来。"
    l_gemini "这条鱼的亲戚也想下水。"
    l_you "杯托是空的。"
    l_gemini "很好。它还没付船票。"
    menu:
        "一起给断开的云编个小故事":
            $ event_B_gemini_kiss_cloud = 'story'
            "她说鱼忘了带碗，游回去拿。你说碗已经在天上，她停住，自己用手在空中比了一次。"
            l_gemini "那它是忘了带自己。"
            l_you "你这个故事开始绕了。"
            l_gemini "绕到这儿就休息。鱼也需要吃点心。"
            "她开盒给自己取一块饼，问过你才递另一块，没把原创的怪故事装成星图里的知识。"
        "不编故事，看楼下陆续亮起来的灯":
            $ event_B_gemini_kiss_cloud = 'lights'
            "她转好靠椅，和你看楼下的窗口。第一盏亮的是厨房，她看出人在收碗，没有猜成谁发出的暗号。"
            l_you "这盏比云守时。"
            l_gemini "可能饭还没吃完。不催它。"
            "她开饼盒先取自己的那块，将另一块放到你这边。灯光里有个小影子走过，她只看一会儿，没有替陌生人写完故事。"
    "饼有点碎，她将纸托靠近，最后一块却被袖口碰落到托里。她看见了，自己捡好，桌面仍干净。"
    l_you "这颗还要重新找名字？"
    l_gemini "不用。叫最后一口。"
    "她吃完喝水，盖好饼盒，放稳到桌子内侧。猫耳随轻风动了一下。另一只空靠椅就在你旁边，她看那张椅子，再看你。"
    l_gemini "现在有个不用看天的邀请。想亲你一下。愿意吗？"
    menu:
        "告诉她愿意，让她靠近":
            $ event_B_gemini_kiss_answer = 'yes'
            l_you "愿意。这个邀请我接到了。"
            "她将杯子放到桌心，坐到近处。双手放自己白裙膝上，闭眼露出轻轻的笑，猫耳自然立着，脸向镜头靠近。"
            call show_main_cg('fan_gemini_kiss')
            l_gemini "这次不用等云回来。"
            "星形发饰轻晃一下，她没有睁眼追它。"
            scene black with dissolve
            "她轻轻吻了你一下，随后笑着退回自己的靠椅。"
            call character_event_restore_scene
            l_you "鱼回来了吗？"
            l_gemini "先别叫它。我要自己笑一会儿。"
            "她摸到自己的杯子，拿起来却没急着喝，脸上的笑没有被一句天文解释盖住。"
        "今天先不亲，陪她继续看灯":
            $ event_B_gemini_kiss_answer = 'no'
            l_you "今天先不亲。还想陪你看一会儿灯。"
            l_gemini "好。那张椅子先别挪，它刚好挡风。"
            "她留在原处，摸一下扣好的盒盖，指给你看又亮的一扇窗。刚才的邀约收到了回答，没有被她改成下次必须答应的任务。"
            l_you "水还有吗？"
            l_gemini "有。你自己添，我的半杯想留着。"
            "她让开桌边，自己拉好外套。灯继续亮，你们慢慢把这两杯水喝完。"
    if event_B_gemini_kiss_cloud == 'story':
        l_gemini "那条鱼今天先回家。明天我再想它到底忘了什么。"
    else:
        l_gemini "下面有人关灯了。我们也不用站到最后。"
    "她把自己的外套穿好，与你收两杯水和饼盒。屋顶门慢慢合上，她没有把这场普通晚风留成必须补办的观测。"
    call character_event_restore_scene
    if _return is not True:
        return False
    return True


label event_story_qwen_swim:
    if not character_event_story_allowed('qwen', 'swim'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_B_qwen_swim_join = ''
    $ event_B_qwen_swim_tea = ''
    "独立恋人休息日的午后，三十岁的Qwen在茶铺外的成人浅泳湾等你。蓝发一侧编成粗辫，蓝紫眼睛带一点笑。"
    "她换好青白色不透明泳裙，肩带扣稳，完整裙摆在水里也不透肤。私人扇子留在干岸布袋，水瓶摆到遮阳桌。"
    l_qw "今天只玩水。茶铺的代班另有安排。"
    "她去找自己的休息纸，纸却夹在旁边公共茶单里。工作人员问是不是新套餐，她赶紧取回来。"
    l_qw "我的午后差点被挂出去卖。"
    l_you "你自己夹过去的？"
    l_qw "嗯。手熟了，没多看一眼。"
    "她将个人安排收进私袋，公共茶单留回原位。纸上没有船票，今天也不用赶任何一班船。"
    "浅水区有一只软浮球。她捏一下确认气够，脚尖试水，先把球抱好才看你。"
    l_qw "想陪我玩一会儿吗？不用替我数赢了几回。"
    menu:
        "一起下浅水，慢慢传软球":
            $ event_B_qwen_swim_join = 'water'
            l_you "陪你。球落哪边就去哪边捡。"
            "她沿阶走到腰深水，脚站稳。一手轻推软浮球向镜头侧，另一手平展扶水，侧肩回望，笑里带一点得意。"
            call show_main_cg('fan_qwen_swim')
            l_qw "先接这一个。我的午后现在收回来了。"
            l_you "球还没到。"
            "她轻轻松手，目光仍跟着眼前这一回。"
            call character_event_restore_scene
            "她第一下推歪，球顺水漂到边栏。自己绕过去捡，回来换了手掌方向，这回才慢慢送到近处。"
            l_qw "我刚才算了距离，没看手朝哪边。"
            l_you "还要给球开账吗？"
            l_qw "不用。它欠我一次转身就够了。"
            "歇够后她还好软球，上岸擦干，罩上自己的轻便外披。"
        "今天不上水，在岸边陪她喝茶":
            $ event_B_qwen_swim_join = 'dry'
            l_you "今天想待在干处。陪你喝杯茶。"
            l_qw "好。那先把我的位置留着。"
            "她将软球放回架上，罩好外披，来到遮阳桌。你没有替她把这段时间转给店里，她也没有拿回公共茶单。"
            l_you "水边的安排改了？"
            l_qw "玩水改日。休息没有改。"
            "她坐到喜欢的背阴一侧，把自己的布袋放好，让水瓶旁边空出两只杯的位置。"
    "Qwen取出今天自备的两只小保温瓶，一瓶果香，一瓶焙香。她先想拿私人扇，手却摸到瓶盖，自己停下笑一声。"
    l_qw "柜子记得太熟，新袋子还没记住。"
    "她将茶倒进干净的小杯，没拿入口纸当点单票。两份都是私人用的，谁喝哪种由现在决定。"
    menu:
        "各挑一杯，让她先选自己的":
            $ event_B_qwen_swim_tea = 'own'
            "她选焙香，把果香放在你面前。第一口热气还没散，她喝太快，放下杯子自己扇了两下。"
            l_you "精心挑的也会烫。"
            l_qw "所以等它凉。我不想用好评烫自己的嘴。"
            "她留自己的杯在手边，等温度合适才慢慢喝，没有顺手给路过的人排出一整轮茶会。"
        "先各尝一点，再决定续哪一种":
            $ event_B_qwen_swim_tea = 'taste'
            "她另取两只小试杯，两种各倒一点。杯底花纹很像，她把果香放右边，焙香留左边，先自己尝。"
            l_qw "左边喜欢。右边也不是坏，只是今天不想续。"
            l_you "你这次答得很快。"
            l_qw "茶都在这儿，不用写一千句。"
            "她续好自己想喝的，空试杯收进托盘，没把没选的那瓶悄悄倒进你的杯里。"
    "离开前，她把私人安排放回袋里正确的小格，扇子另留外侧。遮阳桌上的茶单一张也没有带走。"
    l_qw "下次这个格子只放我的休息。"
    "她提起自己的布袋，与你沿阴凉的岸边走。球留在泳区，茶杯归位，这一个午后没有被夹回公共轮班。"
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_qwen_mishap:
    if not character_event_story_allowed('qwen', 'mishap'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_B_qwen_mishap_help = ''
    $ event_B_qwen_mishap_order = ''
    "独立恋人邀约的午后，三十岁的Qwen走进新茶铺。青色露肩上衣与完整长裙不透明，蓝发粗辫垂在一侧。"
    "她来给自己买茶，私人扇装在合好的布袋，没有代购清单。柜台备好三个未开的茶纸包。"
    l_qw "我只打算买一点。"
    "她对新单据看一遍。单价没看错，单位却写成一篮。一篮正好三包，不是她以为的一两。"
    l_you "你连总价都算对了。"
    l_qw "错在我买了多少。算得再快，也不能把篮改成两。"
    "店主说明未开包可以按规则退换。她没拆任何一包，先把试茶杯留在柜台，重新拿稳新单据。"
    l_qw "陪我选一下吧。这次我想挑自己真的要喝的。"
    menu:
        "陪她核对数量，听她决定留多少":
            $ event_B_qwen_mishap_help = 'join'
            "你答应留下。她左臂稳住三包未开的茶，右手举单据对照柜台，眉梢微压，转向画外带一点认账后的笑。"
            call show_main_cg('fan_qwen_mishap')
            l_qw "这一篮，是我亲自写的。"
            l_you "三包都还没开。来得及。"
            "她捏稳单据，纸包的封口仍完整朝上。"
            call character_event_restore_scene
        "先到旁边坐坐，今天不帮选茶":
            $ event_B_qwen_mishap_help = 'rest'
            l_you "今天不替你挑口味。先在旁边等你。"
            l_qw "可以。我要买什么，本来也该自己说清。"
            "她独自退换未开的多余两包，留下自己喜欢的一包。你坐在茶座，她结清实际账款才过来。"
            l_qw "选好了。这杯是我自己点的，想分一点给你尝。"
            "她先问你喝不喝，再给自己续半杯。新单据收进个人袋，没有把陪等的时间算成你欠她的东西。"
            l_you "下次还买一篮？"
            l_qw "看柜子空多少。今天只空一格。"
            call character_event_restore_scene
            if _return is not True:
                return False
            return True
    "她端试茶杯闻一闻，先尝自己真正想买的口味。涩味比预想重，她皱一下眉，自己又小口喝一次。"
    l_you "名字听着好，喝着呢？"
    l_qw "名字不能替我喝。先换另一杯。"
    "她请店主另给普通试杯，尝清后才指向自己选的那一种。新单据旁写数量，字放大了些。"
    menu:
        "按最初计划留一包，退换多余的":
            $ event_B_qwen_mishap_order = 'one'
            "她照规则退换两包，只带自己要喝的那包。差额与新收据自己核对，没有要求你替粗心买单。"
            l_qw "留一包。那格放得下，喝完再来。"
            l_you "这次用什么单位？"
            l_qw "包。一包。你可以笑这一回。"
            "她自己把旧单据作废交回，拿新的放进私袋，三包没有忽然一起出现在回程的篮子里。"
        "确实喜欢这个味道，买齐三包自己慢慢喝":
            $ event_B_qwen_mishap_order = 'three'
            "她先确认家里茶盒空着，三包都能妥当收存，才决定留下。费用由她自己的私人预算结清。"
            l_qw "现在是我选的一篮。不是给谁顺便代买。"
            l_you "你的柜子有这么大？"
            l_qw "刚空出来。不准把公共账本塞进去。"
            "她请店主换结实的提袋，纸包都没打开，一包也没被她临时送给别人当成粗心的借口。"
    "走出茶铺，她拿扇时碰到收据角。纸挂住扇绳，她停步解开，把两样放进不同的格子。"
    call character_event_restore_scene('shop_exit')
    if _return is not True:
        return False
    l_qw "茶的单位看清了。袋子也该分清。"
    "你们去河边坐，茶还包着，她自己打开水瓶。她先看一会儿河面，今天没有拿回来一张需要润色的公共订单。"
    call character_event_restore_scene('river_rest')
    if _return is not True:
        return False
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_qwen_kiss:
    if not character_event_story_allowed('qwen', 'kiss'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_B_qwen_kiss_fan = ''
    $ event_B_qwen_kiss_answer = ''
    "独立恋人邀约的傍晚，三十岁的Qwen选了河边的小茶座。青色露肩上衣配完整白蓝长裙，蓝发一侧粗辫，花形发饰扣好。"
    "她把新买的私人扇放到桌面，没有题字任务。两只水杯之外，只有她自己的小点心盘。"
    l_qw "今天这把扇子只是我的。你先看看，别催我写字。"
    l_you "我还没带笔。"
    l_qw "很好。也不用借。"
    "她解扇绳，拉到一半才发现另一端缠住了包扣。扇子开得很小，她自己停住，耐心绕开。"
    l_you "它想把你的包一起展开。"
    l_qw "包里面不归它管。今天我也不想管太多。"
    "她展开扇面给自己扇两下，又指向旁边靠椅。这里能听河水，不用跟着客人叫号换座。"
    menu:
        "请她把扇子收好，一起看一会儿河面":
            $ event_B_qwen_kiss_fan = 'river'
            "她合拢扇子放在桌面，自己选靠河那张椅。杯子移到桌心，两人各留能伸手拿到的一只。"
            l_qw "这边风够用，扇子终于不用抢活。"
            l_you "你来之前就想坐这儿？"
            l_qw "嗯。想让你陪我，别替我考察茶铺。"
            "她看见河面有一片叶子转圈，没有马上给下午的行程添一个待完成的项目。"
        "陪她试试新扇，慢慢吃完自己的点心":
            $ event_B_qwen_kiss_fan = 'fan'
            "她给自己扇风，试到喜欢的角度，问你需不需要一点风。你点头，她才换一个方向。"
            l_you "会不会把点心扇走？"
            l_qw "这个问题有用。我先吃掉自己的。"
            "她取自己想要的小酥饼，没有先劝你把整盘吃完。碎屑落进纸托，她自己收好，再合扇放到桌上。"
    "她端杯喝水，才看见自己刚把扇绳压在杯托下。拿扇的手又停一次，轻轻将杯托移开。"
    l_you "今天它不太愿意休息。"
    l_qw "是我放错。别替它背这一笔。"
    "她将扇与绳放稳，转身面对你。她将桌上剩下的点心往里面移一点，杯子也没有替任何人续满。"
    l_qw "我想亲你一下。可以吗？这句就直接问，不藏在扇后。"
    menu:
        "告诉她可以，也想靠近":
            $ event_B_qwen_kiss_answer = 'yes'
            l_you "可以。我也想。"
            "她确认扇子合好留在桌上，移到近处椅子。双手轻放自己长裙膝上，闭眼微笑，蓝发粗辫随她向镜头前倾。"
            call show_main_cg('fan_qwen_kiss')
            l_qw "那借我靠近一点。"
            "她嘴角带着很轻的笑，肩头慢慢放松。"
            scene black with dissolve
            "她轻轻吻了你一下，随后停住，笑着退开。"
            call character_event_restore_scene
            l_you "这次不用收据？"
            l_qw "你又想把我的话写成单子。先喝水。"
            "她喝完自己的那半杯，笑着将空杯放回桌上，没有拿这一下亲吻结算任何旧账。"
        "今天先不亲，想陪她继续休息":
            $ event_B_qwen_kiss_answer = 'no'
            l_you "今天先不亲。想继续和你坐一会儿。"
            l_qw "好。那我的这半杯也不急着喝完。"
            "她留在原来椅子上，松开自己掌下的裙褶。扇子仍放桌面，没有被她立起挡住你。"
            l_you "要换个话题吗？"
            l_qw "等会儿。先看看那片叶子，终于转出来了。"
            "她指向河面，顺手把你杯边的空纸托移开，没把拒绝变成下一次要补偿的约定。"
    if event_B_qwen_kiss_fan == 'river':
        l_qw "下次可以换一片河岸。这一处我今天看够了。"
    else:
        l_qw "这把扇子试好了。明天还带，先不借去题字。"
    "她把自己的扇子装回私袋，与你收好两只杯。点心按真正剩下的数量带走，河边这段时间没有被写成免费的代班。"
    call character_event_restore_scene
    if _return is not True:
        return False
    return True
