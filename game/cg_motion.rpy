# 原生CG轻镜头：PNG字节不变，文字和UI不参与移动；不宣称人物骨骼动画。
default persistent.cg_motion_enabled = True

init -5 python:
    CG_MOTION_KEYS = ('ds_cooldown_exchange','ds_wedding','ds_family','ds_birth','ds_other_hand','gpt_shared_drawing','grok_after_close')

    def cg_motion_enabled_for(key):
        return (key in CG_MOTION_KEYS and bool(persistent.cg_motion_enabled)
                and not bool(persistent.reduce_motion))

    def cg_motion_values(st, enabled=True):
        if not enabled:
            return (1.0, 0.0, 0.0)
        # Minimum overscan covers all offsets; slow independent sine waves do
        # not change anatomy, costume or the drawn hand/bowl action.
        return (1.014 + 0.004 * (1.0 - math.cos(st * math.pi / 5.4)),
                2.0 * math.sin(st * math.pi / 7.3),
                1.25 * math.sin(st * math.pi / 9.1))

    def cg_motion_update(trans, st, at):
        enabled = bool(persistent.cg_motion_enabled) and not bool(persistent.reduce_motion)
        trans.zoom, trans.xoffset, trans.yoffset = cg_motion_values(st, enabled)
        return 0.05 if enabled else None

    def story_cg_picture(cg):
        finite = dynamic_cg_picture(cg)
        if finite is not None:
            return finite
        picture = original_cg_picture(cg)
        if TOK_MOBILE or cg['id'] not in CG_MOTION_KEYS:
            return picture
        moving = Transform(picture, align=(0.5,0.5), function=cg_motion_update)
        clipped = Fixed(moving, xysize=(1280,720), clipping=True)
        # Works both on the story master layer and in the gallery: a settings
        # interaction reselects the child, so OFF does not strand it when ON.
        return ConditionSwitch('persistent.cg_motion_enabled and not persistent.reduce_motion',
                               clipped, 'True', picture, predict_all=True)

