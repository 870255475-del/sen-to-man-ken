default persistent.cg_fan_deepseek_01 = False
default ds_stream_detail = ''

label ds_stream_detour_offer:
    $ ds_stream_detail = ''
    menu:
        '沿石桥浅水走一小段，再回去。':
            call ds_stream_detour
        '今天就在柳树下坐着，先回去吧。':
            $ ds_stream_detail = 'skip'
            'DeepSeek把篮子提起来，没追问。你们沿着平整的石路慢慢回去。'
    return

label ds_stream_detour:
    $ chapter = 'DeepSeek 第二章 / 插段 · 水里那块石头'
    $ story_music('hyy_clouds')
    scene bg river day with dissolve
    $ deepseek_expression = 'happy'
    show sprite deepseek summer as deepseek at sprite_breathe(0.72) with dissolve
    '桥下留着一段脚踝深的缓水。你们先看好石道和回岸的路，她把鞋放在干燥的篮子边。'
    l_ds '只到那块大的。再往前我没走过。'
    l_you '大肥鱼也会怕水？'
    l_ds '怕石头滑。鱼也不是用脸上岸的。'
    '她试好落脚处，一只脚踩上石头，伸出手来。另一只手空着，自然垂在裙侧。'
    $ hide_speaker_portrait = True
    call show_main_cg('fan_deepseek_01')
    l_ds '这边稳。你要不要？'
    menu:
        '握住她递来的手，慢慢走到石头旁。':
            $ ds_stream_detail = 'hand'
            '你先碰到她掌心，她才收拢手指。水绕着石边走，你们没有急着迈下一步。'
            l_ds '等一下。'
            l_you '怎么了？'
            l_ds '我刚才笑得太忙，忘记看路。'
            '她低头确认脚边，再看向你。手没有用力拉，你也没有催。'
        '不牵手，沿旁边的干石道陪她走。':
            $ ds_stream_detail = 'shore'
            '你指了指旁边的石道。她收回手，往岸边让了一点位置。'
            l_ds '那你帮我看篮子。别让饭团也泡脚。'
            l_you '它们在岸上，比我还安全。'
            '她笑着踢起一点很低的水花，没有往你身上泼。'
    '风吹过桥栏，柳叶的影子从她裙边挪到水上。她看了小钟，没再提多走一块。'
    l_ds '好了。到这儿就回。'
    l_you '还早。'
    l_ds '早也可以慢慢擦干。总不能光着脚跑去收花架。'
    scene bg river day with dissolve
    $ hide_speaker_portrait = False
    show sprite deepseek happy as deepseek at sprite_breathe(0.72) with dissolve
    '你们回到篮子旁，用带来的干布擦好脚，等她穿好鞋，再提起没沾水的点心袋。'
    return
