#################################################################
# FILE : ex7.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex7 2023
# DESCRIPTION: Implementing recursive stuff
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: en.wikipedia.org/wiki/Tower_of_Hanoi
# NOTES: N/A
#################################################################

from typing import Any, List
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

def _internal_is_power(b: int, x: int, orig: int) -> bool:
    """
    """
    if (b == x) or (x == 1):
        return True
    # If b is 0 or 1, and it's not equal to x, 
    # then no power in the world can raise b to x
    # If b exceeds x it means there is no possible integer power.
    elif (b > x) or (0 == b) or (1 == b):
        return False
    else:
        current_exponent = log_mult(b, orig)
        if x == current_exponent:
            return True
        return _internal_is_power(current_exponent, x, orig)

def is_power(b: int, x: int) -> bool:
    """
    Checking if b raised to any power results x.
    The function's runtime is O(log b * log x)
    """
    return _internal_is_power(b, x, b)

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

def play_hanoi(hanoi: Any, n: int, src: Any, dest: Any, temp: Any) -> None:
    """
    Playing the Towers of Hanoi Game.
    Expecting to get a valid Hanoi and Tower objects from the module.
    """
    if 0 >= n:
        return
    
    play_hanoi(hanoi, n-1, src, temp, dest)
    hanoi.move(src, dest)
    play_hanoi(hanoi, n-1, temp, dest, src)

def _internal_number_of_ones_(current: int, left: int, cnt: int) -> int:
    """
    """
    if 0 == left:
        return cnt
    # Works only when 1 is on the right
    if (1 == current % 10):
        cnt += 1
    if (1 == current // 10):
        cnt += 1
    return _internal_number_of_ones_(current+1, left-1, cnt)

def _internal_number_of_ones_2(current_n: int, cnt: int) -> int:
    """
    """
    if 0 == current_n:
        return cnt
    
    if (1 == current_n % 10) or (1 == current_n // 10):
        if (1 == current_n % 10):
            cnt += 1
        if (1 == current_n // 10):
            cnt += 1

    if 10 <= current_n // 10:
        cnt = _internal_number_of_ones_2(current_n // 10, cnt)

    return _internal_number_of_ones_2(current_n-1, cnt)

def _count_ones(current_n: int, cnt: int) -> int:
    """
    """
    if 0 == current_n:
        return cnt
    elif 1 == current_n:
        return cnt + 1
    elif 1 == current_n % 10:
        cnt += 1
    return _count_ones(current_n // 10, cnt)

def _internal_number_of_ones(current_n: int, cnt: int) -> int:
    """
    """
    if 0 == current_n:
        return cnt
    return _internal_number_of_ones(current_n-1, _count_ones(current_n, cnt))

def number_of_ones(n: int) -> int:
    """
    """
    counter = 0
    counter = _internal_number_of_ones(n, counter)
    return counter

def _compare_1d_lists(l1: List[int], l2: List[int], index: int) -> bool:
    """
    """
    # Lists are not of the same length, they're obviously not the same
    if len(l1) != len(l2):
        return False
    
    # We reached the end, great success
    # Getting here means that the length of both lists are the same
    if len(l1) == index:
        return True
    
    if l1[index] == l2[index]:
        # If the items are the same, continue for the next items
        return _compare_1d_lists(l1, l2, index+1)
    else:
        # One different element is enough to sell the rights to the 
        # songs we don't have, wrap our instruments and go back to Netanya
        return False

def _internal_compare_2d_lists(l1: List[List[int]], l2: List[List[int]], index: int) -> bool:
    """
    """
    if 0 == index:
        return True
    # Actually comparing
    result = _compare_1d_lists(l1[index-1], l2[index-1], 0)
    if result:
        # Continue for the next lists if this one is okay
        return _internal_compare_2d_lists(l1, l2, index-1)
    else:
        return False

def compare_2d_lists(l1: List[List[int]], l2: List[List[int]]) -> bool:
    """
    """
    # Lists are not of the same length, they're obviously not the same
    if len(l1) != len(l2):
        return False

    return _internal_compare_2d_lists(l1, l2, len(l1))

def magic_list(n: int) -> List[Any]:
    """
    """
    new_list = []
    if 0 != n:
        new_list = magic_list(n-1)
        new_list.append(magic_list(n-1))
    return new_list
    
