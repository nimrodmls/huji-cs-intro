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
    # Only one real solution
    if solution1 == solution2:
        return solution1, None
    else: # Two real solutions
        return solution1, solution2

def quadratic_equation_user_input():
    """
    Solving a quadratic equation receiving from the user
    """
    user_input = input("Insert coefficients for a, b and c: ")
    user_input = user_input.split()
    if '0' == user_input[0]:
        print("The parameter 'a' may not equal 0")
        return
    solution1, solution2 = quadratic_equation(
        float(user_input[0]), float(user_input[1]), float(user_input[2]))
    # No real solutions
    if (solution1 is None) and (solution2 is None):
        print("The equation has no solutions")
    # 1 real solution
    elif (solution1 is not None) and (solution2 is None):
        print("The equation has 1 solution: {sol1}".format(sol1=solution1))
    else: # 2 real solutions
        print("The equation has 2 solutions: {sol1} and {sol2}".format(sol1=solution1, sol2=solution2))
