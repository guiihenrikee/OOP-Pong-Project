from turtle import Turtle, Screen


class Paddle(Turtle):

    # CREATE THE PADDLE
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)

    # MOVE THE PADDLE
    def up(self):
        new_y = self.ycor() + 33
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 33
        self.goto(self.xcor(), new_y)
