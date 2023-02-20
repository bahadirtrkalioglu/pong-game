from turtle import Turtle

SHIFT_NUM = 20

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(self.position)



    def up(self):
        current_y = self.ycor()
        self.goto(x=self.xcor(), y=current_y + SHIFT_NUM)

    def down(self):
        current_y = self.ycor()
        self.goto(x=self.xcor(), y=current_y - SHIFT_NUM)




