import turtle

win = turtle.Screen()
win.setup(800,600)  #width,height
win.bgcolor("blue")
win.title("pong game")
win.tracer(0)

#left paddle
left_paddle = turtle.Turtle()
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5,stretch_len=1) #stretching to convert square into rectangle
left_paddle.penup()
left_paddle.speed(0) #fastest
left_paddle.goto(-380,0)

#right paddle
right_paddle = turtle.Turtle()
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5,stretch_len=1) #stretching to convert square into rectangle
right_paddle.penup()
right_paddle.speed(0) #fastest
right_paddle.goto(380,0)

#ball
ball = turtle.Turtle()
ball.shape("circle")
ball.speed(0)
ball.color("white")
ball.dx = 0.15
ball.dy = 0.15
ball.penup()


#moving paddles
def left_paddle_up():
    left_paddle.sety(left_paddle.ycor()+20)
def left_paddle_down():
    left_paddle.sety(left_paddle.ycor()-20)
def right_paddle_up():
    right_paddle.sety(right_paddle.ycor()+20)
def right_paddle_down():
    right_paddle.sety(right_paddle.ycor()-20)


win.listen()
win.onkeypress(left_paddle_up,'w')
win.onkeypress(left_paddle_down,'s')
win.onkeypress(right_paddle_up,'Up')
win.onkeypress(right_paddle_down,'Down')

while True:
    win.update()
    #ball movement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)