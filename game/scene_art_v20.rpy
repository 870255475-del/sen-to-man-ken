# Working art integration. Background state is ordinary rollback/save state.
# A full redraw with a new camera is one image, not another physical location.
default main_scene_bg_key = 'legacy_echo'
default persistent.cg_v20_c01_safe_connect = False

init -4 python:
    V20_C01_CORE_BG = ('c01_arrival','c01_kitchen','c01_label_desk','c01_gate',
        'c01_teahouse','c01_lane','c01_workbench','c01_dining','c01_departure')
    V20_C01_EXTRA_BG = tuple('c01_bg%02d' % n for n in
        (2,3,4,6,7,8,9,10,11,12,13,15,16,19,21,22,24,25,26,28,29))
    V20_BG_FILES = {key: 'images/backgrounds_v20/'+key+'.png'
        for key in V20_C01_CORE_BG + V20_C01_EXTRA_BG}
    V20_BG_NAMES = {'legacy_echo': 'bg echo'}
    for v20_bg_key, v20_bg_file in V20_BG_FILES.items():
        V20_BG_NAMES[v20_bg_key] = 'bg v20 '+v20_bg_key
        renpy.image(V20_BG_NAMES[v20_bg_key], Transform(v20_bg_file,
            xysize=(1280,720), fit='cover'))

    def v20_bg_name(key=None):
        return V20_BG_NAMES[main_scene_bg_key if key is None else key]

    ORIGINAL_CGS.extend([
        dict(id='v20_c01_safe_connect', title='先把电源断了',
            file='images/events_v20/cg_c01_safe_connect.png',
            flag='cg_v20_c01_safe_connect', compact_dialogue=True),
    ])

label v20_scene_background(key):
    $ main_scene_bg_key = key
    $ main_cg = None
    scene expression v20_bg_name(key) as bg with dissolve
    return

label v20_show_background(key):
    # Keep the existing stage and poses on ordinary camera/work-zone cuts.
    $ main_scene_bg_key = key
    $ main_cg = None
    show expression v20_bg_name(key) as bg zorder -100 with dissolve
    return

label v20_restore_background:
    # Caller rebuilds its actual speakers after a CG has cleared master.
    $ main_cg = None
    scene expression v20_bg_name() as bg with dissolve
    return

label v20_flashback_background(key):
    # Visual flashback does not overwrite the present-time return location.
    $ main_cg = None
    scene expression v20_bg_name(key) as bg with dissolve
    return
