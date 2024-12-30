from turtle import Screen,Turtle
from paddle import paddlea
from ball import Ball
from scoreboard import scoreboard
import time
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("buildpong")
screen.tracer(0)
# paddle=Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5,stretch_len=1)
# paddle.penup()
# paddle.goto(-285,0)
paddle=paddlea()
balll=Ball()
paddle.attri()
Scoreboard=scoreboard()
paddle.pos(-285,0)
paddle1=paddlea()
paddle1.attri()
paddle1.pos(x=285,y=0)
# paddle1.shape("square")
# paddle1.color("white")
# paddle1.shapesize(stretch_wid=5,stretch_len=1)
# paddle1.penup()
# paddle1.goto(285,0)
# screen.update()
screen.listen()
screen.onkey(paddle.go_up,"w")
screen.onkey(paddle.go_down,"s")
screen.onkey(paddle1.go_up,"Up")
screen.onkey(paddle1.go_down,"Down")
game_is_on=True
while game_is_on:
    time.sleep(balll.move_speed)
    screen.update()
    # fooda.refresh()
    balll.move()
    if balll.ycor()>260 or balll.ycor()<-260:
        balll.bounce()
    if balll.distance(paddle1) < 50 and balll.xcor()>260 or balll.distance(paddle) <50 and balll.xcor() -280 :
        balll.bounce1()
    if balll.xcor()>380:
        balll.reset_position()
        scoreboard.l_point()
    if balll.xcor()<-380:
        balll.reset_position()
        scoreboard.r_point()



# screen.update()
screen.exitonclick()