from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.width(20)
        self.teleport(x,y)
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)

    def up(self):
        # x coordinate remains the same
        new_y = self.ycor() + 25
        self.teleport(self.xcor(), new_y)

    def down(self):
        # x coordinate remains the same
        new_y = self.ycor() - 25
        self.teleport(self.xcor(), new_y)