# Only actual selected, story-bound events enter this registry; plans do not.
default persistent.cg_v20_ds01_sort = False
default persistent.cg_v20_ds01_rest_plan = False
default persistent.cg_v20_ds01_hairclip = False
default persistent.cg_v20_c01_safe_connect = False

init -4 python:
    ORIGINAL_CGS.extend([
        dict(id='v20_ds01_sort', title='十分钟的一小盒',
            file='images/events_v20/cg_ds01_sort.png',
            flag='cg_v20_ds01_sort', compact_dialogue=True),
        dict(id='v20_ds01_rest_plan', title='这一段先空着',
            file='images/events_v20/cg_ds01_rest_plan_r2.png',
            flag='cg_v20_ds01_rest_plan', compact_dialogue=True),
        dict(id='v20_ds01_hairclip', title='先别拔夹子',
            file='images/events_v20/cg_ds01_hairclip_r2.png',
            flag='cg_v20_ds01_hairclip', compact_dialogue=True),
        dict(id='v20_c01_safe_connect', title='安全连接',
            file='images/events_v20/cg_c01_safe_connect.png',
            flag='cg_v20_c01_safe_connect', compact_dialogue=True)
    ])
