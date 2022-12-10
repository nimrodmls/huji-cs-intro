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

def _internal_is_even(n: int, flag: bool) -> bool:
    """
    Internal function for the is_even function.
    This allows passing a flag, alternating between Even and Odd
    """
    if 0 == n:
        return flag
    else:
        return _internal_is_even(subtract_1(n), not flag)

def is_even(n: int) -> bool:
    """
    Checking if the given non-negative integer is even
    """
    return _internal_is_even(n, True)




if __name__ == "__main__":
    print(is_even(2))