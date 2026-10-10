# Claude 第六章候选 / 修改的是约定 / 第十三日 / 全员成年三十岁。
# 普通scene/show与call/return；没有新CG调用、关系结局或整线完成写入。

default persistent.main_claude_ch06_seen = False
default claude6_has_ch05 = False
default claude6_previous_response = ""
default claude6_previous_repair = ""
default claude6_has_ch02_echo = False
default claude6_previous_drying = ""
default claude6_map_returned = False
default claude6_public_clear = False
default claude6_new_time_agreed = False
default claude6_reading_start = ""
default claude6_pause_sign = ""
default claude6_pause_used = False
default claude6_old_guess_written = False
default claude6_guess_admitted = False
default claude6_guess_play = ""
default claude6_player_guess_written = False
default claude6_readback_done = False
default claude6_old_guess_kept = False
default claude6_second_chapter_finished = False
default claude6_time_kept = False
default claude6_novel_chapter = 2

label claude_ch06:
    $ claude6_has_ch05 = getattr(persistent, "main_claude_ch05_seen", False) is True and getattr(renpy.store, "main_last_chapter", "") == "claude_ch05" and getattr(renpy.store, "claude5_first_response", "") in ("correct", "retreat") and getattr(renpy.store, "claude5_repair_mode", "") in ("return", "letter") and getattr(renpy.store, "claude5_boxes_returned", False) is True and getattr(renpy.store, "claude5_next_map_kept", False) is True and getattr(renpy.store, "claude5_invitation_made", False) is True and getattr(renpy.store, "claude5_spoken_over", False) is True and getattr(renpy.store, "claude5_public_answer_given", False) is True and getattr(renpy.store, "claude5_local_correction_done", False) is True and getattr(renpy.store, "claude5_absent_listener_pending", False) is True and getattr(renpy.store, "claude5_evening_cancelled", False) is True and ((getattr(renpy.store, "claude5_repair_mode", "") == "letter" and getattr(renpy.store, "claude5_note_delivered", False) is True) or (getattr(renpy.store, "claude5_repair_mode", "") == "return" and getattr(renpy.store, "claude5_note_delivered", None) is False)) and getattr(renpy.store, "claude5_novel_chapter", 0) == 2
    $ claude6_previous_response = getattr(renpy.store, "claude5_first_response", "") if claude6_has_ch05 else ""
    $ claude6_previous_repair = getattr(renpy.store, "claude5_repair_mode", "") if claude6_has_ch05 else ""
    $ claude6_has_ch02_echo = claude6_has_ch05 and getattr(persistent, "main_claude_ch02_seen", False) is True and getattr(persistent, "main_claude_ch03_seen", False) is True and getattr(persistent, "main_claude_ch04_seen", False) is True and getattr(renpy.store, "claude5_has_ch04", False) is True and getattr(renpy.store, "claude4_has_ch03", False) is True and getattr(renpy.store, "claude3_has_ch02", False) is True and getattr(renpy.store, "claude2_drying", "") in ("spread", "cloth") and getattr(renpy.store, "claude2_pause", "") in ("line", "meal") and getattr(renpy.store, "claude2_private_kept", False) is True and getattr(renpy.store, "claude2_shared_line_read", False) is True and getattr(renpy.store, "claude3_previous_drying", "") == getattr(renpy.store, "claude2_drying", "") and getattr(renpy.store, "claude3_previous_pause", "") == getattr(renpy.store, "claude2_pause", "") and getattr(renpy.store, "claude5_previous_response", "") == getattr(renpy.store, "claude4_response", "") and getattr(renpy.store, "claude4_response", "") in ("stand", "press") and getattr(renpy.store, "claude5_previous_repair", "") == getattr(renpy.store, "claude4_repair", "") and getattr(renpy.store, "claude4_repair", "") in ("reprint", "overlay") and getattr(renpy.store, "claude5_previous_paid", 0) == getattr(renpy.store, "claude4_own_print_paid", -1) and getattr(renpy.store, "claude4_previous_reception", "") == getattr(renpy.store, "claude3_reception", "") and getattr(renpy.store, "claude3_reception", "") in ("table", "door") and getattr(renpy.store, "claude4_previous_reading", "") == getattr(renpy.store, "claude3_reading", "") and getattr(renpy.store, "claude3_reading", "") in ("aloud", "quiet")
    $ claude6_has_ch02_echo = claude6_has_ch02_echo and getattr(renpy.store, "claude3_reply_parked", False) is True and getattr(renpy.store, "claude3_first_chapter_finished", False) is True and getattr(renpy.store, "claude3_hour_kept", False) is True and getattr(renpy.store, "claude3_novel_chapter", 0) == 2 and getattr(renpy.store, "claude4_lost_wage_repaid", False) is True and getattr(renpy.store, "claude4_claim_withdrawn", False) is True and getattr(renpy.store, "claude4_meal_taken", False) is True and getattr(renpy.store, "claude4_sites_changed", 0) == 4 and getattr(renpy.store, "claude4_novel_chapter", 0) == 2 and getattr(renpy.store, "claude4_old_print_cost", 0) == 18 and getattr(renpy.store, "claude4_new_print_cost", 0) == (18 if getattr(renpy.store, "claude4_repair", "") == "reprint" else 6) and getattr(renpy.store, "claude4_own_print_paid", 0) == (9 if getattr(renpy.store, "claude4_repair", "") == "reprint" else 3) and ((getattr(renpy.store, "claude4_response", "") == "stand" and getattr(renpy.store, "claude4_private_page_shared", False) is True) or (getattr(renpy.store, "claude4_response", "") == "press" and getattr(renpy.store, "claude4_private_page_shared", None) is False))
    $ claude6_previous_drying = getattr(renpy.store, "claude2_drying", "") if claude6_has_ch02_echo else ""
    $ claude6_map_returned = False
    $ claude6_public_clear = False
    $ claude6_new_time_agreed = False
    $ claude6_reading_start = ""
    $ claude6_pause_sign = ""
    $ claude6_pause_used = False
    $ claude6_old_guess_written = False
    $ claude6_guess_admitted = False
    $ claude6_guess_play = ""
    $ claude6_player_guess_written = False
    $ claude6_readback_done = False
    $ claude6_old_guess_kept = False
    $ claude6_second_chapter_finished = False
    $ claude6_time_kept = False
    $ claude6_novel_chapter = 2
    call claude06_scene1
    call claude06_scene2
    call claude06_scene3
    call claude06_scene4
    call claude06_scene5
    $ persistent.main_claude_ch06_seen = True
    return

label claude06_scene1:
    $ chapter = "Claude 第六章 / 01 · 图上的四个地方"
    scene bg echo morning with dissolve
    show sprite claude as claude at sprite_breathe(0.65) with dissolve
    "第十三日八点五十五，Claude打开柜子，拿出一只空硬夹。蓝封小说仍留在自己的布袋里，没和待领的纸并排放。"
    if claude6_has_ch05:
        l_you "今天这只夹子可以用？"
        l_cl "地点图用。昨天那四页已经跟冯姐走了。"
        "她将九点到九点二十那格转给你看，下面没有补上被划去的晚间共读。你接住硬夹，留给原约的一张图。"
    else:
        "她让你先看预约本：鞋铺的一张地点图，九点到九点二十，四处待核。昨天的装箱单已交还，今天不再收回来重数。"
        l_you "我拿夹子。你说放哪儿。"
        l_cl "桌中间。先别替它找第五个地点。"
    "九点整，鞋铺店主展开原图。桥口、茶摊、书店、东廊四处都画着点，茶摊的点却落在路另一边，门口朝向也倒了。"
    "Claude请店主照自己的送货路线走着说一遍，你将纸转到正向，没替来人补自己熟悉的近路。她把错的一小段圈出，让店主确认。"
    l_cl "是门换边，还是路换边？"
    "店主用手指点出正门，她只改朝向，再核另外三处。九点十八分，四个点都对清；店主亲自沿图指完，收回唯一那张原件。"
    "九点二十，Claude合上空夹，放回柜里。桌上没有留下四张新委托，也没有要求店主等小说读完再来取图。"
    $ claude6_map_returned = True
    "九点二十五分，姚师傅来放归还的杯篮。杯子还没卸齐，他先问今天下午在哪儿听小说，好决定送完货往哪边走。"
    if claude6_has_ch05:
        l_cl "今天没有那场。昨天你听见的明日下午，我没答应。"
        l_you "那句是我擅许的。也不是她说累了要改一天。"
        if claude6_previous_repair == "return":
            "Claude说明昨天已在陶姐柜台亲口说清，姚师傅当时不在。他将记路的便纸转过来，把下午听书那行划掉。"
        else:
            "Claude说明昨天亲写的回答已交陶姐，姚师傅没有读到。她当面把没有另约说清，他才将便纸上的时刻划去。"
        if claude6_previous_response == "correct":
            l_cl "陶姐面前那一行早撤了。你听到的也不能留着等我补。"
        else:
            l_cl "我昨天离开过一会儿，没让人替我添一个新时刻。"
    else:
        "姚师傅拿一张未署名的便纸来核实。Claude说自己没约公开念小说，让他别照那一行专程绕路；你没有替这句话补上昨日怎样同行。"
        l_cl "问到我了，答案就是没有这场。杯篮放这边就好。"
    "姚师傅将篮子卸空，说那就按原送货路走，不再留出下午。他没请Claude拿私人书出来证明，也没收一笔被取消的活动费。"
    $ claude6_public_clear = True
    "他走后，Claude拉出自己的椅子，刚坐稳就碰到椅背上的布袋。她托住袋底，将小说拿到手里，朝凳脚看了一眼。"
    l_you "还有一个地点要改？"
    l_cl "袋子。我要坐在这里，它不能先占满。"
    "她把袋子挂到内侧，自己坐下。工作本合在桌上，手却已经顺着蓝封找到了那张还没挪到结尾的窄签。"
    return

label claude06_scene2:
    $ chapter = "Claude 第六章 / 02 · 谁先把下一句念出来"
    scene bg echo morning with dissolve
    show sprite claude as claude at sprite_breathe(0.65) with dissolve
    "十一点四十分，Claude从小摊带回两份热饼，自己的有糖酥边，你的按刚才点的口味装好。她将两袋放到小台，先掰自己那块。"
    "酥边裂得太快，掉到她掌心里。她想把碎屑倒回饼上，倒了一半，又觉得拿纸接会更好；最后纸和饼一起抬着，嘴迟迟没吃到。"
    l_you "不用把它拼回原形。"
    l_cl "我还没同意让它全到袖子里。"
    "她将手放低，自己咬一口，终于把酥边救回来。你把干净纸推近，她用来垫碎屑，没有拿来塞小说。"
    if claude6_has_ch05:
        l_you "姚师傅那句已经说清。昨晚的七点，不能也算今天恢复吧。"
        l_cl "不能。今天要再问。"
        "她将本子里划过的那张便纸合回去，没有把昨天的横线擦掉。你看见厚座垫还留在柜中，也没先将它拉出来。"
    else:
        "你问她下午是否还留给工作。她翻开今天的小本子，指给你看已经完成的地点图，再把本子合上，没展示之前给谁写过的私约。"
        l_cl "我想去河边读书。今天两点十分到两点五十。你愿意来听吗？"
    if claude6_has_ch05:
        l_cl "我今天还想念给你听。两点十分到两点五十，河边那张长凳。"
        l_you "愿意。你开口的时候，我先听完。"
        l_cl "你也可以开口。不要把今天过成只剩我喘气。"
    else:
        l_you "愿意。先听你念哪一段？"
        l_cl "汤勺之后。你别替我直接翻到最后。"
    $ claude6_new_time_agreed = True
    "她打开柜门，取出两只干净座垫，一厚一薄。厚的在手里多停一会儿，她没立刻交给你，而是抱到自己臂弯。"
    if claude6_has_ch05:
        l_you "今天那只厚的换位置？"
        l_cl "昨天试过，确实软。我今天也想坐。"
    else:
        l_you "你想带哪只？"
        l_cl "厚的。这次不是给来读稿的人挑。"
    "她问你薄的是否合适，你说够用。她才将薄垫递来，没怕你嫌硬便把自己的换过去；抱起厚垫时，书袋刚好挤到肘边，她又放下来重拿。"
    l_you "还可以分两趟。"
    l_cl "可以。别把读书那一趟分给别人。"
    "座垫先放到台边，她从干柜取出两只干净杯子和小水壶。壶盖没旋正，她再拧一回；你等她说要不要你拿，才接过合好的壶。"
    l_cl "读到一半要停，你会怎么说？"
    l_you "直接说。怕碰上你那句还没说完。"
    "她用指尖点一张空便纸，没有写规则。你刚想抬杯，她先伸手挡在杯底，免得你将午饭的水洒到她膝上。"
    l_cl "现在不用演停。先选谁念。"
    menu:
        "请她先念，举起自己的杯子示意想停。":
            $ claude6_reading_start = "her"
            $ claude6_pause_sign = "cup"
            l_you "你先念。我想停时，举杯等你到句号。"
            l_cl "可以。要是你只想喝水，就把杯子放回去。"
            "她把书收进自己的袋内，给你留那只边沿更宽的杯子。你试着提起又放下，杯底只轻轻碰桌，没有遮住她的下一句。"
            l_you "不是每喝一口都让门房停工。"
            l_cl "他已经把尺用进锅里。不能再靠你的杯子开饭。"
            "她将空便纸折好放回公用盒，没另塞一条给你猜是什么信号。书准备由她托，你准备接话时先看她是否念完。"
        "自己先念，请她用空纸签提醒到句号停。":
            $ claude6_reading_start = "you"
            $ claude6_pause_sign = "marker"
            l_you "我先念。你想停，就把这张空签放到那句末尾。"
            l_cl "好。不是拿它替你改字。"
            "她将空纸裁成窄条，试着横放在书外侧，没有压住原位置签。你读一句午饭已吃完，她把纸向前送了一点。"
            l_you "这句没错。"
            l_cl "所以请别再念一次。"
            "你忍不住笑，她拿回新空签，放在袋内另一格。这张用来停，不写猜测，也不替她宣布哪一句已经过去。"
    "热饼吃完，她擦净指尖，将碎屑纸包折住。她把装书的布袋挂到椅背内侧，水壶也扣好了盖；她看清才放到布袋边。"
    return

label claude06_scene3:
    $ chapter = "Claude 第六章 / 03 · 停在句号，不停在嘴边"
    scene bg river day with dissolve
    show sprite claude as claude at sprite_breathe(0.65) with dissolve
    "两点十分，两只座垫铺到长凳上，厚的留在Claude那边。她先理开裙角才坐下，把布袋放到身侧；你将水壶摆在平石上，两只杯子之间留出翻书的空处。"
    "她取出一张新的小便纸，亲手写下借勺人三个字，放在封里。这是今天开读前留下的猜测，原位置签另停在第二章，不拿其中一张顶掉另一张。"
    $ claude6_old_guess_written = True
    l_you "还留这位？"
    l_cl "留。船夫肯借，不等于我已经信他。"
    "她没往后偷看结尾，先将便纸压稳，自己的杯子移到离书更远的一端。河上的小船从桥下出来，橹声恰好盖住半个词。"
    if claude6_previous_drying == "spread":
        l_you "这回不用替屋檐看雨。手留给纸边。"
        l_cl "记得。上次你抬头，书先替你弯了一下。"
        "她托稳旧书脊，将那根翘出的线头避开；你只扶她递来的页角，不把曾晾过的书又摊到同样宽。"
    elif claude6_previous_drying == "cloth":
        l_you "这张角你按，还是我按？"
        l_cl "按递给你的那一角。干布今天不用进书里。"
        "她把手帕留在袋内，你等她托稳，再压住朝你卷起的一小边。这里没有公共湿书，也没有拿私人封面当桌布。"
    else:
        "她自己托住书脊，让页角朝你展开。你等她点出需要扶的位置才按住一角，没因为薄书不好拿就整本接过去。"
    if claude6_reading_start == "her":
        "Claude先念门房带着尺回厨房。刚念到锅，她将刮字读成挂，停了一下，自己退回去重念。"
        l_you "锅可以挂，尺暂时放下来。"
        l_cl "我听到了。你不用替它添挂钩。"
        "下一段里，那双穿走的鞋终于回到窗台，鞋面却挂着一只锅盖。你举起杯，她将目光从书页抬起，念完鞋带被绑住的句子才停。"
        l_you "锅盖到底挂哪儿？我没看清。"
        "她把书稍转向你。你指着带字问，她沿那行慢慢念回来，没有一口气解释后面的三段。"
        l_cl "鞋带。不是门房的腰带。"
        l_you "我先把人从锅里拿出来。"
        "她终于笑了，肩头带得书轻轻一动。你压住那一角，等她重新找到那行，再把杯子放回石面。"
    else:
        "你接过她托稳的书，先念门房用尺刮锅。念到鞋挂回窗台，顺口将锅盖读成锅，你自己也停了半拍。"
        "Claude把新空签放到这一句末尾，手没有拦在你的嘴前。你读完那句，才低头看她指的两个字。"
        l_cl "盖。请别替他挂整只锅。"
        l_you "你刚才很想马上说？"
        l_cl "想。让你念完以后，锅更大了。"
        "你从鞋带那句重读，终于只让一只锅盖上去。她将空签拿回，自己托住翻开的另一边，没有顺势接完你还没念的词。"
        l_you "这回可以继续？"
        l_cl "可以。我还等着他把锅盖摘下来。"
        "你们的手各留在一边，风过来时，她用指节轻轻碰一下页外沿，请你别把整条纸签也按进正文。"
    $ claude6_pause_used = True
    "她看着窗台挂锅盖的那句，忽然想试着不笑念完。嘴角刚压平，目光撞到你这边，又把书抬高，试图用蓝封遮住一点。"
    l_you "我还没说话。"
    l_cl "你脸上已经像要说了。"
    "你把要接的半句留住，她重新念到鞋带，还是笑出一个很轻的气音。书没遮住肩头那一下，她自己也知道，终于放低。"
    l_cl "好。先让我笑完。"
    l_you "这次不用举杯？"
    l_cl "不用。笑得出来的时候，我会自己停。"
    "这一段读完，你松开页角，Claude将书重新托在自己膝上。她挪好原位置签，没有翻过下一段的开头。"
    "两点二十五分，Claude伸手去拿自己的杯子，却发现水壶放得偏远。她刚探身，书脊从膝上向前滑了半寸。"
    l_you "要我托书，还是递壶？"
    l_cl "递壶。书我拿着。"
    "你将壶送到她够得着的地方，她挪近杯子，手没有在半空等你替她倒。第一杯倒得少，她又补一点，才把壶放稳。"
    l_cl "你别一直盯着我的杯子。又不是倒水也要叫停。"
    l_you "在看水有没有够。"
    l_cl "够。现在看书。我想让你也听见下一句。"
    "她向旁边挪出一点位置，问你能否坐近些看那行。你点头才挪过去，衣袖之间仍留着翻页的空处，谁也没把靠近写成别的答复。"
    return

label claude06_scene4:
    $ chapter = "Claude 第六章 / 04 · 这回是我猜错"
    scene bg river day with dissolve
    show sprite claude as claude at sprite_breathe(0.65) with dissolve
    "两点三十分，书中的船夫开始找丢失的鞋。他说鞋被穿走时，借勺的人一直同他在对岸补船，没有离开过那块破船板。"
    "门房把窗台上的鞋拿下来，鞋底粘着另一家灶间的灰；去过哪一家还没写明，借勺的人却确实不在那里。Claude看完，指尖往前页退了半行。"
    l_you "船夫这句，要重读吗？"
    l_cl "不用。我看清了。"
    "她把封里今天新写的小便纸抽出来，借勺人三个字刚好露在你们之间。铅笔在袋里，她的手向袋口动了一下，又留回书页边。"
    l_you "你想添下一位？"
    l_cl "想把这位留下。还有，我这回猜错了。"
    "她说完看向你，嘴角还在往回收。你没立刻举杯，也没伸手把她那张纸抽到自己这边看个够。"
    l_you "借勺子还没还，可以继续盯他？"
    l_cl "可以。但他没偷这双鞋，不能拿没还勺子顶过去。"
    "她将小纸翻到背面，背面是干净的。没有写其实本来想猜别人，也没有往那三个字上加一个作者印错。"
    l_you "第一次肯把这句念给我听。"
    if claude6_has_ch05:
        l_cl "你先别替我圆回来。猜错的是我。"
    else:
        l_cl "那就让它完整留下。你还没猜过今天这一段。"
    "她低头又看一眼船夫的句子，把原猜纸放回封里，留出它被看见的一角；最终是谁做的，下一页也还没有揭开。"
    $ claude6_guess_admitted = True
    menu:
        "也写一张自己的猜测，与她的原猜并排留着。":
            $ claude6_guess_play = "pair"
            l_you "我也写。你愿意把两张留在一起吗？"
            l_cl "愿意。你自己写，不用替我补结论。"
            "你用一张新的干便纸写下大帽子的主人，签自己的名字。Claude等你落完笔才拿过去，先看帽子，又把主人两个字确认一遍。"
            l_cl "我以为你真的把帽子排进七位里面。"
            l_you "我还留了主人。"
            l_cl "很好。帽子不用独自上岸作证。"
            "她将两张新纸并排夹在封里，自己的借勺人朝外，没有偷偷反扣。你还笔，她接回笔套，没替你的字抹平歪着的一横。"
            $ claude6_player_guess_written = True
            "继续读时，你总想瞄那顶帽子，她用指节敲一下真正的正文，让你先把门房的半句话听完，别为了证明自己猜得好漏掉新的鞋印。"
        "把她的原猜留好，交换声音再读一次那段。":
            $ claude6_guess_play = "readback"
            l_you "先留你这张。那段我们换声音再念一遍？"
            l_cl "好。不用为了让我猜对，删掉补船那句。"
            "她把小纸夹回封里，借勺人朝外，未折坏三个字。你们将原位置签暂时横在前页，不新写一张猜测来盖住她的。"
            if claude6_reading_start == "her":
                "这回由你念船夫，Claude接门房。你把补船的补字拖长一点，她手指停在那行，等你拖完才接。"
                l_cl "他补的是船。不是你那口气。"
            else:
                "这回由Claude念船夫，你接门房。她故意将一直在对岸几个字念得很稳，抬眼时你已将要抢的半句咽回去。"
                l_you "门房现在能进来了？"
                l_cl "现在能。鞋别又挂整只锅。"
            "你们读完，Claude笑得向后靠了一点，纸签跟着滑到膝边。她自己接住，你扶稳书页，没有趁那一下摸走她的原猜纸。"
            $ claude6_readback_done = True
    $ claude6_old_guess_kept = True
    "她把自己的三个字再给你看一眼，纸上没有橡皮擦过的毛边。看完就收进封里，不举到路过的人面前问他们谁猜得更准。"
    if claude6_has_ch05:
        l_you "还生我的气吗？"
    else:
        l_you "猜错以后，今天还愿意一起读下去吗？"
    "Claude没立刻回答。她先将书页扶正，杯子喝完那一口才放下，指尖轻轻碰了书外沿。"
    if claude6_has_ch05:
        l_cl "昨天那句还记得。今天这几段，我想继续和你读。"
        "你没有把两件事折成一张已经没事的回条。她将下一段转向你，给你留出开口的地方，也留着自己接话的那一边。"
    else:
        l_cl "愿意。我自己挑的书，后面还想听。"
        "她将下一段转向你。你等到她把那行展开，才接过开头，没有将自己的新猜测抢到正文前面。"
    return

label claude06_scene5:
    $ chapter = "Claude 第六章 / 05 · 原来的字也可以带走"
    scene bg river day with dissolve
    show sprite claude as claude at sprite_breathe(0.65) with dissolve
    "两点四十二分，第二章最后一段念完。门房终于将锅盖从鞋带上卸下，塞回借来的篮子，篮底却多了一个没有说明是谁放的扣子。"
    "Claude看着第三章的题目，没有把它算进今天还剩的八分钟。最终凶手没揭，她把原位置签移到第二章末，先合上书。"
    $ claude6_second_chapter_finished = True
    l_you "还剩一点时间，不读下一页？"
    l_cl "先喝茶。我笑得有点渴。"
    "她倒水时，壶盖轻轻碰了一下石面。你用手扶稳壶底，问她还要不要，她说够了，你才松开，没拿水壶替她决定下一件事。"
    if claude6_guess_play == "pair":
        "两张新猜纸露在封里，一张写借勺人，一张写大帽子的主人。她用拇指各点一下，自己那张没有被压到看不见的下面。"
        l_you "我的也可能留到猜错。"
        l_cl "你今天还没赢。别先把败词准备好。"
        "你低头看了看自己的字，想将主人二字补齐一点。她把铅笔递来，又用另一手扶着封口，让你只改自己的那张。"
        l_you "这一横太歪。"
        l_cl "你可以改横。别顺手把我的人改走。"
    else:
        if claude6_pause_sign == "marker":
            "封里只有她今天的原猜纸，停读空签另放回袋格。原位置签还留在第二章末，没有跟着新空签走。"
        else:
            "封里只有她今天的原猜纸，原位置签留在第二章末。你的宽口杯摆在石面上，身旁没有多带一张停读空签。"
        "你记得门房换过的声音，她刚喝一口水，你故意把盖字念得像要带走整锅。"
        "Claude将杯子放稳才笑，没有含着水接话。她用空出的指节敲一下你手旁的石面，轻轻的，不替这个笑声加一行结论。"
        l_cl "这一句不改了。锅留下。"
        l_you "门房有你的语气。"
        l_cl "他还偷换鞋。别全交给我。"
    "风吹起她的包书纸，名字下面那角还带着旧水痕。她将小角扶平，留着自己写的名字，没有换成经两个人审定。"
    if claude6_reading_start == "her":
        "你拿起宽口杯又放下。她看见杯底碰石，没有再停止自己正在说的话，而是把想喝水那三个字说完。"
        l_you "这次我只是收杯。"
        l_cl "看见了。我的最后一句也不用替它让路。"
    else:
        "她将停读的空签递给你看看，签上没有写一条规矩。你说这张今天没拿来改稿，她点头，自己将它放回另一格。"
        l_cl "下次想停，仍可以直接说。纸只是今天拿着顺手。"
    "两点五十，Claude把水壶盖合好，杯子各擦干一只。你收自己那只，她收她的；她站起来前先托住小说，不让书跟裙角一起从膝上滑走。两只座垫叠好，她抱厚的，你拿薄的。"
    $ claude6_time_kept = True
    l_you "你今天那句猜错，要带回去吗？"
    l_cl "已经在书里了。你别帮我留在这里。"
    "她把封里两边压好，自己的原猜纸仍有一角朝外。你等她将袋扣好才拿起水壶，没有把合书看成请你替她答明天。"
    "沿河回去时，她走到较窄的一段石路，回头问你壶是否要换手。你说现在拿得稳，她便放慢半步，等两人的步子走到一块。"
    l_you "我还以为你会先替我换过去。"
    l_cl "手还在你那边。问一句没有多远。"
    "你把壶拎近自己身侧。她将书袋往另一肩挪，空出的手轻轻提住被风卷起的裙角，鞋尖绕过路边的水洼，没有催你用完最后一句话。"
    "她没有给第十四日另写一个时刻。今天共读的四十分钟结束了，新的纸与原来的字，都被她带在自己的袋里。"
    # 按需CG锚点：scene4她抽出新写的借勺人原猜纸，先看字，再抬眼承认猜错。
    # 同镜位可做低头护纸与放松肩头抬眼两动作；现无PNG、不调用、不解锁。
    return
