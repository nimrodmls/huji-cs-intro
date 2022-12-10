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

def _subtract_times(n: int, times: int) -> int:
    """
    """
    if 0 == times:
        return n
    return _subtract_times(subtract_1(n), subtract_1(times))

def is_even(n: int) -> bool:
    """
    """
    if -1 == n:
        return False
    elif 0 == n:
        return True
    else:
        return is_even(_subtract_times(n, 2))


if __name__ == "__main__":
    print(is_even(0))