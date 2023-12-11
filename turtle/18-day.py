import turtle as t
import random
timmy = t.Turtle()
#timmy.shape("triangle")
t.colormode(255)

def right():    
    timmy.forward(100)
    timmy.right(90)
    

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

def line():
    for _ in range(10):
        timmy.color(random_color())
        timmy.forward(20)
        timmy.pu()
        timmy.forward(20)
        timmy.pd()
line()






def shape(side):
    for _ in range(side):
        timmy.right(360/side)
        timmy.dot(5 , random_color())
        timmy.forward(100)



for i in range(3 , 10):
    timmy.color(random_color())
    shape(i)




  

def random_direction(): 
    directions = [0,90,180,270]
    timmy.pensize(10)
    while True:
        timmy.color(random_color())
        timmy.forward(30)
        timmy.setheading(random.choice(directions))

random_direction()


timmy.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spirograph(5)


def draw_dots():
    timmy.hideturtle()
    timmy.pu()
    timmy.setheading(225)
    timmy.forward(300)
    timmy.setheading(0)
    number_of_dots=200
    for dot_count in range(1, number_of_dots+1):
        timmy.dot(20 , random_color())
        timmy.forward(50)
        if dot_count % 10 == 0:
            timmy.setheading(90)
            timmy.forward(30)
            timmy.setheading(180)
            timmy.forward(500)
            timmy.setheading(0)

draw_dots()


screen = t.Screen()
screen.exitonclick()
