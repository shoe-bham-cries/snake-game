from turtle import Turtle
ALIGN = "center"
FONT = ("Times New Roman", 14, "bold")
with open("data.txt") as d:
    CURRENT_HS = d.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pu()
        self.goto(0, 270)
        self.high_score = int(CURRENT_HS)
        self.hideturtle()
        self.color("white")
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"Score = {self.score} High Score = {self.high_score}", move=False, align=ALIGN, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as e:
                e.write(str(self.score))
        self.score = 0
        self.update()

    # def game_over(self):
    #     self.pu()
    #     self.goto(0, 0)
    #     self.hideturtle()
    #     self.color("white")
    #     self.write(arg=f"GAME OVER", move=False, align=ALIGN, font=FONT)

    def increase(self):
        self.score += 1
        self.update()
