import turtle
import pandas as pd

"""This is a simple game that allows you guess the Capital of a State in Nigeria and then populate the state into 
it's map location. To exit the game, input "Exit" """


# the function keeps all the gaming activities to enable player run the game from shell
def play_game():
    # set up screen with turtle
    screen = turtle.Screen()
    screen.setup(width=1160, height=1040)
    screen.title("Nigeria States Game")
    image = "Nigeria_states_map.gif"
    screen.addshape(image)
    turtle.shape(image)

    # load the csv data and collect a list of the capitals to check users input for correct answer
    data = pd.read_csv("nigeria_state_coordinate.csv")
    capitals = [capital for capital in data.capital]
    guess_capital = []

    while len(guess_capital) < 37:
        answer_capital = screen.textinput(title=f"{len(guess_capital)}/37 States Correct",
                                          prompt="What's another State's name?").title()

        if answer_capital == "Exit":
            break

        if answer_capital in capitals:
            guess_capital.append(answer_capital)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.capital == answer_capital]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(state_data.state.item())


if __name__ == "__main__":
    play_game()
