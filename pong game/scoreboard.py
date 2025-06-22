from turtle import Turtle
FONT = ("Courier", 80, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.teleport(-100, 200)
        self.write(self.l_score, font= FONT, align= ALIGNMENT)
        self.teleport(100, 200)
        self.write(self.r_score, font= FONT, align= ALIGNMENT)

    def update_l_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def update_r_score(self):
        self.r_score += 1
        self.update_scoreboard()