import turtle


image = "india.gif"
game_is_on = True


# UI
screen = turtle.Screen()
screen.setup(width=800, height=700)
screen.title("India State Game")
screen.addshape(image)

turtle.shape(image)


# get x and y value
def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
