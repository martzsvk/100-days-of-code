import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State game")
image = "blank_states_img.gif"
screen.bgpic("blank_states_img.gif")

correct_states = []


while len(correct_states) < 50:
    user_answer = screen.textinput(title=f"{len(correct_states)}/50 Correct states", prompt="What's another state?").title()
    data_file = pandas.read_csv("50_states.csv")
    # checking if guess is right
    for state in data_file["state"]:
        if state == user_answer:
            state_row = data_file[data_file["state"] == user_answer]
            x_cor = int(state_row["x"].values[0])
            y_cor = int(state_row["y"].values[0])
            correct_states.append(state)
            turtle.hideturtle()
            turtle.penup()
            turtle.goto(x_cor,y_cor)
            turtle.write(user_answer)

    if user_answer == "Exit":
        missing_state_list = [missing_state for missing_state in data_file["state"] if missing_state not in correct_states]
        states_to_learn = pandas.DataFrame(missing_state_list)
        states_to_learn.to_csv("states_to_learn.csv")
        break



