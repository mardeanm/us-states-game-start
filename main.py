import  turtle
import pandas
screen=turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_states=[]

score=0
while(len(guessed_states) <50):
    answer=screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                            prompt="What's another state's name?").title()
    if answer=="Exit":
        missing_states=[state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        answer_data = data[data.state == answer]
        t.goto(int(answer_data.x), int(answer_data.y))
        t.write(answer_data.state.item())
        guessed_states.append(answer)



