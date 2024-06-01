import turtle
from math import sqrt

turtle.speed(0)
turtle.hideturtle()

CELL_SIZE = 150
WINNER = None


def draw_line(init_x, init_y, length):
    turtle.penup()
    turtle.setpos(init_x, init_y)
    turtle.pendown()
    turtle.forward(length)


def draw_board():
    turtle.width(10)
    turtle.color("grey")
    draw_line(-1.5 * CELL_SIZE, 0.5 * CELL_SIZE, 3 * CELL_SIZE)
    draw_line(-1.5 * CELL_SIZE, -0.5 * CELL_SIZE, 3 * CELL_SIZE)
    turtle.right(90)
    draw_line(-0.5 * CELL_SIZE, 1.5 * CELL_SIZE, 3 * CELL_SIZE)
    draw_line(0.5 * CELL_SIZE, 1.5 * CELL_SIZE, 3 * CELL_SIZE)
    turtle.left(90)


def draw_cross(x, y):
    turtle.color("red")
    square_edge = CELL_SIZE * 0.8
    diag = sqrt(2 * square_edge ** 2)
    turtle.right(45)
    draw_line(x - square_edge/2, y + square_edge/2, diag)
    turtle.right(90)
    draw_line(x + square_edge/2, y + square_edge/2, diag)
    turtle.left(135)


def draw_circle(x, y):
    turtle.color("blue")
    diameter = 0.8 * CELL_SIZE
    turtle.penup()
    turtle.setpos(x, y - diameter/2)
    turtle.pendown()
    turtle.circle(diameter/2)

def out_of_board(x, y):
    if x < -1.5 * CELL_SIZE:
        return True
    if x > 1.5 * CELL_SIZE:
        return True
    if y < -1.5 * CELL_SIZE:
        return True
    if y > 1.5 * CELL_SIZE:
        return True


def detect_row(x, y):
    if y > 0.5 * CELL_SIZE:
        return 1
    if y < -0.5 * CELL_SIZE:
        return -1
    return 0


def detect_col(x, y):
    if x < -0.5 * CELL_SIZE:
        return -1
    if x > 0.5 * CELL_SIZE:
        return 1
    return 0


draw_board()

turn = True
occupied_cells = dict()


def detect_winner():
    # Check each column - winner or not?
    for col_idx in (-1, 0, 1):
        xs_counter = 0
        os_counter = 0
        for key, value in occupied_cells.items():
            if key[1] == col_idx:
                if value == True:
                    xs_counter = xs_counter + 1
                else:
                    os_counter = os_counter + 1
        if xs_counter == 3:
            # The winner is X
            turtle.color("grey")
            turtle.right(90)
            draw_line(col_idx * CELL_SIZE, 1.6 * CELL_SIZE, 3.2 * CELL_SIZE)
            return True
        elif os_counter == 3:
            # The winner is O
            turtle.color("grey")
            turtle.right(90)
            draw_line(col_idx * CELL_SIZE, 1.6 * CELL_SIZE, 3.2 * CELL_SIZE)
            return False

    # Check each row - winner or not?
    for row_idx in (-1, 0, 1):
        xs_counter = 0
        os_counter = 0
        for key, value in occupied_cells.items():
            if key[0] == row_idx:
                if value == True:
                    xs_counter = xs_counter + 1
                else:
                    os_counter = os_counter + 1
        if xs_counter == 3:
            # The winner is X in this particular row
            turtle.color("grey")
            draw_line(-1.6 * CELL_SIZE, CELL_SIZE * row_idx, 3.2 * CELL_SIZE)
            return True
        elif os_counter == 3:
            # The winner is O in this particular row
            turtle.color("grey")
            draw_line(-1.6 * CELL_SIZE, CELL_SIZE * row_idx, 3.2 * CELL_SIZE)
            return False

    # Check the left diag - winner or not?
    # Check the right diag - winner or not?
    left_diag = [(1, -1), (0, 0), (-1, 1)]
    right_diag = [(1, 1), (0, 0), (-1, -1)]

    left_diag_turns = []
    right_diag_turns = []

    for key, value in occupied_cells.items():
        if key in left_diag:
            left_diag_turns.append(value)

        if key in right_diag:
            right_diag_turns.append(value)

    if len(left_diag_turns) == 3 and left_diag_turns[0] == left_diag_turns[1] == left_diag_turns[2]:
        turtle.color("grey")
        turtle.right(45)
        draw_line(-1.5 * CELL_SIZE, 1.5 * CELL_SIZE, 4.1 * CELL_SIZE)
        return left_diag_turns[0]
    
    if len(right_diag_turns) == 3 and right_diag_turns[0] == right_diag_turns[1] == right_diag_turns[2]:
        turtle.color("grey")
        turtle.right(135)
        draw_line(1.5 * CELL_SIZE, 1.5 * CELL_SIZE, 4.1 * CELL_SIZE)
        return right_diag_turns[0]


def clicked(x, y):
    global WINNER

    if WINNER is not None:
        return

    if out_of_board(x, y):
        return

    column_index = detect_col(x, y)
    row_index = detect_row(x, y)

    if (row_index, column_index) in occupied_cells:
        return

    x = column_index * CELL_SIZE
    y = row_index * CELL_SIZE
    
    global turn
    if turn:
        draw_cross(x, y)
    else:
        draw_circle(x, y)
    
    # occupied_cells.add((row_index, column_index))
    occupied_cells[(row_index, column_index)] = turn
    
    WINNER = detect_winner()
    turn = not turn

turtle.onscreenclick(clicked)
turtle.mainloop()