#################################################################
# FILE : largest_and_smallest.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex1 2023
# DESCRIPTION: Minimum/Maximum utilities
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

def largest_and_smallest(num1, num2, num3):
    """
    Finding the minimal number and the maximal number from 3 given numbers
    """
    nums = [num1, num2, num3]
    max_num = nums[0]
    min_num = nums[0]
    for current_num in nums:
        if current_num > max_num:
            max_num = current_num
        if current_num < min_num:
            min_num = current_num
    return max_num, min_num
