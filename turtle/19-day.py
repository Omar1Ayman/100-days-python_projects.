import turtle as t

timmy = t.Turtle()
timmy.shape("turtle")

my_screen = t.Screen()



def move_forward():
    timmy.forward(20)

def move_backward():
    timmy.backward(20)



def move_up():
    timmy.setheading(90)
    timmy.forward(20)

def move_down():
    timmy.setheading(270)
    timmy.forward(10)

def move_left():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)
    #timmy.setheading(180)
    #timmy.forward(10)

def move_right():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)
    #timmy.setheading(0)
    #timmy.forward(10)

def clear():
    timmy.pu()
    timmy.clear()
    timmy.home()
    timmy.pd()


my_screen.listen()

my_screen.onkey(move_forward , "w")
my_screen.onkey(move_backward , "s")
my_screen.onkey(move_left , "a")
my_screen.onkey(move_right , "d")
my_screen.onkey(clear , "c")


my_screen.exitonclick()
