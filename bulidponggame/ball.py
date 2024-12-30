from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1,1)
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.x_move=10
        self.y_move=10
        self.move_speed=0.1

        # self.refresh()

    # def refresh(self):
    #     x=random.randint(-325,325)
    #     y=random.randint(-325,325)
    #     self.goto(x,y)
    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)
    def bounce(self):
        self.y_move*=-1
    def bounce1(self):
        self.x_move *= -1


