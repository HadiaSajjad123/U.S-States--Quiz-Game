from turtle import Screen, Turtle
import pandas as pd

screen = Screen()
screen.setup(width=500, height=300)
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
Turtle().shape(image)

data = pd.read_csv("50_states.csv")
states = data["state"].to_list()
guessed_states = []
while len(guessed_states) < 50:

  answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                            prompt="What's another state's name?")

  if answer == "exit":
    missing_states = []
    for state in states:
      if state not in guessed_states:
        missing_states.append(state)
    new_data = pd.DataFrame(missing_states)
    new_data.to_csv("Remaining_states.csv")
    break

  if answer in states:
    guessed_states.append(answer)
    t = Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer]
    t.goto(state_data.x.item(), state_data.y.item())
    t.write(answer)

