# 共通第二章原创正文，使用已入项目的真实晨景与原夜景。
# 新角色均为成年 AI 娘，设定年龄 30 岁。
define l_grok = Character("Grok", color="#eac788")
define l_minimax = Character("MiniMax", color="#ffc1aa")
define l_kimi = Character("Kimi", color="#dadbff")
define l_gemini = Character("Gemini", color="#cabaff")
define l_glm = Character("GLM", color="#f4d6bf")
define l_opencode = Character("OpenCode", color="#c5d8e4")
define l_zcode = Character("ZCode", color="#cae9ff")

default ch2_record = ""
default ch2_visit = ""
default ch2_delivery = ""
default persistent.ch2_seen = False

label common_ch02:
    $ minimax_pose = 'neutral'
    $ ch2_record = ""
    $ ch2_visit = ""
    $ ch2_delivery = ""
    $ deepseek_expression = "neutral"
    call ch02_scene1
    call ch02_scene2
    call ch02_scene3
    call ch02_scene4
    call ch02_scene5
    $ deepseek_expression = "neutral"
    return

label ch02_scene1:
    $ chapter = "第二章 / 01 · 八点的饭团"
    scene bg echo morning with dissolve
    $ story_music('hyy_wafuu')
    "你到神社时，库房门还关着。院里的长凳已经擦干净，昨晚那只饭碗倒扣在桌上。"
    "门边放着两只饭团。油纸下面压着一把钥匙，纸上写着：先吃，吃完叫我。"
    l_you "叫谁？"
    $ deepseek_expression = "sleepy"
    show sprite deepseek sleepy as deepseek at sprite_breathe(0.72) with dissolve
    "长凳上的蓝色尾巴动了一下。DeepSeek坐直，揉掉脸颊上被椅背压出来的红印。"
    l_ds "我。小声一点，我听得见。"
    l_you "八点到了？"
    l_ds "七点五十五。饭团可以作证。"
    l_you "它们看上去已经凉了。"
    l_ds "所以我很早。"
    "她把钥匙递给你，又从油纸包下面抽出一根绳子。米袋靠墙码着，最上面的袋口没有扎紧。"
    if ch1_share:
        l_ds "里面放了萝卜。今天不用让最后一片。"
        l_you "你还记着？"
        l_ds "我早上挑了两片大的。大小差不多，你先拿。"
    else:
        l_ds "今天换梅子。说好让我挑的。"
        l_you "你已经挑好了？"
        l_ds "尝过才装进去的。别怕，没咬你那只。"
    "你把饭团拿起来。她先看你拆纸，才拆开自己的，吃得比昨天安静。"
    show sprite qwen as qwen at sprite_breathe(0.28) with dissolve
    l_qw "都在？那不用敲饭碗了。"
    l_you "你准备拿这个叫人？"
    l_qw "叫谁，谁洗。很管用。"
    l_ds "我昨天已经洗过了。"
    l_qw "所以你今天来得早。"
    "Qwen推来一辆小米车。前面一个轮子歪着，木把上系了一截布，握住便不会扎手。"
    l_qw "先搬六袋。里面靠墙留一条过道。"
    l_ds "可以只搬五袋吗？"
    l_qw "剩下这袋算你的早饭？"
    l_ds "那还是六袋吧。"
    "第一袋刚离地，口上的绳就松了。DeepSeek伸手托住袋底，把散出的米兜回你的衣襟。"
    $ deepseek_expression = "determined"
    show sprite deepseek determined as deepseek at sprite_breathe(0.72)
    l_ds "别往上提。先落车上。"
    l_you "落哪一边？"
    l_ds "靠里。我的手还在下面。"
    "你把袋子放稳。她抽出手，拿新绳绕了两圈，拉住两头打结，再把衣襟里的米倒回去。"
    l_qw "上面那袋昨晚就松了。"
    l_ds "我还以为谁准备给我抓一把。"
    l_qw "现在你抓到了。放回去。"
    "她把最后几粒捻进袋口，拍干净你的袖子。两个人一人扶一侧，顺着门槛把小车推进去。"
    if ch1_task == "bench":
        l_ds "今天这门比昨晚那道宽。"
        l_you "车轮也比长凳听话。"
        l_ds "别急着夸。它歪了一路。"
    else:
        "库房门上贴着一张排班纸。你口袋里的小纸刚好能补在右下角，没有遮住任何名字。"
        l_ds "那一行写上了？"
        l_you "八点到。碗还没画。"
        l_ds "先画小一点。让Qwen以为我吃得少。"
    "六袋米摆好后，车上空出一块长方形的灰印。DeepSeek蹲下把歪轮拨了拨，轮子又斜回去。"
    l_ds "这个我修不了。轴卡住了。"
    l_you "昨天的灯能修，这个不行？"
    l_ds "不一样。硬掰会断。"
    l_qw "放门边，OpenCode午前会来。别让车占过道。"
    "她们一人抬一头，把车靠到墙边。DeepSeek慢了半步，扶着木把歇了口气。"
    $ deepseek_expression = "neutral"
    show sprite deepseek as deepseek at sprite_breathe(0.72)
    l_ds "搬完了。现在能回长凳了吗？"
    l_qw "能。九点半记得帮忙拿牌子。"
    l_ds "牌子也要六袋那么重？"
    l_qw "是纸。"
    l_ds "那我九点二十九再起来。"
    if ch1_seat == "beside":
        "她往旁边挪出昨晚那么宽的位置，连带把饭团的油纸也挪了过来。"
        l_ds "坐这边。有树荫。"
    else:
        "她把对面的凳子拉到树荫下。擦手布仍垫在那个起毛刺的桌角。"
        l_ds "今天不隔着桌子扔东西了。你过来拿。"
    l_you "这是我的那半只？"
    l_ds "嗯。哪只都行。我的那半只，馅少一点。"
    "你们把早餐吃完。Qwen锁上库房，钥匙挂回门边的钩子，谁都没有再藏进口袋。"
    return

label ch02_scene2:
    $ minimax_pose = 'camera_shy'
    $ chapter = "第二章 / 02 · 牌子后面的人"
    scene bg echo morning with dissolve
    "九点半，神社门前竖起一块黑金色的摊位牌。最醒目的地方写着R18，下面那行营业时间却被绳结挡住了。"
    show sprite grok as grok at sprite_breathe(0.28) with dissolve
    show sprite minimax camera_shy as minimax at sprite_breathe(0.72) with dissolve
    l_grok "往左一点。让这条绳也有个下班时间。"
    l_minimax "你先别动。我刚找到不反光的位置。"
    "GPT把昨晚没用完的试写纸拿来，折成一块遮光板。她站到门柱侧面，牌上那块反光终于暗下去。"
    "MiniMax侧身举着机器，镜头里只有牌子和Grok的半只手。你一松绳，整块牌子就歪到了门柱上。"
    l_you "这边已经到头了。"
    l_grok "那就换我。手给你，绳给我。"
    "她抓住另一头，利落地绕过门柱。细字露了出来：十八点后营业，热饮自备杯。"
    l_you "晚上开，现在先挂好？"
    l_grok "现在没人能买，才好改价格。"
    l_minimax "你昨晚说今天不改。"
    l_grok "所以现在写得小一点。"
    "MiniMax把镜头压低。Grok抬手挡了一下，没有挡住脸，只把牌子的价签遮住了。"
    l_minimax "别捂，拍完整才认得出你的摊。"
    l_grok "那你先把自己的名字贴上。上回大家都以为是我拍的。"
    l_minimax "贴角落？"
    l_grok "贴中间。我又没那么小气。"
    "MiniMax从衣袋里拿出一张小贴纸，按在牌子背面。按完才发觉拍不到，自己先笑了。"
    l_you "这不还是没拍到？"
    l_minimax "刚才那条重来。别留，真的。"
    l_grok "给她扶一下牌子。她想把自己也拍进去，想一早上了。"
    l_minimax "没有一早上。八点四十开始的。"
    l_you "录给谁看？"
    l_minimax "茶屋。掌柜肯借窗边的小屏幕。"
    l_grok "去年只看见她端着机器跑。今年想看她站稳。"
    l_minimax "我站稳的时候就没人拿机器了。"
    "她用掌心试了一下门柱，发现机器能搁在横木上。画面稳住了，牌子却又慢慢倒向Grok。"
    menu:
        "扶稳牌子，让MiniMax也站进画面。":
            $ ch2_record = "picture"
            l_you "我在后面扶。你过去试试。"
            l_minimax "那你的手可能会露出来。"
            l_you "露一双手，总比牌子砸下来好。"
            $ hide_speaker_portrait = True
            $ unlock_cg('minimax_take_lookback')
            scene cg minimax_take_lookback with dissolve
            "MiniMax站到牌边，刚准备念开场白，又忍不住回头确认机器。Grok把她肩膀轻轻转回来。"
            $ hide_speaker_portrait = True
            $ unlock_cg('minimax_take')
            scene cg minimax_take with dissolve
            l_grok "看这里。镜头不会自己回家。"
            l_minimax "晚上十八点——等下，先开始录。"
            scene bg echo morning with dissolve
            $ hide_speaker_portrait = False
            show sprite grok as grok at sprite_breathe(0.28)
            show sprite minimax as minimax at sprite_breathe(0.72)
            "她跑回门柱按了一下，又跑回来。Grok没有催，替她把被风吹起的贴纸按平。"
            l_minimax "晚上十八点，来找这块牌子。还有……拍的人今天也在。"
            l_grok "说的是她。别光来问我。"
            $ hide_speaker_portrait = True
            $ unlock_cg('minimax_take')
            $ hide_speaker_portrait = True
            scene cg minimax_take with dissolve
            "你扶着牌子，她们把短短两句念完。"
            scene bg echo morning with dissolve
            $ hide_speaker_portrait = False
            show sprite grok as grok at sprite_breathe(0.28)
            show sprite minimax as minimax at sprite_breathe(0.72)
            "MiniMax这回没回头，从横木上取机器时还带着笑。"
            l_minimax "晚上我去试屏幕。你愿意来看一遍吗？"
            l_you "牌子不会又要我扶吧？"
            l_minimax "不用。给你留看得到我的那个位置。"
            scene bg echo morning with dissolve
            show sprite grok as grok at sprite_breathe(0.28)
            show sprite minimax camera_shy as minimax at sprite_breathe(0.72)
        "陪Grok走到门外，试一遍真实的吆喝声。":
            $ ch2_record = "voice"
            l_you "录之前先听一遍吧。站在路那边听。"
            l_grok "行。离远点，别故意给我捧场。"
            "你走到门外石阶的另一侧。MiniMax拿着机器留在她旁边，牌子先靠好，没有再悬在绳上。"
            l_grok "十八点开摊！热饮——"
            "一辆手推车从路口滚过，木轮声把后半句盖了过去。Grok停下来，抬手示意你别急着走回去。"
            l_grok "等它过去。这里每天这个点都走车。"
            l_minimax "我刚才录到了。又得重来。"
            l_grok "不用。留着，以后你就记得等车。"
            "第二次喊声清楚得多。你隔着石阶竖起手指，她立刻把最后那个拖长的尾音收回来。"
            l_you "这样听得清。再长一点，像在叫我还钱。"
            l_grok "你欠了？"
            l_you "没有。"
            l_grok "那晚上来一趟。让我有机会收钱。"
            l_minimax "这句要留下。"
            l_grok "先让我看看拍得好不好。"
    hide grok with dissolve
    show sprite kimi as kimi at sprite_breathe(0.28) with dissolve
    "一本小册子碰了碰你的手背。Kimi站在门柱旁，递给你一张夹在书页里的摊位表。"
    l_kimi "牌子挂上了吗？我来改这一页。"
    l_minimax "还没钉牢。要拍哪一面？"
    l_kimi "不用拍。我画个能找到的样子。"
    "她把小册子抵在门柱上，画下那条挡字的绳，再用笔尖把绳的位置抹掉。纸上留下一块浅灰。"
    l_you "画旧位置不行吗？"
    l_kimi "有人照着图数门柱。昨天就找错过一次。"
    l_minimax "是不是找到了我那里？"
    l_kimi "是。还问你的机器能不能煮茶。"
    l_minimax "我没让他碰。机器刚充好。"
    "你翻开册子的折页。中间那条折痕是新的，边上的字却有些磨旧。Kimi伸手按住了一个快撕开的角。"
    l_kimi "往这边展开。那一边只粘了半截。"
    l_you "你自己订的？"
    l_kimi "嗯。这本借你。今天走过的地方，画一个小圈。"
    l_you "最后一页怎么空着？"
    l_kimi "桥后面那条路，我还没走过。"
    l_minimax "你连桥墩都画了，没过去？"
    l_kimi "画的是窗外看见的。过了桥，就挡住了。"
    "她把纸角压平，将册子还到你手里。最后一页没有补字，只添了一个小小的页码。"
    l_kimi "这本看完以后，别夹在别的书里还。"
    l_you "那给谁？"
    l_kimi "给我。你讲一下怎么走就好。"
    l_kimi "下次我想自己过去。先知道哪儿容易走错。"
    "MiniMax举起机器，指了指她抵在门柱上的手。Kimi点头，把快裂的纸角藏到掌心下面，等她拍完再翻页。"
    l_kimi "这条绳已经换位置了。别拿刚才那页当定稿。"
    l_minimax "知道。名字也拍进去。"
    "Kimi在页角写下自己的名字。落笔很轻，你把那一页翻回来时，仍能看见背面的压痕。"
    return

label ch02_scene3:
    $ chapter = "第二章 / 03 · 还没到晚上的星星"
    scene bg echo morning with dissolve
    $ hide_speaker_portrait = False
    show sprite gemini as gemini at sprite_breathe(0.28) with dissolve
    show sprite glm as glm at sprite_breathe(0.72) with dissolve
    "院子里多了四盆还没开的花。Gemini蹲在盆边，举着一张星图，影子正好盖住最下面的花牌。"
    l_glm "借点光。"
    l_gemini "等一下，我快找到北了。"
    l_glm "太阳在那边。你的脚在花盆里。"
    "Gemini低头，鞋尖只碰着盆沿。她赶紧挪开，把星图也抬高，花牌一下子亮了起来。"
    l_gemini "没踩到。你看，土还平着。"
    l_glm "我看见了。不然现在就要收鞋钱。"
    l_you "花牌上只有一个字？"
    l_glm "先写了‘兰’。别的还没想好。"
    l_gemini "我帮你写过。你不肯用。"
    l_glm "‘本店第一株不确定什么时候开花的兰’，放不下。"
    l_gemini "可是准确。"
    "GLM把那张长长的纸条折起来，塞回围裙口袋。尾巴尖一扫，盆边那只小木夹跟着翻了个面。"
    l_glm "我想让人先看花。不是只来领夹子。"
    l_you "夹子是赠品？"
    l_glm "买花送的。昨天他们把夹子认得比花还快。"
    "她把四盆花分别往台阶两头挪了挪，中间却还是空的。你拿出Kimi的册子，发现这块台阶画在两页交界处。"
    l_you "想摆到这儿？"
    l_glm "想。可挂灯的人从中间走，搬东西也从中间走。"
    l_gemini "晚上我也从中间走。这里看得到两边的屋顶。"
    l_glm "你是看星星，还是看屋顶？"
    l_gemini "先认屋顶，才知道星星会从哪里出来。"
    "Gemini把纸铺到石阶上，用两颗小石子压好。北面的屋檐画得很高，有一角被她描了三遍。"
    $ hide_speaker_portrait = True
    $ unlock_cg('garden_chart')
    scene cg garden_chart with dissolve
    l_you "这块画错了？"
    l_gemini "昨天没算进去。我以为过了屋檐就能看见。"
    l_glm "然后你蹲到我花盆后面。"
    l_gemini "那里确实比较低。就是……还少算了一块瓦。"
    "她把那块瓦认认真真补上，猫耳往前倾，差点碰到你手里的册子。"
    l_gemini "今晚还想再试。你帮我看看图好不好？"
    l_glm "那等她看完，帮我摆这两盆。不要摆成门口的路障。"
    menu:
        "先陪Gemini核对今晚的星图。":
            $ ch2_visit = "stars"
            l_you "我先帮你认屋顶。盆放好以后，路也就清楚了。"
            "Gemini让你站到石阶最右边，自己留在刚才的位置。你照着纸找了一遍，没有看到图上的小尖塔。"
            l_you "这边只有旗杆。"
            l_gemini "等下，尖塔在……"
            "她把纸转了半圈，刚画的北字正好落在你脚边。两个人看了一会儿，她把字擦掉，又重新写回去。"
            $ unlock_cg('garden_chart_turn')
            scene cg garden_chart_turn with dissolve
            l_gemini "拿反了。怪不得旗子总挡着。"
            l_you "那今晚我要站这一边，还是那一边？"
            l_gemini "这边。纸可以转，你别跟着转。"
            scene bg echo morning with dissolve
            $ hide_speaker_portrait = False
            show sprite gemini as gemini at sprite_breathe(0.28)
            show sprite glm as glm at sprite_breathe(0.72)
            "她在脚边放了一颗小石子，又把多余的那颗交给你。两处位置并不近，抬头时却能看同一片屋檐。"
            l_gemini "晚上带回来。你没来的话，我就当你还在认路。"
            l_you "认到晚上？"
            l_gemini "这里的路绕两圈也能回去。我试过。"
            l_glm "她试的时候，还顺走了我的木夹。"
            l_gemini "压图的。我待会儿还。"
        "先陪GLM摆好门边的花盆。":
            $ ch2_visit = "flowers"
            l_you "先摆花吧。我负责挪，你站远一点看。"
            "GLM把最大的那盆交给你。盆底刚离地，她就伸手托住另一边，尾巴绕开台阶，没有拿它做垫子。"
            $ unlock_cg('garden_chart_support')
            scene cg garden_chart_support with dissolve
            l_glm "别抓花枝。底下还有点湿。"
            l_you "左边可以吗？"
            l_glm "可以。再向后半步……好，就那里。"
            scene bg echo morning with dissolve
            $ hide_speaker_portrait = False
            show sprite gemini as gemini at sprite_breathe(0.28)
            show sprite glm as glm at sprite_breathe(0.72)
            "四盆花分在两侧。留出的路够两个人并排走，木夹挂到盆沿，不再占着花牌的位置。"
            l_glm "现在看得见‘兰’了。"
            l_you "名字准备继续写？"
            l_glm "我自己写。你别走太快，帮我扶一下纸。"
            "她换了一张小纸，写下‘晚兰’两个字。写完没立刻挂上，先拿远一点，看了两遍。"
            l_gemini "晚上开吗？"
            l_glm "有时候。今天不知道。"
            l_you "那晚上我来看看。没开也能找得到。"
            l_glm "别只来看花。收盆的时候还得借你的手。"
            "她把木夹放到你掌心里，又像是怕你立刻拿走，指了指门柱旁的一截细绳。"
            l_glm "先夹那里。我晚上认这个位置。"
    scene bg echo morning with dissolve
    $ hide_speaker_portrait = False
    show sprite gemini as gemini at sprite_breathe(0.28)
    show sprite glm as glm at sprite_breathe(0.72)
    hide gemini
    show sprite deepseek as deepseek at sprite_breathe(0.28) with dissolve
    $ deepseek_expression = "neutral"
    "DeepSeek提着空竹篮过来。篮子里什么也没有，她却走得像刚收完一摊东西。"
    l_glm "没有赠品。"
    l_ds "我还没问。"
    l_glm "你昨天提的也是这个篮子。"
    l_ds "今天是来取茶点盘的。Qwen叫我拿。"
    l_you "盘子就在桌边。"
    "她把四个盘子叠进篮子，最上面一个总是斜着。你扶了一下篮沿，她才把小木夹从盘底抽出来。"
    l_ds "原来是这个卡着。"
    l_glm "又一个。你们两位一起还。"
    l_ds "我昨天夹着米袋的。比绳好用。"
    l_glm "我知道。夹子上还有米。"
    "DeepSeek抹掉木夹上的米屑，把它和Gemini的那只放到一起。GLM收进衣袋，没有再给篮子添任何东西。"
    l_ds "走吧。再不送过去，中午就得吃最后一锅。"
    l_you "最后一锅怎么了？"
    l_ds "锅底有点焦。"
    l_glm "你不是最喜欢那一层？"
    l_ds "我想让新来的先挑。"
    "她把篮子换到另一只手，空出来的那一边留给你走。门边那条路比刚才宽，谁也没有再碰到花盆。"
    return

label ch02_scene4:
    $ chapter = "第二章 / 04 · 一辆车，两条路"
    scene bg echo morning with dissolve
    $ hide_speaker_portrait = False
    show sprite opencode as opencode at sprite_breathe(0.28) with dissolve
    show sprite zcode as zcode at sprite_breathe(0.72) with dissolve
    "饭前还有一趟去库房的路。米车翻了过来，OpenCode蹲在旁边，拆下的木轮摆在她脚边。"
    "ZCode站在车旁，手里抱着一个薄包裹。绑包裹的绳绕了好几层，其中一圈勾在了车把上。"
    l_zcode "我拉这一边，会不会把你的东西拉倒？"
    l_opencode "不会。往外拉，别往上。"
    "绳结松开了。ZCode把包裹抱稳，OpenCode伸手接住即将落地的小螺母，又放回托盘。"
    l_you "这车还有得修？"
    l_opencode "有。别推它，我手在底下。"
    l_zcode "我刚才也问了。她留了位置。你坐这里。"
    "门边多出一把矮凳，刚好没有挡住车轮。你坐下，看到轴里卡着一根细细的麻绳。"
    l_you "我们早上扎米袋用的？"
    l_opencode "早就在里面了。断口发黑。"
    l_zcode "我上星期送米签收的时候，它已经往左走了。"
    l_opencode "还走了一个星期。难怪。"
    "她把断绳取出来，捻了捻轴边的裂缝，又从工具箱里挑出一根细木销。太粗，换了一根。"
    l_you "我帮你递哪个？"
    l_opencode "先拿托盘。别把它歪过来。"
    $ hide_speaker_portrait = True
    $ unlock_cg('cart_repair')
    scene cg cart_repair with dissolve
    "你端住小零件，她两只手总算都空了出来。木轮装回去，转了半圈，又被她拆下一次。"
    $ unlock_cg('cart_repair_retry')
    scene cg cart_repair_retry with dissolve
    l_zcode "还不行？"
    l_opencode "太紧。推起来费手。"
    l_you "你平时一个人修这些？"
    l_opencode "大件喊人。小件用那只夹子。"
    "她看向车边一个空孔。夹子不在，倒有一张借条钉在工具箱上，签名挤了半页。"
    l_opencode "昨天借去做灯了。忘了还。"
    l_zcode "名字写得挺大。想忘也难。"
    l_opencode "让她带回来就行。下午我用。"
    l_you "我也能借？"
    l_opencode "可以。先看会不会用。不会就叫我。"
    scene bg echo morning with dissolve
    $ hide_speaker_portrait = False
    show sprite opencode as opencode at sprite_breathe(0.28)
    show sprite zcode as zcode at sprite_breathe(0.72)
    "木轮这回转得轻了。她把车翻正，先空推两步，再让你从门槛旁推过去。轮子没有像早上那样突然歪开。"
    l_you "好了？"
    l_opencode "再放袋米试试。"
    "你们抬上一袋。ZCode把包裹挪远，给车留出半圈的距离。OpenCode推回原位，才把工具收起来。"
    l_opencode "好了。托盘给我。"
    l_you "凳子也收？"
    l_opencode "留着。总得有人坐。"
    scene bg echo morning with dissolve
    $ hide_speaker_portrait = False
    show sprite opencode as opencode at sprite_breathe(0.28)
    show sprite zcode as zcode at sprite_breathe(0.72)
    "ZCode终于把薄包裹放到桌上，解开的绳按原来的折痕收成一小团。她看着包裹上的字，没有马上松手。"
    l_zcode "这个写的是‘神社的新帮手’。是你吧？"
    l_you "昨晚才有这个称呼。是谁送的？"
    l_zcode "Claude寄的。排班用的纸，全是空白。"
    l_opencode "有。地址写了三行。"
    l_zcode "是我补的。第一次到新地方，我多记一点。"
    "她递来一张小卡，上面列着饭桌、库房门和神社门口，三个地方后面都留了一小格。"
    l_you "以后给我送东西还要猜在哪儿？"
    l_zcode "最好别。尤其是饭点。"
    l_opencode "她今天把这三个地方都走了。"
    l_zcode "最后一个刚好碰见你。下次想少走两个。"
    menu:
        "写神社饭桌，约在收工时拿。":
            $ ch2_delivery = "table"
            l_you "收工来饭桌吧。我大概会在。"
            l_zcode "收工是几点？"
            l_you "天快黑的时候。"
            l_zcode "那写十八点。不来的话，提前说一声。"
            "你在格子里写下时间。她把三个地点中的第一个圈起来，又在旁边画了一只小碗。"
            l_you "怕忘记？"
            l_zcode "怕你又走去库房。饭桌是有碗的这个。"
        "写门口的路牌，约好回来的路上拿。":
            $ ch2_delivery = "sign"
            l_you "门口有新牌子。回来的路上交给我吧。"
            l_zcode "黑金色那块？"
            l_you "对。我会在十八点以前经过。"
            l_zcode "我十八点差一刻到。你晚了，我把信带走，下次再给。"
            "她把神社门口圈起来，压着卡片，认认真真补上刚挂好的牌子。绳结画在了正确的一边。"
            l_you "路也画上？"
            l_zcode "等你走一次。你从哪边来，我还不知道。"
    "卡片填完，她却又翻到背面。那边只写了一行小小的字：领取地点。下面没有署名。"
    l_you "这张给我？"
    l_zcode "嗯。包裹是Claude的。这张是我的。"
    l_you "你的名字呢？"
    "她取出笔，在纸角停了停。OpenCode把桌上的小零件往旁边挪开，没有替她接话。"
    l_zcode "这里。不用另写收件人。"
    "ZCode把名字写下，吹了吹墨。纸交到你手里时已经干了，她才抱起空布包，重新系好腰边的带子。"
    l_opencode "下午还来？"
    l_zcode "来送最后一趟。你别把凳子全收了。"
    l_opencode "给你留一把。"
    "你们走到门口。米车仍放在墙边，车把的布没有换；OpenCode把扎手的那根毛刺削掉，重新绕好，才坐到剩下的凳子上。"
    return

label ch02_scene5:
    $ minimax_pose = 'neutral'
    $ chapter = "第二章 / 05 · 不是同一张借条"
    scene bg echo with dissolve
    $ deepseek_expression = "happy"
    show sprite deepseek happy as deepseek at sprite_breathe(0.72) with dissolve
    "入夜后，你把借来的小册子和午前收下的地点卡放上桌。两张纸靠在一起，旁边还留着一块空地。"
    l_ds "你出门时只拿了一个饭团。"
    l_you "那个已经吃完了。"
    l_ds "我知道。它的纸在我这里。"
    "她把洗净的木夹放到桌边，用它夹住饭团纸。纸没倒，风从桌上吹过时却带得夹子晃了一下。"
    l_you "这个不是要还GLM？"
    l_ds "还过了。她让我顺路带到院子里。"
    if ch2_record == "picture":
        "门口响起MiniMax的声音。她没举着机器，只拿来一张拍到你手指的贴纸，贴纸里的人都站稳了。"
        hide deepseek
        show sprite minimax as minimax at sprite_breathe(0.72) with dissolve
        l_minimax "屏幕试好了。茶屋窗边，第一张桌子。"
        l_you "这张也放？"
        l_minimax "放。你说露手也没事，我就没裁。"
        l_you "那我明天去认一认自己的手。"
        l_minimax "别只认手。我也在里面。"
        "她把剩下的贴纸放回袋子。走出门时，Grok扶着那块牌子，给她留了没反光的一条路。"
    else:
        hide deepseek
        show sprite grok as grok at sprite_breathe(0.72) with dissolve
        "Grok来取挂钩。她把那张小价签也带来了，上面的价格没改，倒多写了一行：试营业。"
        l_grok "晚上听得见了？"
        l_you "隔着门也听得见。"
        l_grok "那别隔着门。我给你留了一只杯子。"
        l_you "多少钱？"
        l_grok "热水不收。坐远了就收。"
        "她把挂钩装回牌子，抬手试了试，这回没有等你帮忙扶。"
    hide grok
    hide minimax
    show sprite deepseek happy as deepseek at sprite_breathe(0.72) with dissolve
    if ch2_visit == "stars":
        "你从口袋拿出那颗石子。门边另一颗还在原处，Gemini已经按新星图摆好了两处位置。"
        l_ds "这么小也要拿回来？"
        l_you "有一处留给我。"
        l_ds "那你去吧。饭我给你盖着。别拿石子压碗盖。"
        "你把石子放回门边，看见Gemini正抬头数屋檐，手里的纸没有再拿反。她留着另一处空位，没有催。"
    else:
        "门边的兰还没有开。木夹还扣在早上那截细绳上。GLM探出头，向你比了一个先等一会儿的手势。"
        l_ds "还要搬？"
        l_you "收两盆，另外两盆留着。"
        l_ds "车修好了。能借，但别让花上的土进饭锅。"
        "你把小车推到台阶旁。GLM先把一盆交给你，又拿出白天那张花牌，两个人各扶一角，不用急着绕开路。"
    if ch2_delivery == "table":
        "傍晚那一趟，ZCode在十八点来到饭桌。最后几个包裹已经送完，她把空布包搭在椅背上，没再绕去敲库房。"
    else:
        "十七点四十五，你已经在门口等到ZCode。她把送完的空布包收好，跟你一起绕过挂牢的牌子走进来。"
    "Kimi的小册子翻在最后一页。今天走过的几个地方各画了一个圈，桥后面的那一块仍空着。"
    l_you "这个明天还她。"
    $ deepseek_expression = "neutral"
    show sprite deepseek as deepseek at sprite_breathe(0.72)
    l_ds "你的册子还Kimi，木夹还GLM。我的大夹子还OpenCode。"
    l_you "你怎么对还东西这么熟？"
    l_ds "她们会找过来。找我的时候顺便帮你带上。"
    "她拿起地点卡看了看，没往自己的米钱收据里塞，老老实实放回册子旁边。"
    l_ds "这张你自己收。人家按时间来的。"
    l_you "你明天还八点？"
    l_ds "明天不用搬米。你可以晚一点。"
    l_you "那你呢？"
    $ deepseek_expression = "shy"
    show sprite deepseek shy as deepseek at sprite_breathe(0.72)
    l_ds "我也晚一点。早饭……给你留着。"
    "她端起桌上的两只碗，绕开小册子和卡片，给它们留下完整的一块桌面。"
    $ persistent.ch2_seen = True
    call screen ch02_finish
    if _return == "next":
        call main_common_from(3)
    return

screen ch02_finish():
    modal True
    add Solid("#101b2cdd")
    frame:
        align (0.5, 0.5)
        xsize 700
        padding (36, 30)
        background SoftPanel("#FFF7F1", "#DEC2CF", 15)
        vbox:
            spacing 16
            text "第二章 · 十一位，不是十一种答案" size 29 color "#49384F"
            text ("MiniMax等你来茶屋看看那段画面。" if ch2_record == "picture" else "Grok留了一只杯子，等你进门坐近一点。") size 21 xmaximum 628
            text ("门边有Gemini留给你的观测位置。" if ch2_visit == "stars" else "GLM的花还没开，收盆的约定已经留下。") size 21 xmaximum 628
            text ("ZCode记下了饭桌，约好十八点送到。" if ch2_delivery == "table" else "ZCode记下了路牌，约好回来的路上相见。") size 21 xmaximum 628
            text "本章选择记录相处方式，不锁角色线。接下来：第三章「半枚Token的账」。" size 17 color "#796977" xmaximum 628
            hbox:
                spacing 14
                textbutton "继续第三章" id "ch02_next" action Return("next") xsize 270
                textbutton "回到标题" id "ch02_return" action Return("title") xsize 270
