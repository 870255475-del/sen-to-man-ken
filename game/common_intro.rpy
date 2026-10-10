# 原创共通篇片段。长篇各章另行制作；不替代完整共通篇。
# 四位角色均为成年 AI 娘，本作设定年龄 30 岁。
define l_ds = Character("DeepSeek", color="#97d9ff")
define l_gpt = Character("GPT", color="#f8e8c8")
define l_cl = Character("Claude", color="#ffc5b1")
define l_qw = Character("Qwen", color="#c5b7ff")
define l_you = DynamicCharacter("player_name", color="#f5eaf0")

default rice_trust = 0

transform intro_left:
    xalign 0.28
    yalign 1.0
    yoffset 105
    zoom 0.48

transform intro_right:
    xalign 0.72
    yalign 1.0
    yoffset 105
    zoom 0.48

label common_intro:
    $ rice_trust = 0
    $ deepseek_expression = 'neutral'
    $ chapter = "第一章 / 01 · 借一碗饭"
    play music "audio/festival.ogg" fadein 1.0
    call v20_scene_background('c01_arrival')
    "山路尽头亮着一排灯。最后三盏没亮，旁边倒扣着一只饭碗。"
    call v20_show_background('c01_bg02')
    "你放下行李，刚碰到碗沿，长椅后面就冒出一双蓝色的鳍耳。"
    show sprite deepseek rice as deepseek at sprite_breathe(0.72) with dissolve
    l_ds "那个不能动！"
    l_you "有电？"
    l_ds "有饭。"
    l_you "……底下藏着？"
    l_ds "刚才有。现在没有了。"
    "她端着另一只碗站起来。碗里还冒着热气。"
    call opening_ds_first_bowl_begin
    l_you "那你手里这只呢？"
    l_ds "这碗是宵夜。"
    call opening_ds_first_bowl_clear
    l_you "天才刚黑。"
    l_ds "宵夜得趁早。不然会饿。"
    l_you "我是来帮祭典的。请问筹备处在哪儿？"
    l_ds "到了。行李放这儿，我替你看着。"
    l_you "然后我去干活？"
    l_ds "上手这么快，谁介绍你来的？"
    show sprite qwen as qwen at sprite_breathe(0.28) with dissolve
    l_qw "我。现在有点后悔。"
    call v20_show_background('c01_bg03')
    "提着茶壶的姑娘把一张纸压在饭碗底下。"
    l_qw "DeepSeek，签个字。"
    l_ds "这个饭……是自助的吧？"
    l_qw "是。账也请自助结一下。"
    l_you "这儿连吃饭都要签字？"
    l_qw "吃饭不用。借走我的米，还让我送上山，需要。"
    l_ds "我留了米袋。"
    l_qw "空的。还写着‘谢谢代班’。"
    l_ds "字是我亲手写的！"
    l_qw "那真是辛苦你了。"
    "DeepSeek用碗挡住纸上的金额。筷子却从另一边掉了出来。"
    l_you "我帮你捡。别用碗砸我就行。"
    l_qw "她是怕你看见第五碗。"
    l_ds "是第四碗半！"
    l_you "差半碗，值得专门澄清？"
    l_ds "值得。剩下半碗还没盛。"
    l_qw "灯修完之前，不许续。"
    l_ds "修完了啊。"
    l_you "那三盏还是黑的。"
    l_ds "总线没接。接完就得搬下山。"
    l_qw "所以你一直不接？"
    call opening_ds_caught_pose
    l_ds "现在接。现在就接。"
    call opening_ds_caught_pose_clear
    "她看看手中的饭，又看看地上的线，偷偷把碗往你这边挪了一点。"
    menu:
        "替她端一会儿碗。":
            $ rice_trust += 1
            l_you "我拿着。你接线。"
            l_ds "别把勺子给Qwen。"
            l_qw "我不没收饭。"
        "替她搬灯，饭碗留给她。":
            l_you "你接线。我负责搬，行了吧？"
            l_ds "成交。那这一口——"
            l_qw "接完再吃。"
            l_ds "……成交得太早了。"
    hide deepseek
    show sprite deepseek as deepseek at sprite_breathe(0.72)
    call v20_show_background('c01_bg04')
    "DeepSeek把碗放上长椅，蹲到灯架旁。她刚拧开盖子，旧插头便滑出了一截。"
    l_ds "先别碰那条线。"
    l_you "这个？"
    l_ds "手往后。对，抓木头架子。"
    "她拔掉电源，换上一枚新的卡扣。蓝色尾巴抵住架脚，晃动的灯罩停了下来。"
    l_qw "要帮忙吗？"
    l_ds "接头递给我。你带的那枚。"
    $ hide_speaker_portrait = True
    call show_main_cg('v20_c01_safe_connect')
    l_qw "你知道我带了？"
    l_ds "茶壶盖一直在响。又不是装的茶叶。"
    call v20_restore_background
    $ hide_speaker_portrait = False
    show sprite deepseek as deepseek at sprite_breathe(0.72)
    show sprite qwen as qwen at sprite_breathe(0.28) with dissolve
    "三盏灯依次亮起。最旧的一盏有一对歪歪的鲸鱼眼睛。"
    l_you "眼睛也是你画的？"
    l_ds "修好了顺手画的。"
    l_qw "午后就画好了。"
    l_you "那从午后到现在，你在——"
    l_ds "等胶干。"
    l_qw "从第一碗等到第四碗半。"
    l_ds "……今天有点潮。"
    l_you "看起来挺干的。"
    l_ds "你怎么也开始验收我了。"
    "她从口袋摸出一粒干硬的米，低头看了看，立刻藏回去。"
    l_you "那也是在等胶干？"
    l_ds "别问了。傍晚被你们抓到一次就够了。"
    $ chapter = "第一章 / 01 · 傍晚的厨房"
    $ hide_speaker_portrait = True
    call v20_flashback_background('c01_kitchen')
    "傍晚，你来问路时，厨房桌边就是这么一副光景。"
    call show_main_cg('rice_break')
    l_you "我还以为你只是路过厨房。"
    l_ds "路过是饿了才路过的。"
    call v20_flashback_background('c01_bg06')
    show sprite deepseek rice as deepseek at sprite_breathe(0.72)
    "她把碗抱近一点，筷子停在碗沿。脸上的饭粒还没摘掉，眼睛倒先看向你。"
    call show_main_cg('rice_break_caught')
    l_you "旁边这盏灯呢？"
    l_ds "给筹备处的新帮手。"
    l_you "你那时还不认识我。"
    l_ds "所以没写名字。现在可以写了。"
    $ chapter = "第一章 / 01 · 借一碗饭"
    $ hide_speaker_portrait = False
    call v20_restore_background
    call v20_show_background('c01_bg07')
    show sprite deepseek as deepseek at sprite_breathe(0.72)
    show sprite gpt as gpt at sprite_breathe(0.28) with dissolve
    l_gpt "新帮手已经到了？正好，多备的杯子有用了。"
    l_ds "你带了几只？"
    l_gpt "十二只。"
    l_ds "就我们几个，喝得完吗？"
    l_gpt "杯子不用喝。你放过它们吧。"
    hide gpt
    show sprite claude as claude at sprite_breathe(0.28) with dissolve
    call v20_show_background('c01_bg08')
    "Claude抱着灯的清单走来，把一支笔递到你手里。"
    l_cl "名字写这里。不是收据，是饭碗的标签。"
    l_you "刚来就领饭碗？"
    l_cl "厨房少了五只。先标好，免得明天继续少。"
    l_ds "我明天还会来的。"
    l_cl "我知道。所以才现在写。"
    l_you "我的碗也会被借走吗？"
    l_cl "你可以写大一点。"
    l_ds "写再大也只装一碗。"
    "她伸手扶住你膝上的灯。歪眼睛朝着你，背面留着一块干净的纸。"
    if rice_trust:
        l_ds "还有，刚才那口饭……你没偷吃吧？"
        l_you "没有。"
        l_ds "那明天坐我旁边。"
    else:
        l_ds "明天别急着搬灯。先吃饭。"
        l_you "你教我偷懒？"
        l_ds "我教你挑好座位。我旁边那个。"
    l_cl "两位，笔还在手里。"
    l_ds "先写你的。我再给鲸鱼补个笑脸。"
    "你低头写名字。她凑得太近，鳍耳的影子晃过纸面，压住了最后一笔。"
    call v20_scene_background('c01_bg10')
    jump common_ch01_scene2
