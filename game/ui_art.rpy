init -8 python:
    class SoftPanel(renpy.Displayable):
        # Only serializable geometry is cached. Render/Canvas objects are never
        # retained in the displayable or a save; animation belongs to its parent.
        def __init__(self, color, border, radius=10, **kwargs):
            super(SoftPanel, self).__init__(**kwargs)
            self.color = color
            self.border = border
            self.radius = radius
            self._soft_panel_plans = []

        @staticmethod
        def _plan(width, height, fill, border, radius):
            import math
            commands = []
            radius = max(0.0, min(float(radius), width // 2, height // 2))

            def span(y, inset):
                w, h = width - inset * 2, height - inset * 2
                if w <= 0 or h <= 0 or not inset <= y < height - inset:
                    return None
                r = max(0.0, min(radius - inset, w // 2, h // 2))
                distance = min(y - inset + 0.5, height - inset - y - 0.5)
                if r and distance < r:
                    dx = r - math.sqrt(max(0.0, r*r - (r-distance)**2))
                else:
                    dx = 0.0
                return (inset + dx, width - inset - dx)

            def rect(rgba, x, y, w, h):
                if w > 0 and h > 0 and rgba[3] > 0:
                    commands.append((rgba, (x, y, w, h)))

            def row(y):
                outer = span(y, 0)
                inner = span(y, 1)
                cuts = {0, width}
                for interval in (outer, inner):
                    if interval:
                        for endpoint in interval:
                            cuts.add(max(0, min(width, int(math.floor(endpoint)))))
                            cuts.add(max(0, min(width, int(math.ceil(endpoint)))))
                cuts = sorted(cuts)
                for x, stop in zip(cuts, cuts[1:]):
                    length = stop - x
                    if not length:
                        continue
                    def coverage(interval):
                        if interval is None:
                            return 0.0
                        return max(0.0, min(stop, interval[1]) - max(x, interval[0])) / length
                    outside = coverage(outer)
                    inside = min(outside, coverage(inner))
                    # Area-weighted premultiplied color: the translucent fill
                    # replaces the inner area instead of being drawn over border.
                    ba = border[3] * max(0.0, outside - inside)
                    fa = fill[3] * inside
                    alpha = ba + fa
                    if alpha <= 0.0:
                        continue
                    rgba = tuple(max(0, min(255, int(round(
                        (border[c]*ba + fill[c]*fa) / alpha)))) for c in range(3))
                    rgba += (max(0, min(255, int(round(alpha)))),)
                    rect(rgba, x, y, length, 1)

            edge_rows = max(1, int(math.ceil(radius)))
            for y in range(min(edge_rows, height)):
                row(y)
                mirror = height - y - 1
                if mirror >= edge_rows and mirror != y:
                    row(mirror)
            middle_height = height - edge_rows * 2
            if middle_height > 0:
                if width == 1:
                    rect(border, 0, edge_rows, 1, middle_height)
                else:
                    rect(border, 0, edge_rows, 1, middle_height)
                    rect(fill, 1, edge_rows, width - 2, middle_height)
                    rect(border, width - 1, edge_rows, 1, middle_height)
            return tuple(commands)

        def render(self, width, height, st, at):
            width, height = max(1, int(width)), max(1, int(height))
            fill = tuple(renpy.color.Color(self.color))
            border = tuple(renpy.color.Color(self.border))
            radius = max(0.0, min(float(self.radius), width // 2, height // 2))
            key = (width, height, fill, border, radius)
            # getattr also covers an old saved instance without the new member.
            plans = getattr(self, '_soft_panel_plans', [])
            self._soft_panel_plans = plans
            commands = None
            for index, (old_key, old_commands) in enumerate(plans):
                if old_key == key:
                    commands = old_commands
                    plans.append(plans.pop(index))
                    break
            if commands is None:
                commands = self._plan(width, height, fill, border, radius)
                plans.append((key, commands))
                if len(plans) > 2:
                    del plans[:-2]
            result = renpy.Render(width, height)
            canvas = result.canvas()
            for rgba, rectangle in commands:
                canvas.rect(rgba, rectangle)
            # st/at do not affect this static panel. Do not schedule redraw here;
            # Ren'Py owns its normal render cache, parent transforms own motion.
            return result

        def visit(self):
            return []

# Bounded choice effects; original SoftPanel stays byte-for-byte above.
init -7 python:
    import math as choice_math
    import time as choice_clock

    def choice_redraw_interval():
        return None if bool(persistent.reduce_motion) else 1.0/30.0

    def choice_viewport_height(items):
        # Measure the actual font/line spacing, once per screen update. Character
        # counts underestimated Source Han line height and clipped a second row.
        heights = [max(72, int(choice_math.ceil(Text(item.caption,
            style='choice_card_text').size(818,720,0,0)[1])) + 30)
            for item in items]
        return min(396, max(152, sum(heights) + max(0,len(items)-1)*10 + 4))

    class ChoiceOptionButton(renpy.display.behavior.Button):
        def __init__(self, caption, action, **kwargs):
            self._choice_pressed = False
            child = Text(caption, style='choice_card_text')
            super(ChoiceOptionButton,self).__init__(child=child, action=action, style='choice_card', **kwargs)

        def event(self, ev, x, y, st):
            if ev.type == renpy.pygame.MOUSEBUTTONDOWN and ev.button == 1 and self.is_focused():
                self._choice_pressed = True
                self.set_style_prefix('activate_', True)
            elif ev.type == renpy.pygame.MOUSEBUTTONUP and ev.button == 1 and self._choice_pressed:
                self._choice_pressed = False
                self.set_style_prefix('hover_' if self.is_focused() else 'idle_', True)
            return super(ChoiceOptionButton,self).event(ev,x,y,st)

    class ChoiceSpeck(renpy.Displayable):
        def __init__(self, color, size, **kwargs):
            super(ChoiceSpeck,self).__init__(**kwargs)
            self.color,self.size=color,size

        def render(self,width,height,st,at):
            result=renpy.Render(self.size,self.size)
            canvas=result.canvas()
            center=self.size//2
            canvas.line(self.color,(center,1),(center,self.size-2),1)
            canvas.line(self.color,(1,center),(self.size-2,center),1)
            return result

    class ChoiceSparkles(renpy.Displayable):
        def __init__(self,count=14,**kwargs):
            super(ChoiceSparkles,self).__init__(**kwargs)
            self.count=max(0,min(18,int(count)))
            self._glyphs=(ChoiceSpeck('#f3c7de88',6),ChoiceSpeck('#ffe8f3aa',8),ChoiceSpeck('#d6c5ed88',10))
            self._paths=tuple((i/self.count,i%3,i%2,0.073+(i%5)*0.007) for i in range(self.count)) if self.count else ()
            self.render_calls=0
            self.redraw_requests=0
            self.last_schedule=None
            self._cost_samples=[]

        def visit(self):
            return list(self._glyphs)

        def event(self,ev,x,y,st):
            return None

        def render(self,width,height,st,at):
            started=choice_clock.perf_counter()
            width,height=max(1,int(width)),max(1,int(height))
            result=renpy.Render(width,height)
            self.render_calls+=1
            interval=choice_redraw_interval()
            self.last_schedule=interval
            if interval is not None:
                glyphs=tuple(renpy.render(g,g.size,g.size,0,0) for g in self._glyphs)
                for phase,kind,side,speed in self._paths:
                    travel=(phase+float(st)*speed)%1.0
                    px=5+choice_math.sin(travel*6.283185)*3 if not side else width-16+choice_math.sin(travel*6.283185)*3
                    py=7+travel*max(1,height-24)
                    result.blit(glyphs[kind],(int(px),int(py)))
                self.redraw_requests+=1
                renpy.redraw(self,interval)
            elapsed=(choice_clock.perf_counter()-started)*1000.0
            self._cost_samples.append(elapsed)
            if len(self._cost_samples)>120:
                del self._cost_samples[0]
            return result

        def profile_report(self):
            values=sorted(self._cost_samples)
            return dict(particles=self.count,render_calls=self.render_calls,
                redraw_requests=self.redraw_requests,last_schedule=self.last_schedule,
                samples=len(values),mean_ms=sum(values)/len(values) if values else 0.0,
                p95_ms=values[min(len(values)-1,int(len(values)*0.95))] if values else 0.0,
                max_ms=max(values) if values else 0.0,
                scope='local ChoiceSparkles.render CPU; not total frame or GPU FPS')