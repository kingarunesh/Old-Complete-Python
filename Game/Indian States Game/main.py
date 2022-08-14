import turtle
import pandas


image = "india.gif"
game_is_on = True
correct_guess = 0


# UI
screen = turtle.Screen()
screen.setup(width=800, height=700)
screen.title("India State Game")
screen.addshape(image)

turtle.shape(image)


# CSV
data = pandas.read_csv("states-of-india.csv")
states = data.state.to_list()


while game_is_on:
    user = turtle.textinput(title=f"{correct_guess}/29 Correct Guess", prompt="Enter Indian state names?").title()

    if user in states:
        correct_guess += 1
        
        x = data[data.state == user].x
        y = data[data.state == user].y

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(x), int(y))
        t.write(user)

    elif user == "Exit":
        game_is_on = False



screen.exitonclick()
