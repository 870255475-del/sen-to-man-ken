# root_review_fixes：仅修实际审读确证，原作者冻结文件保留。
# 本修订all_writing_ended=true；由root整合、看图与原生验收。
# v17 A组独立平行事件正文候选：30岁、已恋人、自愿主动进入。
# 入口/registry/隔离/场景恢复由root controller提供；不改正式路线或完成次数。
# 各入口guard先行。event_A_局部值每次进入重置；拒绝不会减分。
default event_A_deepseek_swim_join = ''
default event_A_deepseek_swim_task = ''
default event_A_deepseek_mishap_help = ''
default event_A_deepseek_mishap_share = ''
default event_A_deepseek_kiss_seat = ''
default event_A_deepseek_kiss_answer = ''
default event_A_gpt_swim_join = ''
default event_A_gpt_swim_game = ''
default event_A_gpt_mishap_fix = ''
default event_A_gpt_mishap_place = ''
default event_A_gpt_kiss_picture = ''
default event_A_gpt_kiss_answer = ''
default event_A_grok_swim_join = ''
default event_A_grok_swim_target = ''
default event_A_grok_mishap_wait = ''
default event_A_grok_mishap_dessert = ''
default event_A_grok_kiss_walk = ''
default event_A_grok_kiss_answer = ''
default event_A_claude_swim_join = ''
default event_A_claude_swim_task = ''
default event_A_claude_mishap_fix = ''
default event_A_claude_mishap_read = ''
default event_A_claude_kiss_book = ''
default event_A_claude_kiss_answer = ''

label event_story_deepseek_swim:
    if not character_event_story_allowed('deepseek','swim'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_A_deepseek_swim_join = ''
    $ event_A_deepseek_swim_task = ''
    "这是独立的恋人泳池邀约。三十岁的DeepSeek提着已经盖好的饭盒，到浅水池边找你。"
    "她已经换好不透明蓝白连体泳装，泳帽没戴，长蓝发边的蓝色蝴蝶夹扣稳。干毛巾和饭盒都放在池外的遮阳桌。"
    l_ds "饭盒不能下水。我可以。它在这儿等。"
    l_you "你刚才把它放在泳圈上。"
    l_ds "测试座位。现在撤回。它没交门票。"
    "她将空泳圈从桌边拿走，终于露出下面那张租借清单。清单正中还被饭盒压着，她把盒子移开，自己核对时段。"
    l_ds "我们有一小时。不是一整天。"
    l_you "一小时里还包括吃饭？"
    l_ds "吃饭另算。那是我自己的安排。"
    "浅池的浮标还没归位。她看见最远那枚停在绳边，先用脚尖试了试水，鲸鱼尾梢避开踏板，没有横扫旁边的小桶。"
    l_ds "那枚蓝的，看起来特别好捞。"
    l_you "你已经看了三分钟。"
    l_ds "我在给水一点时间。它还挺凉。"
    menu:
        "一起进浅水池，帮她捞浮标":
            $ event_A_deepseek_swim_join = 'water'
            "你答应一起下水。她先确认浅池开放，沿扶梯慢慢进到腰间的水里，双脚踩稳才朝你抬起空泳圈。"
            l_ds "这个不是饭盒座位了。现在归我。"
            "她双手扶住蓝色泳圈，笑着看向画外，尾巴留在自己身后，水面没有盖到泳装肩带。"
            call show_main_cg('fan_deepseek_swim')
            l_ds "先拿蓝的。红的会抢着跑。"
            "她把泳圈扶稳，尾梢仍留在自己身后。"
            call character_event_restore_scene
            "她用手拨开一点水，蓝浮标却向相反方向转。她停下来，又把手掌换到另一侧。"
            l_ds "看见了。刚才是我送它走。"
        "留在干处陪聊，今天不下水":
            $ event_A_deepseek_swim_join = 'dry'
            l_you "我今天想待在干处。陪你坐会儿。"
            l_ds "好。那把小凳给我留着，别让饭盒坐了。"
            "她也从扶梯边退回来，穿好防滑拖鞋，将蓝白泳装外罩上已经备好的宽松短外套，坐到遮阳桌旁。"
            l_you "你可以自己去玩。"
            l_ds "可以。现在先坐。水不会因为我晚一点就关门。"
            "她从桌下拿出两枚备用浮标，摆成一小排。她把备用的蓝红浮标留到桌上，先替自己的水杯腾出一块干地方。"
    call event_story_deepseek_swim_scene02
    if _return is not True:
        return False
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_deepseek_swim_scene02:
    if not character_event_story_allowed('deepseek','swim'):
        return False
    if not event_A_deepseek_swim_join:
        return False
    if event_A_deepseek_swim_join == 'water':
        "她托起手边的蓝浮标，放进池边小桶，沿扶梯上岸，擦干手，罩好短外套，再把小桶提到遮阳桌旁。"
    "她把手边的毛巾折成两半，先让干的那半朝上，摸一下桌角才把饭盒移近。外套的小袋里还装着自己的柜匙，没有和租借的编号牌混在一处。"
    "池边的小喇叭响了一次，工作人员将待归还的浮标送到桌边，请大家按颜色收回箱子。DeepSeek举起手边那枚，正好给自己揽了个小活。"
    menu:
        "先分蓝红两堆，再逐枚收":
            $ event_A_deepseek_swim_task = 'sort'
            "你提议先分开颜色。她嘴上说两堆也会吵架，手却已经把蓝的放到右边，红的留到左边。"
            l_ds "这一枚算哪边？它背面也是蓝的。"
            l_you "看编号，不看它怎么翻身。"
            "她找到小小的编号，把那枚归到红堆，自己笑出声。这回没有把一个翻面算成多捞一枚。"
        "顺着编号挨个收，免得漏":
            $ event_A_deepseek_swim_task = 'number'
            "你们从最小编号找起。她念到第三枚时跳了一格，停住，重新把前两枚排近。"
            l_ds "我不是少拿一枚。它藏在桶后边。"
            l_you "刚才你把桶挪过去的。"
            "她把桶提开，那枚浮标露出来。她先把它放回队尾，才将自己的脚也从桶边挪开。"
    "箱子收满时，她认真压好盖，却发现干毛巾还铺在盖下面。她提起半边，抽出毛巾，这次才听见扣子咔哒一声。"
    l_ds "它也想占座。今天座位不够。"
    "到了休息时刻，她把湿手擦干，回到遮阳桌检查饭盒。盒盖扣得稳，里面的饭团没有被谁偷换成浮标。"
    l_you "现在终于轮到它了？"
    l_ds "轮到我。它已经歇很久了。"
    "她拆开一只小饭团，纸边折得太紧，海苔差点留在纸上。她自己把那片取下，重新贴好。"
    l_ds "你先挑一个。剩下的我再挑。"
    "她把饭盒放到桌中央，自己仍护着离手近的那只。泳池那枚蓝浮标安稳躺在箱里，这回没有跟饭盒一块被带回家。"
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_deepseek_mishap:
    if not character_event_story_allowed('deepseek','mishap'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_A_deepseek_mishap_help = ''
    $ event_A_deepseek_mishap_share = ''
    "独立恋人邀约的午后，三十岁的DeepSeek在厨房门口等你。她穿好蓝白日常连衣裙，围裙已经系稳，双手提着一个鼓起来的纸袋。"
    l_ds "点心拿到了。店里比约好的早关门。"
    "她把袋子放在桌上，里面只有整整齐齐的空纸盒。最上头的收据写着包装用，数量六只。"
    l_you "你买了六只盒子。"
    l_ds "我知道它们长得很规矩。没想到规矩到不放点心。"
    "她将收据举高，又发现自己在订单栏写的是纸盒样品。取货时店员还特意问过，她忙着腾手拿饭团，答了一声对。"
    l_ds "这个对，确实是我说的。"
    l_you "现在去换？"
    l_ds "人已经关店了。盒子又没烤错。先留下。"
    "桌边有昨天买好但尚未开封的面粉，她看向小烤盘，又看看盒子的尺寸。盘子明明比盒子大一圈。"
    l_ds "我们自己做一点。不能让它们今天白来。"
    l_you "你这是替盒子安排工作？"
    l_ds "也替我。我要吃到的。"
    menu:
        "陪她一起烤小米饼":
            $ event_A_deepseek_mishap_help = 'bake'
            "你答应留下。她拆开面粉，和饭拌匀，刚用汤勺舀一下，就觉得太大，自己放回一半。"
            l_ds "这口不能按吃饭来算。"
            "你们将六枚小饼压平，放进预热的烤箱。她设好时刻，等颜色转浅黄便关热，先让烤盘放到冷架上。"
            "她换好干净的橙黄隔热手套，把已经放凉的小烤盘端到桌前，六枚小米饼整齐留在烘焙纸上。"
            "蓝白裙和围裙都穿稳，鲸鱼尾梢绕开热烤架。她双手托住盘子，先向画外展示自己没有空着回来的那一批。"
            call show_main_cg('fan_deepseek_mishap')
            l_ds "看。盒子终于有内容了。"
            "她托稳已经放凉的盘底，六枚小饼没有挤到一边。"
            call character_event_restore_scene
            "你们先用平铲将米饼移到纸托里。她把头一枚放得太偏，盒盖压到一角，自己挪回中间才合。"
            l_ds "这次盒子才真能带走。"
            "她洗净手，取两只杯子泡好茶，又将自己买来没吃完的饭团放在手边，先拆好自己那只。"
        "陪她喝茶，今天不一起烤":
            $ event_A_deepseek_mishap_help = 'tea'
            l_you "我今天想歇着，陪你喝杯茶。"
            l_ds "好。米饼我晚点自己烤，别让茶陪空盒坐牢。"
            "她先把烤盘收回冷架，把两只干净杯子摆上桌。空纸盒叠到墙边，桌面终于够放一小盘她自己买的饭团。"
            l_you "它们本来就有。"
            l_ds "嗯。现在不用假装它们是新点心。"
            "她拆开饭团的纸，先留自己那只，又把茶壶转到你够得着的方向。"
    call event_story_deepseek_mishap_scene02
    if _return is not True:
        return False
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_deepseek_mishap_scene02:
    if not character_event_story_allowed('deepseek','mishap'):
        return False
    if not event_A_deepseek_mishap_help:
        return False
    "她拿最小的纸盒比了一下盘边，盒盖关不住，先把里面撑纸托的小卡取出。纸托竟然正好是一对。"
    l_ds "店里连空盒都按两口装。"
    l_you "不是两人装？"
    l_ds "别给我少算。两口也可以两人。"
    "厨房窗外的风把收据吹到杯边。她伸手压住，指尖碰到一点茶水，自己用布擦掉，没有把湿纸塞回盒里。"
    menu:
        "给两只盒子画小标签":
            $ event_A_deepseek_mishap_share = 'tags'
            "你拿出空白贴纸，让她自己写盒里会放什么。她先写饭，想了想，又在旁边添了一个小小的饼字。"
            l_ds "这下有人看得懂了。"
            l_you "那第三盒？"
            l_ds "留空。明天再决定，不预支明天的饭。"
            "她把贴纸贴到盒侧，头一张有点歪，自己揭起一角重新贴平。"
        "把盒子留给下次野餐":
            $ event_A_deepseek_mishap_share = 'picnic'
            "你建议把没用的盒子留到下次。她把两只套在一起，正想压扁第三只，又发现底板会因此折坏。"
            l_ds "它们需要一点自己的空间。"
            l_you "你不是说只留两个？"
            l_ds "我改了。六个都花过零钱，我要用完。"
            "她腾出架上半格，把完整盒子放进去，收据留在最前面，免得下次再把样品当点心。"
    "她将桌边的碎米收进小碗，手里那只饭团吃到只剩一角，仍认真把海苔折住，没让它落在杯底。"
    l_you "今天这单要写投诉吗？"
    l_ds "不用。下次我先把自己的字看完。"
    "她把订单照片收回手机，不拿空盒去逗已经下班的店员。茶壶里还有一点热茶，她倒进自己的杯子。"
    l_ds "我想让它们装得满一点。现在也想先喝完这杯。"
    if event_A_deepseek_mishap_share == 'picnic':
        "六只完整纸盒留在架上，桌面空出了喝茶的位置。她拉近自己的椅子，脚没有再碰到空烤盘。"
    else:
        "桌上留着两只准备好的盒子，其余四只在架上。她拉近自己的椅子，脚没有再碰到那只空烤盘。"
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_deepseek_kiss:
    if not character_event_story_allowed('deepseek','kiss'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_A_deepseek_kiss_seat = ''
    $ event_A_deepseek_kiss_answer = ''
    "独立恋人约会的夜里，三十岁的DeepSeek送你走到门前。她穿着扣好的蓝白日常外套和长裙，手里还拿着两只没吃完的饭团。"
    "她刚才说要先收饭盒，收完却把已经叠好的纸巾拆开，又慢慢叠回去。门边的椅子因此一直没腾出来。"
    l_you "你还在找东西？"
    l_ds "找个能让你再待五分钟的东西。已经找到了。"
    "她把纸巾包举给你看，自己先笑。饭团没有重新打开，夜风也没有替她找出一顿新的晚饭。"
    l_ds "五分钟不是添一餐。先别拆。"
    menu:
        "在门边坐一会儿":
            $ event_A_deepseek_kiss_seat = 'sit'
            "你答应坐一会儿。她把椅上的纸巾移到桌角，自己搬来另一只小凳，搬得太近又挪开一点。"
            l_ds "这次脚都有地方放。"
            l_you "饭盒呢？"
            l_ds "饭盒在厨房。我没有请它来送人。"
            "她将没拆的饭团放进小袋，折好袋口，送进厨房冷柜，贴上今天的日期，再回到门边，终于让双手空下来。"
        "沿门前的小路慢慢走":
            $ event_A_deepseek_kiss_seat = 'walk'
            "你提议沿门前的小路走一段。她把饭团送回厨房冷柜，贴好今天的日期，回来时手上只剩自己的门钥匙。"
            l_ds "来回两盏灯。别悄悄加到第三盏。"
            l_you "你先提的五分钟。"
            l_ds "我也可以走慢一点。时间还没催。"
            "她把钥匙收进口袋，尾梢从路边小花盆旁绕过，没有把花盆带成同行。"
    call event_story_deepseek_kiss_scene02
    if _return is not True:
        return False
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_deepseek_kiss_scene02:
    if not character_event_story_allowed('deepseek','kiss'):
        return False
    if not event_A_deepseek_kiss_seat:
        return False
    "门边的灯一亮，她才发现自己的外套袋口塞着一张订饭单。单子已经用完，角上却还卷着。她把它取出来折平，放进回收袋，再摸一下钥匙还在。"
    call character_event_restore_scene('door_light_on')
    if _return is not True:
        return False
    l_ds "这张今天不需要跟着出门。它已经报过我的饭了。"
    "她想说刚才的饭团哪只更好，又停住，抬眼看向你。嘴角那一点海苔已经自己擦干净，话却还没找好开头。"
    l_ds "我还有一件想做的事。不是找你再吃一口。"
    l_you "这次你想说什么？"
    l_ds "想轻轻亲你一下。你现在愿意吗？"
    "她站在干燥的门灯下，没有用尾巴挡住路，也没有抓住你的衣袖。钥匙安稳留在自己的口袋。"
    menu:
        "我愿意。可以靠近":
            $ event_A_deepseek_kiss_answer = 'yes'
            l_you "我愿意。你可以靠近。"
            l_ds "好。等一下，我得先把这一句说完。"
            "她自己确认鞋跟踩稳，蓝白外套仍扣好。长蓝发边的蓝色蝴蝶夹没有歪，嘴边已经擦净，双手放松在自己身前。"
            "她向你轻轻靠近，闭眼笑起来，双手仍放松在自己身前。"
            call show_main_cg('fan_deepseek_kiss')
            l_ds "这口不记到饭团里。"
            "她的呼吸轻下来，双手仍留在自己身前。"
            scene black with dissolve
            "双方答应后，一个很轻的吻落下。她随即退开。"
            call character_event_restore_scene
            "门灯重新照亮她的脸。她抬手摸摸自己有点乱的发梢，没有急着把刚才的停顿说成什么大的承诺。"
            l_ds "五分钟好像用掉一点了。"
        "今晚先陪聊，不亲吻":
            $ event_A_deepseek_kiss_answer = 'talk'
            l_you "今晚我想先陪你说话，不亲吻。"
            l_ds "好。那我把这一口撤回来。"
            "她自然退回自己刚才站的位置，双手仍空着。门灯没有暗下去，五分钟也没有因此被她收走。"
            l_you "刚才还没说哪只饭团好吃。"
            l_ds "梅子的。海苔那只也行，但我自己包少了米。"
            "她蹲下把倾斜的花盆转稳，起身时先抹去指尖一点土，再继续陪你说那只没包够的饭团。"
    "门边的纸巾还放在小桌上。她取一张擦净自己的手，确认冷柜里的小袋已经贴上今天的日期。"
    l_ds "贴的是今天。不能写成明天。"
    l_you "你怎么会写成明天？"
    l_ds "刚才已经在想明早吃哪只。手会跟着跑。"
    "她把钥匙取出来，找到两枚里正确的那一枚，另一枚是空饭盒柜的。她自己看清才开门，没有让你再等一次。"
    l_ds "下次你来，先敲门。也不用带一盒饭换进门。"
    "她停了一下，又把话收得更具体。"
    l_ds "带不带都可以。我先给自己留一份。"
    "你们把这一晚的道别说完。她回到门内，确认冷柜关好，再将自己那把小凳收到不挡路的墙边。"
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_gpt_swim:
    if not character_event_story_allowed('gpt','swim'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_A_gpt_swim_join = ''
    $ event_A_gpt_swim_game = ''
    "三十岁的GPT在独立恋人泳池邀约里等你。她已穿好不透明白金连体泳装，龙角与发饰保持原样，干浴巾整齐留在池外长椅。"
    "她带了一张小速写，纸上只有泳圈与水线。真正的泳圈却比她画的宽，放上椅子以后，干浴巾只能垂下一半。"
    l_gpt "我把它画得太听话了。实物有自己的尺寸。"
    l_you "纸上还能多坐一个你。"
    l_gpt "那是画里的优惠。这里没有。"
    "她把速写收进防水袋，把浴巾拿到高处，才将白色泳圈轻轻推到浅池边。龙尾避开扶梯，没有替她挤出新的座位。"
    l_gpt "今天只试一段，不比赛。"
    l_you "你那张纸上有三个箭头。"
    l_gpt "三个转弯。画时觉得很轻松，现在要听手臂的。"
    "她先沿池边伸展肩头，发梢束到颈后。最末一束没夹住，她摸到松动的小夹，又自己重新夹稳。"
    menu:
        "一起到浅池，试她画的转弯":
            $ event_A_gpt_swim_join = 'water'
            "你答应下水。她沿扶梯入浅池，确认脚下站稳，双手扶住白金泳圈，龙尾留在水里自己的那一侧。"
            "白金连体泳装完整穿好，发梢已束稳。她微笑看向画外，泳圈在胸下水面，空着的池道没有其他身体。"
            call show_main_cg('fan_gpt_swim')
            l_gpt "第一弯，先让它慢下来。"
            "她按稳泳圈边缘，浅浅的水纹慢慢散开。"
            call character_event_restore_scene
            "她轻推泳圈，圈却自己转了半圈。她跟着调整手掌，让它停到池道线旁。"
            l_gpt "很好。我现在知道箭头少画了什么。"
        "今天不上水，在长椅陪她看速写":
            $ event_A_gpt_swim_join = 'bench'
            l_you "我今天想留在长椅上，看看那张速写。"
            l_gpt "好。浴巾移开以后，长椅终于肯留座。"
            "她先穿好干燥的浅色宽松罩衫，坐到池外长椅，把防水袋平放到自己的膝上。泳圈靠在不挡路的栏杆内侧。"
            l_you "你自己可以去试。"
            l_gpt "我会去。先让我把它画得没那么自信。"
            "她将纸上最急的箭头改得平一点，没有替你写下已经一起游过的圈数。"
    call event_story_gpt_swim_scene02
    if _return is not True:
        return False
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_gpt_swim_scene02:
    if not character_event_story_allowed('gpt','swim'):
        return False
    if not event_A_gpt_swim_join:
        return False
    if event_A_gpt_swim_join == 'bench':
        "她将泳圈从栏杆旁取回，平放到长椅另一端。现在只拿它示意纸上的转弯，双脚仍留在干的地面上。"
    else:
        "她沿扶梯上岸，擦干手，穿好浅色罩衫，再从防水袋里取出纸和铅笔。白金泳圈先留在近处水面。"
    "水面把顶棚的一块光晃到她手上，她伸指去接，光又滑走。她笑了一声，终于把本来想当参照的那道水线放过。"
    l_gpt "它不肯站着让我画。"
    menu:
        "用轻推泳圈的小游戏找方向":
            $ event_A_gpt_swim_game = 'ring'
            if event_A_gpt_swim_join == 'bench':
                "你们只在长椅上慢慢转圈，拿圈边比纸上的弯。她将过长的箭头缩短，泳圈始终没下水。"
            else:
                "你们在池外轻推近处泳圈，让它慢慢转。她起初将箭头画得太长，发现一推便过线，就自己缩短。"
            l_gpt "这次只走一格。再大方一点，圈会去隔壁。"
            "她将手指从圈边收回来，等它停稳再接。池外的纸上添了小小一段弯，终于贴近实物愿意走的路。"
        "沿池边观察，画一条实际水线":
            $ event_A_gpt_swim_game = 'line'
            "你们沿池边换个角度，避开刺眼的光。她以扶梯为固定点，画下水线刚才停过的位置。"
            l_you "这一条没有箭头。"
            l_gpt "它只负责在这里。先别给它派远行。"
            "她擦去一个想当然的尖角，留下浅浅波纹。龙尾绕过长椅脚，没有碰到放好的防水袋。"
    "休息铃响时，她把纸重新装进袋里，封条第一下没压实。她沿边轻按一遍，确认不会从那一小段漏进去。"
    l_you "画稿也要休息？"
    l_gpt "要。今晚不能让它替手臂多游一遍。"
    "她取出一小盒切好的水果，盒盖与叉子分开放。叉子却正好藏在浴巾折角下，她自己找回来，没给泳圈再添一项罪。"
    l_gpt "想先吃甜的那块。你也挑自己的。"
    if event_A_gpt_swim_join == 'bench':
        "她把水果盒放到长椅中间，自己留下最想吃的两块。泳圈仍平放在另一端，没有沿水线漂走。"
    else:
        "她把水果盒放到长椅中间，自己留下最想吃的两块。近处泳圈贴着水线慢慢转，她看一眼，没再伸手去纠正。"
    l_you "那张要留下？"
    l_gpt "留下。下次我看它，就知道第三个箭头先别画。"
    if event_A_gpt_swim_join == 'water':
        "她将自己的泳圈从近处池边提回，擦去表面水珠，放到长椅另一端。"
    "她将防水袋收好，浴巾从靠背上拿下来叠成正方。长椅这次终于留得下她，也留得下那只过于宽的泳圈。"
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_gpt_mishap:
    if not character_event_story_allowed('gpt','mishap'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_A_gpt_mishap_fix = ''
    $ event_A_gpt_mishap_place = ''
    "独立恋人邀约的下午，三十岁的GPT已穿好白银日常长裙，来到画室。她拆开自己订的画框，把那张新画平铺在桌上。"
    "框窄了一截。她先转画框，又转画稿，两件东西都没有因为多转半圈就合适起来。"
    l_gpt "我把纸的短边写到长边那一栏了。"
    l_you "刚才它已经转了三次。"
    l_gpt "第三次是我自己还没死心。现在停。"
    "她取出卷尺重新量，在订货单上划去错的尺寸。卖框的人照着她的字做，边角规规矩矩，连赠送的小钉都装在袋中。"
    l_gpt "不能退它一个不属于它的错。"
    l_you "那画呢？"
    l_gpt "不裁。那一角我画了很久，今天还想留着。"
    "窗边有张小画正好能放进窄框。她伸手取下，又发现那张画自己也还没画完，最右边的窗帘只有一道铅笔线。"
    l_gpt "两件未完成的东西，倒是先约上了。"
    menu:
        "陪她把窄框用来试小画":
            $ event_A_gpt_mishap_fix = 'small'
            "你答应一起找位置。她先把大画妥帖收平，将窄画框拿到胸前，纸尺横搭在框角，双手稳稳扶住已经量过的边。"
            "白银长裙与龙角发饰都保持原样。她看向画外，笑着把尺寸明显偏小的空框举给你看，桌边的大画完整未裁。"
            call show_main_cg('fan_gpt_mishap')
            l_gpt "至少这一次，错得很清楚。"
            "她扶稳两侧窄边，框角的纸尺留在原处。"
            call character_event_restore_scene
            "她将小画试放进框里，留出铅笔窗帘的那边。背板还没扣下，就先把钉袋挪远，免得一时顺手钉完。"
        "先坐下来喝茶，暂时不一起修画框":
            $ event_A_gpt_mishap_fix = 'tea'
            l_you "我今天想先坐着喝茶，画框晚点再处理。"
            l_gpt "好。尺寸已经记下了，不会趁我们喝茶再缩。"
            "她把框立稳在桌内侧，展开一块干净杯垫。画稿收进大夹，完整的纸角没有被塞到窄框下面。"
            l_you "你还想去换一个？"
            l_gpt "明早订。现在先喝我自己泡的茶。"
            "茶比她料想的浓，她尝过才往自己杯里添水，没有先让你替这杯茶作证。"
    call event_story_gpt_mishap_scene02
    if _return is not True:
        return False
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_gpt_mishap_scene02:
    if not character_event_story_allowed('gpt','mishap'):
        return False
    if not event_A_gpt_mishap_fix:
        return False
    "她在抽屉里找到一只小木托，想给窄框当临时脚架。木托的槽朝反了，框一放上去便往前滑，她立即托住。"
    l_gpt "它提醒我先看底下。比刚才那张单直接。"
    "她自己把木托转正，框终于能站稳。桌上的铅笔被她随手压在木托边，她拿回时又带走了半张小画。"
    l_you "今天连铅笔都想挂画。"
    l_gpt "让它先只负责画。升职太快了。"
    "她又喝一口自己的茶，才问这张小画接下来想留在哪里。"
    menu:
        "把小画放窗边，补上窗帘":
            $ event_A_gpt_mishap_place = 'window'
            "你指向窗边留着的空处。她把木托和画一同挪过去，对着真实窗帘补了两条线，却故意留下最底下一角。"
            l_you "那里还是空的。"
            l_gpt "还没想好画它往哪边飘。先留给明早的风。"
            "她将铅笔扣好帽，窄框立在木托里，不替空白先盖上一个结束的章。"
        "放到矮架上，今晚先不补笔":
            $ event_A_gpt_mishap_place = 'shelf'
            "你们找出矮架中间一格。她自己移开空颜料盒，把小画放进去，框角没有挡住后面的水杯。"
            l_gpt "这个高度合适。我的角也不用和架子争。"
            l_you "不添最后两笔？"
            l_gpt "不添。想先看它站稳，再看你喝完这杯。"
            "她把画面轻轻转正，只扶边，没有把还没干的浅色擦开。"
    "订货单仍留在桌上。她写下新的尺寸，另添一句明早再联系，把笔放回杯里才关抽屉。"
    l_you "小钉还剩着。"
    l_gpt "留给新框。今晚不拿它们练习墙。"
    "她将钉袋收进带盖的小盒，画稿平平整整放在旁边。茶壶还温着，她给自己续了小半杯。"
    "那张小画没有变成大画，桌上的大画也没有少一角。她看着两个各有去处的尺寸，终于把卷尺收了起来。"
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_gpt_kiss:
    if not character_event_story_allowed('gpt','kiss'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_A_gpt_kiss_picture = ''
    $ event_A_gpt_kiss_answer = ''
    "独立恋人约会的夜里，三十岁的GPT坐在画室窗前。她穿好白银日常长裙，晚风只碰到窗帘，没有吹开衣领。"
    "桌上一张小画画的是两只杯子。她刚要收笔，发现自己把其中一只的柄画到另一边，和眼前实物完全相反。"
    l_gpt "你先别碰杯子。我想确认这一错归谁。"
    l_you "归铅笔？"
    l_gpt "归我。铅笔还没学会主动喝茶。"
    "她将自己的杯子转半圈，画里那只终于看着顺眼，却又把真的杯柄推远。她笑着转回来，把画按在桌内侧。"
    l_gpt "实物还是这样好拿。纸上明天再改。"
    menu:
        "想看她刚画的那一张":
            $ event_A_gpt_kiss_picture = 'look'
            "你想再看一眼。她将小画朝向你，自己把两处不合实物的地方指给你看，没拿空白纸遮住。"
            l_gpt "这张不送。今晚想先留给我自己。"
            l_you "那我只有看过的份？"
            l_gpt "还有一杯茶。价钱先不加。"
            "她把画放回桌面，留在她自己伸手就够得到的那一侧。"
        "让她先把画收好":
            $ event_A_gpt_kiss_picture = 'pack'
            "你让她先把画收好。她抽出大夹，小画却比夹子小，纸角一进便藏得看不见。"
            l_gpt "选大了。今晚从杯子开始都爱换边。"
            "她换一只小夹，把自己的画收平，再用干净布擦去指尖的浅色颜料。"
            l_you "这样明早找得着。"
            l_gpt "嗯。也不用让你现在替我找。"
    call event_story_gpt_kiss_scene02
    if _return is not True:
        return False
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_gpt_kiss_scene02:
    if not character_event_story_allowed('gpt','kiss'):
        return False
    if not event_A_gpt_kiss_picture:
        return False
    "窗台上有一只她自己的小陶鸟，刚才夹画时被挪到杯边，尾巴正对着壶嘴。她取回来，放到不碰水的干处，顺手抹去鸟脚一点灰。"
    l_gpt "它今晚已经看过两只杯子，先换个方向。"
    l_you "换去看窗外？"
    l_gpt "嗯。我也想看一会儿，不必让手一直拿着笔。"
    "她把笔洗好，水杯盖上盖。桌边只留两只喝茶的杯子，你们之间的椅子也没有被画稿占去。"
    l_gpt "刚才还有一件事，我没画在纸上。"
    l_you "你想做什么？"
    l_gpt "想亲你一下。很轻的，现在可以吗？"
    "她的手掌停在自己膝上，龙尾自然留在椅旁，没有绕住路。她看着你，等到你亲口回答才再往前动。"
    menu:
        "可以。我也想靠近":
            $ event_A_gpt_kiss_answer = 'yes'
            l_you "可以。我也想靠近。"
            l_gpt "好。那这次先把杯子放稳。"
            if event_A_gpt_kiss_picture == 'look':
                "她将桌上的小画收进自己的小夹，放稳到架上第二格，双手这才空下来。"
            "她确认两只杯子都离桌沿够远，自己站到灯光柔和的窗前。白银长裙完整穿好，手里没有笔，龙角不碰窗框。"
            "她轻轻靠近，闭眼露出一点笑意，肩头比刚才放松。"
            call show_main_cg('fan_gpt_kiss')
            l_gpt "这一句不用画下来。"
            "她的肩头放松，白淡紫发梢轻轻垂到自己肩前。"
            scene black with dissolve
            "双方答应后，她轻吻一下，随后缓缓退开。"
            call character_event_restore_scene
            "窗前的灯重新亮在她眼里。她抬手理好自己一束发梢，嘴角仍弯着，没急着替刚才补一个更漂亮的画名。"
            l_gpt "这次杯子没有倒。可以放心回去喝。"
        "今晚先不亲吻，想再聊一会儿":
            $ event_A_gpt_kiss_answer = 'talk'
            l_you "今晚先不亲吻。我想再聊一会儿。"
            l_gpt "好。还有半壶茶，别让它只陪我的画。"
            "她留在自己的椅子边，拿起茶壶给自己续一点。刚才的邀请已经答完，不需要你再列出理由。"
            l_you "杯柄明天会改好吗？"
            l_gpt "会。也可能先重画一只，免得这一只擦薄。"
            if event_A_gpt_kiss_picture == 'look':
                "她将桌上的小画收进自己的小夹，笑着说下次想画更小的糖罐，不再让两只杯子抢一整页。"
            else:
                "她看向自己收好的画，笑着说下次想画更小的糖罐，不再让两只杯子抢一整页。"
    "茶已经没那么热。她将壶盖放稳，窗帘的角又碰到杯边，她自己把窗帘束到另一侧。"
    l_you "今晚一直在找合适的位置。"
    l_gpt "现在找到了。我这只杯子也终于轮到手里。"
    "她喝过一口，把画夹留到架上第二格。最上面那格太高，龙角会碰到边，她没有再勉强伸手。"
    l_gpt "明天想去买一只合尺寸的小框。只买一只。"
    "你们说好可以再确认时间，她没有把今晚的道别变成一张行程表。灯下那张小画留在自己的夹里，杯柄朝着她习惯拿起的方向。"
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_grok_swim:
    if not character_event_story_allowed('grok','swim'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_A_grok_swim_join = ''
    $ event_A_grok_swim_target = ''
    "独立恋人泳池邀约的下午，三十岁的Grok已经穿好不透明黑紫连体泳装，在浅池外检查一小筐漂浮圆环。"
    "她说带了十只，筐里却只有九只。第十只套在筐把手上，刚才她自己扣好，提起来便一直没看见。"
    l_grok "我宣布第十只今天休假。"
    l_you "它还提着另外九只。"
    "她低头取下圆环，先放进筐里，笑着重新数了一次。黑紫泳装的肩带稳稳留好，干浴巾放在遮阳椅上。"
    l_grok "休假取消。不是它的，是我的。"
    l_you "你的也取消？"
    l_grok "没有。现在就是，我可以数错一只再回来。"
    "浅池里放着一只红色漂浮篮，给投环小游戏当目标。她先沿水边把篮推正，水流又慢慢把它带偏。"
    l_grok "这篮子有自己的观众席。"
    l_you "你刚才往左边推得更用力。"
    l_grok "被你看见了。那等会儿别向它那边站。"
    menu:
        "一起下浅水池，玩投环":
            $ event_A_grok_swim_join = 'water'
            "你答应一起玩。她沿扶梯到浅池，双脚踩稳后拿起一只紫圆环，另一手扶住红篮边。"
            "她的黑紫连体泳装完整穿好，头发已束离肩头，目光向画外带着笑。紫环举在胸前，身后只有空的浅池水面。"
            call show_main_cg('fan_grok_swim')
            l_grok "先来一只。投歪也归我们自己笑。"
            "她握稳胸前的紫环，另一只手仍扶着红篮边。"
            call character_event_restore_scene
            "她扔第一只时收手过早，圆环落在篮外，绕着篮边转了半圈。她自己把它捡回，不把篮子偷偷挪到里面。"
            l_grok "好，第一只负责让场面不完美。"
        "不上水，留在池外陪她":
            $ event_A_grok_swim_join = 'dry'
            l_you "我今天不上水，在干处陪你。"
            l_grok "好。干处也留一筐，不向你派救援。"
            "她穿好黑紫宽松罩衫和防滑拖鞋，坐到池外的小桌前，把两只备用环放到干净的托盘上。"
            l_you "你也不玩了？"
            l_grok "我稍后再去。现在想把第十只的冤案结完。"
            "她指给你看筐把手，环刚才卡过的印子还在。你们用干环比一下，终于找到了她自己扣上的那一边。"
    call event_story_grok_swim_scene02
    if _return is not True:
        return False
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_grok_swim_scene02:
    if not character_event_story_allowed('grok','swim'):
        return False
    if not event_A_grok_swim_join:
        return False
    if event_A_grok_swim_join == 'dry':
        "她借来一只干的小筐，摆在桌对面，只用干环做桌上的轻投。浅池的红篮还留在水里，十只干环各自有自己的位置。"
    "工作人员把红篮移近，让漂浮的环别进到另一条池道。Grok点头，先把自己的十只都收回手边，没拿更远的环来补数量。"
    menu:
        "目标近一点，练三次轻投":
            $ event_A_grok_swim_target = 'near'
            "你们把目标放近，只各试三次。她想把第一只算热身，刚张嘴又自己收回。"
            l_grok "好吧。三次就是三次，嘴不能再多投一个。"
            "最后一只擦着边落进去，她把那只环摆到最前头，故意让它待一会儿，才和别的放回筐里。"
        "先把环排成一行，找最好拿的那只":
            $ event_A_grok_swim_target = 'line'
            "你们先把十只环排平。她拿最轻的那只，转过来发现缝边正好卡指尖，又换到另一边。"
            l_you "不是越轻越好？"
            l_grok "现在知道了。手指没读过它的宣传。"
            "她挑出拿起来最顺的那只，余下九只留在原地，没把选环变成给它们排一整套名次。"
    "休息时她把圆环按颜色套回筐里，第十只这次最后入筐，筐把手终于能被正常提起来。"
    l_grok "它现在真的下班了。不给它加别的职责。"
    "她取来一杯凉水，杯盖扣反一边，轻轻一碰便翘起来。她按稳另一边，喝之前先确认杯身没有漏。"
    l_you "今天它们轮流提醒你。"
    l_grok "嗯。下一个想提醒我的，先排在水后面。"
    "遮阳椅上的浴巾被风吹下半角，她起身夹稳。夹子正好在自己的小袋里，没把已经收好的环再拿去当压纸圈。"
    l_grok "这只不归泳池。我的，跟我回家。"
    "她往椅背靠一点，将喝完的水杯放到桌内侧。红篮留在开放的浅池里，十只圆环回到它们自己的筐。"
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_grok_mishap:
    if not character_event_story_allowed('grok','mishap'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_A_grok_mishap_wait = ''
    $ event_A_grok_mishap_dessert = ''
    "独立恋人邀约的傍晚，三十岁的Grok穿好黑金日常裙装，拿着订位短信来找你。她说今天订了临窗桌，却领着你走到院里。"
    "院中第三桌只有一盆花。她看一眼短信，又看一眼花盆上的小牌，自己先把手机放低。"
    l_grok "我把室内三号看成了院内三号。"
    l_you "这桌已经有客人。"
    l_grok "客人只喝水。我们先别和它争。"
    "服务员指向室内，她礼貌道谢，没要求对方临时将花盆桌搬去窗前。刚才的短信里，室内两个字写得很清楚。"
    l_grok "今晚这句我收回，花没有订位。"
    "室内第三桌确实临窗，窗户却看向院里的同一盆花。她站到门边，忽然又笑起来，找到自己刚才绕的那一圈。"
    l_you "那你想坐哪儿？"
    l_grok "订的那儿。让腿的错误别继续替眼睛作主。"
    menu:
        "陪她进到订好的桌边":
            $ event_A_grok_mishap_wait = 'table'
            "你答应到订好的桌边坐。她先确认桌号，再把已经标清室内三号的小订位卡拿在手里。"
            call character_event_restore_scene('window_table')
            if _return is not True:
                return False
            "黑金裙装完整穿好，她停在窗边，另一手轻扶空椅背，目光向画外笑。窗外那盆花清清楚楚留在院中。"
            call show_main_cg('fan_grok_mishap')
            l_grok "这一回，椅子终于订给人了。"
            "她将订位卡捏稳，扶椅背的手没有急着移开。"
            call character_event_restore_scene
            "她把卡放到桌角，拉开自己的椅子。椅背碰到挂包的小钩，她停下来，把包移到侧边才坐稳。"
        "先在院里走一会儿，今晚不一起入座":
            $ event_A_grok_mishap_wait = 'walk'
            l_you "我今晚想先在院里走一会儿，不入座。"
            l_grok "好。我先跟店里讲清楚，别让空椅子等我们。"
            "她主动告知今晚不使用预留桌，按约定处理订位，没有怪你临时想散步。手机收回小包后，她到院里的小路陪你。"
            l_you "那盆花不用让位了。"
            l_grok "本来也不用。它比我先看清桌牌。"
            "她将伸到路上的枝叶绕开，脚步慢下来，刚才绕错的那一圈也有了真正想走的理由。"
    call event_story_grok_mishap_scene02
    if _return is not True:
        return False
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_grok_mishap_scene02:
    if not character_event_story_allowed('grok','mishap'):
        return False
    if not event_A_grok_mishap_wait:
        return False
    "店里有一份外带菜单，她拿到手里先翻到饮品页。页角的小贴纸挡住名称，她想揭开，又发现是店家贴好的季节说明。"
    l_grok "它还在营业。不能顺手给它提前撤。"
    l_you "你可以直接问。"
    "她问清有哪两种点心，听见只剩一份柚子小饼，自己先指向那份，并确认这回订的不是包装盒。"
    menu:
        "分一块小饼，再选各自饮料":
            $ event_A_grok_mishap_dessert = 'cake'
            "你们选一份小饼分着吃，饮料各自决定。她切第一下稍偏，便把更大的那半留给自己。"
            l_grok "刚才没切匀。我现在想要大的，可以吗？"
            l_you "可以，小的给我。"
            "她点头，认真把两半移开。饼屑落在纸托上，她拿自己的小叉收拢，没把大小差异藏到笑话里。"
        "各拿一杯热茶，今晚不分点心":
            $ event_A_grok_mishap_dessert = 'tea'
            "你想只喝茶。她给自己另点小饼，等你选好饮料才去取，不把那份饼顺手划成必须一起吃的。"
            l_grok "这一块我自己来。你那杯别被我说凉。"
            "她端回杯子时把自己的杯垫留在柜台，发现后自己走回去取，又将小饼放到不会挡杯柄的那一边。"
    "街灯亮起来，她隔着杯子又望到那盆花。窗内与院里看过去，是同一片叶子，刚才却让她多跑了一趟。"
    l_you "下次还订临窗？"
    l_grok "想订。先把两个字看完，也先问你当天想不想坐。"
    "她在手机上删掉自己给院内桌做的错误备注，只留下真正使用过的地址，没有替今晚编一个全程很顺的版本。"
    l_grok "回去绕短路吧。今天已经走过花盆那条。"
    "她把空杯和纸托收好，沿干燥的那边走出院门。那盆花仍在第三桌上，谁也没有把它当成一场乌龙的赔礼。"
    call character_event_restore_scene('courtyard_exit')
    if _return is not True:
        return False
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_grok_kiss:
    if not character_event_story_allowed('grok','kiss'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_A_grok_kiss_walk = ''
    $ event_A_grok_kiss_answer = ''
    "独立恋人夜市邀约散场时，三十岁的Grok已穿好黑金日常长裙和薄外套。她将自己买的一小袋点心扣好，和你站在亮着灯的街边。自己的带盖水杯放在小包外袋。"
    "袋扣朝反了，她按了两次才发现一直扣在空处。她把它转正，咔哒一声，又抬眼确认你有没有看见。"
    l_you "这回真扣上了。"
    l_grok "看得很仔细。先不要给我的袋子写点评。"
    "店铺打烊的木牌在风里晃，她伸手扶住旁边将倒的空篮，再把篮放回店门内侧。没有借收尾把你留成临时店员。"
    l_grok "我们自己的路也该选了。"
    menu:
        "沿亮着灯的街慢慢走":
            $ event_A_grok_kiss_walk = 'street'
            "你选灯还亮着的街。她点头，走到路边停一下，让送货小车先过，再回到你身旁。"
            l_grok "今天走慢一点。袋子也别再被我扣反。"
            l_you "你只提着一只袋。"
            l_grok "够了。我能让一只忙两遍。"
            "她把点心稳稳放进自己的小包，双手终于不必一路护着纸袋。"
        "在店外的干净长椅坐会儿":
            $ event_A_grok_kiss_walk = 'bench'
            "你提议坐一会儿。她先擦去长椅上的一点灰，把小包放在自己腿边，没拿袋子替你占座。"
            l_grok "这一位不会收费。长椅现在也下班。"
            l_you "你还要逗它？"
            l_grok "逗你。它刚才没答。"
            "她说完自己笑了半拍，抬头看见你仍等着下一句，反而先喝了一口手里的水。"
    call event_story_grok_kiss_scene02
    if _return is not True:
        return False
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_grok_kiss_scene02:
    if not character_event_story_allowed('grok','kiss'):
        return False
    if not event_A_grok_kiss_walk:
        return False
    "她从小包外袋摸出一张买点心的单子，纸背还有店里盖的小花。刚才她只顾口味，竟把那朵花当成了零钱店的记号。"
    l_grok "还好没拿它去换钱。今天能闹的，先闹到这里。"
    l_you "这张也留着？"
    l_grok "留到明早。得知道我先吃的是哪一味。"
    "她把单子放回点心袋侧面，指尖从袋扣移开，终于不再忙着替手里每一件小东西接话。"
    "她将水杯盖稳，话忽然比刚才慢一些。街边的风只吹起她外套一角，衣服仍完整穿好。"
    l_grok "刚才一路接话，现在有句要认真问。"
    l_you "你说。"
    l_grok "我想轻轻亲你一下。你现在愿意吗？"
    "她没有借笑话先跨过那一步，目光仍看着你。手掌放松在自己身侧，街边那条路一直留着能走的位置。"
    menu:
        "愿意。现在可以":
            $ event_A_grok_kiss_answer = 'yes'
            l_you "愿意，现在可以。"
            l_grok "好。那句逗人的，先让我忘一会儿。"
            if event_A_grok_kiss_walk == 'bench':
                "她从长椅上起身，先踩稳干燥的地面。"
            "她将水杯扣好放回包外袋，将小包放稳到干净长椅内侧，确认自己脚下站好。黑金日常裙装与外套都完整穿着，发饰留在原来的位置。"
            "她向你轻轻靠近，闭眼笑得很浅，停下刚才还想接的半句。"
            call show_main_cg('fan_grok_kiss')
            l_grok "这次我不抢下一句。"
            "她的双手放松在身侧，金色发梢从肩前垂下。"
            scene black with dissolve
            "双方答应后，一个轻吻落下。她随后退开。"
            call character_event_restore_scene
            "街灯重新照到她的眼里。她摸到小包上的袋扣，笑了一声，这回没拿它去遮住自己的脸。"
            l_grok "刚才那半拍，比我想的长一点。"
        "今晚想陪聊，先不亲吻":
            $ event_A_grok_kiss_answer = 'talk'
            l_you "今晚想陪你聊，先不亲吻。"
            l_grok "好。那让我找回刚才没接完的话。"
            "她留在原处，没有把拒绝翻成考题。她看看小包里的点心，忽然想起摊主把口味标签贴在袋底。"
            l_you "现在看得见吗？"
            l_grok "看不见。回去再看，不能让点心在街上倒立。"
            "她拍了拍已经扣好的小包，把那份好奇留给回家，不把今晚陪聊的时间撤掉。"
    "街角最后一家店把灯调暗一格，她看清回去的路，先把水杯放到包外侧的袋里。杯盖牢牢压好，没有让水替她再走一遍。"
    l_you "明天那袋点心还吃得到？"
    l_grok "吃得到。今晚我想先留一半，不让嘴把明早也吃完。"
    "临走时，她取回自己放在身边的小包，袋扣仍朝着正确方向。旁边的空篮也已安稳，没有追出来拦住谁。"
    l_grok "到你要转弯的地方再道别。现在路还没走完。"
    "你们将剩下那段亮着灯的路慢慢走完。她在真正的路口停下，说好晚安，手里只有自己那一小包明早的点心。"
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_claude_swim:
    if not character_event_story_allowed('claude','swim'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_A_claude_swim_join = ''
    $ event_A_claude_swim_task = ''
    "独立恋人泳池邀约的上午，三十岁的Claude已经换好不透明橘奶油连体泳装，把蓝封休闲小说留在池外的干书袋里。"
    "书袋放在高架上，旁边有干毛巾。她先将窄书签收好，再看浅池边的练习牌，牌上只有五个浮标位置。"
    l_cl "今天不把它们当阅读量。拿完就收。"
    l_you "你还带了小计时器。"
    l_cl "提醒休息。不是考谁先到第五枚。"
    "她把计时器按到十分钟，屏幕却停在一分钟。她看清数字，自己重新设好，没有把这一分钟解释成新的训练方法。"
    l_cl "按少了一下。现在是十。"
    "远处橘浮标贴着池边，她起身去看扶梯，脚下的拖鞋却还朝外摆着。她将自己的拖鞋转正，才给扶梯留出位置。"
    l_you "小说今天也有位置。"
    l_cl "有。干的那一格。它不参加下水。"
    menu:
        "一起进浅池，慢慢捞浮标":
            $ event_A_claude_swim_join = 'water'
            "你答应下水。她确认浅池开放，沿扶梯进去，双脚稳稳踏住浅池底，再拿起已经漂到身旁的橘色浮标。"
            "橘奶油连体泳装完整穿好，长橙发束在肩后，花饰与黑蝴蝶结保持身份位置。她双手在胸前托着浮标，抬眼看向画外。"
            call show_main_cg('fan_claude_swim')
            l_cl "第一枚就在这儿。先别替它写很远。"
            "她托稳橘色浮标，水纹从手边慢慢散开。"
            call character_event_restore_scene
            "她试着让浮标朝水线挪近，手掌一推，浮标反倒绕过身侧。她停住，换到另一边轻轻带回。"
            l_cl "刚才方向错了。现在这边。"
        "今天不下水，在干处陪她":
            $ event_A_claude_swim_join = 'dry'
            l_you "今天想在干处陪你，不下水。"
            l_cl "好。架下那张椅子是干的，我们移近一点。"
            "她先穿好橘白宽松罩衫和防滑拖鞋，和你坐在池外。计时器仍运行，她将表面转向另一边，只让它提醒久坐后的休息。"
            l_you "你可以自己去。"
            l_cl "我知道。现在想坐着，稍后再决定。"
            "她没有打开小说填满每一段空白，只取出一张干卡，记下池边真正标出的五个浮标位置。"
    call event_story_claude_swim_scene02
    if _return is not True:
        return False
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_claude_swim_scene02:
    if not character_event_story_allowed('claude','swim'):
        return False
    if not event_A_claude_swim_join:
        return False
    "工作人员提醒浮标第二枚与第四枚交换过颜色。Claude看向练习牌，牌上编号没有换，只是颜色与刚才看到的不同。"
    l_cl "那就按现在的拿。旧颜色不再算。"
    menu:
        "按编号确认一遍":
            $ event_A_claude_swim_task = 'number'
            "你们从编号最小的开始核对。她刚要凭记忆指向第二枚，便停下，先看清浮标侧面的小字。"
            l_cl "这只原来是第四枚。手比眼睛快了。"
            "她将刚才指错的方向收回，照着实际编号重排一遍，没有让同一枚浮标在清单上占两格。"
        "先记现在颜色，再核对位置":
            $ event_A_claude_swim_task = 'color'
            "你们将现在的颜色各记一格。她在橘色那格落笔时，笔帽还没取下，纸上没有出现她预想的点。"
            l_you "这次不是纸的问题。"
            l_cl "对。笔还没开。"
            "她取下帽，重新标好橘色位置，再把笔帽扣到另一端，没让它滚进水边的排水口。"
    "十分钟到时，计时器在桌上响。她先关掉提示，确认手边这件小活已经收尾，没有再给自己加一段必须完成的圈数。"
    l_you "现在看小说？"
    l_cl "先擦干手。再看我想不想读。"
    "她用干毛巾擦净指缝，把潮湿的一角单独摊开。书袋还在高架，她取下来时发现拉链只拉到一半，自己轻轻合稳。"
    l_cl "刚才以为关好了。里面仍是干的。"
    "小说没有被拿来垫清单。她将干卡收到自己的小袋，留出桌中间放水杯的地方，杯底稳稳压住杯垫。"
    l_you "那张练习牌要带回去？"
    l_cl "不用。它属于泳池。我的这张只记今天看见的。"
    "她喝过一口水，将计时器收进口袋。蓝封小说安稳放在自己膝上，却仍没打开；她想先坐完这阵不会再响的休息时间。"
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_claude_mishap:
    if not character_event_story_allowed('claude','mishap'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_A_claude_mishap_fix = ''
    $ event_A_claude_mishap_read = ''
    "独立恋人邀约的午后，三十岁的Claude穿好白橙日常披肩、白荷叶领上衣和黑色长裙，拿着她自己刚买的两本书来到茶桌。"
    "两本都叫花园开头。一本是蓝封小说，另一本塑封遮着副标题，她回到桌边拆开自己的包装，才看见里面全是种子插图。"
    l_cl "这本是播种小册。买的时候我只看完花园两个字。"
    l_you "你想买的也叫花园？"
    l_cl "花园里的不在场。少读了后面，真的去了别处。"
    "她打开收据，店员写得很清楚，两本分别列好。小册也没有装错，她将自己的错指给你看，没给书店添一笔责任。"
    l_cl "留下吧。今天不用把它赶回店里。"
    "小说里有一张新送的窄书签，她想把它夹到蓝封那本，低头却看见小册里页角已经立着它。她自己笑了一下。"
    l_you "已经在种花了？"
    l_cl "只种下了一张书签。先移回来。"
    menu:
        "陪她整理两本自己的书":
            $ event_A_claude_mishap_fix = 'sort'
            "你答应一起分清。她先将蓝封小说合好放到桌内侧，把已经打开的播种小册拿在胸前，双手扶住纸边。"
            "白橙披肩、白荷叶领与黑长裙完整穿好，金色花饰和黑蝴蝶结保持原位。她看向画外，小册清楚展示一页简洁种子图。"
            call show_main_cg('fan_claude_mishap')
            l_cl "这位暂时没有作案时刻。"
            "她双手扶稳书边，简洁的种子图仍朝着你。"
            call character_event_restore_scene
            "她将书签移回小说，另给小册夹一张自己找来的空白卡。两本现在各有记号，不必再凭封面前两个字猜。"
        "先喝茶，暂时不一起整理":
            $ event_A_claude_mishap_fix = 'tea'
            l_you "今天先喝茶吧，书晚点再分。"
            l_cl "好。我先把包装纸收走，别让它挤进杯底。"
            "她把两本自己的书分别放到桌内侧，窄书签收进小格。你们先坐下来，小册没有被要求证明买错也一定很有用。"
            l_you "回去再看它？"
            l_cl "可能。现在先看茶壶还够不够。"
            "她倒好自己的那杯，发现壶嘴带着一片茶叶，自己夹出来放到小碟，不让它顺水进杯里。"
    call event_story_claude_mishap_scene02
    if _return is not True:
        return False
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_claude_mishap_scene02:
    if not character_event_story_allowed('claude','mishap'):
        return False
    if not event_A_claude_mishap_fix:
        return False
    "窗边那盆薄荷有一点向外歪。她看着小册上的盆栽图，想照图转正，却先发现花盆只是被垫了一张折起的纸。"
    l_cl "先把纸取下。不需要让植物重新学习站立。"
    "她将干纸展平，给花盆换一块稳的垫片。薄荷回到桌角，两本书仍在干的那一边，没人拿它们当临时托盘。"
    if event_A_claude_mishap_fix == 'tea':
        "她自己将小格里的窄书签夹回小说，另取一张空白卡夹进播种册，才把两本放好。"
    menu:
        "读小说的开头，不先猜凶手":
            $ event_A_claude_mishap_read = 'novel'
            "你们选蓝封小说。她念开头一小段，读到那位园丁的名字，自己又看了一眼花盆。"
            l_you "已经开始怀疑？"
            l_cl "还没。只是名字和这株薄荷不相干。"
            "她读完这段便夹好书签，没有翻到最后确认。她仍想知道谁进过那座花园，只把这个问题留到下次真的想继续读时。"
        "翻种子图，挑一种她真的想种的":
            $ event_A_claude_mishap_read = 'seeds'
            "你们翻到种子图。她挑了一种不需要大盆的花，接着又看到花期，终于将那张图旁的字也读完。"
            l_cl "这回不只读它叫什么。"
            l_you "今天就买种子？"
            l_cl "不买。先看窗边能不能放得下。"
            "她用空白卡量一下桌角，留下自己想看的那页，没把一时喜欢写成已经种好了。"
    "茶渐渐温下来，她将小册和小说各自合好，包装纸折进回收袋。袋口还带着一次没撕净的胶条，她自己取干净。"
    l_you "今天带回两本，够重吗？"
    l_cl "够。我自己选的两本，也可以分两只袋拿。"
    "她将书袋的底部铺平，不让薄荷垫片跟书一同回去。空白卡留在小册里，窄书签留在小说里，各自压住真正看过的位置。"
    l_cl "下次先看完整名字。今天的这两本，我都带走。"
    "她站起时把自己的杯子送到洗杯盘，桌上那株薄荷仍稳稳立着。门外的书店招牌已翻到休息，她没有追过去让别人替这次买书加班。"
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_claude_kiss:
    if not character_event_story_allowed('claude','kiss'):
        return False
    call character_event_restore_scene('entry')
    if _return is not True:
        return False
    $ event_A_claude_kiss_book = ''
    $ event_A_claude_kiss_answer = ''
    "独立恋人河边邀约的傍晚，三十岁的Claude穿好白橙披肩、白荷叶领上衣和黑色长裙，坐在干燥的长椅边。"
    "她今天带来的蓝封小说才读到半页。到了自己选定的段尾，她的指尖却停在还没说出口的一句上。"
    l_you "还要往下读？"
    l_cl "想。但现在还有别的想做。"
    "她将书签拿出来，夹时偏了一页。她自己看清页码，移回真正读完的位置，没让一个着急的手势替故事多读一段。"
    l_cl "差一点。现在没有漏。"
    "晚风碰到书页，她用自己的手掌压住，没有拿外套遮在你身上。披肩稳稳留在肩头，黑蝴蝶结与金色花饰都保持原位。"
    menu:
        "先听完这页最后一段":
            $ event_A_claude_kiss_book = 'read'
            "你想听完最后一段。她重新打开书，念到故事里一扇没上锁的门，在那句末尾自然停住。"
            l_cl "这一页完了。后面的门明天再看。"
            l_you "你还没有猜谁进去。"
            l_cl "现在不用猜。想给自己留点没读过的。"
            "她把书重新合好，窄书签没有滑出，自己的名字留在封角。"
        "让她合书，先说她想说的话":
            $ event_A_claude_kiss_book = 'close'
            "你让她先合书。她确认书签夹稳，蓝封小说完整合在膝上，手掌终于离开书页。"
            l_cl "好。我刚才还想再找一个整齐的开头。"
            l_you "现在这个也可以。"
            l_cl "可以。那我不重写了。"
            "她将书放进自己的袋里，袋口轻轻压平，没把刚才那段藏到一张新的批注纸上。"
    call event_story_claude_kiss_scene02
    if _return is not True:
        return False
    call character_event_restore_scene
    if _return is not True:
        return False
    return True

label event_story_claude_kiss_scene02:
    if not character_event_story_allowed('claude','kiss'):
        return False
    if not event_A_claude_kiss_book:
        return False
    "长椅边有一枚她自己的夹子，刚才压着书袋，取书时掉到垫角。她先把夹子找回来，扣到袋边。垫角留着浅浅一道印，她用手掌抚平才坐稳。"
    l_cl "找到了。它没有被河边借走。"
    l_you "你刚才想回去找第二只？"
    l_cl "想过。现在不用。我自己这只也够用。"
    "她看一眼真正读过的那半页，把夹子留在手边，终于没再给今晚添另一项找东西的安排。"
    "河边的灯依次亮了。她把杯子移到长椅内侧，确认盖子扣好，转过脸看着你，话很短。"
    call character_event_restore_scene('river_lights')
    if _return is not True:
        return False
    l_cl "我想轻轻亲你一下。你现在愿意吗？"
    "她在自己坐着的位置等，没有拿精确的时刻催你。长椅另一端仍有空处，书袋没有挡住起身的路。"
    menu:
        "我愿意。可以":
            $ event_A_claude_kiss_answer = 'yes'
            l_you "我愿意。可以。"
            l_cl "好。我也愿意，现在靠近。"
            "她将已经合好的蓝封小说和杯子放稳到自己侧边，确认披肩仍穿好。长橙发绕开书袋带子，双手空下来，放松在裙边。"
            "她轻轻靠近，闭眼露出一点笑，手掌仍放松在自己的裙边。"
            call show_main_cg('fan_claude_kiss')
            l_cl "这句我没有改。"
            "她的手掌轻放裙边，肩头慢慢松下来。"
            scene black with dissolve
            "双方答应后，她轻吻一下，然后自然退开。"
            call character_event_restore_scene
            "河边灯重新映到她眼里。她把松了一点的披肩理平，手没有立刻回去翻书。"
            l_cl "现在可以再坐一会儿。我自己也想。"
        "今晚想继续陪聊，不亲吻":
            $ event_A_claude_kiss_answer = 'talk'
            l_you "今晚想继续陪你聊，不亲吻。"
            l_cl "好。那我们继续坐一会儿。"
            "她没有伸手跨过你的回答，蓝封小说仍合着留在自己那边。刚才的邀请已说清，不用再把拒绝改成另一种承诺。"
            l_you "你还想聊那本小说吗？"
            l_cl "想聊封面。画的人把门把手画到了门外另一边。"
            "她从袋里取出自己的书，给你看那处别扭的细节，自己先轻轻笑了一声。故事的最后一页仍没被翻开。"
    "杯里的水喝完以后，她把空杯放回自己的袋中。袋底有一张没用的纸，折角朝上，她展开再铺平，终于让杯底放稳。"
    l_you "明天还在这儿读？"
    l_cl "可能。明天再问。我现在只想把这段路走完。"
    "她站起来先取自己的书袋，又回头确认长椅上没有留下窄书签。书签确实在书里，没成为多留一次的借口。"
    l_cl "灯下那条路是干的。我们从这边走。"
    "你们沿亮着灯的河岸走到实际的分岔口。她说好晚安，书在她的袋里，未读的门后也仍留着明天愿不愿继续打开的余地。"
    call character_event_restore_scene
    if _return is not True:
        return False
    return True



# all_writing_ended=true
