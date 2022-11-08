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
    * This function implements Task 1 of the Exercise
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

def inner_product(vec1, vec2):
    """
    """
    product = 0
    # Vectors should be of the same length
    if len(vec1) != len(vec2):
        return None
    # Since we checked the lists are of the same length, 
    # we can use zip to iterate over both vectors at the same instant
    for num1, num2 in zip(vec1, vec2):
        product += num1 * num2
    return product

def sequence_monotonicity(sequence):
    """
    """
    # The monotonicity state - Index 0 is 'Increasing', Index 1 is 'Strictly Increasing,
    # Index 2 is 'Decreasing' and Index 3 is 'Strictly Decreasing'.
    monotonicity = [True, True, True, True]
    current_max = sequence[0]
    current_min = sequence[0]
    for num in sequence[1:]:
        # Sequence is not increasing nor decreasing
        if (num < current_max) and (num > current_min):
            return [False, False, False, False]
        # Sequence is increasing
        elif num >= current_max:
            if num > current_max:
                current_max = num
            else:
                # Sequence is not strictly increasing, we had the same maximal value
                monotonicity[1] = False
            # Possibly an increasing sequence, all decreasing values are set to False
            monotonicity[2] = False
            monotonicity[3] = False
        # Sequence is decreasing
        elif num <= current_min:
            if num < current_min:
                current_min = num
            else:
                # Sequence is not strictly decreasing, we had the same minimal value
                monotonicity[3] = False
            # Possibly a decreasing sequence, all increasing values are set to False
            monotonicity[0] = False
            monotonicity[1] = False
    return monotonicity
        
print(sequence_monotonicity([1,1, 2,3, 0, 4]))


