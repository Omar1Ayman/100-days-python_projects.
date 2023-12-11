import turtle
import json




screen = turtle.Screen()
screen.title("U.S States")
image = "blank_states_img.gif" 
screen.addshape(image)
turtle.shape(image)
guessed_states = []
missed_states = []

while len(guessed_states) < 50:
    
    wer_state = screen.textinput(f"Guess the stata {len(guessed_states)}/50" , "what`s another state`s name").title()
    if wer_state == "Exit":
        with open("50_states.csv") as file:
            states = file.readlines()
            for state in states[1:]:
                if state not in guessed_states:
                    with open("missed_state.txt" , "a") as f:
                        f.write(state+"\n")
        break
    with open("50_states.csv") as file:
        states = file.readlines()
        for state in states[1:]:
            state = state.split(",")
            print(state)
            if wer_state == state[0]:
                guessed_states.append(wer_state)     
                print(wer_state)
                t = turtle.Turtle()
                t.hideturtle()
                t.pu()
                t.goto(int(state[1]) , int(state[2]))
                t.write(wer_state)
                with open("anwer_state.txt" , "a") as f:
                    f.write(wer_state+"\n")
            
            

            







##def get_mouse_click(x,y):
##    print(x,y)
##
##turtle.onscreenclick(get_mouse_click)
##
##turtle.mainloop()

screen.exitonclick()
