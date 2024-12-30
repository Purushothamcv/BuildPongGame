from turtle import Turtle
class paddlea(Turtle):
    def __init__(self):
        super().__init__()
        self.attri()
    def attri(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
    def pos(self,x,y):
        self.goto(x,y)

    def go_up(self):
        new_ycor = self.ycor() + 20
        self.goto(self.xcor(), new_ycor)

    def go_down(self):
        new_ycor1 = self.ycor() - 20
        self.goto(self.xcor(), new_ycor1)


