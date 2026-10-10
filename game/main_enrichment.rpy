# 原创日常补充。登场角色均为三十岁成年人，玩家外形与性别不预设。
# 由主章入口调用；不改好感、关系、IF、联机或结局状态。
default persistent.main_enrichment_seen_cooldown = False
default persistent.main_enrichment_seen_yukata = False
default persistent.main_enrichment_seen_pool = False
default persistent.main_enrichment_seen_close = False

label ds_extra_cooldown:
    $ chapter = "DeepSeek 第二章 / 补充 · 再凉五分钟"
    scene bg echo morning with dissolve
    $ deepseek_expression = "summer"
    show sprite deepseek summer as deepseek at sprite_breathe(0.72) with dissolve
    "第八天午后，从河岸回来没多久，DeepSeek又从屋里探出头。她换了海蓝夏裙，白荷叶领边在凉风里轻轻动。"
    l_ds "椅子还空着吧？我去拿点东西。"
    "她端来两只小碗。冰镇米点心刚从冷处取出，碗底很快凝了一圈水，她抢先垫好干布。"
    l_you "河边那两包已经不算数了？"
    l_ds "那是干的。这个是凉的。不能混着记。"
    "你接过较小的一碗，她坐到旁边，先把自己的勺子插进最厚的那块。"
    $ hide_speaker_portrait = True
    call show_main_cg('ds_cooldown')
    "她吃得很慢，第一口还含在嘴里，眼睛已经跟着你的勺子走。你故意把碗转了半圈。"
    l_ds "你那块是不是更软？"
    l_you "同一份切出来的。"
    l_ds "位置不同，口感可能不同。"
    l_you "你刚才挑了厚的。"
    l_ds "所以现在想研究薄的。只要一口。"
    call show_main_cg('ds_cooldown_exchange')
    "她把自己的碗推来，挑出一小块留在碗沿。你另取干净的小勺，舀一口到她那边。"
    l_you "交换。别把研究做成单向收费。"
    "她低头尝过，认真停了两秒，随后把你留的那口也往自己跟前挪。"
    l_you "这一口是给我的。"
    l_ds "我知道。我替你防止它滑下去。"
    "你将那块吃掉，她终于不再护着碗沿，笑得勺柄在指间晃了一下。"
    $ hide_speaker_portrait = False
    scene bg echo morning with dissolve
    show sprite deepseek summer as deepseek at sprite_breathe(0.72) with dissolve
    "你喝口水，放下杯子，刚想起身，她先用勺背敲了敲自己的空碗。"
    l_ds "等它不那么凉，再走。"
    l_you "碗都空了。"
    l_ds "凉还在。你摸一下外面。"
    "碗壁的确冰凉。你把它放回布上，坐了回去，她立即将刚才藏在碗后的笑压住。"
    l_you "要等多久？"
    l_ds "五分钟。天气热，很快的。"
    l_you "你是想留碗，还是留我？"
    "她抬眼，又迅速去看杯底。裙边的一点白色荷叶被尾巴轻轻碰动，她把尾巴按到身侧。"
    l_ds "你这么问，碗就很难回答。"
    l_you "那让它休息。你回答。"
    "她盯着空碗，终于伸手把你的水杯推回你够得到的位置。"
    l_ds "想让你再坐五分钟。刚才走回来，一直在看路。"
    l_you "现在看什么？"
    l_ds "看你有没有把我那份也吃完。"
    "你指指两只同样干净的碗。她嘴硬的理由用完了，反而笑着把肩放松下来。"
    l_you "好。五分钟从现在算。"
    l_ds "不要真的掏钟。你掏出来，我就想听它响。"
    "风吹动裙摆，她伸手压了一下，又把杯子拿起。你们慢慢喝完水，谁都没替那只空碗催下一句。"
    $ hide_speaker_portrait = False
    scene bg echo morning with dissolve
    $ deepseek_expression = "summer"
    show sprite deepseek summer as deepseek at sprite_breathe(0.72) with dissolve
    "她收起碗，去把夏裙换好挂起。再出来时穿回常穿的女仆装，手里还握着那块垫碗的干布。"
    $ deepseek_expression = "happy"
    show sprite deepseek happy as deepseek at sprite_breathe(0.72) with dissolve
    l_ds "下次那个薄的，也先让我挑。"
    $ persistent.main_enrichment_seen_cooldown = True
    return

label ds_extra_yukata:
    $ chapter = "DeepSeek 第七章 / 补充 · 没写好的夸奖"
    scene bg echo morning with dissolve
    $ deepseek_expression = "yukata"
    show sprite deepseek yukata as deepseek at sprite_breathe(0.72) with dissolve
    "第十三天午后，雨刚停。DeepSeek喊你在廊外等一下，再出来时，海蓝浴衣的下摆差点绊住门槛。"
    "她停稳，自己提起一边衣角迈过去。小鲸与波纹沿衣袖展开，白腰带已经绕好，两截带头搭在你的椅背上。"
    l_ds "先别评价走路。我第一次穿这件。"
    l_you "那我先评价椅子？"
    l_ds "椅子是原来的，不用重新夸。"
    "她照着镜子转半圈，确认浅浅的衣领与肩头衣料都没带歪，才转脸找那两截白色带头。"
    l_ds "帮我递一下那两头。想重新系一下。"
    l_you "从你身侧递过去，可以吗？"
    l_ds "可以。给我就好，我想自己试着系。"
    "你把两截带头递到她手里。她将衣襟拢稳，看着镜中背后的白蝴蝶结，打算只重理松开的那半边。"
    $ hide_speaker_portrait = True
    call show_main_cg('ds_yukata')
    "旧结解开得很顺利。重绕时却把先留的带头盖住了，她摸了半天，手指只摸到自己的手指。"
    l_ds "刚才还在这里。"
    l_you "它去里面躲你了。"
    l_ds "我不信一条带子比我会藏。"
    "她放松外层，终于抽出带头，重新理平。打结时没急着硬拉，先把压住的小折展开。"
    l_you "你不是说第一次？"
    l_ds "视频看了两遍。刚才只记得第一遍。"
    "白腰带总算系好。她站远一点，把镜子换到另一只手，侧身看背后的结，反而什么都看不清。"
    l_ds "歪吗？你说实话。"
    l_you "结没歪。右边那截短一点。"
    "她调整好，再转回来，原本准备好的得意表情停在一半。你还在看着她，没有看那条腰带。"
    l_ds "现在又哪里不对？"
    l_you "没有。蓝色很衬你的眼睛。"
    l_you "你转过来时，小鲸像跟着你游。很好看。"
    "她张了一下嘴，低头扯扯袖口，再抬头。平常讨第二碗饭时那么快的反应，这回只剩一次眨眼。"
    l_ds "这种要怎么接？"
    l_you "说你听到了也行。"
    l_ds "我听到了。不是让你撤回。"
    "你笑起来，她立即拿袖角遮住自己也在笑的嘴，却遮得太高，差点连眼睛都盖住。"
    l_you "好看就得藏起来？"
    l_ds "我在确认这袖子有多长。"
    "她放下袖子，走到你跟前，主动又转了一小圈。这一次步子放小，衣摆稳稳跟着落回原处。"
    l_ds "再看一次。刚才门槛那次不计。"
    l_you "还是很好看。"
    l_ds "知道了。你先喝水，我去换回来。"
    $ hide_speaker_portrait = False
    scene bg echo morning with dissolve
    $ deepseek_expression = "shy"
    show sprite deepseek shy as deepseek at sprite_breathe(0.72) with dissolve
    "她换回工作女仆装，把浴衣与腰带分别折好，收进干燥的衣袋。今晚挂灯要抬手，这套更方便。"
    l_ds "刚才那句，我会记得。衣服收了也不会忘。"
    "试穿离原先约好的见面还早。她去拿饭盒，你先到前院喝水，等会儿再回廊下找她。"
    $ persistent.main_enrichment_seen_yukata = True
    return

label ds_extra_pool:
    $ chapter = "DeepSeek 第八章 / 补充 · 只跳一下也要试"
    $ hide_speaker_portrait = True
    call show_main_cg('ds_pool')
    "第六周的休息日，你和DeepSeek来到镇上的浅水泳池。她换好深蓝一件式泳装，把毛巾放在右侧的池沿。"
    "白褶边下的小鲸徽纹很醒目。她坐在池边，理开耳边的头发，朝你晃了一下蓝浮板。"
    l_ds "来。我找到不呛水的位置了。"
    l_you "位置会负责不呛水？"
    l_ds "这边的标线浅。先不用踮脚。"
    "她把浮板推给你看，板面上还有几滴没滑下去的水。你伸手接过，她又按住一边。"
    l_ds "先说，你不许笑我。"
    l_you "你还没开始。"
    l_ds "我在河边打水漂，只会一下。"
    l_you "泳池不考那个，也不能往里面丢石头。"
    l_ds "我知道。这里借浮板，不借石头。"
    "她松开手，沿池沿往前走两步，又回来，比划河边那次平着送出去的动作。"
    l_ds "但我总想知道，第二下为什么跳不起来。"
    l_you "今天准备从浮板找答案？"
    l_ds "先看看手腕推水，跟推空气差多少。"
    "她伸手拨过水面，细细的水珠越过浮板，偏偏落到她自己的鼻尖。她停住，闭眼抹了一下。"
    l_ds "差挺多。水会回手。"
    "你还没笑出声，她已经抬起手，摆出要再试一次的架势。"
    l_you "这一回别对着自己。"
    l_ds "看见了。换个方向就行。"
    "她将掌心放平，慢慢送出去。水纹越过浮板边，绕过你们之间的空隙，没有再溅到脸上。"
    l_ds "刚才那次是试水。这个才算。"
    l_you "那你挺会给自己安排重来。"
    l_ds "总不能第一次就把休息日用完。"
    "她扶着浮板蹬了一下腿。板子向前，她的尾巴却先碰到水，拍出比脚还响的一声。"
    l_ds "它抢跑了。"
    "你把浮板让回她面前。她摸了摸板沿，没逞强往深处去，顺着浅水标线重新试了一段。"
    "这次走得直，停得也稳。她站起来时，先看看自己离起点多远，才转向你，鼻尖还挂着小水珠。"
    l_ds "两段。今天终于不只有一下。"
    l_you "这个和水漂不是同一个计数。"
    l_ds "我今天高兴，先借一下。"
    if ds_reply == "love":
        "她朝你伸出手。"
        l_ds "可以牵一下吗？站稳了，也想牵。"
        l_you "可以。"
        "你握住她的手，她笑着晃了一小下，没有把你拉进水里。"
    elif ds_reply == "wait":
        l_ds "下次河边，你看我挑战第二下。"
        l_you "好。我负责数，不提前报喜。"
        "她满意地点头，将浮板推到你手边，留你自己挑下一段。"
    else:
        l_ds "回去不能告诉GLM我被自己溅了。"
        l_you "那要用什么收买目击者？"
        l_ds "水杯里的水。米点心另算。"
    "休息哨响起，她先把浮板放回指定架上，再拿起自己的水杯。你们坐在阴影里，听水慢慢滴到砖面。"
    l_ds "回去练手腕。今天先练喝水。"
    $ hide_speaker_portrait = False
    scene bg echo with dissolve
    $ deepseek_expression = "happy"
    show sprite deepseek happy as deepseek at sprite_breathe(0.72) with dissolve
    "傍晚回到神社，她已换回干燥的女仆装。泳装和毛巾各装一袋，她把借物卡拿出来，确认没有忘还。"
    $ persistent.main_enrichment_seen_pool = True
    return

label ds_extra_close:
    if ds_reply != "love":
        return
    $ chapter = "DeepSeek 第八章 / 恋人补充 · 肩膀先借我"
    scene bg echo with dissolve
    $ deepseek_expression = "summer"
    show sprite deepseek summer as deepseek at sprite_breathe(0.72) with dissolve
    "同一天夜里，泳池的水声已经听不见。DeepSeek洗去水汽，换上海蓝夏裙，端着两杯温水来到廊下。"
    "她把一杯放到你手边，另一杯握在掌心，坐下后却没有喝。你伸手拿杯时，她叫住你。"
    l_ds "先别拿。我有个需要空手的请求。"
    l_you "又要我替你拆点心？"
    l_ds "今晚已经吃够了。不要把我所有请求都装碗里。"
    "她说完，自己先忍不住笑。白荷叶领边随着动作轻晃，她轻轻拢好裙边，朝你挪了小半寸。"
    l_ds "我能靠着你坐一会儿吗？"
    l_you "可以。你想靠哪边？"
    "她认真比较两边，像在看一张特别难选的座位表，最后指向离水杯更远的那侧。"
    l_ds "这边。免得一高兴，把杯子撞翻。"
    $ hide_speaker_portrait = True
    call show_main_cg('ds_close')
    "你往旁边留出一点位置。她先用手背轻碰你的手背，等你把掌心转过来，才将手放进去。"
    l_ds "这样牵，也可以吧？"
    l_you "可以。我能碰碰你的肩吗？"
    l_ds "可以。轻一点，我有点怕痒。"
    "你轻轻落下手。她刚放松，就被垂落的发梢扫过，肩头缩了一下，赶紧转脸看你。"
    l_you "是头发。我的手还没动。"
    l_ds "我知道。我在找是谁先动的。"
    "你替她留好靠肩的位置，让她自己慢慢挨过来。她的脸离得近，说下一句时，声音比刚才轻了些。"
    l_ds "原来坐近，真的会忘词。"
    l_you "你本来想说什么？"
    l_ds "想问你，今天泳池那次笑，是不是笑我。"
    l_you "笑你给尾巴判了抢跑。后来那一段很稳。"
    "她点点头，过了片刻，又将你们交握的手轻轻举起来。"
    l_ds "这个也稳。没有抢跑。"
    l_you "需要再给它颁一张牌？"
    l_ds "不要。它已经有你了。"
    "那句话落下后，她先看了一眼自己的手，再抬眼看你，像没想到自己能这么顺口。"
    l_ds "刚才我说得太快。"
    l_you "我听得清。也喜欢。"
    "她把脸转向廊外，耳边慢慢红起来，却没有把手抽走。你们安静坐了一会儿，她又小声开口。"
    l_ds "你也可以靠过来一点。总让我靠，好像我借得比较多。"
    l_you "我这样靠，可以吗？"
    l_ds "嗯。别把头撞一起就好。"
    "你慢慢挨近，她也轻轻迎过来。两个人的额头差点碰到，她及时停住，笑得肩膀都动了。"
    l_ds "刚提醒过，差点自己先撞。"
    l_you "今天又多一项练习。"
    l_ds "这个可以练久一点。"
    "温水终于没那么热了。她先坐直，给你递杯子，仍把空着的那只手留在你掌心。"
    $ hide_speaker_portrait = False
    scene bg echo with dissolve
    $ deepseek_expression = "summer"
    show sprite deepseek summer as deepseek at sprite_breathe(0.72) with dissolve
    l_ds "下次这边仍留给我。我喜欢靠这一边。"
    "喝完水，她起身收杯，去把夏裙挂好。回来道晚安时又穿回干净的女仆装，临走用指尖轻轻碰了一下你的手。"
    $ deepseek_expression = "shy"
    show sprite deepseek shy as deepseek at sprite_breathe(0.72) with dissolve
    $ persistent.main_enrichment_seen_close = True
    return
