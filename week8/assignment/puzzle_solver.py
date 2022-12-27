#################################################################
# FILE : puzzle_solver.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex8 2023
# DESCRIPTION: Puzzle Solving with Backtracking
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

from typing import List, Tuple, Set, Optional

# We define the types of a partial picture and a constraint (for type checking).
Picture = List[List[int]]
Constraint = Tuple[int, int, int] # Row, Column, Value

# Cell values for the Picture
BLACK_CELL = 0
WHITE_CELL = 1
UNDEF_CELL = -1 # Undefined cell

# Constraints values for check_constraints
CONSTRAINTS_INVALID = 0
CONSTRAINTS_VALID = 1
CONSTRAINTS_PARTIAL = 2

# Indices for the constraints tuple
CONSTRAINT_ROW_INDEX = 0
CONSTRAINT_COLUMN_INDEX = 1
CONSTRAINT_SEEN_INDEX = 2

def _get_cells_to_check(picture: Picture, row: int, col: int) -> Tuple[List[int], 
                                                                       List[int], 
                                                                       List[int], 
                                                                       List[int]]:
    """
    Getting all the cells that need to be checked for a specific coordinate (at row, col)
    The cells are NOT getting checked in this function.
    Returns 4 lists of integers from the picture - 
        Cells to the left, to the right, up and down
    The cells above and to the right are flipped, 
        so checking them can be peformed from closest to farthest
    """
    # Arranging all the cells we need to check,
    # the cells are arranged FROM the cell to each direction,
    # so the cells to the right and the cells above are flipped
    row_cells_right = picture[row][:col][::-1]
    row_cells_left = picture[row][col+1:]
    column_cells_above = [picture[row_index][col] for row_index in range(row)][::-1]
    column_cells_below = [picture[row_index][col] for row_index in range(row+1, len(picture))]

    return row_cells_left, row_cells_right, column_cells_above, column_cells_below

def _seen_cells(picture: Picture, row: int, col: int, count_undef: bool=True) -> int:
    """
    Checking how many cells are 'seen' from the current cell (e.g. how many
        white cells are between the (row, col) cell and the next black cell (if exists).
    It is possible to count the undefined cells as 'seen' via count_undef parameter.
    """
    invalid_cells = [BLACK_CELL] if count_undef else [BLACK_CELL, UNDEF_CELL]
    seen_cells = 0

    # Current cell is black, nothing is seen from here but darkness
    if picture[row][col] in invalid_cells:
        return 0
    
    seen_cells += 1 # Adding 1 to self, as long as it's not black cell

    # Going over all the relevant cells
    for cells_direction in _get_cells_to_check(picture, row, col):
        current_cell = BLACK_CELL
        current_index = 0

        # If the current direction has no cells, it means we're on the edge
        if 0 != len(cells_direction):
            current_cell = cells_direction[current_index]

        # As long as we don't meet with a black cell, continue
        while (current_cell not in invalid_cells) and (current_index < len(cells_direction)):

            current_cell = cells_direction[current_index]
            if current_cell not in invalid_cells:
                seen_cells += 1 # Incrementing the seen cells

            current_index += 1 # Advancing to the next index

    return seen_cells

def max_seen_cells(picture: Picture, row: int, col: int) -> int:
    """
    Returns the maximum of seen cells from the requested (row, col) cell.
    The maximum of seen cells includes the undefined cells.
    """
    return _seen_cells(picture, row, col, count_undef=True)

def min_seen_cells(picture: Picture, row: int, col: int) -> int:
    """
    Returns the minimum of seen cells from the requested (row, col) cell.
    The minimum of seen cells excludes the undefined cells (e.g. only whites)
    """
    return _seen_cells(picture, row, col, count_undef=False)

def check_constraints(picture: Picture, constraints_set: Set[Constraint]) -> int:
    """
    Validates the constraints compared to the given picture.
    The status returned indicates whether the constraints are met, 
        not met at all, or partially met
    :return: Either CONSTRAINT_INVALID, CONSTRAINT_VALID or CONSTRAINT_PARTIAL
    """
    constraint_status = CONSTRAINTS_VALID
    for constraint in constraints_set:
        minimal_seen = min_seen_cells(picture, 
                                      constraint[CONSTRAINT_ROW_INDEX], 
                                      constraint[CONSTRAINT_COLUMN_INDEX])
        maximal_seen = max_seen_cells(picture, 
                                      constraint[CONSTRAINT_ROW_INDEX], 
                                      constraint[CONSTRAINT_COLUMN_INDEX])

        # The minimal and maximal are different, 
        # we can't have a fully valid result at this time
        if maximal_seen != minimal_seen:
            # Checking the constraint's 'seen' value to determine the result
            if (minimal_seen <= constraint[CONSTRAINT_SEEN_INDEX]) and (maximal_seen >= constraint[CONSTRAINT_SEEN_INDEX]):
                # If the constraint is partially valid then we mark it that way
                # for now, if the loop finishes then it means that partial is the final result
                constraint_status = CONSTRAINTS_PARTIAL
            else:
                # The constraint is not valid no matter what, we should return with that
                return CONSTRAINTS_INVALID
        # Since we have determined that the max and min are the same, 
        # we just need to check that it matches with the requirement in the seen value
        elif constraint[CONSTRAINT_SEEN_INDEX] != minimal_seen:
            return CONSTRAINTS_INVALID

    return constraint_status

def _set_seen_1(picture: Picture, row: int, column: int) -> Picture:
    """
    If we have 1 in the 'seen' field of a constraint, the solution picture
    must have black cells surrounding the '1' cell. There's no other way.
    """
    if 0 != row: # Setting black to the left of the cell
        picture[row-1][column] = BLACK_CELL
    if len(picture)-1 != row: # Setting black to the right of the cell
        picture[row+1][column] = BLACK_CELL
    if 0 != column: # Setting black above the cell
        picture[row][column-1] = BLACK_CELL
    if len(picture[row])-1 != column: # Setting black below the cell
        picture[row][column+1] = BLACK_CELL
        
    return picture

def _create_picture(constraints_set: Set[Constraint], rows: int, columns: int) -> Optional[Picture]:
    """
    Creating a picture of rows X columns with the given constraints.
    Some constraints can be interpreted immediately to black or white cells.
    If some constraints overlap, None is returned as this is impossible.
    """
    picture = [[UNDEF_CELL for column in range(columns)] for row in range(rows)]
    for constraint in constraints_set:
        row_index = constraint[CONSTRAINT_ROW_INDEX]
        column_index = constraint[CONSTRAINT_COLUMN_INDEX]

        # We have two overlapping constraints - This is bad
        if UNDEF_CELL != picture[row_index][column_index]:
            return None
        
        # Choosing which color to assign to this cell
        cell_color = WHITE_CELL
        if 0 == constraint[CONSTRAINT_SEEN_INDEX]:
            cell_color = BLACK_CELL

        # We encountered 1 as seen, this means it's 
        # supposed to be surrounded with black cells
        if 1 == constraint[CONSTRAINT_SEEN_INDEX]:
            picture = _set_seen_1(picture, row_index, column_index)

        picture[row_index][column_index] = cell_color

    return picture

def _internal_solve_puzzle(picture: Picture, 
                           constraints_set: Set[Constraint], 
                           row_size: int, 
                           column_size: int, 
                           index: int) -> int:
    """
    Internal function optimized to backtracking for solving the puzzle.
    The index provided when first calling this function should be 0 -
        unless you wish to experiment, and that's on you if anything goes wrong.
    """
    # We reached the end, let the drums roll and decide the result of this picture
    if (row_size * column_size) == index: 
        return check_constraints(picture, constraints_set)

    # Calculating the position of the index
    row, column = (index // column_size), (index % column_size)

    # The index points to a white or black cell, we can't decide its fate
    # (perhaps it was decided by a constraint, or earlier by the "loop")
    if UNDEF_CELL != picture[row][column]:
        return _internal_solve_puzzle(picture, 
                                      constraints_set, 
                                      row_size, 
                                      column_size, 
                                      index + 1)

    constraints_status = CONSTRAINTS_INVALID
    # Iterating on all possible cell values, trying them out on the board
    for cell_value in [BLACK_CELL, WHITE_CELL]:
        
        picture[row][column] = cell_value
        constraints_status = check_constraints(picture, constraints_set)

        # If the constraints are (partially) met, then continue placing values
        # onto the puzzle and see if anything comes out of it.
        if CONSTRAINTS_INVALID != constraints_status:
            constraints_status = _internal_solve_puzzle(picture, 
                                                        constraints_set, 
                                                        row_size, 
                                                        column_size, 
                                                        index + 1)
            # The inner iterations indicate that a solution has been found
            # we can return as we search for a single solution.
            if CONSTRAINTS_VALID == constraints_status:
                return constraints_status
        else:
            # Reverting the committed value, as this cell causes the board to be invalid
            picture[row][column] = UNDEF_CELL

    return constraints_status

def solve_puzzle(constraints_set: Set[Constraint], n: int, m: int) -> Optional[Picture]:
    """
    Creates a solution for the given n X m puzzle board with the given constraints.
    None is returned if no solution has been found, the picture is returned otherwise.
    """
    picture = _create_picture(constraints_set, n, m)
    if picture is None: # Failed to create picture with the given constraints
        return None

    puzzle_status = _internal_solve_puzzle(picture, constraints_set, n, m, 0)
    # The constraints can't be met. Partial shouldn't return probably.
    if puzzle_status in [CONSTRAINTS_INVALID, CONSTRAINTS_PARTIAL]:
        return None

    return picture

def _internal_how_many_solutions(picture: Picture, 
                                 constraints_set: Set[Constraint], 
                                 row_size: int, 
                                 column_size: int, 
                                 index: int,
                                 sol_count: int) -> int:
    """
    Internal function optimized for backtracking, 
        for finding the number of solutions a picture has
    index & sol_count should be 0 when first calling the function.
    If they are not 0, then you either wish to experiment, 
        or lie to yourself about the number of solutions, and that's on you
    """
    # We reached the end, let the drums roll and decide the result of this picture
    if (row_size * column_size) == index:
        if check_constraints(picture, constraints_set):
            sol_count += 1
        return sol_count

    row, column = (index // column_size), (index % column_size)

    # If the cell is already set (usually by constraints), 
    #   then ignore and continue as it is considered constant
    if UNDEF_CELL != picture[row][column]:
        return _internal_how_many_solutions(picture, 
                                            constraints_set, 
                                            row_size, 
                                            column_size, 
                                            index + 1, 
                                            sol_count)

    # We set all the possible values for the cells and 
    #   check if they give us some sort of a valid solution
    for cell_value in [BLACK_CELL, WHITE_CELL]:
        picture[row][column] = cell_value
        constraints_status = check_constraints(picture, constraints_set)

        # If the constraints are not met, we should not 
        #   continue setting values in the picture and backtrack. 
        # If they are (partially) met, then continue setting 
        #   values until either we have a solution and reach a 
        #   full picture (see the first condition in the function),
        #   or we reach invalid constraints 
        #   (meaning here, but further recursively inside).
        if CONSTRAINTS_INVALID != constraints_status:
            sol_count = _internal_how_many_solutions(picture, 
                                                     constraints_set, 
                                                     row_size, 
                                                     column_size, 
                                                     index + 1, 
                                                     sol_count)

    # No matter what, revert the comitted cell value, 
    #   as we look for all possible solutions.
    # (+ we don't intend to return a picture in the end, 
    #   so the whole thing can be undefined by the end)
    picture[row][column] = UNDEF_CELL
    return sol_count

def how_many_solutions(constraints_set: Set[Constraint], n: int, m: int) -> int:
    """
    Checking how many solutions are possible with the given
    constraints set on a n X m board.
    """
    base_picture = _create_picture(constraints_set, n, m)
    if base_picture is None: # Failed to create picture with the given constraints
        return 0
        
    return _internal_how_many_solutions(base_picture, constraints_set, n, m, 0, 0)

def generate_puzzle(picture: Picture) -> Set[Constraint]:
    """
    Generates a set of constraints for the given picture.
    The function returns a single set, but more are possible.
    The set returned is optimal, there are no redundant constraints.
    """
    temp_constraints: Set[Constraint] = set()
    # Generate temporary constraints, those are not optimal in any way
    for row_index in range(len(picture)):
        for cell_index in range(len(picture[row_index])):

            current_cell = picture[row_index][cell_index]
            if current_cell is WHITE_CELL:
                # It's a white cell, insert a constraint with all the seen cells from this cell
                temp_constraints.add(
                    (row_index, cell_index, _seen_cells(picture, row_index, cell_index)))
            elif current_cell is BLACK_CELL:
                # It's a black cell, just insert a constraint of a black cell
                temp_constraints.add((row_index, cell_index, BLACK_CELL))

    final_constraints: Set[Constraint] = set()
    # Now checking how many of those constraints are actually necessary
    # We do this by removed constraint and checking if the solution is the same
    # - If it is, this constraint is redundant
    # - If it isn't this constraint is necessary
    for constraint_index in range(len(temp_constraints)):
        constraint = temp_constraints.pop()
        # Building the 'current' constraints, built of the necessary ones
        #   we found thus far, and of the unknown necessity ones.
        current_constraints: Set[Constraint] = set()
        current_constraints.update(final_constraints, temp_constraints)
        # Trying to solve the puzzle, checking if the solution is the same
        solution = solve_puzzle(current_constraints, len(picture), len(picture[0]))
        # If the picture is different than the original, or there
        #   are more solutions than a single one, it means that this 
        #   constraint is necessary
        if (solution != picture) or \
            (1 != how_many_solutions(current_constraints, len(picture), len(picture[0]))):
            final_constraints.add(constraint)

    return final_constraints
