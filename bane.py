import pyxel
import math

class QuizGame:
    def __init__(self):
        pyxel.init(400, 300)
        pyxel.load('sounds.pyxres')
        pyxel.playm(0, loop=True)

        self.questions = [
            {
                'question': " Are you FBI?? ",
                'caption': "!Press Yes or No!",
                'correct_answer': pyxel.KEY_N
            },
            {
                'question': "Who is the most dopeness? ",
                'caption': "Snoop ma-fuckin' D.O dublle ' '?? ",
                'correct_answer': pyxel.KEY_G
            },
            {
                'question': "West side? East side?",
                'caption': "YA KNOW MY REPRESENT? ",
                'correct_answer': pyxel.KEY_W
            },
            {
                'question': "Did you bring the Ganjah?",
                'caption': "Yes or No",
                'correct_answer': pyxel.KEY_Y
            }
        ]

        self.current_question_index = 0
        self.current_question = self.questions[self.current_question_index]

        self.is_answered = False
        self.is_correct = False
        self.is_finished = False

        self.angle = 0
        self.stripe_width = 10
        self.stripe_speed = 1
        self.stripe_colors = [pyxel.COLOR_WHITE, pyxel.COLOR_GREEN]

        self.bgm_playing = False

        pyxel.run(self.update, self.draw)

    def next_question(self):
        self.is_answered = False
        self.is_correct = False

        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.current_question = self.questions[self.current_question_index]
            pyxel.playm(0, loop=True)
        else:
            self.is_finished = True

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE) and self.is_finished:
            pyxel.quit()

        if not self.is_finished:
            if not self.is_answered:
                for key in (pyxel.KEY_0, pyxel.KEY_1, pyxel.KEY_2, pyxel.KEY_3, pyxel.KEY_4,
                            pyxel.KEY_5, pyxel.KEY_6, pyxel.KEY_7, pyxel.KEY_8, pyxel.KEY_9,
                            pyxel.KEY_A, pyxel.KEY_B, pyxel.KEY_C, pyxel.KEY_D, pyxel.KEY_E,
                            pyxel.KEY_F, pyxel.KEY_G, pyxel.KEY_H, pyxel.KEY_I, pyxel.KEY_J,
                            pyxel.KEY_K, pyxel.KEY_L, pyxel.KEY_M, pyxel.KEY_N, pyxel.KEY_O,
                            pyxel.KEY_P, pyxel.KEY_Q, pyxel.KEY_R, pyxel.KEY_S, pyxel.KEY_T,
                            pyxel.KEY_U, pyxel.KEY_V, pyxel.KEY_W, pyxel.KEY_X, pyxel.KEY_Y,
                            pyxel.KEY_Z):
                    if pyxel.btnp(key):
                        if key == self.current_question['correct_answer']:
                            self.is_correct = True
                            pyxel.playm(1)
                        else:
                            self.is_correct = False
                            pyxel.playm(2)
                        self.is_answered = True
                        break
            elif self.is_answered:
                if pyxel.btnp(pyxel.KEY_SPACE):
                    if self.is_correct:
                        self.next_question()
                    else:
                        self.is_finished = True

        self.angle += self.stripe_speed

    def draw(self):
        pyxel.cls(0)

        # 背景にストライプを描画する
        for i in range(pyxel.height):
            stripe_color = self.stripe_colors[int((i + self.angle) / self.stripe_width) % 2]
            pyxel.line(0, i, pyxel.width, i, stripe_color)

        if self.is_finished:
                pyxel.blt(100, 100, 0, 0, 0, 180, 180, 14)
                pyxel.text(200, 60, "Can you roll ma Joint?", 0) 
        elif self.is_answered:
            if self.is_correct:
                pyxel.text(180, 50, "Cool Men!!", 11)
                pyxel.blt(180, 80, 1, 0, 0, 180, 210, 14)
            else:
                pyxel.text(200, 60, "FUCK OFF ", 8)
                pyxel.blt(100, 60, 2, 0, 0, 220, 240, 14)
                pyxel.playm(1)
        else:
            pyxel.text(270, 200, self.current_question['question'], 0)
            pyxel.text(180, 80, self.current_question['caption'], 0)
            pyxel.text(180, 10, "Be snoop's dogs!", 0)
            pyxel.blt(100, 100, 0, 0, 0, 180, 180, 14)

QuizGame()
