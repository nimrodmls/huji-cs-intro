#################################################################
# FILE : shapes.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex2 2023
# DESCRIPTION: Calculating shapes' properties
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

import math

def shape_area():
    """
    Calculating the area of different geometric shapes
    """
    choice = input("Choose shape (1=circle, 2=rectangle, 3=triangle): ")
    if choice not in ["1", "2", "3"]: # Invalid input
        return None
    if "1" == choice: # Calculating the area of a circle
        return math.pi * math.pow(float(input()), 2)
    elif "2" == choice: # Calculating the area of a rectangle
        return float(input()) * float(input())
    elif "3" == choice: # Calculating the area of equilateral triangle
        return (math.sqrt(3)/4) * math.pow(float(input()), 2)
