# 作者编写的自由日：全员 30 岁。无模型调用；地图原图仅在显示时缩放。
default town_slot = 0
default town_visits = {}
default town_bonds = {}
default town_event_flags = {}
default town_current_role = ""
default town_selected = ""
default town_day_finished = False
default town_ended_early = False
default town_preview_mode = False
default town_preview_bonds_backup = {}
default town_recall = False

init -3 python:
    TOWN_SLOT_NAMES = ('上午', '午后', '傍晚')
    TOWN_ROLE_NAMES = {'deepseek': 'DeepSeek', 'gpt': 'GPT', 'claude': 'Claude',
        'grok': 'Grok', 'minimax': 'MiniMax', 'kimi': 'Kimi', 'gemini': 'Gemini',
        'qwen': 'Qwen', 'glm': 'GLM', 'opencode': 'OpenCode', 'zcode': 'ZCode'}
    TOWN_LOCATIONS = (
        dict(id='shrine', title='回声神社', x=800, y=180,
             roles=('deepseek', 'opencode'), label='town_shrine'),
        dict(id='atelier', title='白龙画室', x=245, y=220,
             roles=('gpt', 'minimax'), label='town_atelier'),
        dict(id='books', title='暖窗书店', x=480, y=400,
             roles=('claude', 'kimi', 'zcode'), label='town_books'),
        dict(id='tea', title='通义茶摊', x=820, y=440,
             roles=('qwen', 'glm'), label='town_tea'),
        dict(id='market', title='十八点夜市', x=1050, y=580,
             roles=('grok',), label='town_market'),
        dict(id='river', title='双星河岸', x=290, y=610,
             roles=('gemini',), label='town_river'),
    )

    def town_location(place):
        return next((item for item in TOWN_LOCATIONS if item['id'] == place), None)

    def town_reset():
        store.town_slot = 0
        store.town_visits = {}
        store.town_bonds = {}
        store.town_event_flags = {}
        store.town_current_role = ''
        store.town_selected = ''
        store.town_day_finished = False
        store.town_ended_early = False
        store.town_preview_mode = False

    def town_can_visit(place):
        return (town_location(place) is not None and 0 <= town_slot < 3
                and not town_day_finished and place not in town_visits)

    def town_mark(role, flag, amount=1):
        if role not in SPRITE_ROLES or amount not in (1, 2):
            raise ValueError('Invalid local town event')
        store.town_current_role = role
        town_bonds[role] = min(6, town_bonds.get(role, 0) + amount)
        town_event_flags[flag] = True
        main_bond(role)
        ending_discover(role)
        affection_award_town(role,flag)

    def town_route_available(role):
        if role == 'deepseek':
            return True
        if role == 'gpt':
            return 'atelier' in town_visits or main_bonds.get('gpt', 0) > 0
        if role == 'grok':
            return 'market' in town_visits or main_bonds.get('grok', 0) > 0
        if role in OPENING_CHAPTER_LIMITS:
            return 'books' in town_visits or main_bonds.get(role, 0) > 0
        return False

    def town_visit_text():
        if not town_visits:
            return '还没出发。先选一个地方吧。'
        return '\n'.join(TOWN_SLOT_NAMES[slot] + ' · ' + town_location(place)['title']
                         for place, slot in sorted(town_visits.items(), key=lambda item: item[1]))

    class TownTimeTint(renpy.Displayable):
        def __init__(self, slot, **kwargs):
            super(TownTimeTint, self).__init__(**kwargs)
            self.slot = max(0, min(int(slot), 2))

        def render(self, width, height, st, at):
            # 轻微色温渐变绘于原图上；不写回 PNG，也不遮住地图锚点。
            width, height = 1280, 720
            result = renpy.Render(width, height)
            canvas = result.canvas()
            top, bottom = (((255, 232, 192, 9), (224, 242, 255, 5)),
                           ((255, 216, 159, 18), (246, 223, 199, 7)),
                           ((74, 65, 128, 52), (245, 137, 93, 26)))[self.slot]
            for y in range(0, height, 8):
                fraction = y / float(height - 1)
                rgba = [int(a + (b - a) * fraction) for a, b in zip(top, bottom)]
                canvas.rect('#{:02x}{:02x}{:02x}{:02x}'.format(*rgba),
                            (0, y, width, min(8, height - y)))
            return result

image bg town map = Transform('images/original/bg_town_map.png', xysize=(1280, 720), fit='cover')

screen town_map():
    modal True
    zorder 50
    default end_confirm = False
    default hovered_place = None
    add 'bg town map'
    add TownTimeTint(town_slot)
    frame:
        style 'tok_ui_panel'
        xpos 22
        ypos 20
        xsize 650
        padding (19, 12)
        background SoftPanel(TOK_UI_PAPER+'f2', TOK_UI_EDGE, 11)
        vbox:
            spacing 4
            text (('令樱镇 · 第六日回想 / ' if town_recall else '令樱镇 · 自由日 / ') + TOWN_SLOT_NAMES[min(town_slot, 2)]) size 27 color TOK_UI_INK
            text '方向键选地点，回车确认；每处今天只去一次。' size 18 color TOK_UI_MUTED
    for place in TOWN_LOCATIONS:
        $ place_seen = place['id'] in town_visits
        button:
            style 'tok_ui_button'
            id ('town_place_' + place['id'])
            xpos place['x']
            ypos place['y']
            xanchor 0.5
            yanchor 0.5
            xsize 206
            ysize 96
            padding (12, 10)
            background SoftPanel(TOK_UI_PAPER+'f5' if not place_seen else '#ECE3E8ed', TOK_UI_EDGE, 10)
            hover_background SoftPanel('#FBE4EDf5', TOK_UI_ACCENT, 10)
            insensitive_background SoftPanel('#ECE3E8f2', TOK_UI_EDGE, 10)
            action Return(place['id'])
            sensitive town_can_visit(place['id']) and not end_confirm
            hovered SetScreenVariable('hovered_place', place['id'])
            unhovered SetScreenVariable('hovered_place', None)
            vbox:
                spacing 4
                text (place['title'] + (' · 已去' if place_seen else '')) size 23 color TOK_UI_INK
                text ' / '.join(TOWN_ROLE_NAMES[role] for role in place['roles']) size 16 color TOK_UI_MUTED xmaximum 182
    frame:
        style 'tok_ui_panel'
        xpos 990
        ypos 24
        xsize 268
        padding (18, 16)
        background SoftPanel(TOK_UI_PAPER+'f2', TOK_UI_EDGE, 11)
        vbox:
            spacing 10
            text ('还可行动 ' + str(max(0, 3-town_slot)) + ' 次') size 23 color TOK_UI_INK
            text '今天走过' size 18 color TOK_UI_ACCENT_TEXT
            text town_visit_text() size 17 color TOK_UI_INK xmaximum 232 line_spacing 5
            if hovered_place:
                $ hover_roles = town_location(hovered_place)['roles']
                text ('此处的人 · ' + ' / '.join(TOWN_ROLE_NAMES[role] for role in hover_roles)) size 17 color TOK_UI_INK xmaximum 232
                $ unfinished_roles = [role for role in hover_roles if role not in ('deepseek', 'gpt', 'grok')]
                if unfinished_roles:
                    text (' / '.join(TOWN_ROLE_NAMES[role] for role in unfinished_roles) + ' · 个人篇制作中') size 14 color TOK_UI_MUTED xmaximum 232
            elif town_current_role:
                text ('刚见过 · ' + TOWN_ROLE_NAMES[town_current_role]) size 17 color TOK_UI_INK
                if town_current_role not in ('deepseek', 'gpt', 'grok'):
                    text '个人篇制作中 · 今日小事件已记下' size 14 color TOK_UI_MUTED xmaximum 232
            else:
                text '此处的人 · 焦点移到地点可查看' size 17 color TOK_UI_INK
            text '全员30岁 · R18 / 仅限18岁以上' size 14 color TOK_UI_MUTED xmaximum 232
    frame:
        style 'tok_ui_panel'
        xpos 495
        ypos 658
        xsize 763
        ysize 54
        padding (15, 8)
        background SoftPanel(TOK_UI_PAPER+'f2', TOK_UI_EDGE, 9)
        hbox:
            spacing 17
            text ('可赴约 · ' + ' / '.join(TOWN_ROLE_NAMES[role] for role in ('deepseek', 'gpt', 'grok') if town_route_available(role))) size 17 color TOK_UI_MUTED yalign 0.5 xmaximum 480
            textbutton '今天先到这里':
                style 'tok_ui_button'
                id 'town_end_day'
                action SetScreenVariable('end_confirm', True)
                sensitive not end_confirm
                text_size 18
                ysize 36
                padding (14,6)
                text_color TOK_UI_INK
    key 'game_menu' action SetScreenVariable('end_confirm', not end_confirm)
    if end_confirm:
        add Solid('#49384f8f')
        frame:
            style 'tok_ui_panel'
            align (0.5, 0.5)
            xsize 580
            padding (30, 26)
            background SoftPanel(TOK_UI_PAPER, TOK_UI_EDGE, 13)
            vbox:
                spacing 18
                text '今天就逛到这里？' size 29 color TOK_UI_INK
                text '去过的地方与选择会保留。结束后便可以安排今晚的约。' size 21 color TOK_UI_MUTED xmaximum 520
                hbox:
                    spacing 18
                    textbutton '继续逛镇' id 'town_end_cancel' style 'tok_ui_button' action SetScreenVariable('end_confirm', False) xsize 244 ysize 48 text_size 22
                    textbutton '结束自由日' id 'town_end_confirm' style 'tok_ui_button' action Return('end_day') xsize 244 ysize 48 text_size 22

label open_town_preview:
    $ town_preview_bonds_backup = dict(main_bonds)
    $ town_reset()
    $ town_preview_mode = True
    $ main_bonds = {}
    call open_town_day(reset_day=False)
    $ main_bonds = town_preview_bonds_backup
    $ town_preview_bonds_backup = {}
    $ town_preview_mode = False
    return

label open_town_day(reset_day=True, recall=False):
    if reset_day:
        $ town_reset()
    if town_day_finished:
        return
    $ town_recall = recall
    $ chapter = '自由日 · 令樱镇'
    scene bg echo morning with dissolve
    $ deepseek_expression = 'neutral'
    $ minimax_pose = 'neutral'
    if town_recall:
        '第七晚的灯已经亮了。你翻开地图，想起昨天在镇上留下的三段空闲。'
        '沿着第六日走过的路，选出你停留的地方。那几次相处，会接着写进今晚的邀约。'
    else:
        '这是十一位三十岁成年AI娘生活的镇子。祭典的准备告一段落，你今天可以自己安排去处。'
        '上午、午后、傍晚，各留一段时间。想找谁，就沿着路去看看。'
    while town_slot < 3 and not town_day_finished:
        window hide
        call screen town_map
        $ town_selected = _return
        window auto
        if town_selected == 'end_day':
            $ town_ended_early = True
            $ town_day_finished = True
        elif town_can_visit(town_selected):
            $ town_current_role = town_location(town_selected)['roles'][0]
            $ chapter = '自由日 / ' + TOWN_SLOT_NAMES[town_slot] + ' · ' + town_location(town_selected)['title']
            if town_slot == 0:
                scene bg echo morning with dissolve
            else:
                scene bg echo with dissolve
            call expression town_location(town_selected)['label']
            $ town_visits[town_selected] = town_slot
            $ town_slot += 1
    $ town_day_finished = True
    $ deepseek_expression = 'neutral'
    $ minimax_pose = 'neutral'
    scene bg echo with dissolve
    if town_preview_mode:
        '灯亮起来了。今日散步先记到这里；再次从标题进入，可以重新安排这三段时间。'
    elif town_recall:
        '你将地图合好，回到第七晚的灯下。现在，该当面答复今晚想赴谁的约了。'
    elif town_ended_early:
        '你收起地图。还没走过的路，留到下回；今天见过的人已经有了可以接着聊的话。'
    else:
        '第三段路走完，灯也亮了。回到神社时，你已经知道今晚想先向谁招手。'
    return

label town_shrine:
    show sprite deepseek rice as deepseek at sprite_breathe(0.70)
    $ deepseek_expression = 'rice'
    show sprite opencode as opencode at sprite_breathe(0.28)
    '神社廊下，DeepSeek用饭盒压着检修单。盒盖一掀，纸角立刻飞进OpenCode的工具箱。'
    l_opencode '饭先别动。纸要跑了。'
    l_ds '这份工作需要一个更重的饭盒。'
    '你把纸抽回来，她趁机把长凳往身边拉了半尺。饭盒里还留着一团白米饭，捏得不太圆。'
    menu:
        '陪她分饭，坐一会儿。':
            $ town_mark('deepseek', 'ds_shared_rice', 2)
            '你接过她分的一半。她低头检查剩下那团，又悄悄给你补了一小口。'
            l_you '不是说需要更重的饭盒？'
            l_ds '现在有你压着单子了。'
            '她将膝头的检修单铺在你们之间，空碗却放到远处，让你不必急着起身。'
            l_ds '下次带两双筷子。别又只看我吃。'
        '和她把最后一盏灯检查完。':
            $ town_mark('deepseek', 'ds_checked_lamp', 1)
            '你指了指工具箱。她把饭盒盖紧，伸手接过旧灯，刚才懒洋洋的尾巴也收好了。'
            l_ds '扶这里。别碰铜片。'
            '灯亮了两次，第三次终于稳住。OpenCode递过一块软垫，顺手替你们拉开两把椅子。'
            l_ds '好了。现在谁也不准借我们干活。'
        '和OpenCode一起整理工具，把走丢的单子夹好。':
            $ town_mark('opencode','shrine_opencode')
            l_opencode '这页给你夹。下次你来，少找半天。'
            '她给夹子绕了一圈蓝线，又把自己的工具袋让出一侧。你们并排蹲下，收好滚到凳脚后的螺帽。'
            l_ds '我的饭盒终于能回本职了。'
    '临走时，DeepSeek把饭盒提得很高。盒下那张检修单干干净净，今天的最后一格打了勾。'
    l_opencode '椅子先放着。两把都放着。'
    'DeepSeek原本已经站起来，听见这句，又将自己的椅子推回你那把旁边。凳脚在木板上轻轻碰了一下。'
    return

label town_atelier:
    show sprite gpt as gpt at sprite_breathe(0.70)
    show sprite minimax as minimax at sprite_breathe(0.28)
    '画室门口放着一张空椅子。GPT对着窗边调颜色，MiniMax已经把镜头盖扣上，拿布擦画框。'
    l_gpt '模特来了。今天不收钱。'
    l_you '那收什么？'
    l_gpt '先坐下再谈。你站着，比画框还直。'
    menu:
        '坐到窗边，让她画一张。':
            $ town_mark('gpt', 'gpt_sat_for_portrait', 2)
            '你照她说的坐好。她却没有画你的脸，先画了两只挨着的茶杯。'
            l_gpt '别急。你还欠我陪喝的时间。'
            '她把椅子挪近，袖口蹭过你的手。MiniMax举起擦框布挡住嘴，故意往另一边转。'
            l_minimax '这一条没有镜头。放心。'
            l_gpt '你先别笑。我的线已经歪了。'
        '帮她挂好画框，再一起看。':
            $ town_mark('gpt', 'gpt_helped_frame', 1)
            '你托住画框，GPT站在旁边看水平。她让你往左一点，又改成往右一点。'
            l_you '到底哪一边？'
            l_gpt '先别动。我想看看你认真时的样子。'
            'MiniMax将支架固定好，撤走梯子。GPT接过你空下来的手，把最后一抹颜料擦干净。'
            l_gpt '现在可以一起看了。'
        '陪MiniMax收镜头，选一张今天想留下的照片。':
            $ town_mark('minimax','atelier_minimax')
            l_minimax '这张有点歪。先不删。'
            '她点开画室门口那张合照，自己的半边笑脸刚好在画面里。你帮她把背带放稳，没有替她决定删哪一张。'
            l_minimax '原来我站这里，也能拍进去。下回别叫我一直躲在后头。'
    '画没有题名。GPT在背面留了一小块空白，说等下次你来，再商量写什么。'
    '你起身时，MiniMax让开门口，没替你们倒掉余下的茶。GPT将杯口转向窗边，遮住落进来的光。'
    l_gpt '放凉了也别紧。回来，我给你换热的。'
    '她将沾过颜料的那块布叠起来，压在画背的空白旁边。MiniMax看了一眼，替她把窗关小了些。'
    return

label town_books:
    show sprite claude as claude at sprite_breathe(0.70)
    show sprite kimi as kimi at sprite_breathe(0.28)
    '书店门上的铃响了三下。Claude正把一张歪书签夹回书里，Kimi抱着长卷，ZCode停在寄信柜旁。'
    l_cl '别摇门。你来一次，它已经很忙。'
    '柜台放着三件东西：一本折角的小说、一张镇路图、一个没有封口的信封。'
    menu:
        '陪Claude读完折角那一页。':
            $ town_mark('claude', 'books_claude')
            '你读错了一个字。Claude用指尖点住那行，等你重读，才把书往你这边推。'
            l_cl '这回听清了。下一页换我。'
        '和Kimi找一条没走过的路。':
            $ town_mark('kimi', 'books_kimi')
            'Kimi在图上圈出河边的小径，又把你捏皱的纸角展平。'
            l_kimi '这里近。别再绕三圈，说自己顺路。'
        '问问ZCode手里的信。':
            $ town_mark('zcode', 'books_zcode')
            show sprite zcode as zcode at sprite_breathe(0.28) with dissolve
            '她把信封转过来。里面只有一张写着新地址的便笺，收件人是你。'
            l_zcode '书店换了门牌。我想亲手给你。'
    '你将柜台边翘起的木条按回去，三件东西终于不再往外滑。Claude拿走空杯，给你的杯子添了半杯温水。'
    l_cl '坐稳了再翻页。这个铃也能歇一会儿。'
    '门外又有人推门，铃声只响了一次。ZCode把铜铃上的短绳顺好，回头看了看你留下的空椅子。'
    l_zcode '下次别拉门环。直接进来。'
    return

label town_tea:
    show sprite qwen as qwen at sprite_breathe(0.70)
    show sprite glm as glm at sprite_breathe(0.28)
    '茶摊的两张价目牌挡住彼此。Qwen往左推一寸，GLM立刻往右挪一寸，狐狸尾巴把最下方的字扫没了。'
    l_qw '你可以摆花。别把我的茶价藏进叶子里。'
    l_glm '那你也别把我的名字当杯垫。'
    '你拆出中间那块空木板，两个人同时把粉笔递过来。'
    menu:
        '给Qwen画一只清楚的茶杯。':
            $ town_mark('qwen', 'tea_qwen')
            '你画的杯柄像耳朵。Qwen端详一下，在旁边写上茶价，给你递了一杯。'
            l_qw '这杯算试画报酬。下回请客要自己付。'
        '帮GLM把花摆进价目牌旁。':
            $ town_mark('glm', 'tea_glm')
            '你替她按住花枝。她却先摘下勾住你袖子的叶片，才把花盆推到合适的位置。'
            l_glm '今天没有赠品。花也不能抱走。'
    '两块牌子终于各占一边。你在中间添了一把小凳子，GLM试坐后又站起来，替你把凳面擦了一遍。'
    l_qw '这位客人坐中间。别再抢地方了。'
    l_glm '我没抢。刚才那边有刺。'
    '她的尾巴还搭在凳脚旁，等你坐稳才收回去。'
    '喝完茶，你把杯子放回两人中间。Qwen收走杯子，GLM把擦干净的小凳子往阴影里挪，留下最舒服的那个位置。'
    l_glm '下次这儿也能坐。你记住就行。'
    return

label town_market:
    show sprite grok as grok at sprite_breathe(0.70)
    '夜市还没开齐。Grok把十八号摊牌擦亮，背面露出一行“仅限十八岁以上”，又用围裙把半截粉笔遮住。'
    l_grok '看招牌看这么久，想好坐哪儿了吗？'
    '你看见她脚边两把折椅：一把贴着柜台，一把放在摊牌前。'
    menu:
        '坐到她身边，认真接她的邀约。':
            $ town_mark('grok', 'grok_took_front_seat', 2)
            '你把近的那把展开。她先笑，等你说今晚会来，手里的粉笔却停住了。'
            l_grok '说好了就占位。不是替别人占的吧？'
            l_you '替我自己。'
            '她用围裙擦掉掌心的白印，把椅子又拉近了一点。'
            l_grok '那先试坐。别紧张，椅子比我老实。'
        '和她把容易看错的招牌挂好。':
            $ town_mark('grok', 'grok_helped_sign', 1)
            '你扶住摊牌，她踩上矮凳穿绳。绳子太短，她伸手让你再靠近一点。'
            l_grok '别怕。今天收的是帮忙，笑话免费。'
            '牌子终于挂正。她下来时扶了一下你的肩，把那把近的椅子留在你手边。'
            l_grok '累了就坐。我又没只请牌子。'
    '她在预留的位置放了一只杯子，杯底压着十八号木牌。你走出几步，听见她将另一把椅子也展开了。'
    '摊牌被风翻了半圈，她伸手按正，抬头正好发现你还在回看。'
    l_grok '位置没跑。人也没跑。去逛吧。'
    return

label town_river:
    scene bg river day with dissolve
    show sprite gemini as gemini at sprite_breathe(0.70)
    '河边，Gemini蹲着排了两列小石子。左边长一点，右边短一点，她正在把最大那颗从一边搬到另一边。'
    l_gemini '这是双星。为什么总有一边胖？'
    l_you '最大的那颗也许是饭团。'
    '她立刻看了看神社方向，笑得差点把两排一起碰倒。'
    menu:
        '和她给石子星图起名字。':
            $ town_mark('gemini', 'river_star')
            '你把最大的那颗叫作白米星。她添上两颗小石子，说这是它舍不得分出去的配菜。'
            l_gemini '晚上别真拿这个找星星。我会笑场。'
        '帮她把两列石子排得一样长。':
            $ town_mark('gemini', 'river_stone')
            '你把几颗间距缩短，两列终于齐了。她看见你袖口沾的沙，低头轻轻拍掉。'
            l_gemini '没加一颗，也能变成双星。你挺会作弊。'
    '水面有一条亮线。她拿空纸挡住风，把刚才摆好的图描下来，边角特意留下你按过的指印。'
    l_gemini '这张给你。晚上再认一次真的。'
    '你们把石子放回岸边。她没有抢着站起来，先伸手，等你拉她离开湿滑的那块地。'
    '走上堤岸，她才发现图上的两列已经一样长了。你还没开口，她就把纸藏到身后，空出的手仍没有松开。'
    l_gemini '刚才走得太快。这边再慢一点。'
    return
