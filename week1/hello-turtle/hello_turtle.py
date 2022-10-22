#################################################################
# FILE : hello_turtle.py
# WRITER : Nimrod Mallis , mallis , 316598747
# EXERCISE : intro2cs1 ex1 2023
# DESCRIPTION: A simple program that...
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

import turtle

# Accomplishes part 1 of the task
def draw_triangle():
    """
    Draws a triangle using the turtle module
    """
    for iter in range(3):
        turtle.forward(45)
        turtle.right(120)

# Accomplishes part 2 of the task
def draw_sail():
    """
    Draws the sail of a ship using the turtle module.
    """
    turtle.left(90)
    turtle.forward(50)
    turtle.right(150)
    draw_triangle()
    turtle.right(30)
    turtle.up()
    turtle.forward(50)
    turtle.down()
    turtle.left(90)

# Accomplishes part 3 of the task
def draw_ship():
    """
    Draw a single ship using the turtle module.
    """
    # Draws the sails and board of the ship
    for iter in range(3):
        turtle.forward(50)
        draw_sail()
    turtle.forward(50)
    # Draws the "head" of the ship
    turtle.right(120)
    turtle.forward(20)
    # Draws the hull of the ship
    turtle.right(60)
    turtle.forward(180)
    # Draws the "back" of the ship
    turtle.right(60)
    turtle.forward(20)
    # Reset turtle orientation
    turtle.right(120)

if __name__ == "__main__" :
    draw_ship()
