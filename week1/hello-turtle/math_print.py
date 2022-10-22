#################################################################
# FILE : math_print.py
# WRITER : Nimrod Mallis , mallis , 316598747
# EXERCISE : intro2cs1 ex1 2023
# DESCRIPTION: A simple program that...
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

import math

def golden_ratio():
    print((1 + math.sqrt(5)) / 2)

def six_squared():
    print(math.pow(6, 2))

def hypotenuse():
    print(math.hypot(5, 12))

def pi():
    print(math.pi)

def e():
    print(math.e)

def squares_area():
    areas = [str(math.pow(edge, 2)) for edge in range(1, 11)]
    print(" ".join(areas))

if __name__ == "__main__" :
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_area()
