# Fixed 16:9 game and UI. Only surplus device area receives ambient fill.
# No separate reading rail: all existing screens keep 1280x720 coordinates.
init -8 python:
    TOK_MOBILE = bool(renpy.variant('mobile') or renpy.variant('android') or renpy.variant('touch'))

    def tok_mobile_geometry(width, height):
        # The Android build is landscape. Also retain a complete stage on 4:3
        # tablets; taller windows receive extra ambient space, never cropping.
        width, height = max(1, int(width)), max(1, int(height))
        ratio = float(width) / height
        canvas_height = max(720, int(round(1280 / ratio)))
        return (int(round(canvas_height * ratio)), canvas_height)

    def tok_mobile_configure(width, height):
        config.screen_width, config.screen_height = tok_mobile_geometry(width, height)

    def tok_mobile_stage_x():
        return (config.screen_width - 1280) // 2

    def tok_mobile_stage_y():
        return (config.screen_height - 720) // 2

    class TokMobileStage(renpy.Displayable):
        """Force legacy layout constraints before positioning the whole stage.

        No stored Render, redraw timer, or saved per-device coordinates.
        Render.blit transports focus rectangles; events use the same offset.
        """
        def __init__(self, child, **properties):
            super(TokMobileStage, self).__init__(**properties)
            self.child = Fixed(child, xysize=(1280,720), clipping=True)

        def render(self, width, height, st, at):
            child_render = renpy.render(self.child, 1280, 720, st, at)
            canvas = renpy.Render(config.screen_width, config.screen_height)
            canvas.blit(child_render, (tok_mobile_stage_x(), tok_mobile_stage_y()))
            return canvas

        def event(self, ev, x, y, st):
            return self.child.event(ev, x - tok_mobile_stage_x(), y - tok_mobile_stage_y(), st)

        def visit(self):
            return [self.child]

    def tok_mobile_stage_layer(child):
        return TokMobileStage(child)

    def tok_mobile_first_window():
        # SDL's drawable window can differ from the cached display dimensions
        # (navigation area or Chromebook). Correct once, before the first frame.
        width, height = renpy.get_physical_size()
        target = tok_mobile_geometry(width, height)
        if target != (config.screen_width, config.screen_height):
            tok_mobile_configure(width, height)
            renpy.display.interface.set_mode()

    def tok_mobile_ensure_ambient():
        # HideInterface suppresses overlay_screens. Ambient belongs to the
        # scenery and remains present during that interaction as well.
        renpy.show_screen('tok_mobile_ambient', _layer='mobile_ambient')

    if TOK_MOBILE:
        info = renpy.display.get_info()
        tok_mobile_configure(max(info.current_w, info.current_h), min(info.current_w, info.current_h))
        config.display_start_callbacks.append(tok_mobile_first_window)
        # Native SayBehavior/Keymap live on transient/overlay and own the
        # full-canvas dismiss focus. Do not clip/offset those behavior layers.
        for layer in ('master', 'screens'):
            config.layer_transforms.setdefault(layer, []).append(tok_mobile_stage_layer)
        renpy.add_layer('mobile_ambient', below='master')
        config.start_interact_callbacks.append(tok_mobile_ensure_ambient)
        # Full drawing canvas, rather than coloring the old physical bars.
        config.gl_clear_color = '#D9CED4'

init -1 python:
    def tok_mobile_ambient_key():
        legacy_gallery = renpy.get_screen('cg_view')
        if legacy_gallery:
            return legacy_gallery.scope.get('path') or 'bg moon'
        tragedy_gallery = renpy.get_screen('optional_tragedy_cg_view')
        if tragedy_gallery:
            selected = tragedy_gallery.scope.get('selected', 'final')
            if selected in (persistent.tragedy_cg_seen or []) or (selected == 'final' and persistent.cg_ds_tragedy):
                return tragedy_cg_path(selected)
        gallery = renpy.get_screen('original_cg_view')
        if gallery:
            key = gallery.scope.get('displayed_key', gallery.scope.get('cg_key'))
            cg = original_cg_by_id(key) if key else None
            if cg and original_cg_unlocked(cg):
                return cg['file']
        if renpy.get_screen('main_menu'):
            return 'bg moon'
        attributes = renpy.get_attributes('bg', layer='master')
        if attributes:
            return 'bg ' + ' '.join(attributes)
        attributes = renpy.get_attributes('cg', layer='master')
        if attributes:
            return 'cg ' + ' '.join(attributes)
        if main_cg:
            return main_cg['file']
        return 'bg moon'

    def tok_mobile_ambient(st, at):
        # Downsample before blur. Only the background/CG is sampled: no text,
        # sprites, screenshots, extra image files, or animation polling.
        source = tok_mobile_ambient_key()
        small = Transform(source, xysize=(160, 90), fit='cover', blur=5)
        return Transform(small, xysize=(config.screen_width, config.screen_height)), None

screen tok_mobile_ambient():
    layer 'mobile_ambient'
    zorder -1000
    if TOK_MOBILE:
        add DynamicDisplayable(tok_mobile_ambient)
        add Solid('#EEE1E848')
