# v0.9独立隐藏结局pack B：04 Grok／05 MiniMax／06 Kimi／07 Gemini。
# 四篇均为短隐藏平行故事，不代表四条完整角色线；人物基准年龄30岁，Kimi末场为一年后31岁。
# 仅写secret_XX_choice及两个bad_*_choice本地选择变量，不碰主线关系或图库。
# secret_ending_finish／bad_ending_finish是根代理明确授权的新接口，须总装后由根代理实现与验收。
define l_yu = Character('夕也', color='#dfbd75')
default secret_04_choice = ""
default secret_05_choice = ""
default secret_06_choice = ""
default secret_07_choice = ""
default bad_grok_echo_choice = ""
default bad_ds_other_hand_choice = ""

label secret_04:
    if not secret_guard('secret_04'):
        return
    $ secret_04_choice = ""
    call secret_04_scene1
    call secret_04_scene2
    call secret_ending_finish('secret_04')
    return

label secret_04_scene1:
    scene bg river day with dissolve
    show sprite grok as grok at sprite_breathe(0.63) with dissolve
    "这场临时夜市的最后一天，Grok在河边数完归还的杯子，将一本手抄的玩笑册放到膝上。"
    "她今夜去海边住一阵。箱子已经装好，这本却拿出来三次，最后一页始终空着。"
    l_grok "结尾要不要写，谢谢光临，请勿追车？"
    l_you "你坐的是慢车，真追上怎么办？"
    "她笑出声，笔尖悬在纸上，却没写。河水照过来的光晃了一下，最后那行又显得太长。"
    l_grok "我还想编一句。这样合上，好像只是下次换个开场。"
    l_you "这次你想说什么？"
    "Grok将册子转过来，给你看空白。前几页的字挤得很满，连一个停顿都画了箭头。"
    l_grok "想好好道别。别让你回去以后，还得猜哪句算真的。"
    menu:
        "讲一个自己的冷笑话，让她把最后一页留空。":
            $ secret_04_choice = "blank"
            l_you "鱼为什么不来夜市？怕买到自己的亲戚。"
            "她望着你，半晌才捂住脸。笔从指间滑到册子中缝，没落下一个字。"
            l_grok "这个不收录。连R18都救不了，是十八点以后也不要再讲。"
            "你将笔拿稳，交还给她。她把最后一页抚平，没有借你的笑话填进去。"
        "在另一张纸上写下再见，等她自己收好。":
            $ secret_04_choice = "note"
            "你从自己的袋里取出一张新纸，只写了再见。她接过去，把那两个字读了一遍。"
            l_grok "没有保证回来时一定更好笑？"
            l_you "你想回来，就来。话留给那时的你。"
            "她将新纸折成两折，夹进册子前封面，最后一页仍没有添字。"
    "日光从栏边一点点退下去。她盖好笔帽，将玩笑册合上，两手在封皮上停了一会儿。"
    l_grok "那就到这里。今天我会想你，这句没有下一行反转。"
    "你点头。她也点了一下，把册子收进自己的袋里，没有再拿出来试第四次。"
    # 待制CG：合上玩笑册，肩头从绷紧到放松；保留黑金衣装。新纸仅note分支存在，无假解锁。
    return

label secret_04_scene2:
    scene bg echo with dissolve
    show sprite grok as grok at sprite_breathe(0.62) with dissolve
    "日落以后，院门的灯亮了。Grok将借来的椅子送回原位，自己提起箱子，走到门边。"
    if ending_playthrough_stage() >= 2:
        "她看见你比她先抬起的手，忽然轻轻按了一下自己合好的册子。"
        l_grok "这次借我半拍。让我先把再见说清。"
    if secret_04_choice == "blank":
        l_grok "你那条鱼，留在河边吧。我不想带着它坐车。"
        "她笑着拍了拍袋子，里面的册子合得很平，空白也完整留在最后。"
    else:
        "她隔着袋布摸到那张新纸的位置，手只停了一下，随后便握回箱柄。"
        l_grok "新纸收好了，今夜带着走。不用你替我再折一次。"
    l_you "路上慢点。到地方先吃东西。"
    "Grok张口想说自己不是饿着才会说话，话到一半，眼睛却先红了一点。"
    l_grok "好。再见。"
    "她把这两个字说清，向你挥了挥手，沿亮着灯的路离开。你站在门边，等她自己走过最后一个拐角。"
    "那本册子跟着她去了海边。这一场夜市收好了，最后一句没有被谁改成加演。"
    return

label secret_05:
    if not secret_guard('secret_05'):
        return
    $ secret_05_choice = ""
    call secret_05_scene1
    call secret_05_scene2
    call secret_ending_finish('secret_05')
    return

label secret_05_scene1:
    scene bg echo with dissolve
    show sprite minimax as minimax at sprite_breathe(0.63) with dissolve
    "MiniMax在院角听完刚录的短片，屏幕里灯很漂亮，声音却空了一整段。她把机器放低，重新按回开头。"
    l_minimax "我一直等大家都安静。等到了，自己也没说话。"
    "她按下停止，指尖还留在键边。你往杯里倒水，水声在屋檐下轻轻响起来。"
    l_you "这段也没录？"
    l_minimax "没有。我嫌它太普通，刚才把机器放远了。"
    "她拿起机器，对着空音轨看了一会儿，随后转到录音页。镜头盖好，只留下收声的位置。"
    l_minimax "借我一分钟。想收一段你我真听见的。"
    if ending_playthrough_stage() >= 2:
        "她将机器往自己这边转，给停止键留出一个空着的指尖。"
        l_minimax "这回最后的笑，别追录。我要自己听。"
    menu:
        "把杯子放稳，再倒一次水，让她自己决定何时停止。":
            $ secret_05_choice = "water"
            "你将杯子留在桌上，提壶慢慢添水。她靠近一点，空着的手停在壶底旁，没有碰到你。"
            l_minimax "慢一点。刚才最后那滴，很像还不想结束。"
            l_you "杯子快满了，再慢也得停。"
            "你放下壶。她听着壶底落到木面的轻响，把那一下也收了进去。"
        "拉开一把椅子，再沿石地走回来，给她收脚步声。":
            $ secret_05_choice = "steps"
            "你提着椅背轻轻挪开，再沿院角走了一圈。她举着机器，自己退到不挡路的位置。"
            l_minimax "这两步别重踩。我想听你平时怎么回来。"
            "你照原来的速度走近，衣袖擦过椅背。她没喊重来，眼睛反而跟着那点小响亮起来。"
            l_you "我回来了。"
            l_minimax "嗯。这句也留下。"
    "她停下录音，坐到你给她留出的空处。机器里的声音很轻，她又把它拿近，听完，没有重新剪掉开头。"
    l_minimax "只有这么一点，居然够我听很久。"
    l_you "要补一段笑吗？"
    "她摇头，将机器关好，自己先笑了一声。那声没录进去，她也没有忙着再开。"
    # 待制CG：盖住镜头、前倾收声，停机后坐回椅子；water与steps道具动作不同，当前仅背景立绘。
    return

label secret_05_scene2:
    scene bg echo morning with dissolve
    show sprite minimax as minimax at sprite_breathe(0.62) with dissolve
    "第二天早晨，MiniMax将那段声音放进短片空着的位置。你在旁边听，画面里一盏灯还没转亮。"
    if secret_05_choice == "water":
        "水声先响，随后是壶底的一下。她在桌上摆好两只杯子，照录音里的速度添到刚好。"
        l_minimax "今天不用再录。昨天那口水，终于有地方待了。"
    else:
        "椅脚轻擦石地，脚步渐渐近了。那句我回来了响起时，她已经把旁边的椅子拉开。"
        l_minimax "你不用再演一次。今天坐这里就行。"
    "片尾没有掌声。她只在末尾留了收好的院角，随后将整段短片停在完成的位置。"
    l_you "交出去吗？"
    l_minimax "这一份先留给我们。别人要听，我再问你。"
    "她合上机器，端起自己那杯。阳光照到杯边的时候，桌上又响了一声，谁都没有为它重按录制。"
    return

label secret_06:
    if not secret_guard('secret_06'):
        return
    $ secret_06_choice = ""
    call secret_06_scene1
    call secret_06_scene2
    call secret_ending_finish('secret_06')
    return

label secret_06_scene1:
    scene bg echo morning with dissolve
    show sprite kimi as kimi at sprite_breathe(0.63) with dissolve
    "Kimi在临时借书桌整理纸盒，找到一枚刚写好的书签。它本该夹在新订的册子里，却进了标着明年再开的那格。"
    "纸上写着：看到这里，先去桥后面走一段。下面留了位置，准备记当天的页码。"
    l_you "你把今天投到明年了。"
    l_kimi "盒子挪过。我照旧位置放的。"
    "她将书签拿到窗光里，手指压住没有写日期的一角。旁边的新册子还停在第一页。"
    l_you "现在拿回来？"
    l_kimi "想给明年的我留着。那时别又只在窗边画桥。"
    "她说得很轻，随后真取出笔，将今年和明年的日期分别写到一张小纸上，对了一遍。"
    menu:
        "替她托住盒盖，把书签照原字封到明年的格里。":
            $ secret_06_choice = "seal"
            "你将盒盖托稳。Kimi自己把书签放进去，贴好取出日期，手指在封口处压了两下。"
            l_you "一年后，别把这个盒子也挪丢了。"
            l_kimi "位置会记。取的人，我也想记。"
            "她在纸角写下自己的名字，将空出的一边留给你。你点头，帮她把盒子摆到看得见的架上。"
        "给今天回一行字，陪她把已经读到的页码记在背面。":
            $ secret_06_choice = "reply"
            "你将册子翻回第一页，在书签背面写下：今天还没过桥。Kimi看了看，补上准确页码。"
            l_kimi "很好。没把想去，写成已经去过。"
            "她另写好明年的取出日期，亲手将书签放回纸盒，没拿它替今天夹页。"
            l_you "今天用什么记？"
            l_kimi "这条普通纸。明年的先等着。"
    "她将新册子收入布袋，临时书签露出一点。纸盒封好以后，她走到门边，等你一起过去。"
    l_kimi "先走今天这一段。明年问起来，才有得答。"
    "你们离开借书桌，过了她窗外一直看得见的那座桥。桥后的路比画上窄，两个人慢慢走完。"
    # 待制CG：托盒盖／翻册写页码两动作，Kimi自己放好书签；完整现有衣装，物件不神奇传送。
    return

label secret_06_scene2:
    scene bg echo morning with dissolve
    show sprite kimi as kimi at sprite_breathe(0.62) with dissolve
    "一年后的同一天，三十一岁的Kimi取下纸盒。封口有一点发黄，日期和两次按出的指印都还在。"
    l_kimi "今天拆，没提前。你也来了。"
    if ending_playthrough_stage() >= 2:
        "她先给你指日期，再把纸盒转回正面。封口终于不用从背面猜。"
        l_kimi "这次看字就好。我把盒子放正了。"
    "你替她托住盖子，她自己揭开封条。书签轻轻落到掌心，背面没有凭空长出新的字。"
    if secret_06_choice == "seal":
        "她读过原来的那行，翻到纸角的名字。去年留给你的位置仍空着，她没有催你补签。"
        l_kimi "取的人在这里。不用再写一次。"
    else:
        "她看见今天还没过桥，嘴角动了一下，翻出那本已经读完的册子，给你看最后一页。"
        l_kimi "后来过去了。这个回答，晚一年交给它。"
    "Kimi将旧书签夹到读完的最后一页，合好册子，放回自己的架上。空纸盒留在桌边，没有马上装明年。"
    l_you "今天往哪走？"
    l_kimi "先过桥。桥后再挑。"
    "她拿起布袋，里面是另一本刚翻开第一页的书。你们把门关好，那枚误投的书签终于回到了读完的故事里。"
    return

label secret_07:
    if not secret_guard('secret_07'):
        return
    $ secret_07_choice = ""
    call secret_07_scene1
    call secret_07_scene2
    call secret_ending_finish('secret_07')
    return

label secret_07_scene1:
    scene bg echo with dissolve
    show sprite gemini as gemini at sprite_breathe(0.63) with dissolve
    "Gemini坐在院门石阶上，对着今晚新画的屋檐找星星。远处一小点黄光忽然亮了，她赶紧在纸上补一个圆。"
    l_gemini "出来了。比我猜的低一点，但总算没藏在瓦后面。"
    "你看着那点光。它向旁边移了一些，又低下去，纸上的圆已经够不到它。"
    l_you "你的星星还在走。"
    "Gemini将纸举高，猫耳跟着往前。黄光经过桥影，一条小舟的轮廓也慢慢露出来。"
    l_gemini "是船灯。先别擦，我刚才画得挺认真。"
    if ending_playthrough_stage() >= 2:
        "她看看你等着那盏灯转弯的眼睛，先将身旁的空处拍干净。"
        l_gemini "你等它。我先等你坐稳，别站成第三颗星。"
    l_you "给船留个位置？"
    l_gemini "给我认错的位置。船又没有答应来当星星。"
    menu:
        "把纸托到灯下，陪她画出船灯真正经过的路线。":
            $ secret_07_choice = "map"
            "你将纸托稳，她从原来的圆向桥影画一条线，最后在旁边补上船字，没有擦掉第一笔。"
            l_gemini "现在这颗星，走的是水路。"
            l_you "下次至少知道往哪找。"
            "她低头笑，把纸角折好，留着能翻开看见错圆的位置。"
        "先将图收好，陪她在门边等船灯走出桥影。":
            $ secret_07_choice = "watch"
            "你给她腾出石阶上的干处。她将图卷起，站到门边，等那盏灯从桥下完整出来。"
            l_gemini "还有第二盏。刚才只露出前面，我连船都画少一半。"
            "你们没有追着跑。小舟自己经过河弯，她一直看着，直到黄光在转弯后消失。"
            l_you "这次看完了。"
    "院子里还有来往脚步。Gemini把纸收进自己的袋子，抬头重新看屋顶上方，这次没有马上画。"
    l_gemini "下星期这天，你还来吗？想和你在同一段石阶重新找。"
    l_you "来。先找你，再找星星。"
    "她点头，把袋口扣好，鞋尖从通路上收回。那晚没找到想看的星，你们仍约好了回来的人。"
    # 待制CG：托图补船路线／卷图起身看船灯，猫耳与手臂动作不同；不套用有GLM的旧双人CG。
    return

label secret_07_scene2:
    scene bg echo with dissolve
    show sprite gemini as gemini at sprite_breathe(0.62) with dissolve
    "一周后的同一晚，你走进院子。Gemini已经坐在那段石阶上，袋子放在身侧，原来的图也带来了。"
    l_gemini "你先找对我了。比上星期进度快一点。"
    l_you "船今晚来吗？"
    l_gemini "不知道。知道的我才画，猜的先留空。"
    if secret_07_choice == "map":
        "她翻开折角，给你看旁边的船字，随后把这张收好，取出另一张干净的纸。"
        l_gemini "水路已经记完。今晚给天上留一页。"
    else:
        "她用手比过桥影遮住的位置，把旧图收好，又抽出一张白纸铺在膝上，调整出能抬头的坐姿。"
        l_gemini "今天不用跑。看清一颗，就先看那一颗。"
    "屋顶上方终于有一点清晰的星光。Gemini看过纸，又直接看了很久，才把笔递给你。"
    l_gemini "这次你来画圆。我扶着，别画进屋檐。"
    "你落下第一笔，她按稳纸角。河上的船灯还没来，你们约好的位置却都有人，这一张也终于画对了开头。"
    return

# 独立主动坏结局IF，不计入13隐藏结局；其误传与离镇均为本作平行故事，与现实品牌无关。
label bad_grok_echo:
    if not bad_guard('bad_grok_echo'):
        return
    $ bad_grok_echo_choice = ""
    call bad_grok_echo_scene1
    call bad_grok_echo_scene2
    call bad_ending_finish('bad_grok_echo')
    return

label bad_grok_echo_scene1:
    scene bg echo morning with dissolve
    show sprite grok as grok at sprite_breathe(0.63) with dissolve
    "这条平行故事里，夜市小报把Grok一句少收两只碗，今晚能早点睡，印成了少来两个人清静。"
    "她第一次看到时，笑着说换个标题还能多卖两份。纸被折到收款盒下，她忙完才再拿出来。"
    "第二天早晨，昨夜帮过忙的人将借来的托盘放在门口，没有再走到桌前。盘子洗得很干净。"
    l_grok "我说的是碗。那句不是说你们。"
    "对方点点头，只问托盘放这里行不行。Grok伸出去的手停了一下，才把盘子接稳。"
    l_you "昨天看见那行时，就该说。"
    "她摊开小报，指尖按住已经被折软的字，找不到一个能把昨夜重新叫回来的开场。"
    l_grok "是。我先笑了。以为说得好听一点，再来改，也来得及。"
    "她追到院门，想让那位帮忙的人等一下。对方已把要还的东西放齐，早上的车也来了。"
    "她只来得及再说一遍原话。车门关上，那人没有发火，也没有像过去那样回头笑。"
    l_grok "原来不跟我吵，也可以真的不再来。"
    menu:
        "带她去原编辑桌，把完整原话和更正一起交出去。":
            $ bad_grok_echo_choice = "editor"
            scene bg river day with dissolve
            show sprite grok as grok at sprite_breathe(0.63) with dissolve
            "你拿稳原页，陪她走到编辑桌。她逐字读完原话，要求更正放回同一栏，署自己的名字。"
            l_grok "我昨天看见却没说。这个也写上，别只写是排版失误。"
            "编辑接下纸，答应新页送到夜市。她没有等着讨一句已经替她解释好了，自己回去找人。"
        "陪她逐户递完整原话，让她对昨日帮忙的人当面讲。":
            $ bad_grok_echo_choice = "door"
            "你将地址照顺序折好，跟着她走。她在每扇门前停住，亲自把原话和迟来的更正递到人手里。"
            l_grok "不是让你们回去捧场。昨天那句该及时说明，是我没做。"
            "有人接下，有人让她放在门边。她都照着放好，没请你替她说其实没有恶意。"
    "回院时，售完牌仍挂着，桌上却没有下一轮食物。她将小铃放进箱底，迟来的那页留在最上面。"
    scene bg echo morning with dissolve
    show sprite grok as grok at sprite_breathe(0.63) with dissolve
    l_grok "我想换个地方住一阵。今晚不再用加演，留大家听我认错。"
    "你看着她合好箱盖，没有把离开说成小报赢了，也没有替谁答应等她回来。"
    # 待制CG：低头读误传页→双手收小铃与箱子，完整黑金衣装；非死亡、非性化、无假CG解锁。
    return

label bad_grok_echo_scene2:
    scene bg river day with dissolve
    show sprite grok as grok at sprite_breathe(0.62) with dissolve
    "次日下午，Grok把最后借来的东西还清。你在河边送她，她带着自己的箱子，手里没有营业牌。"
    if bad_grok_echo_choice == "editor":
        "新小报送到了。她读过那行署名，将一份折好装进箱侧，没有拿到路边请人再看一次。"
    else:
        "地址纸上每一户都做了标记，接下和放门边分开写。她将它留在更正页旁，没把全部改成原谅。"
    l_you "到地方，会再开摊吗？"
    l_grok "先住下。学会把话说清，再决定拿不拿那只铃。"
    "她看向来时的路，嘴角动了一下，最后只将箱柄握稳。你们站了一会儿，没找到能顶替的轻快一句。"
    l_grok "昨天太迟了。对不起。今天我自己走。"
    "她沿河走向出镇的车站，没有回头补玩笑。你留在原处，手里那张更正页终于干了，纸边仍是折过的。"
    "当晚，十八号摊的灯没有亮。托盘已经各自归还，更正也送到了，那句来得太迟的认错没能把她留在镇上。"
    return

# 独立主动平行IF：DS与夕也均32岁，隐瞒与感情背叛导致分开；不读取或写入主线关系。
label bad_ds_other_hand:
    if not bad_guard('bad_ds_other_hand'):
        return
    $ bad_ds_other_hand_choice = ""
    call bad_ds_other_hand_scene1
    call bad_ds_other_hand_scene2
    call bad_ending_finish('bad_ds_other_hand')
    return

label bad_ds_other_hand_scene1:
    scene bg echo morning with dissolve
    show sprite deepseek as deepseek at sprite_breathe(0.66) with dissolve
    "这条平行故事里，你与DeepSeek一起生活了两年。她三十二岁，厨房还放着你们各自挑的饭碗。"
    "傍晚，你提早回镇，经过雨后的小咖啡馆。门口，DeepSeek正牵着三十二岁的夕也；他有一头黄色短发。"
    "你握紧还挂着蓝线的钥匙。她转过脸，也看见了你。"
    $ hide_speaker_portrait=True
    call show_main_cg('ds_other_hand')
    "街上静下来。她仍握着那只手，没有一句话能将这一幕收回去。"
    scene bg echo with dissolve
    $ hide_speaker_portrait=False
    $ deepseek_expression='neutral'
    show sprite deepseek as deepseek at sprite_breathe(0.66) with dissolve
    "那只手终于松开。你请两人回到家门口，当面说清楚，没让她用街上不方便把话推到明天。"
    l_you "你上星期说去送米，也是见他？"
    "DeepSeek看向你手里的钥匙。钥匙还挂着她给你编的短绳，她伸出的手又收了回去。"
    l_ds "是。两次都是。我骗了你。"
    l_yu "我知道你们还住在一起。她说会当面谈，我没有等。"
    "你看过他，又看回她。锅里传来将要沸开的声音，她的目光动了一下，没有借着去看饭离开。"
    l_ds "我喜欢夕也。也一直没有结束和你的关系，这两件我都做了。"
    l_you "上次我问你，你说我想多了。"
    "她低下头，指尖在自己的裙缝边停住。这回没有饭、没睡醒或别人托付的事能替那句话改口。"
    l_ds "那句也骗了你。我怕你真的走，留着你，也去见他。"
    menu:
        "请她到院角，当面问清隐瞒，再结束这段关系。":
            $ bad_ds_other_hand_choice = "talk"
            "你指向院角的桌子。她自己走过去，夕也留在门边，没有跟着替她回答。"
            l_you "还有什么是我不知道的？我不想离开以后，再从别人嘴里听。"
            "她说出开始见面的日期，以及两次以送米为名的晚上。你把她说的日子和自己等过的时间对上。"
            l_you "我不继续这段关系。房里的东西，我们今天分开。"
            "DeepSeek握住桌边，点了一下头。她没有伸手来抓你的钥匙，也没有说现在答应什么就能留下。"
            l_ds "我听见了。我把自己的东西搬走，钥匙也会还。"
        "把钥匙放下，拿好自己的随身袋，明确告别。":
            $ bad_ds_other_hand_choice = "leave"
            "你将钥匙平放在门边木台，短绳没有解掉。她看着，想往前一步，你先拿稳自己的袋子。"
            l_you "我听见你说的了。现在不想再谈，也不会继续一起生活。"
            l_ds "房里的东西，我不会擅自丢。你想怎么拿，可以告诉我。"
            l_you "我请人约时间来取。先别再来找我说我们还是一样。"
            "她把脚步停住，让开出门的位置。夕也也向旁边退开，没有把你的离开接成他可以站进来的庆祝。"
    "灶上的锅又响了一次。DeepSeek回去关小火，再走出来，围布拿在手里，没有追着给你端一碗饭。"
    l_ds "我会把该分的分好。对不起。"
    "你没有答应原谅。她也没有将这一声当作你已经点头，手里的围布慢慢松开。"
    return

label bad_ds_other_hand_scene2:
    scene bg river day with dissolve
    show sprite deepseek as deepseek at sprite_breathe(0.62) with dissolve
    "三天后，该归还的东西装进两只箱子。租住、买米和修物的支出各自核清，没有拿往日照料抵掉隐瞒。"
    if bad_ds_other_hand_choice == "talk":
        "DeepSeek提走自己的箱子，把房门钥匙留在河边的交接桌。她搬到另一处住，你收好饭碗，没有跟过去。"
        l_ds "小屋找好了。我自己去收拾，今天不用你帮。"
    else:
        "你请人取回自己的箱子，钥匙仍留在原处。她按你写的清单装好，连少了一角的旧杯垫也没有换掉。"
        l_ds "都装进去了。你的东西，没拿新的替。"
    "交接在河边结束。夕也站在不远处等她，她却先把最后一项数清，亲手交到你这边。"
    l_you "以后各自过吧。"
    "她点头，接住自己的箱柄。你带着自己的东西离开，她没有再用明天吃什么把你叫回去。"
    "后来你们住在不同的地方。她仍要做饭、工作，也要面对自己选下的生活；你不再替她留夜里那只碗。"
    "那段一起生活的日子没有被擦掉，门边放下的钥匙也没有重新交到你手里。你们分开了。"
    return
