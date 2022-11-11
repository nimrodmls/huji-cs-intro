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
    The function returns the product of two vectors (list) of the same length.
    Giving vectors of varied lengths will return None.
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
    This function receives a list (sequence) of possibly-infinite real numbers,
    and returns whether the sequence is (strictly) increasing or (strictly) decreasing.
    The list returned by this function is of 4 elements, signifying the monotonicity state:
    Index 0 is 'Increasing', Index 1 is 'Strictly Increasing, Index 2 is 'Decreasing' 
    and Index 3 is 'Strictly Decreasing'.
    If the list returned has 4 elements of False, it means the sequence is neither of the options.
    """
    monotonicity = [True, True, True, True]
    if len(sequence) < 2:
        return monotonicity

    current_max = sequence[0]
    current_min = sequence[0]
    for num in sequence[1:]:
        # Sequence is increasing
        if num > current_max:
            current_max = num
            # Possibly an increasing sequence, all decreasing values are set to False
            monotonicity[2] = False
            monotonicity[3] = False
        # Sequence is decreasing
        elif num < current_min:
            current_min = num
            # Possibly a decreasing sequence, all increasing values are set to False
            monotonicity[0] = False
            monotonicity[1] = False
        elif (num < current_max) and monotonicity[0]:
            # Sequence was marked as increasing, but infact we found a smaller number, 
            # so it has no monotonicty
            return [False, False, False, False]
        elif (num > current_min) and monotonicity[2]:
            # Sequence was marked as decreasing, but infact we found a greater number, 
            # so it has no monotonicty
            return [False, False, False, False]
        else:
            # Sequence has the same number twice consecutively, 
            # henceforth it's not strictly increasing/decreasing
            monotonicity[3] = False
            monotonicity[1] = False
    return monotonicity
        
def monotonicity_inverse(def_bool):
    """
    This function receives a list of 4 boolean elements, signifying the monotonicity state:
    Index 0 is 'Increasing', Index 1 is 'Strictly Increasing, Index 2 is 'Decreasing' 
    and Index 3 is 'Strictly Decreasing'.
    According to the input, the function returns a sequence (list) of 4 real numbers made
    as example to the state given in the booleans list.
    Warning: Giving a bad combination of booleans (e.g. Increasing & Decreasing) returns None.
    """
    MONOTONICITY_CASES = {
        '[False, False, False, False]': [1, 0, 1, 0],
        '[True, False, False, False]': [0, 0, 1, 1],
        '[True, True, False, False]': [1, 2, 3, 4],
        '[False, False, True, False]': [1, 1, 0, 0],
        '[False, False, True, True]': [4, 3, 2, 1],
    }

    if str(def_bool) not in MONOTONICITY_CASES.keys():
        return None
    else:
        return MONOTONICITY_CASES[str(def_bool)]

def convolve(mat):
    """
    This function implements the convolution operator.
    The function receives a matrix (list) of at least 3x3, with rows as list elements, and within
    the list elements the columns, so each element in the given list should be of the same length.
    The function returns another matrix with each row containing summation of all the 3x3 combinations.
    """
    if 0 == len(mat):
        return None
    
    convolution_matrix = []
    # We iterate over all the rows, row_index signifies the *last* row in the current 3x3 matrix iteration
    for row_index in range(2, len(mat)):
        convolution_row = []
        # We iterate over all the columns, column_index points to the *last* row in the current 3x3 matrix
        for column_index in range(2, len(mat[row_index])):
            # The length of every row is the same, we can rely on that
            matrix_sum = 0
            # We iterate over every row in the current 3x3 matrix and calculating its sum,
            # adding it to the total summation of the 3x3 matrix.
            for current_row in mat[row_index-2:row_index+1]:
                matrix_sum += sum(current_row[column_index-2:column_index+1])
            # 3x3 matrix sum is done, next!
            convolution_row.append(matrix_sum)
        # All combinations of the 3x3 matrices in the current 3 rows are done, next!
        convolution_matrix.append(convolution_row)
    return convolution_matrix

def sum_of_vectors(vec_list):
    """
    The function returns the sum of vectors.
    The function receives a list of vectors (lists of the same lengths).
    The value returned is at the length of each vector, and each element is the sum of each index.
    If the list received is empty, None is returned.
    If the lists within the vector list are empty, an empty list is returned.
    """
    if 0 == len(vec_list):
        return None

    summation = []
    # Build and iterate over combinations of single elements in the vector list
    for vector_comb in zip(*vec_list):
        summation.append(sum(vector_comb))
    return summation

def num_of_orthogonal(vectors):
    """
    The function returns the number of orthogonal vectors in the given vector list.
    The function receives a list of vectors (lists).
    The returned value is an integer.
    """
    orthogonal_count = 0
    limit = 1
    for vector in vectors:
        for sub_vector in vectors[limit:]:
            if 0 == inner_product(vector, sub_vector):
                orthogonal_count += 1
        limit += 1
    return orthogonal_count
