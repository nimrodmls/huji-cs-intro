#################################################################
# FILE : ex7.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex7 2023
# DESCRIPTION: Implementing recursive stuff
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: en.wikipedia.org/wiki/Tower_of_Hanoi
# NOTES: N/A
#################################################################

from typing import Any
from ex7_helper import N, add, subtract_1, divide_by_2, is_odd, append_to_end

def mult(x: N, y: int) -> N:
    """
    Multiplies the given number x with the given non-negative number
    """
    if 0 == y:
        return 0
    if 1 == y:
        return x
    return add(x, mult(x, subtract_1(y)))

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

def log_mult(x: N, y: int) -> N:
    """
    Multiplies the given number x with the given non-negative integer y.
    The function's runtime is O(log x)
    """
    if 0 == y:
        return 0
    elif 1 == y:
        return x
    h = log_mult(x, divide_by_2(y))
    if is_odd(y):
        return add(add(h, h), x)
    else:
        return add(h, h)

def is_power(b: int, x: int) -> bool:
    """
    Checking if b raised to any power results x.
    The function's runtime is O(log b * log x)
    """
    if b == x:
        return True
    # If b is 0 or 1, and it's not equal to x, 
    # then no power in the world can raise b to x
    # If b exceeds x it means there is no possible integer power.
    elif (b > x) or (0 == b) or (1 == b):
        return False
    else:
        return is_power(log_mult(b, b), x)

def _internal_reverse(s: str, index: int, current_str: str) -> str:
    """
    Helper function for the reverse function.
    Allows the passing of extra parameters needed for the operation.
    """
    if len(s) == len(current_str):
        return current_str

    current_str = append_to_end(current_str, s[index-1])
    return _internal_reverse(s, len(s)-len(current_str), current_str)

def reverse(s: str) -> str:
    """
    Reverses a string from end to beginning
    """
    new_s = ""
    return _internal_reverse(s, len(s), new_s)

def play_hanoi(hanoi: Any, n: int, src: Any, dest: Any, temp: Any):
    """
    Playing the Towers of Hanoi Game.
    Expecting to get a valid Hanoi and Tower objects from the module.
    """
    if 0 >= n:
        return
    
    play_hanoi(hanoi, n-1, src, temp, dest)
    hanoi.move(src, dest)
    play_hanoi(hanoi, n-1, temp, dest, src)

if __name__ == "__main__":
    print(reverse("intro"))