# v17有限帧动态候选。仅显示层；不注册CG，不修改收藏、关系或剧情状态。
# 两张PNG必须由root原样绑定；运行时Crop，不落地任何裁切／改图文件。
init -4 python:
    import hashlib as dynamic_cg_hashlib
    import struct as dynamic_cg_struct

    DYNAMIC_CG_KEYS = ('fan_deepseek_mishap',)
    DYNAMIC_CG_SOURCES = {
        'fan_deepseek_mishap': {
            'source': 'images/original/cg_fan_deepseek_mishap.png',
            'blink': 'images/original/cg_fan_deepseek_mishap_blink.png',
            'source_size': (1672, 940),
            'source_sha256': '0ef3241017add899086622dd57501d28453955d76bfa694eb8631bc3a002a69c',
            'blink_sha256': 'f3f0c9fdc07bdf16553aa828feaf5d21aa4e228046758973cac0352d3b808059',
            # 源坐标(x,y,w,h)，不是1280x720屏幕坐标。三块互不重叠。
            # 首次沿原件目测标定；root需真实截图确认皮肤／发丝接缝。
            'patches': {
                'left_eye': (702, 173, 77, 73),
                'right_eye': (790, 139, 77, 63),
                'mouth': (784, 220, 57, 47),
            },
        },
    }
    # 一轮4.34s；眼闭0.12s；嘴的轻笑共0.54s。没有每帧函数或推镜。
    DYNAMIC_CG_TIMELINE = (('open', 3.8), ('smile', 0.18), ('blink', 0.12), ('smile', 0.24))
    _dynamic_cg_asset_cache = {}

    def _dynamic_cg_read_asset(path):
        """只读PNG头和SHA；成功结果缓存，失败不缓存以免阻止root补齐素材。"""
        if not renpy.loadable(path):
            return None
        if path in _dynamic_cg_asset_cache:
            return _dynamic_cg_asset_cache[path]
        try:
            with renpy.file(path) as asset:
                header = asset.read(24)
                if (len(header) != 24 or header[:8] != b'\x89PNG\r\n\x1a\n'
                        or header[12:16] != b'IHDR'):
                    return None
                digest = dynamic_cg_hashlib.sha256(header)
                while True:
                    chunk = asset.read(65536)
                    if not chunk:
                        break
                    digest.update(chunk)
                result = (dynamic_cg_struct.unpack('>II', header[16:24]), digest.hexdigest())
            _dynamic_cg_asset_cache[path] = result
            return result
        except Exception:
            return None

    def dynamic_cg_asset_status(cg):
        """精确自身来源守卫；不把同名、重缩放或别的闭眼图当本帧。"""
        key = cg.get('id') if isinstance(cg, dict) else None
        spec = DYNAMIC_CG_SOURCES.get(key)
        if not spec:
            return {'ready': False, 'reason': 'not-target'}
        if cg.get('file') != spec['source']:
            return {'ready': False, 'reason': 'source-path-mismatch'}
        width, height = spec['source_size']
        rectangles = list(spec['patches'].values())
        for x, y, w, h in rectangles:
            if min(x, y) < 0 or min(w, h) <= 0 or x + w > width or y + h > height:
                return {'ready': False, 'reason': 'patch-out-of-source'}
        for index, (x, y, w, h) in enumerate(rectangles):
            for ox, oy, ow, oh in rectangles[index + 1:]:
                if x < ox + ow and ox < x + w and y < oy + oh and oy < y + h:
                    return {'ready': False, 'reason': 'patch-overlap'}
        source = _dynamic_cg_read_asset(spec['source'])
        blink = _dynamic_cg_read_asset(spec['blink'])
        if source is None or blink is None:
            return {'ready': False, 'reason': 'missing-or-invalid-png'}
        if source[0] != spec['source_size'] or blink[0] != spec['source_size']:
            return {'ready': False, 'reason': 'source-size-mismatch'}
        if source[1] != spec['source_sha256'] or blink[1] != spec['blink_sha256']:
            return {'ready': False, 'reason': 'source-sha-mismatch'}
        return {'ready': True, 'reason': 'ready', 'source_size': source[0],
            'source_sha256': source[1], 'blink_sha256': blink[1]}

    def dynamic_cg_enabled_for(key):
        cg = original_cg_by_id(key)
        return (key in DYNAMIC_CG_KEYS and bool(getattr(persistent, 'cg_motion_enabled', False))
            and not bool(getattr(persistent, 'reduce_motion', False))
            and dynamic_cg_asset_status(cg)['ready'])

    def dynamic_cg_phase_at(elapsed):
        """纯时间解析，供静态／原生断言；它不驱动render或redraw。"""
        remaining = float(elapsed) % sum(duration for state, duration in DYNAMIC_CG_TIMELINE)
        for state, duration in DYNAMIC_CG_TIMELINE:
            if remaining < duration:
                return state
            remaining -= duration
        return 'open'

    def _dynamic_cg_build_frames(cg, size=(1280, 720)):
        spec = DYNAMIC_CG_SOURCES[cg['id']]
        base = (spec['source_size'], (0, 0), spec['source'])
        mouth_rect = spec['patches']['mouth']
        mouth = (mouth_rect[:2], Crop(mouth_rect, spec['blink']))
        eye_layers = []
        for part in ('left_eye', 'right_eye'):
            rectangle = spec['patches'][part]
            eye_layers.extend((rectangle[:2], Crop(rectangle, spec['blink'])))
        source_frames = {
            'open': Composite(*base),
            'smile': Composite(*(base + mouth)),
            'blink': Composite(*(base + tuple(eye_layers) + mouth)),
        }
        # 与现有original_cg_picture的cover→contain缩放顺序一致。
        return {state: Transform(Transform(frame, xysize=(1280, 720), fit=('contain' if TOK_MOBILE else 'cover')),
                    xysize=size, fit='contain') for state, frame in source_frames.items()}

    def dynamic_cg_frame(cg, state='open', size=(1280, 720)):
        """标定／截图用的确定帧；不收藏、不表示实际动画已测。"""
        if state not in ('open', 'smile', 'blink'):
            raise ValueError('Unknown finite CG frame: ' + str(state))
        if not dynamic_cg_asset_status(cg)['ready']:
            return original_cg_picture(cg, size)
        return _dynamic_cg_build_frames(cg, size)[state]

    def dynamic_cg_animation(cg, size=(1280, 720)):
        """SDK Animation负责边界定时，非自写每帧回调。"""
        if not dynamic_cg_asset_status(cg)['ready']:
            return None
        frames = _dynamic_cg_build_frames(cg, size)
        arguments = []
        for state, duration in DYNAMIC_CG_TIMELINE:
            arguments.extend((frames[state], duration))
        return Animation(*arguments, anim_timebase=False)

    def dynamic_cg_picture(cg, size=(1280, 720)):
        """接在story_cg_picture最前：None意味着继续原显示链。"""
        if not isinstance(cg, dict) or cg.get('id') not in DYNAMIC_CG_KEYS:
            return None
        if not dynamic_cg_asset_status(cg)['ready']:
            return original_cg_picture(cg, size)
        static = dynamic_cg_frame(cg, 'open', size)
        animation = dynamic_cg_animation(cg, size)
        # 开关在当前interaction重新求值；旧画面无需自写redraw轮询。
        # root在fullview保留ToggleField(persistent,'cg_motion_enabled')即可。
        return ConditionSwitch('persistent.cg_motion_enabled and not persistent.reduce_motion',
            animation, 'True', static, predict_all=True)