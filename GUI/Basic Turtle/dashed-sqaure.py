from turtle import Turtle, Screen


tom = Turtle()
screen = Screen()


tom.color("red")


# Dashed Square Drawing
for _ in range(4):
    for _ in range(10):
        tom.forward(10)
        tom.penup()
        tom.forward(10)
        tom.pendown()
    
    tom.left(90)
    
        



screen.exitonclick()
