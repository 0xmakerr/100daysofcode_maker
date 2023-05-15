import turtle
import pandas

turtle_write = turtle.Turtle()
turtle_write.hideturtle()
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle_write.penup()
correct_guess = []

while True:
    len_correct_guess = len(correct_guess)
    answer_state = screen.textinput(title=f"{len_correct_guess}/50 States Correct", prompt="What is state name?").title()
    data = pandas.read_csv("50_states.csv")
    state_list = data.state.to_list()
    state = data[data["state"] == answer_state]
    if answer_state == "Exit":
        break
    if not state.empty:
        state_str = state["state"].iloc[0]
        state_x = state["x"].iloc[0]
        state_y = state["y"].iloc[0]
        turtle_write.goto(state_x, state_y)
        turtle_write.write(state_str)
        correct_guess.append(state_str)
    else:
        pass

remaining_states = [state for state in state_list if state not in correct_guess]
remaining_states_dict = {
    "states": remaining_states
}

df = pandas.DataFrame(remaining_states_dict)
df.to_csv("remaining_states.csv")
