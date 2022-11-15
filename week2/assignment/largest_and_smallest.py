#################################################################
# FILE : largest_and_smallest.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex2 2023
# DESCRIPTION: Minimum/Maximum utilities. In the testing function,
#              the two custom values I chose are:
#              1) Same 3 values, then min/max should be the same
#              2) Negative values
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

def check_largest_and_smallest():
    """
    Testing the largest_and_smallest function with a matrix of different edge cases
    """
    test_matrix = (((17, 1, 6), (17, 1)), 
                   ((1, 17, 6), (17, 1)), 
                   ((1, 1, 2), (2, 1)),
                   ((1, 1, 1), (1, 1)),
                   ((-1, -1, -2), (-1, -2)))
    has_all_cases_passed = True
    for test_case in test_matrix:
        if test_case[1] != largest_and_smallest(*test_case[0]):
            has_all_cases_passed = False
    return has_all_cases_passed
