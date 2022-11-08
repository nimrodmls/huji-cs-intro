#################################################################
# FILE : ex3.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex3 2023
# DESCRIPTION: Implementing exercise 3
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

def input_list():
    """
    The function receives undefined amount of numbers from the stdin.
    Input is terminated when the user enters an empty string.
    All numbers given by the user are then returned in the same order in a list.
    Including the summation of all numbers as last element of the list.
    """
    num_list = []
    num_sum = 0

    # Receiving the first input, this is a special case
    user_input = input()
    if "" == user_input:
        return [0]

    while "" != user_input:
        user_num = float(user_input)
        num_list.append(user_num)
        num_sum += user_num
        user_input = input()
        
    # Appending the summation as the last element
    num_list.append(num_sum)
    return num_list
