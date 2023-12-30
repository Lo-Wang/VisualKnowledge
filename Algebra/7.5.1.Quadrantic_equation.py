from manim import *

class Quadrantic_equation(MovingCameraScene):
    def construct(self):

        intro_text = Text("Квадрат суммы двух переменных").scale(1.2)
        equal = MathTex("({{a}}", "+", "{{b}})^2 = ?").scale(1.6)
        equal_1 = MathTex("({{a}}", "+", "{{b}})^2", "=","{{a}}^2", "+", "2", "{{a}}", "{{b}}", "+", "{{b}}^2").move_to(3.5*DOWN).scale(1.2)
        box_for_equal_1 = SurroundingRectangle(equal_1, corner_radius=0.5, buff=0.3, stroke_width=4, stroke_color=ORANGE)
        info_square = MathTex("a^2").move_to(2 * LEFT)
        info_square_1 = MathTex("b^2").move_to(3.5*UP + 1.5*RIGHT)
        info_rectangle = MathTex("a * b").move_to(2*LEFT + 3.5* UP)
        info_rectangle_1 = MathTex("a * b").move_to(1.5*RIGHT)
        main_square = Square(7 , stroke_color=WHITE, stroke_width=10).move_to(1.5 * UP + 0.5 * LEFT)
        square = Square(side_length=4, fill_color=ORANGE, fill_opacity=0.25, stroke_color=WHITE, stroke_opacity=0.8).move_to(2*LEFT)
        square_1 = Square(side_length=3, fill_color=ORANGE, fill_opacity=0.25, stroke_color=WHITE, stroke_opacity=0.8).move_to(3.5*UP + 1.5*RIGHT)
        rectangle = Rectangle(height=3, width=4, fill_color=DARK_BROWN, fill_opacity=0.25, stroke_color=WHITE, stroke_opacity=0.8).move_to(2*LEFT + 3.5* UP)
        rectangle_1 = Rectangle(height=4, width=3, fill_color=DARK_BROWN, fill_opacity=0.25, stroke_color=WHITE, stroke_opacity=0.8).move_to(1.5*RIGHT )
        
        self.wait()
        self.play(Write(intro_text), run_time=2)
        self.play(FadeOut(intro_text))
        self.play(Write(equal), run_time=2)
        self.wait()
        self.play(Unwrite(equal), run_time= 1)
        self.play(self.camera.frame.animate.set(width=19), lag_ratio=0)
        self.play(GrowFromCenter(square), Write(info_square))
        self.play(GrowFromCenter(square_1), Write(info_square_1))
        self.play(GrowFromCenter(rectangle), Write(info_rectangle))
        self.play(GrowFromCenter(rectangle_1), Write(info_rectangle_1))
        self.play(FadeIn(main_square, run_time=0.5), ShowPassingFlashWithThinningStrokeWidth(main_square.copy().set_color(RED), run_time=3, time_width=0.7))
        self.play(Write(equal_1[0:5]))
        self.play(Transform(info_square, equal_1[5:8]))
        self.play(Transform(info_rectangle, equal_1[8:10]))
        self.play(Transform(info_rectangle_1, equal_1[10:12]))
        self.play(Transform(info_square_1, equal_1[12:15]))
        self.play(Create(box_for_equal_1), run_time=2.5)
        self.play(Indicate(equal_1, scale_factor=1.02, color=WHITE))

        self.wait(2)

# Send star in Alex Deluxe :)
