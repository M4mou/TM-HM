from manim import *

class test(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-30, 30], y_range=[-20, 120, 10], axis_config={"include_tip": False},
        )
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")

        t = ValueTracker(-5)
        t1 = ValueTracker(-5)
        def func(x):
            return 4/9 * x * x + 1
        def yt(t):
            return 4 * t* t + 1
        def xt(t):
            return 3* t
        velocity = Vector([1,1])
        graph = ax.plot(func, color=MAROON)

        initial_point = [ax.coords_to_point(xt(t.get_value()), yt((t.get_value())))]
        dot = Dot(point=initial_point)
         
        def velocityupdate(x):
            d1 = Dot(ax.c2p(xt(t.get_value()), yt(t.get_value())))
            d2 = Dot(ax.c2p(3 + xt(t.get_value()),  yt(t.get_value()) +yt(t.get_value()) * 8 + 1))
            velocity.set_x(*ax.c2p(xt(t.get_value())))
        
        dot.add_updater(lambda x: x.move_to(ax.c2p(xt(t.get_value()), yt(t.get_value()))))
        velocity.add_updater(lambda y: velocityupdate(y))
        self.add(ax, labels, graph, dot, velocity)
        self.play(t.animate.set_value(5),run_time = 2)

        self.wait()