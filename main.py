import pandas
from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
screen.setup(800,600)
screen.title("U.S States Game")
image = "/Users/SarahJC/Desktop/Python Projects/Pandas/US State Quiz/blank_states_img.gif"
screen.addshape(image)
t.shape(image)

data = pandas.read_csv("/Users/SarahJC/Desktop/Python Projects/Pandas/US State Quiz/50_states.csv")
all_states = data["state"].to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title = f"{len(guessed_states)}/ 50 States Correct",prompt = "What's a state's name?").title()
    
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        #missing_states = []
        #for state in all_states:
        #    if state not in guessed_states:
        #        missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("/Users/SarahJC/Desktop/Python Projects/Pandas/US State Quiz/states_to_learn.csv")
        break

    # Check if user answer is a state
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_turtle = Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_data = data[data["state"] == answer_state]
        state_turtle.goto(int(state_data.x),int(state_data.y))
        state_turtle.write(state_data.state.item())

