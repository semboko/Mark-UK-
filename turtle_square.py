import turtle
from math import sqrt

turtle.speed(10)

def draw_square(x, y, size):
    inital_shift = size / 2
    turtle.penup()
    turtle.setpos(x - inital_shift, y - inital_shift)
    turtle.pendown()

    for i in range(4):
        turtle.forward(size)
        turtle.left(90)

def draw_square_crossed(x, y, size):
    draw_square(x, y, size)

    turtle.setpos(x - size/2, y + size/2)
    turtle.left(-45)
    diag = sqrt(2 * size ** 2)
    turtle.forward(diag)
    
    turtle.setpos(x + size/2, y + size/2)
    turtle.left(-90)
    turtle.forward(diag)
    
    turtle.left(135)

TURTLE_IS_DRAWING = False

def clicked(x, y):
    global TURTLE_IS_DRAWING
    if TURTLE_IS_DRAWING:
        return
    TURTLE_IS_DRAWING = True
    draw_square_crossed(x, y, 50)
    TURTLE_IS_DRAWING = False

turtle.onscreenclick(clicked)
turtle.mainloop()