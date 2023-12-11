import turtle as t




screen = t.Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


class Paddle(t.Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.pu()
        self.goto(position)
        
    def go_up(self):
        if self.ycor() <= 250: 
            new_cy = self.ycor() + 20
            self.goto(self.xcor(),new_cy)

    def go_down(self):
        if self.ycor() > -240:
            new_cy = self.ycor() - 20
            self.goto(self.xcor(),new_cy)

class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.y_move = 10
        self.x_move = 10
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.pu()
        self.goto(new_x,new_y)
    def bounce_y(self):
        self.y_move *= -1
    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
    

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score , align="center",font=("Courier", 80, "normal"))
        self.goto(100,200)
        self.write(self.r_score , align="center",font=("Courier",80 , "normal"))
        
    def l_point(self):
        self.l_score +=1
        self.update_score()
        
    def r_point(self):
        self.r_score +=1
        self.update_score()

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()




screen.listen()
screen.onkey(r_paddle.go_up , "Up")
screen.onkey(r_paddle.go_down , "Down")
screen.onkey(l_paddle.go_up , "w")
screen.onkey(l_paddle.go_down , "s")


import time
game_is_on = True
while game_is_on:
    time.sleep(.09)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        

screen.exitonclick()
