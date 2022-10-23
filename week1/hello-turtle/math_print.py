#################################################################
# FILE : math_print.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex1 2023
# DESCRIPTION: A simple program that...
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

import math

def golden_ratio():
    """
    Calculates the golden ratio
    """
    print((1 + math.sqrt(5)) / 2)

def six_squared():
    """
    Calculates 6^2
    """
    print(math.pow(6, 2))

def hypotenuse():
    """
    Calculates the hypotenuse of a right triangle
    """
    print(math.hypot(5, 12))

def pi():
    """
    Prints the pi constant
    """
    print(math.pi)

def e():
    """
    Prints Euler's constant 
    """
    print(math.e)

def squares_area():
    """
    Prints the area of squares with edges from 1 to 10 (including)
    """
    areas = [str(math.pow(edge, 2)) for edge in range(1, 11)]
    print(" ".join(areas))

if __name__ == "__main__" :
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_area()
