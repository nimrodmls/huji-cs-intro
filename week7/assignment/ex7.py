#################################################################
# FILE : ex7.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex7 2023
# DESCRIPTION: Implementing recursive stuff
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

from ex7_helper import N, add, subtract_1
import hanoi_game

def mult(x: N, y: int) -> N:
    """
    Multiplies the given number x with the given non-negative number
    """
    if 0 == y:
        return 0
    if 1 == y:
        return x
    return add(x, mult(x, subtract_1(y)))


if __name__ == "__main__":
    print(mult(5,20))