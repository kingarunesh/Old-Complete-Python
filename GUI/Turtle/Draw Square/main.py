from turtle import Turtle, Screen


tom = Turtle()
screen = Screen()


tom.color("red")


# Normal Square Drawing
for _ in range(4):
    tom.forward(100)
    tom.left(90)


screen.exitonclick()
