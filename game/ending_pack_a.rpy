# 五个独立隐藏短 IF 候选；未接入 gates/hub/finish，未原生验收。
# 只赋值各 IF 的 choice 及 root 指定的生育／老年头像显示状态；不手工设置任何解锁 flag。
# secret_ending_finish 是 root 约定的待总装 API，本包不实现或伪造其验收。
# guard 为 root 约定返回 bool 的函数，stage/finish 也待 controller 总装。

default secret_01_choice = ""
default secret_02_choice = ""
default secret_03_choice = ""
default secret_12_choice = ""
default secret_13_choice = ""
default bad_ds_last_bowl_choice = ""

label secret_01:
    if not secret_guard('secret_01'):
        return
    $ secret_01_choice = ""
    call secret_01_scene1
    call secret_01_scene2
    call secret_ending_finish('secret_01')
    return

label secret_01_scene1:
    scene bg echo morning with dissolve
    show sprite deepseek as deepseek at sprite_breathe(0.68) with dissolve
    "镇上试办白饭品尝会，DeepSeek在报名单前停了很久。纸上写着：米饭搭档，限两位共同报名。"
    l_ds "两位。你正好站这里。"
    l_you "正好，还是你拉来的？"
    "她把你的袖口松开，手指立刻压住报名单，免得你看见另一行小字。"
    l_ds "先写名字。那个不急。"
    "你把纸往上一推。两位须共同说明米的香气，试吃结束后协助收桌。"
    l_you "你以为只要一起吃？"
    l_ds "说明香气我会。收桌算香气的售后？"
    "她拿起笔，笔尖却在搭档两个字上停住。工作人员已经把两枚纸牌递到桌边，她没立刻接。"
    l_ds "刚才有人问，我们是不是一对。"
    l_you "你怎么答的？"
    l_ds "我说一对要给两份。她就笑了。"
    "你翻过纸牌，背面只有号码。DeepSeek仔细看过，没有找到刚才被她想象出来的恋人专席。"
    l_ds "原来不是那个搭档。"
    l_you "你想报的是哪个？"
    "她把笔递给你，耳尖微微发红。饭香从屋里飘过来，她又看了一眼门口。"
    menu:
        "认真写两个人的名字，和她共同试吃。":
            $ secret_01_choice = "pair"
            "你写好两个名字，将纸牌分给她一枚。她别在衣襟上，先确认你的号码与她相邻。"
            l_you "先当这一回搭档。收桌也一起。"
            l_ds "好。你负责数桌，不许负责数我的碗。"
        "先替她把收桌那行圈好，再一起报名。":
            $ secret_01_choice = "circle"
            "你将收桌那行圈起来，才写下两个人的名字。DeepSeek看着那一圈，拿笔补了一枚小饭碗。"
            l_ds "这是共同责任，不能只圈我的名字。"
            l_you "两个都写了。"
            l_ds "那可以。碗也画两个。"
    return

label secret_01_scene2:
    scene bg echo morning with dissolve
    show sprite deepseek as deepseek at sprite_breathe(0.67) with dissolve
    "品尝会的最后一锅饭揭开盖子。DeepSeek已经把意见写完，最后一行比前面的字都大：这个请再煮一锅。"
    "最开始那一碗，她忍了很久，才等你端稳一起尝。如今你把意见递出去，她又将笔从纸边抽回，补上米粒没有黏住的那一处。"
    l_ds "这句要写清楚。不然下次换米，我们就没处查了。"
    l_you "这算意见，还是追加订单？"
    l_ds "它们不冲突。"
    "她将空碗叠好，抱到回收桌旁。有人递来一张感谢券，她先看清背面，再放心地交到你手里。"
    if secret_01_choice == "pair":
        l_ds "两份。你那份别送人。"
        l_you "我留着和搭档一起用。"
        "她摸了摸衣襟上的纸牌，没摘下来。你抬起最后一张桌角，她立刻扶住另一边。"
    else:
        "她指给你看报名单上那两个小碗，收桌一栏已经盖过章。"
        l_ds "两个名字，两个章。我没偷懒。"
        l_you "那枚小碗是你刚补的吧？"
        l_ds "不影响。它已经认真站岗了。"
    "你们把桌子收进屋，带着感谢券坐到台阶上。DeepSeek终于将纸牌翻过去，在背面写了下一次试吃的日期。"
    if ending_playthrough_stage() >= 2:
        "她递笔时停了一下，笔尾已经正对着你的掌心。"
        l_ds "奇怪。还没看你伸手，好像就知道该递这边。"
    l_ds "那种搭档，要是你也想试……可以不等有饭的时候。"
    l_you "先约一次普通的散步？"
    l_ds "可以。但饭后。"
    "你应下，她把纸牌重新别正。品尝会当天结束，镇上却多了两名会一起收桌的米饭搭档。"
    return

label secret_02:
    if not secret_guard('secret_02'):
        return
    $ secret_02_choice = ""
    call secret_02_scene1
    call secret_02_scene2
    call secret_ending_finish('secret_02')
    return

label secret_02_scene1:
    scene bg echo morning with dissolve
    show sprite gpt as gpt at sprite_breathe(0.65) with dissolve
    "GPT的画桌收得很空。前几日的委托已经交清，今天门边却多了一张新纸：休业，龙也需要晒太阳。"
    "你推门进去，她正在替两个杯子挑杯垫。看见你，她将第三只杯子放回架上，没有忙着展开画袋。"
    l_gpt "你来得正好。今天没有能顺便交给你的工作。"
    l_you "连顺便的都没有？"
    l_gpt "认真找过了。所以现在可以安心坐下。"
    "门外有人询问一张新画的价钱。GPT站起来，亲自说明明天再谈，又把门推回半掩的位置。"
    l_you "你今天不接，真的可以？"
    l_gpt "今天的我已经写在门上。你别也来替我擦掉。"
    "她回到桌边，手里却不知何时又多了一支铅笔。笔尖还没落下，你看了看她。"
    l_gpt "习惯。不是准备给休业画一套说明。"
    l_you "你想拿它做什么？"
    "她望向窗外。院角那只花盆还空着，盆边的旧漆掉了一块，正好像一只缺角的蛋。"
    l_gpt "想在那只盆上，画一条很懒的龙。不是送谁，也不收钱。"
    menu:
        "替她扶住花盆，让她画自己想画的龙。":
            $ secret_02_choice = "paint"
            "你搬来花盆，扶稳盆底。她拿着笔蹲下来，先画一条团着的尾巴，再试了两个大小不一的角。"
            l_gpt "它今天不接见来客。"
            l_you "可以把头画进尾巴里。"
            l_gpt "你对休业很有经验。"
        "先带着茶到窗旁，让花盆再空一会儿。":
            $ secret_02_choice = "tea"
            "你将两只杯子移到窗旁。GPT把铅笔压在杯垫外，坐下来时还看了一眼花盆，随后端起自己的茶。"
            l_gpt "再空一天，好像也不会被别的龙抢走。"
            l_you "这只盆也没发邀请。"
            l_gpt "那我先占一个窗边的位置。"
    return

label secret_02_scene2:
    scene bg echo with dissolve
    show sprite gpt as gpt at sprite_breathe(0.64) with dissolve
    "日影移过窗沿。来问价的人已经离开，院里只有茶杯放回小碟的轻响。GPT伸了伸手指，没看墙上的钟。"
    "一片叶影落到桌面，形状正好遮住杯垫的一角。GPT移了移杯子，又移回来，将那点影子留在自己这边。"
    l_gpt "刚才看着它，差点又想画。我今天好像也没有变得特别懒。"
    if ending_playthrough_stage() >= 2:
        "她给自己续好茶，把热水壶交给你，没有提前替你挑下一杯。"
        l_gpt "这一回你自己试。壶里确实是茶，放心。"
    if secret_02_choice == "paint":
        "花盆上多了一条蜷着的龙，角都藏在尾巴旁。她在盆底签自己的名字，没有署成你的委托。"
        l_gpt "今晚把它放窗下。我明早想先看见它。"
        l_you "不等有人来夸？"
        l_gpt "等太阳。你可以比太阳晚一点。"
    else:
        "两杯茶喝完，花盆仍然空着。她将没用过的铅笔收好，给空盆选了一个窗下的位置。"
        l_gpt "明天也许画。今天的茶倒是没有放凉。"
        l_you "还有一杯要续吗？"
        l_gpt "要。给我自己的那种，不用按来客喜欢的选。"
    "临走前，你抬手碰了碰门边的休业纸。GPT先把纸按住，又从里面取来一枚小夹子。"
    l_gpt "风吹下来会有人误会。我还没休够。"
    "你帮她夹好。纸上的龙不负责招揽任何人，明天的委托留到明天，今天那两只茶杯已经洗净。"
    "后来，画桌每月都空出这样一天。那张休业纸晒得褪色，GPT仍用同一枚夹子，将它端端正正夹在门旁。"
    return

label secret_03:
    if not secret_guard('secret_03'):
        return
    $ secret_03_choice = ""
    call secret_03_scene1
    call secret_03_scene2
    call secret_ending_finish('secret_03')
    return

label secret_03_scene1:
    scene bg echo rain with dissolve
    show sprite claude as claude at sprite_breathe(0.64) with dissolve
    "平行的另一页里，镇上借用的阅读室到了归还期限。最后一天，雨把门外的闭馆通知淋湿了一角。"
    "Claude把借书卡按姓氏分好，剩下一张空卡没有姓名。她拿起来，又放回桌上。"
    l_cl "不是漏了一位读者。这张一直没有用。"
    l_you "要一起放进箱子吗？"
    l_cl "先等一下。我还没看完手里的书。"
    "你看向她指间的纸页。书只有最后一页没翻，她却把同一行读了两遍，指尖停在页脚。"
    l_you "不想念最后一句？"
    l_cl "想。只是念完，这间屋子就没有能拖一会儿的事了。"
    "她将钥匙从袖边解下来，放在已经归还的登记册上。没有谁忘记办手续，门明天仍然要交出去。"
    l_you "我可以再坐一会儿。"
    l_cl "那把椅子拉近。最后一句很短，不必站在门外听。"
    menu:
        "坐在她旁边，将最后一段读给她听。":
            $ secret_03_choice = "read"
            "你坐下来，接过书，从她停住的那一行读起。Claude纠正了一个念错的字，没有让你重新开始。"
            l_cl "后面还有一句。别因为短就吞掉。"
            "你念完，她用指腹压平最后一页，合上书，手掌在封面停了片刻。"
        "替她扶住空卡，让她写下这本书的名字。":
            $ secret_03_choice = "card"
            "你压住空卡，她写好书名，又在借阅人一栏停笔。你将自己的名字写在旁边，留了一半位置。"
            l_cl "这本归我，不在归还的名单里。"
            l_you "那下次向你借。"
            "她在另一半写下自己的名字，最后一页慢慢翻过去，没有催你今晚借完。"
    return

label secret_03_scene2:
    scene bg echo rain with dissolve
    show sprite claude as claude at sprite_breathe(0.63) with dissolve
    "钥匙交出去了。Claude抱着自己的书，与你站在门外的檐下。屋里那盏阅读灯最后熄灭，雨还没有停。"
    "你转头看她的袖口，那里曾被钥匙压出一道细折。她把袖子理平，怀里的书却抱得更紧，封面擦过你垂在身侧的手。"
    l_you "拿得住吗？"
    l_cl "拿得住。你替我挡一下雨就行。"
    "你们换了位置，书脊没再沾到檐外的水。"
    if secret_03_choice == "read":
        l_cl "你刚才念错的那个字，记住了吗？"
        l_you "记住了。下次还检查？"
        l_cl "会。检查完也让你继续念。"
        "她把空卡夹进书里，页脚露出一点白边。没有写还书日期，那里也不再是阅读室的登记册。"
    else:
        "她翻出写过两个人名字的卡，将借阅日期留空，再把书递给你。"
        l_cl "拿稳。里面那张别丢了。"
        l_you "读完以后，去哪儿还？"
        l_cl "院里的长椅。先看看哪一边不漏雨。"
    "你们沿檐下走出一小段。她回头看了门牌，随后将目光收回来，没有再伸手摸已经交出的钥匙。"
    if ending_playthrough_stage() >= 2:
        "Claude翻到书中间，夹进一条细纸，没在纸上写终止日期。"
        l_cl "下周有一个字要你念。我先不告诉你是哪一个。"
    l_you "下周，还一起读吗？"
    l_cl "读。不过这次我挑书。"
    "一周后，长椅上铺了两张干纸。Claude带来一本更薄的书，坐下时先让你看见她已经留好的页角。"
    "阅读室没有重新开放。你们失去那盏灯、那排书架和一间能随时坐下的屋子，仍按约定读完了下一页。"
    return

label secret_12:
    if not secret_guard('secret_12'):
        return
    $ secret_12_choice = ""
    call secret_12_scene1
    call secret_12_scene2
    call secret_ending_finish('secret_12')
    return

label secret_12_scene1:
    scene bg echo morning with dissolve
    $ hide_speaker_portrait = True
    # 七十三岁的 DeepSeek 暂用环境与对白，不冒充已有老年立绘。
    "这一页跳到许多年后。DeepSeek七十三岁，小满四十岁，从别处寄来一袋新米，袋口塞着一张写得匆忙的纸。"
    l_ds "又说只有一点。这个一点，够她小时候在盆里捞半天。"
    "她与你把米袋抬进柜子，随后抱着旧相册坐到窗下。封面换过一次，婚礼那张照片仍夹在第一页。"
    l_you "今天怎么想起翻这个？"
    l_ds "她问我们要一张近照。别让她以为我一直长这样。"
    "她指指照片里的自己，接着把今天的头发拨到肩后。你拿起相机，她立刻将还剩一点脆饭的小碟推远。"
    l_you "已经拍进去了。"
    l_ds "删掉。那个是相机路过时的误会。"
    "你把画面转给她看。她认真看了几秒，没按删除，先用手帕擦掉嘴角的一小粒饭。"
    menu:
        "并排端起空碗，拍一张给小满的新合照。":
            $ secret_12_choice = "bowls"
            "你将两只干净的碗拿来，坐在她旁边。DeepSeek将自己的碗抬得太高，只露出一双眼睛。"
            l_you "这样她只能检查你洗没洗碗。"
            l_ds "洗了。那也值得寄。"
            "她把碗放低一点，肩轻轻贴过来。快门响时，你们都没有再看旧照片里的姿势。"
        "保留她偷拣脆饭的照片，再和她拍一张。":
            $ secret_12_choice = "rice"
            "你把小碟放回中间，问她可不可以留下刚才那张。DeepSeek看了看，终于点头。"
            l_ds "前面先放合照。这个放后面。"
            l_you "怕她先看见饭？"
            l_ds "怕她以为碟子都归我。你也拿一块。"
            "你在她身旁坐下，她将脆饭推给你一半。相机定时亮起，她笑着看你手里的那一块。"
    return

label secret_12_scene2:
    scene bg echo with dissolve
    "照片送出后，小满回了一句：妈妈还是会先护碗。DeepSeek将字放大一点，哼了一声，回复却很快。"
    "新米的纸袋还留在地上，她用脚尖推到柜旁，让你能走过去。相册铺在两人中间，旧照片的边已经卷起来，被她轻轻压平。"
    l_ds "下次她回来，叫她自己挑位置。老说照片看不清，我们明明坐得好好的。"
    if secret_12_choice == "bowls":
        l_ds "告诉她，空碗也得有人护。"
        l_you "她还问，我们晚饭吃什么。"
        l_ds "新米。她寄来的，一点都没浪费。"
    else:
        l_ds "那个碟子确实有一半是你的。这个要说明。"
        l_you "她说看出来了。"
        "她把消息往上翻，看着你们同框的那张，没再要求把脆饭藏到照片外。"
    "饭锅响了一声。你起身拿碗，DeepSeek从相册后抽出一张空纸，写下今日的日期，夹在旧婚照旁边。"
    if ending_playthrough_stage() >= 3:
        "她翻到另一页空白，指尖却像记着那里一张纸牌的位置。"
        l_ds "很奇怪。总觉得有张纸，上面画着两只饭碗。"
        l_you "那就给这一页补两只。"
        "她画了两个小圆，一个稍歪，随后把纸平平地按进相册。这页终于也有了字。"
    l_you "不用换掉旧的？"
    l_ds "不用。那张有人给我摆了半天裙子，这张比较省事。"
    "你端来两碗饭，给她的小碗留出平稳的位置。她慢慢坐好，筷子先伸向你的碗，挑走一粒沾在碗沿的米。"
    l_ds "这粒归我。刚才我抬了米袋。"
    l_you "我也抬了。"
    l_ds "那下一粒归你。"
    "窗外的树已经高过屋檐，桌子仍只摆两只碗。新的合照夹在旧照片旁，你们吃完这顿饭，商量明天给小满回什么话。"
    return

label secret_13:
    if not secret_guard('secret_13'):
        return
    $ secret_13_choice = ""
    call secret_13_scene1
    call secret_13_scene2
    call secret_ending_finish('secret_13')
    return

label secret_13_scene1:
    scene bg echo morning with dissolve
    "婚礼后的第一个春天，DeepSeek三十三岁。你们为快到来的孩子腾出一格柜子，小衣服洗好，叠在两只旧饭碗旁。"
    l_ds "碗不用拿走。只是暂时借这里晾一下。"
    l_you "这件是不是买大了？"
    "她把衣服展开，比了比，又放回手心。袖子软软地垂下来，与你们刚买时想的大小不一样。"
    l_ds "先留着。长大一点还可以穿。"
    "你找来一个干净的盒子，她将小衣服收进去，认真压平那块折起来的袖口。桌上另有一只空照片袋。"
    l_ds "照片还没有。这个也先占位。"
    menu:
        "和她收好小衣服，再给照片袋留一个位置。":
            $ secret_13_choice = "clothes"
            "你托住盒底，她一件件放好，将最小的那件留在上面。盒子放进柜子时，照片袋紧挨着它。"
            l_ds "这样一开门就能看见。别又被你那条围巾盖住。"
            l_you "围巾搬家了。"
            l_ds "搬到你的那格，不许趁机搬到我床上。"
        "先在照片袋里放一张空卡，留给两个人写字。":
            $ secret_13_choice = "photo"
            "你将空卡放到袋里，没有提前替孩子填上称呼。DeepSeek拿起笔试了一下，笔尖停在白纸旁。"
            l_ds "到时候一起写。你别睡着以后让我代签。"
            l_you "写完再睡。"
            "她点头，把笔放到照片袋边，随后与你一起将小衣服收好。"
    scene black with dissolve
    "生产那天，你抱着她出门前交来的外套，坐在走廊里。天色从窗边移到门旁，等门再打开，已经过了很久。"
    "你走进病房时，她穿着整齐的宽松衣服，靠在枕上。新生儿穿着小衣服，裹在襁褓里，安静睡在她身旁。"
    "她抬起双臂，稳稳将襁褓接到臂弯，低头看了一会儿。小满仍睡着，她的手没有从孩子身旁移开。"
    # root 已确认母亲33岁与全包襁褓新生女儿图选入；ds_birth 注册、演出待 root 总装。
    $ hide_speaker_portrait = True
    call show_main_cg('ds_birth')
    return

label secret_13_scene2:
    # 延续上一场病房 CG；年龄跳转前清除它，不让新生儿画面冒充四岁小满。
    l_ds "你吃午饭了没有？"
    l_you "吃了。你的那份也留着。"
    l_ds "没倒掉就好。我刚才……还有点想。"
    scene black with dissolve
    "你把小满放回旁边的婴儿小床。她腾出双手，慢慢靠回枕上，望着你收起饭盒。"
    "她说到一半，眼睛已经合上一会儿。你坐到旁边，没让她撑着聊，外套收在椅背，饭盒留在另一张桌上。"
    "她醒来时，饭已温好。她吃了几口，低头看看睡着的孩子，再看你。"
    l_ds "真的多了一位。"
    l_you "我们家的。"
    "你们在第一张照片背面写下小满。她补上日期，将照片放进那只袋子。"
    if secret_13_choice == "clothes":
        "你把柜子里的小衣服连盒带来，最上面那件正好。DeepSeek翻了翻，见盒里没有混进你的围巾，轻轻笑了一声。"
        l_ds "这次没占错格。"
    else:
        "空卡也有了字。她认出你留下的那一半笔迹，将卡片夹在照片后面，没有代签任何人的名字。"
        l_ds "你真的等着一起写。"
    scene bg echo morning with dissolve
    show sprite deepseek as deepseek at sprite_breathe(0.68) with dissolve
    $ hide_speaker_portrait = False
    "四年后，DeepSeek三十七岁，小满四岁。那张照片留在柜中，饭桌上多了一只小碗。"
    l_child "妈妈，我小时候这么小？"
    l_ds "嗯。那件大衣服，你后来也穿过。"
    "小满伸出两只手比了一会儿，怎么比都比照片里的襁褓大。她索性抱住母亲的袖子，又把你拉到桌旁。"
    l_child "都坐。"
    l_ds "坐。饭好了以后就不搬家了。"
    "你将三只碗摆稳。DeepSeek把旧照片收好，给孩子腾出不被饭碗压住的地方，再坐到你身旁。"
    if ending_playthrough_stage() >= 2:
        "小满也想留下字。DeepSeek递来一张新纸，孩子画两只圈，数过一遍，又赶快补上第三只。"
        l_ds "没漏你。别画到饭上，这张先让我收好。"
    "相册留下那个下午。今天门内有三个人，饭还热着，谁也不用急着吃完。"
    return

label bad_ds_last_bowl:
    if not bad_guard('bad_ds_last_bowl'):
        return
    $ bad_ds_last_bowl_choice = ""
    call bad_ds_last_bowl_scene1
    call bad_ds_last_bowl_scene2
    call bad_ending_finish('bad_ds_last_bowl')
    return

label bad_ds_last_bowl_scene1:
    scene bg echo morning with dissolve
    # 独立、主动进入的平行未来；已相互选择并成婚，没有孩子，不改正史关系。
    "你们成婚那年，DeepSeek三十二岁。她把两只碗并排放进柜子，说这个架子暂时不用再换。"
    "那条平行的日子里，家中一直只有你们两个人。年岁往前走，米袋换过牌子，碗旁的位置始终没有空下来。"
    "后来你病了。病名没有留在这一页上，只留下越来越长的等待，和她放到椅背上的外套。"
    scene black with dissolve
    "DeepSeek在走廊坐了半夜，手里抱着保温袋。再见到你时，她先将袋子放下，自己坐到床旁。"
    l_ds "今天没放太多。你想吃多少就吃多少。"
    l_you "你那份呢？"
    l_ds "带了。别把我当只会端碗进来的人。"
    "她拿出自己的碗，吃了两口，随后看着你。筷子没有停在半空，你却知道她一直在留意你有没有力气说话。"
    l_you "回家以后，别一直等我开锅。"
    l_ds "锅会自己响。这个不用你教。"
    "你点头。她低头把保温袋口折好，折了两次也没有压平，终于放到旁边。"
    l_you "那两只碗，想怎么放都可以。"
    l_ds "我现在不想改。你也先别替我安排。"
    "桌旁有一张旧便笺，是你出门前留的买米提醒。DeepSeek拿起来，认出纸上少写了一个字。"
    l_ds "你每次都把买写得像卖。幸好我没听过。"
    menu:
        "和她把便笺夹回保温袋里。":
            $ bad_ds_last_bowl_choice = "note"
            "你扶住袋口，她把便笺放进内侧。手指轻轻压过你扶着的位置，没有再拿出笔来纠正。"
            l_you "回来以后，再写一张清楚的。"
            l_ds "这张也收着。别趁我洗碗偷偷丢。"
        "请她把家里那只旧碗留在原来的格子。":
            $ bad_ds_last_bowl_choice = "bowl"
            "她听完，点了一下头。你握到她伸来的手，她没有把手抽出去拿饭盒。"
            l_ds "还在那里。我昨天擦过了。"
            l_you "我记得。"
            "她将你的手放回被面，坐在原来的位置，等你慢慢把话说完。"
    "那个冬天，你因病去世了。她在关上的门前坐了很久，带回外套与两只碗，独自走进家门。"
    return

label bad_ds_last_bowl_scene2:
    scene bg echo with dissolve
    $ hide_speaker_portrait = True
    "最初几天，DeepSeek仍在锅响以后喊你的名字。喊完才想起，门外没有你正在洗手的声音。"
    "她只盛自己的一份饭，另一只干净的碗仍摆在对面。等饭吃完，再将两只碗一同放回柜子。"
    if bad_ds_last_bowl_choice == "note":
        "买米便笺被夹在柜门里面。字褪了，她用透明纸护住，没有将那个写错的字改过来。"
        l_ds "今天买的是新米。没有卖掉。"
    else:
        "那只旧碗始终留在原来的格子。碗沿的细痕被擦得很干净，她取下来时，仍先避开同一个地方。"
        l_ds "放回去了。明天还在这里。"
    "镇上有人来陪她坐过，也有人劝她将桌子换小。她收下新米，送走来客，晚间还是坐在自己的那一边。"
    "生日、年节、院里的树又长出新叶。她活了很长一段日子，出门时带自己的钥匙，回来时没有第二个人等着。"
    "到了七十多岁，她走得慢了。桌角那只空碗仍在，装过许多次水，又被她洗净，留到下一顿。"
    if ending_playthrough_stage() >= 2:
        "她有时带着两把钥匙去买米。回来后，另一把仍挂回原来的钩上。"
        l_ds "没弄丢。"
    l_ds "以前你总说，一只空碗占不了多少地方。"
    "屋里没人接话。她将自己的饭拌匀，吃完才起身关窗，没有把饭倒进那只等不到人的碗。"
    "相册留着两个人的婚照，此后新增的大多只有窗、树与一锅饭。她没有再和谁组成一桌，也没有把你的名字从门牌背面擦掉。"
    "八十四岁那年，她在家安静地走完了这一生。邻人整理旧柜子，看见两只碗并排放着。"
    if bad_ds_last_bowl_choice == "note":
        "那张买米的纸仍贴在柜门里面，那个错字留到最后。"
    "桌子后来被搬开，碗收进同一个盒子。那间屋子最后一次熄灯，再也没有人掀开锅盖，问另一份饭要不要添。"
    return
