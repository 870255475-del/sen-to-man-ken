# Claude 第五章候选 / 请别替我道歉 / 第十二日 / 全员成年三十岁。
# 仅既有scene/show、l_cl/l_you与sprite_breathe；无CG、关系或整线完成写入。

default persistent.main_claude_ch05_seen = False
default claude5_has_ch04 = False
default claude5_previous_response = ""
default claude5_previous_repair = ""
default claude5_previous_paid = 0
default claude5_boxes_returned = False
default claude5_next_map_kept = False
default claude5_invitation_made = False
default claude5_spoken_over = False
default claude5_first_response = ""
default claude5_repair_mode = ""
default claude5_public_answer_given = False
default claude5_local_correction_done = False
default claude5_absent_listener_pending = False
default claude5_evening_cancelled = False
default claude5_note_delivered = False
default claude5_novel_chapter = 2

label claude_ch05:
    $ claude5_has_ch04 = getattr(persistent, "main_claude_ch04_seen", False) is True and getattr(renpy.store, "main_last_chapter", "") == "claude_ch04" and getattr(renpy.store, "claude4_response", "") in ("stand", "press") and getattr(renpy.store, "claude4_repair", "") in ("reprint", "overlay") and getattr(renpy.store, "claude4_old_print_cost", 0) == 18 and getattr(renpy.store, "claude4_new_print_cost", 0) == (18 if getattr(renpy.store, "claude4_repair", "") == "reprint" else 6) and getattr(renpy.store, "claude4_own_print_paid", 0) == (9 if getattr(renpy.store, "claude4_repair", "") == "reprint" else 3) and getattr(renpy.store, "claude4_lost_wage_repaid", False) is True and getattr(renpy.store, "claude4_claim_withdrawn", False) is True and getattr(renpy.store, "claude4_sites_changed", 0) == 4 and getattr(renpy.store, "claude4_meal_taken", False) is True and ((getattr(renpy.store, "claude4_response", "") == "stand" and getattr(renpy.store, "claude4_private_page_shared", False) is True) or (getattr(renpy.store, "claude4_response", "") == "press" and getattr(renpy.store, "claude4_private_page_shared", None) is False)) and getattr(renpy.store, "claude4_novel_chapter", 0) == 2
    $ claude5_previous_response = getattr(renpy.store, "claude4_response", "") if claude5_has_ch04 else ""
    $ claude5_previous_repair = getattr(renpy.store, "claude4_repair", "") if claude5_has_ch04 else ""
    $ claude5_previous_paid = getattr(renpy.store, "claude4_own_print_paid", 0) if claude5_has_ch04 else 0
    $ claude5_boxes_returned = False
    $ claude5_next_map_kept = False
    $ claude5_invitation_made = False
    $ claude5_spoken_over = False
    $ claude5_first_response = ""
    $ claude5_repair_mode = ""
    $ claude5_public_answer_given = False
    $ claude5_local_correction_done = False
    $ claude5_absent_listener_pending = False
    $ claude5_evening_cancelled = False
    $ claude5_note_delivered = False
    $ claude5_novel_chapter = 2
    call claude05_scene1
    call claude05_scene2
    call claude05_scene3
    call claude05_scene4
    call claude05_scene5
    $ persistent.main_claude_ch05_seen = True
    return

label claude05_scene1:
    $ chapter = "Claude 第五章 / 01 · 箱子今天要走"
    scene bg echo morning with dissolve
    show sprite claude as claude at sprite_breathe(0.65) with dissolve
    "第十二日九点五十分，东廊桌上只留一个工作夹。Claude将四枚木夹排在右边，摸到第五枚，又把它放回盒里。"
    l_you "第五个箱子不来？"
    l_cl "四页。箱子在干果摊，我不收箱子。"
    "她把小本子转到今天：十点到十点半，装箱单四页。下一页另写第十三日九点到九点二十，鞋铺一张地点图，四处待核。"
    "她用窄纸盖住来人的姓名，只将两个约时露给你看。两份纸之间没有追加一条顺便，也没把明早的图划到今天。"
    l_you "明天那张比今天少。"
    l_cl "有四个地点。不拿页数当走路的长度。"
    "十点整，干果摊的冯姐带来四页。她负责装箱，Claude核对箱号与袋数；你坐在另一侧，将翻过的纸按顺序接住。"
    "第三页的一行写着每盒两袋，末尾又有散袋四包。Claude指尖停在总数旁，请冯姐把盒子和散包分开说，没将四包直接塞进每盒。"
    l_cl "这四包另放哪儿？"
    "冯姐说明它们放进最上层，用不同颜色的小纸扎住，单上缺的是另装两字。她自己补好，又指给你们看。"
    "你翻到第四页，Claude要在回条上写日期。笔下先落了十三，她看见旁边今天的格子，立刻将最后一个字划掉。"
    l_you "箱子想住一晚？"
    l_cl "我刚看了明天的图。不是箱子申请的。"
    "她重写十二日，把错的一小条折到背面。冯姐收回四页，逐枚松开木夹；最后一枚夹住的只有空回条，没有第五份任务。"
    "十点二十九分，冯姐将纸装进自己的硬夹。她说午前就去装箱，不用Claude跟过去再数一遍；Claude起身送到廊口，手里没有拿工作本。"
    $ claude5_boxes_returned = True
    $ claude5_next_map_kept = True
    "回来后，她拿起蓝封的《第七位嫌疑人》。自己的名字仍写在包书纸上，窄签停在第二章，勺柄的绳结还没走出那几页。"
    if claude5_has_ch04:
        if claude5_previous_repair == "reprint":
            "工作夹内留着新告示的副样，九元那张收条已经记过。她将它们合好，没有让剪去错段的旧纸回到桌上。"
        else:
            "工作夹内留着更正条的副样，三元那笔已经记清。昨天覆贴时用的布已晾干，她把布收进公用盒，没拿来擦书封。"
        if claude5_previous_response == "stand":
            l_you "昨天那双鞋穿走了，今天还回来吗？"
            l_cl "我想读到它回来。不是替鞋铺追货。"
        else:
            l_you "今天这段也先自己读？"
            l_cl "白天先看。晚上想念给你听。你昨天那句，我还记着。"
    else:
        "她把公共工作夹收入柜里，告诉你这本是自己买的小说。第二章还没读完，书中的人把汤勺拿去量鞋，直到现在也没还。"
        l_you "你先留了哪位嫌疑人？"
        l_cl "借勺子的。人没走，勺子先走遍了。"
    "她找一张干便纸，写上今晚七点到七点半，东廊。写完没有塞进日程本，而是先将那行转向你。"
    l_cl "你今晚愿意听吗？我想把这几段念完。"
    l_you "七点来。带一个能听完的耳朵。"
    l_cl "两个都带。风会替你用掉一个。"
    $ claude5_invitation_made = True
    "她从柜里取出两只干净座垫，自己先坐了一下，又将厚些的留在另一把椅子上。你伸手摸，她按住垫角，没让你把它抱走。"
    l_cl "晚上用。免得你听到第二段，就站起来找别的凳子。"
    l_you "你还试了我的椅子？"
    l_cl "硬。门房不用坐，你要坐。"
    "你接过便纸。她翻看小说两行，想到门房终于拿了尺，嘴角先动；又看见他用尺刮锅底，没忍住将书抬高了一点。"
    l_you "量鞋用勺，做饭用尺。他缺的到底是哪一件？"
    l_cl "有人先让他把锅放下。别借我的本子。"
    "她把书合好，纸签留在原处。十点四十分，她去取自己点的豆沙饼，问清你的那份是咸的，带走两份各自的零钱。"
    return

label claude05_scene2:
    $ chapter = "Claude 第五章 / 02 · 没轮到的那一句"
    scene bg echo morning with dissolve
    show sprite claude as claude at sprite_breathe(0.65) with dissolve
    "午饭后一点二十分，书摊的陶姐来东廊拿活动用的空杯，顺手帮着把一只倒扣的杯子翻过来。"
    if claude5_has_ch04:
        "她昨天参加过共读，公用短文的哪一页要归还，Claude与她直接点清。"
    else:
        "她经营桥边书摊。Claude从公用夹里找出借用单，让她照着数杯，没有让你代答之前办过什么活动。"
    "Claude把空杯的数量点清，自己的蓝封小说放在臂弯里。陶姐看见礼帽封面，笑着问今天傍晚能否去书摊读十分钟，给街坊解解乏。"
    "陶姐将一页活动便表放在台上，说只是一问，不愿意就不添名字。她把笔握在自己手里，等Claude回答。"
    "Claude将书封贴回掌心，吸了一口气。你看到她停的那一下，抢先把话接过去。"
    l_you "对不起，她上午赶箱子赶累了。今天就不读了，明天下午我带她来。"
    "陶姐低头记下明天下午。旁边来借杯的姚师傅已提着提篮出门，隔着柱子应了一声说那就明天来听，脚步没有停。"
    "Claude抬起头。她没有接住你的对不起，手指却将蓝封压出了一个浅弯，你才发现她那句话一直没说出来。"
    $ claude5_spoken_over = True
    $ claude5_absent_listener_pending = True
    l_cl "箱单十点半已经交了。我刚才还没答。"
    l_you "我只是怕你又被拉过去。"
    l_cl "所以你给我另约了明天？"
    "陶姐把笔尖从纸上拿开，说可以擦掉。Claude看着你，没顺势承认是自己累，也没有让你的抱歉替她点头。"
    l_you "晚一点去，总比当场拒绝难看。"
    "这句说完，你看见她将书从两人之间收回胸前。她的肩没有躲开，目光也没换到陶姐那边，先让你听清。"
    l_cl "我准备好了怎么拒绝。你没让我说。"
    menu:
        "当场撤回自己擅许的明日，让她回答。":
            $ claude5_first_response = "correct"
            l_you "明天下午是我擅自说的。别记那一行，让她自己答。"
            "你往桌边退半步，手没有去替陶姐擦纸。Claude将蓝封的书放到自己的袋里，这才转过来。"
            l_cl "我暂时不在书摊念这本。刚才想说的就是这句。"
            "陶姐划掉明日下午，问活动用的一页短文是否照常归还。Claude从公用夹里取出那页，请她数完空杯再一起拿走。"
            l_cl "这张是活动的。那本不是。你想办下一场，另找时间问我。"
            "陶姐点头，说私人书不必拿来凑场。她见你伸手想再解释，先将公用那页收好，给Claude留出放布袋的地方。"
            $ claude5_public_answer_given = True
            l_you "我刚才说她累，也不是她告诉我的。"
            l_cl "听见了。还有一句晚去比较好看，我们出去说。"
            "她自己选了离门口远的廊柱。你跟过去，陶姐没有被留下代替你们劝和，那一行也没有换成下次待定。"
        "先离开人多的廊口，不继续替她解释。":
            $ claude5_first_response = "retreat"
            l_you "我先不说了。你愿意换个地方说，还是在这里？"
            "她看了一眼来借杯的人，捏紧布袋带子，先向陶姐伸出空手。"
            l_cl "我想先离开一会儿。那一行别往外传，我下午回来答。"
            "陶姐将便表折起，收回自己袋里，说等她本人回来，不把明日抄到书摊的小黑板。Claude将公用短文交给她，未交私人小说。"
            "你没有补上她需要休息，也没催陶姐先把名字留住。Claude走到后廊那根柱子旁，直到布袋落稳，才回头看你。"
            l_cl "这里没有别人在等。刚才那句，你想让我怎么接？"
            l_you "不用接。明天下午不是你的约定。"
            "她没立刻松开带子。前廊还有空杯相碰的声音，你看向那边，她将书袋放到自己身侧，没有回去替你圆场。"
            l_cl "那先别再替我添加原因。陶姐那里，我还要自己答。"
    return

label claude05_scene3:
    $ chapter = "Claude 第五章 / 03 · 今晚不共读"
    scene bg echo morning with dissolve
    show sprite claude as claude at sprite_breathe(0.65) with dissolve
    "一点三十五分，后廊的茶盘只剩两只倒扣的空杯。Claude将布袋搁到凳上，自己站着；你没把另一把凳推到她腿边。"
    l_you "我不该答应明天。但那句道歉，是想让你少为难。"
    l_cl "你替我说累，替我拒绝今天，再替我答应明天。哪里轮到我？"
    "她将手掌摊在空杯旁，三个指尖依次碰过桌面。碰到第三下，她停住，指尖没有替你的话又添出第四项。"
    l_you "那我该当面说，你想留着这本自己读？"
    l_cl "不该。那句话也让我说。"
    "你想起她吸气时的样子。书没有藏，她只是准备把最普通的一句不愿意，完整交给提问的人。"
    if claude5_previous_response == "stand":
        l_you "昨天你把书转给我，我以为已经能帮你接几句。"
        l_cl "我给你看绳结。没把明天下午夹在那一页里。"
        "她从布袋取出蓝封，指腹压在已经展平的包书纸上。昨天给你看的地方没有被撕掉，她却没将书再转向你。"
    elif claude5_previous_response == "press":
        l_you "昨天你说想自己读，我怕今天再当众拒绝，让人觉得你不愿意来。"
        l_cl "那就是我不愿意来。你昨天听过，今天却给它换了一个累。"
        "你没有拿更正告示的手工抵掉这句话。她将书收回臂弯，等你把目光从那袋工作纸移回来。"
    else:
        "她将小说拿出来，翻到包书纸上的名字，再合好。那两个字给你看了片刻，没被改成公用借读。"
        l_cl "我选这本，想找人听。不是找人替我向别人介绍。"
    l_you "我刚才怕场面冷下来。你说之前，我先把它填满了。"
    "Claude拉出凳子坐下，袋子仍留在另一侧。她望着空杯，拇指擦过杯底的水印，没有急着替你挑一个好听的动机。"
    l_cl "陶姐在等我。那几秒没有坏。"
    l_you "后来坏在我这里。"
    l_cl "嗯。你现在不用再替这句道歉找一个借口。"
    "你将早晨写七点的便纸拿出来，准备问是否还照旧。她伸出手，先问你能否把那张还给她。"
    "你放到桌上，她拿起笔，将今晚七点到七点半划去，只留下东廊两个字。小说的位置签仍留在书里，没有随时间一起抽掉。"
    l_cl "今晚不共读了。我想自己看。"
    $ claude5_evening_cancelled = True
    "她将早晨试过的厚座垫叠好，收回柜里。自己的那只仍留着，空出来的椅面比刚才亮了一块，你也看见了她早晨特意抚平的垫角。"
    l_you "是我把你原本想念的也弄没了。"
    l_cl "我还想念。今天不想一边念，一边猜你会替我接哪句。"
    "她将划过的时间给你看清，折好收进自己本子。你没有拿出另一张空纸马上约后天，也没有靠近去碰她拿笔的手。"
    l_you "好。七点我不来占你的椅子。"
    "Claude把笔放回笔套。你们之间那只凳子没有被她推远，她却将书放在自己能托住的一侧，目光仍留在页边。"
    l_cl "我现在有点生气。别替我说不是。"
    l_you "不说。"
    "风掀起公用茶盘的垫纸，你伸手压住。她看到纸角稳下来才拿回空杯，把杯口向上，不让剩余的水流到小说旁。"
    l_cl "这张可以压。它不会另约明天。"
    "你将手留在垫纸上，笑意只到嘴边。她没跟着笑，低头把杯子排开一寸，终于喝了一口自己倒的水。"
    return

label claude05_scene4:
    $ chapter = "Claude 第五章 / 04 · 你负责哪一句"
    scene bg echo morning with dissolve
    show sprite claude as claude at sprite_breathe(0.65) with dissolve
    "三点四十分，Claude合上读到一半的第二章。门房找到了尺，穿走的鞋还没回来；书签只挪过半页，猜的那个人仍留着。"
    "她到前廊问陶姐是否还在书摊，拿回一张干净便纸。你正收杯，听见她叫你的名字，先将手里的杯子放稳再过去。"
    l_cl "陶姐那边，我要把自己的回答交过去。你也要把擅许的那一句撤掉。"
    if claude5_first_response == "correct":
        l_you "明日下午那行已经划掉。还有我替你说累。"
        l_cl "对。别把我不愿意读，说成等我睡一觉就会去。"
        "她将笔推到空纸中央，没有再写一份新的时刻。陶姐听过她的拒绝，留下的误会仍是你加上的缘由。"
    else:
        l_you "我跟你过去时，把话停在我的那一句。"
        l_cl "她还没听完我的回答。纸上也不能只删掉你，不留我。"
        "她摊开便纸，写下今天与明日的公开朗读都未答应，私人小说不作活动稿。她只写自己要说的，没有替你署名。"
    menu:
        "陪她回书摊，当面撤回自己说过的话。":
            $ claude5_repair_mode = "return"
            l_you "我跟你去。我撤我的话，你答你的。"
            l_cl "到了先别抢着进门。陶姐要是问我，你就等一下。"
            "四点整，你们到书摊取杯的位置。陶姐将折起的便表拿出来，挪开一摞空纸，为两人留出可以站着说话的地方。"
            if claude5_first_response == "correct":
                "那行明日下午已有一道横线。陶姐先问Claude是否愿意把短文的公用夹带回，你没有将她的工作问话接到自己嘴里。"
                l_cl "我带。私人那本仍不在这场念，不是等我休息后补一晚。"
                "她把公用夹收好才看向你。你等到这个空档，将上午工作已经结束、所谓赶累是自己猜的说清。"
            else:
                "陶姐的笔停在未划的那一行。Claude把自己的便纸放到旁边，先将不愿意公开念这本的回答说完。"
                l_cl "今天不念，明日也没答应。请划掉，不转成另约。"
                "陶姐划去时刻，将便表转给她看。你等Claude确认过，才说明那一行是自己未经她同意许下的，不能算她临时失约。"
            $ claude5_public_answer_given = True
            l_you "说她累，是我猜的。明天下午也是我添的。她没托我答这些。"
            "陶姐听完，说空杯照旧归还，不会为了少一段私人朗读收别的费用。她将那行划得很清楚，没在旁边留一个等她点头。"
            "Claude自己提公用夹，你提还回来的空杯。回程你差点又要问她是不是消气，看到她正理袋带，把那句话留住了。"
        "送她亲写的更正，另署自己那句，不拆封代念。":
            $ claude5_repair_mode = "letter"
            l_you "我送纸。你的回答你写，我另外说明是我擅许的。"
            l_cl "可以。我今天不想再挤到柜台前面。你等她当面收下。"
            "Claude将自己的回答写齐：私人小说不作活动朗读，今天不参加，明日也未约。你在另一张纸写明自己擅加时刻和疲累缘由，署了自己的名字。"
            "她读过你那张，指向只是一时误会几个字。你把那半句划掉，留下是谁说了什么，没有让陶姐猜你在替谁解释。"
            if claude5_first_response == "correct":
                l_cl "她已经听过我的不愿意。你这张别把它改成身体好些就来。"
                "你将撤回缘由写完整。她把两张一起封好，私人书仍留在自己膝上，没有给你附一段拿去逗笑的正文。"
            else:
                "她将自己的那张放在上面，第一句就是不在书摊念。封口前，她又看了一遍，没有把它换成推迟一天。"
                l_cl "这是我下午回来答的方式。陶姐若还问时刻，你只说没有另约。"
            "四点整，你到书摊，将封好的两张交给陶姐。她当面拆开，读过Claude署名的回答，再看你自己那张，划掉明日下午。"
            "你等她收好，没有借递纸念出小说里哪一段，也没有补一个Claude刚才笑过所以没生气。回去时，两只手只提归还的空杯。"
            $ claude5_public_answer_given = True
            $ claude5_note_delivered = True
            l_you "陶姐当面看过，划掉了。她收的是你写的回答。"
            l_cl "好。纸没有替我增加一晚。"
    $ claude5_local_correction_done = True
    "姚师傅下午去了河外送杯，今晚不回书摊。陶姐说自己不会再转述明日有朗读，但他午后已经听见的那一句仍须另告知。"
    l_cl "明天他回来，我亲口说。地点图先照九点到九点二十做完。"
    "她在工作本里添一条姚师傅，未写要你代答。九点那格保持原样，旁边没有为私书补上下午几点。"
    "你把自己那张错许的时刻记在便纸上，不塞进她的小说。她看见，没替你折边，也没因此把今晚划掉的时间重新打开。"
    return

label claude05_scene5:
    $ chapter = "Claude 第五章 / 05 · 还剩自己的半小时"
    scene bg echo with dissolve
    show sprite claude as claude at sprite_breathe(0.65) with dissolve
    "傍晚六点二十分，Claude将公共工作夹锁进干柜。第十三日地点图的空位还留着，装箱四页已随冯姐走，桌上没有借来的任务等她补一晚。"
    "晚饭是她自己选的一碗拌面。你拿自己的饭坐在另一张小台，没将共读取消当成两人必须连吃饭也回避。"
    "她拌面时，将长面绕过筷尖，转到一半散了两根。她看了一眼你那边，没有叫你接手，拿汤匙托住，慢慢吃下去。"
    l_you "尺子先不借给你。"
    l_cl "我的面没有差一寸。"
    "她说完仍低头吃，没将玩笑延成一段和好的宣告。你把面碗外侧的一点水擦净，自己的那份也吃到了碗底。"
    if claude5_repair_mode == "return":
        "归还的空杯已摆进公用盘。你记得在柜台前等她答完的那几秒，此刻也没有先把她看书时的停顿接成一个问题。"
        l_cl "下午你等过了。我知道。今晚还是照刚才说的。"
    else:
        "她写更正时留下的封纸边被收进废纸盒。你伸手去拿自己的饭钱，不再将一只空纸袋当作替她捎晚间邀请的机会。"
        l_cl "陶姐收过纸了。今晚不需要再帮我送什么。"
    l_you "七点留给你。桌上的另一只杯，我洗好放回公用盘。"
    "Claude将自己的杯子留在手边，点头让你收走那只。你拿杯时，布袋带子勾到凳沿；她按住自己的袋，没有让小说跟杯子一起被提走。"
    l_cl "这件不归盘子。"
    l_you "看见了。我松手，你自己拿。"
    "你松开带子，她将布袋挪到另一侧。蓝封没有掉地，她打开包书纸，摸平先前被自己攥弯的那一角，眉头才松开一点。"
    if claude5_first_response == "correct":
        l_you "在陶姐面前撤了明日，不等于我没抢过你的话。"
        l_cl "对。现在让我把面吃完。它也快冷了。"
    else:
        l_you "下午交回了你的回答。午后离开时没说完的，我记着。"
        l_cl "你记自己那句。我的我还留着。"
    "你没有去看她封里写过的猜测。她将窄签挪开，重读门房刮锅那一行；笑声短短漏出来，抬眼时看见你还在收饭袋。"
    l_you "不用为了我停。"
    l_cl "没停。刚才那句太响。"
    "她把书往近处托一点，给自己的杯子留出地方。书里那个借勺的人仍在她的嫌疑名单上，第二章也还没读完。"
    "六点四十分，你将洗净的杯子放回盘子，向她道别。没有把凳子搬到她旁边，也没替七点另找一个顺路回来的理由。"
    l_you "明早那张图，若需要我拿空夹，等你自己问。"
    l_cl "空夹就在柜里。你不用先替它来。"
    "你点头走到廊口。她叫住你，等你回头，指了指桌外你忘拿的饭袋，没有借这一下把半小时又递出来。"
    l_cl "这个是你的。别把午饭也留给我复读。"
    "你回来拿好自己的袋子，再离开。七点，Claude将那张划过的便纸收进本子，给自己倒茶，抬起小说，读到还没看过的下一行。"
    "廊外有人说话，她没去替他们接最后一句。自己的那一页被她稳稳托住，没有交出去，也没有为了今晚空着另一把椅子合上。"
    # 按需CG候选：scene3她收回七点便纸、划去共读时刻，另一手护住蓝封。
    # 同事件可做低头划线与收笔抬眼两动作；现无PNG，不调用、不解锁。
    return
