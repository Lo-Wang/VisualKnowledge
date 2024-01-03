from manim import *

class Pythagoras(Scene): 
    def construct(self):
        intro_text = Text("Теорема Пифагора").scale(1.2)

        info_text = Tex(r"В прямоугольном треугольнике квадрат гипотенузы \\ равен сумме квадратов двух других сторон (катетов)").move_to(np.array([0,-3,0])) 
        info_text_1 = Tex(r"").move_to(np.array([0,-3,0]))
        info_text_2 = Tex(r"").move_to(np.array([0,-3,0]))
        info_text_3 = Tex(r"", font_size=38).move_to(np.array([0,-3,0]))
        info_text_4 = Tex(r"", font_size=38).move_to(np.array([0,-3,0]))
        info_text_5 = Tex(r"", font_size=38).move_to(np.array([0,-3,0]))

        # Создаем треугольник
        dot_A1 = Dot(LEFT + DOWN)
        dot_B1 = Dot(LEFT + 2 * UP)
        dot_C1 = Dot(RIGHT + DOWN)

        line_A1B1 = always_redraw(lambda: Line(dot_A1, dot_B1, color=WHITE))
        line_B1C1 = always_redraw(lambda: Line(dot_B1, dot_C1, color=WHITE))
        line_C1A1 = always_redraw(lambda: Line(dot_C1, dot_A1, color=WHITE))

        # Создаем названия для сторон треугольника
        Label_triangle = MathTex("a", "b", "c")
        Label_triangle[0].next_to(line_A1B1.get_center() + DOWN)
        Label_triangle[1].next_to(line_B1C1.get_center() + LEFT)
        Label_triangle[2].next_to(line_C1A1.get_center() + UP + RIGHT)  

        triangle_group = VGroup(dot_A1, dot_B1, dot_C1, line_A1B1, line_B1C1, line_C1A1, Label_triangle)
        

        # Задаем точки для квадрата внешнего
        dot_A = Dot(2 * LEFT + 2 * DOWN)
        dot_B = Dot(2 * RIGHT + 2 * DOWN)
        dot_C = Dot(2 * RIGHT + 2 * UP)
        dot_D = Dot(2 * LEFT + 2 * UP)
        dot_Main = VGroup(dot_A, dot_B, dot_C, dot_D)

        # Задаем копии точек для квадрата внутри
        dot_E = dot_A.copy()
        dot_H = dot_B.copy()
        dot_Q = dot_C.copy()
        dot_O  = dot_D.copy()

        # Задаем названия для точек квадрата
        label_A = always_redraw(lambda: MathTex("A").next_to(dot_A, LEFT))
        label_B = always_redraw(lambda: MathTex("B").next_to(dot_B, RIGHT))
        label_C = always_redraw(lambda: MathTex("C").next_to(dot_C, UP))
        label_D = always_redraw(lambda: MathTex("D").next_to(dot_D, LEFT))
        label_Main = VGroup(label_A, label_B, label_C, label_D)
        
        # Задаем названия точек для доп построений
        label_H = always_redraw(lambda: MathTex("H").next_to(dot_H, RIGHT))
        label_E = always_redraw(lambda: MathTex("E").next_to(dot_E, DOWN))
        label_Q = always_redraw(lambda: MathTex("Q").next_to(dot_Q, UP))
        label_O = always_redraw(lambda: MathTex("O").next_to(dot_O, LEFT))

        label_DLC = VGroup(label_H, label_E, label_Q, label_O)


        # Задаем стороны для параллелограма
        line_AB = always_redraw(lambda: Line(dot_A, dot_B, color=WHITE))
        line_BC = always_redraw(lambda: Line(dot_B, dot_C, color=WHITE))
        line_CD = always_redraw(lambda: Line(dot_C, dot_D, color=WHITE))
        line_DA = always_redraw(lambda: Line(dot_D, dot_A, color=WHITE))
        line_Main = VGroup(line_AB, line_BC, line_CD, line_DA)

        # Линии начинаются в точке 1 и следуют за точкой 2
        line_QO = always_redraw(lambda: Line(dot_Q, dot_O, color=PURPLE))
        line_OE = always_redraw(lambda: Line(dot_O, dot_E, color=PURPLE))
        line_EH = always_redraw(lambda: Line(dot_E, dot_H, color=PURPLE))
        line_HQ = always_redraw(lambda: Line(dot_H, dot_Q, color=PURPLE))        

        
        line_DLC = VGroup(line_QO, line_OE, line_EH, line_HQ)
        
        # Анимации
        self.wait(0.5)
        self.play(FadeIn(intro_text))
        self.wait(1)
        self.play(FadeOut(intro_text))

        self.wait(0.5)
        self.play(Write(triangle_group), run_time=2)
        self.wait(0.5)
        self.play(Write(info_text))
        self.wait(4)
        self.play(FadeOut(triangle_group))
        self.play(Unwrite(info_text))

        self.play(Write(dot_Main), Write(label_Main), Write(line_Main), run_time=3, lag_ratio=0.1)
        self.play(Write(dot_H), Write(dot_E), Write(label_DLC), Write(line_DLC), run_time=2)
        self.wait(0.1)
        self.play(ApplyMethod(dot_E.shift, 3 * RIGHT), ApplyMethod(dot_H.shift, 3 * UP), ApplyMethod(dot_Q.shift, 3 * LEFT), ApplyMethod(dot_O.shift, 3 * DOWN))
        self.play(FadeIn(info_text_1, shift=UP))
        self.wait(6)
        self.play(TransformMatchingTex(info_text_1, info_text_2))
        self.wait(6)
        self.play(TransformMatchingTex(info_text_2, info_text_3))
        self.wait(6)
        self.play(TransformMatchingTex(info_text_3, info_text_4))
        self.wait(6)
        self.play(TransformMatchingTex(info_text_4, info_text_5))
        self.play(ApplyMethod(dot_E.shift, 2 * LEFT), ApplyMethod(dot_H.shift, 2 * DOWN), ApplyMethod(dot_Q.shift, 2 * RIGHT), ApplyMethod(dot_O.shift, 2 * UP), Unwrite(label_DLC), run_time=2)
        self.wait(0.1)
        self.play(ApplyMethod(dot_E.shift, 2 * RIGHT), ApplyMethod(dot_H.shift, 2 * UP), ApplyMethod(dot_Q.shift, 2 * LEFT), ApplyMethod(dot_O.shift, 2 * DOWN), Write(label_DLC), run_time=2)
        self.wait(0.1)
        self.play(ApplyMethod(dot_E.shift, 3 * LEFT), ApplyMethod(dot_H.shift, 3 * DOWN), ApplyMethod(dot_Q.shift, 3 * RIGHT), ApplyMethod(dot_O.shift, 3 * UP), Unwrite(label_DLC), run_time=2)
        self.wait(2)
        self.play(FadeOut(dot_Main, shift=DOWN), FadeOut(label_Main, shift=DOWN), FadeOut(line_Main, shift=DOWN), FadeOut(line_DLC, shift=DOWN), FadeOut(info_text_5, shift=DOWN), FadeOut(dot_H, shift=DOWN), FadeOut(dot_E, shift=DOWN), lag_ratio=0.02)
        self.wait(1)

# Send star in Alex Deluxe :)