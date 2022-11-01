#################################################################
# FILE : quadratic_equation.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex2 2023
# DESCRIPTION: Solving quadratic polynomials using the formula
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

import math

def quadratic_equation(a, b, c):
    """
    Solving quadratic polynomial of the form ax^2 + bx + c, with a,b,c being the coefficients
    """
    discriminant = math.pow(b, 2) - (4*a*c)
    if discriminant < 0:
        # Discriminant is negative -> No solutions
        return None, None
    solution1 = ((-b) + (math.sqrt(discriminant)))/(2*a)
    solution2 = ((-b) - (math.sqrt(discriminant)))/(2*a)
    if solution1 == solution2:
        return solution1, None
    else:
        return solution1, solution2
