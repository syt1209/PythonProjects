import pandas
import turtle

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
states_names = states_data.state.to_list()
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("black")

answered_states = []
while len(answered_states) < len(states_names):
    answer_state = screen.textinput(title=f"{len(answered_states)}/50 States Correct", prompt="What is the state's "
                                                                                              "name?").capitalize()
    if answer_state.capitalize() == "Exit":
        not_answered = []
        for state in states_names:
            if state not in answered_states:
                not_answered.append(state)
        states_to_learn = pandas.DataFrame(not_answered)
        states_to_learn.to_csv("states_to_learn.csv")
        break
    if answer_state in states_names and answer_state not in answered_states:
        answered_states.append(answer_state)
        row = states_data[states_data["state"] == answer_state]
        x_cor = row.x.to_list()[0]
        y_cor = row.y.to_list()[0]
        pen.goto(x_cor, y_cor)
        pen.write(answer_state.capitalize(), align="center", font=("Arial", 8, "normal"))



screen.exitonclick()
