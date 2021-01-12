import turtle
import pandas
from state_name import State_Name

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=725, height=491)

correct_answer_count = 0
correct_answers = []
input_box_title = "Guess the State"
states_data = pandas.read_csv("50_states.csv")

while correct_answer_count != 50:
    answer_state = screen.textinput(title=input_box_title, prompt="What's another state's name?").title()
    # print(states_data.state)
    # print(answer_state in states_data.state.tolist())
    if answer_state in states_data.state.tolist():
        state_name = State_Name()
        state_x = int(states_data[states_data.state == answer_state].x)
        state_y = int(states_data[states_data.state == answer_state].y)
        state_name.update_state_name(answer_state, state_x, state_y)
        if answer_state not in correct_answers:
            correct_answer_count += 1
            correct_answers.append(answer_state)
    input_box_title = f"{correct_answer_count}/50 States Correct"

screen.exitonclick()
