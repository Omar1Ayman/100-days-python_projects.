import turtle as t
import random
height = 600
width = 800
half_width = width /2
screen = t.Screen()
screen.bgcolor("lightgreen")
screen.setup(width,height)
screen.title("Welcome to the turtle zoo!")




st_pos = -150
all_turtles = []
set_color = ["red","green","blue","yellow","cyan","orange","gray"]

name_player1 = screen.textinput("player 1" ,"please type your name")        
guess_player1 = screen.textinput("Make your bet",f"hello guys this race have {len(set_color)} turtles, you can guess which color will win the race {set_color} ")

name_player2 = screen.textinput("player 2" ,"please type your name")        
guess_player2 = screen.textinput("Make your bet",f"hello guys this race have {len(set_color)} turtles, you can guess which color will win the race {set_color} ")

for i in range(len(set_color)-1):
    st_pos += 50
    timmy = t.Turtle("turtle")
    timmy.pu()
    timmy.color(set_color[i])
    timmy.goto(-(half_width-20) , st_pos)
    all_turtles.append(timmy)
    


if guess_player1 and guess_player2:
    is_race_on = True

while is_race_on:

    for timmy in all_turtles:
        if timmy.xcor() > (half_width-30):
            if timmy.pencolor() == guess_player2 and timmy.pencolor() == guess_player1:
                print(f"Draw!")
            elif timmy.pencolor() == guess_player1:
                print(f"cong {name_player1} wins")
            elif timmy.pencolor() == guess_player2:
                print(f"cong {name_player2} wins")
            else:
                print(f"sorry! you los the turtle {timmy.pencolor()} win.")
            is_race_on = False
            all_turtles.remove(timmy)
            for t in all_turtles:
                t.ht()
            timmy.home()
            for i in range(0,361):
                timmy.speed("fastest")
                timmy.setheading(i)

        rand_int = random.randint(0,10)
        timmy.forward(rand_int)
     



screen.exitonclick()
