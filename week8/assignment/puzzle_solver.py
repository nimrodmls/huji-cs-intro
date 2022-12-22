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
    """
    # Arranging all the cells we need to check,
    # the cells are arranged FROM the cell to each direction,
    # so the cells to the right and the cells above are flipped
    row_cells_right = picture[row][:col][::-1]
    row_cells_left = picture[row][col+1:]
    column_cells_above = [picture[row_index][col] for row_index in range(row)][::-1]
    column_cells_below = [picture[row_index][col] for row_index in range(row+1, len(picture))]

    return row_cells_left, row_cells_right, column_cells_above, column_cells_below

def _seen_cells(picture: Picture, row: int, col: int, count_undef=True) -> int:
    """
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
    """
    return _seen_cells(picture, row, col, count_undef=True)

def min_seen_cells(picture: Picture, row: int, col: int) -> int:
    """
    """
    return _seen_cells(picture, row, col, count_undef=False)

def check_constraints(picture: Picture, constraints_set: Set[Constraint]) -> int:
    """
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
                # If we happen to come across a valid constraint, 
                # then we mark the whole result as partial 
                # (it's enough to have 1 to determine this)
                return CONSTRAINTS_PARTIAL
            else:
                # The constraint is not valid, then we mark it so and if
                # the loop finishes with it, it means no constraint is valid
                constraint_status = CONSTRAINTS_INVALID
        # Since we have determined that the max and min are the same, 
        # we just need to check that it matches with the requirement in the seen value
        elif constraint[CONSTRAINT_SEEN_INDEX] != minimal_seen:
            return CONSTRAINTS_INVALID

    return constraint_status

picture1 = [[-1, 0, 1, -1], 
            [0, 1, -1, 1], 
            [1, 0, 1, 0]]
picture2 = [[0, 0, 1, 1], 
            [0, 1, 1, 1], 
            [1, 0, 1, 0]]

def _set_seen_1(picture: Picture, row: int, column: int) -> Picture:
    """
    If we have 1 in the 'seen' field of a constraint, the solution picture
    must have black cells surrounding the '1' cell. There's no other way.
    """
    if 0 != row:
        picture[row-1][column] = BLACK_CELL
    if len(picture)-1 != row:
        picture[row+1][column] = BLACK_CELL
    if 0 != column:
        picture[row][column-1] = BLACK_CELL
    if len(picture[row])-1 != column:
        picture[row][column+1] = BLACK_CELL
        
    return picture

def _create_picture(constraints_set: Set[Constraint], rows: int, columns: int) -> Picture:
    """
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

constraints_set = {(0, 0, 0), (0, 3, 3), (1, 2, 5), (2, 0, 1)}

def _internal_solve_puzzle(picture: Picture, 
                           constraints_set: Set[Constraint], 
                           row_size: int, 
                           column_size: int, 
                           index: int):
    """
    """
    # We reached the end, let the drums roll and decide the result of this picture
    if (row_size * column_size) == index: 
        return check_constraints(picture, constraints_set)

    row, column = (index // (row_size+1)), (index % column_size)

    if UNDEF_CELL != picture[row][column]:
        return _internal_solve_puzzle(picture, constraints_set, row_size, column_size, index + 1)

    for cell_value in [BLACK_CELL, WHITE_CELL]:

        picture[row][column] = cell_value
        constraints_status = check_constraints(picture, constraints_set)

        if CONSTRAINTS_PARTIAL == constraints_status:
            result = _internal_solve_puzzle(picture, constraints_set, row_size, column_size, index + 1)
            if result == CONSTRAINTS_VALID:
                return result
        elif CONSTRAINTS_VALID == constraints_status:
            return constraints_status
        elif CONSTRAINTS_INVALID == constraints_status:
            picture[row][column] = UNDEF_CELL

    return constraints_status

def _internal_solve_puzzle_c(picture: Picture, 
                           constraints_set: Set[Constraint], 
                           row_size: int, 
                           column_size: int, 
                           index: int,
                           sol_count: int):
    """
    """
    # We reached the end, let the drums roll and decide the result of this picture
    if (row_size * column_size) == index: 
        return sol_count

    row, column = (index // row_size), (index % column_size)

    if UNDEF_CELL != picture[row][column]:
        return _internal_solve_puzzle_c(picture, constraints_set, row_size, column_size, index + 1, sol_count)

    for cell_value in [BLACK_CELL, WHITE_CELL]:

        picture[row][column] = cell_value
        constraints_status = check_constraints(picture, constraints_set)

        if CONSTRAINTS_PARTIAL == constraints_status:
            sol_count = _internal_solve_puzzle_c(picture, constraints_set, row_size, column_size, index + 1, sol_count)
        elif CONSTRAINTS_VALID == constraints_status:
            return sol_count + 1
        elif CONSTRAINTS_INVALID == constraints_status:
            picture[row][column] = UNDEF_CELL

    return sol_count

def solve_puzzle(constraints_set: Set[Constraint], n: int, m: int) -> Optional[Picture]:
    """
    """
    picture = _create_picture(constraints_set, n, m)
    if picture is None: # Failed to create picture with the given constraints
        return None

    puzzle_status = _internal_solve_puzzle(picture, constraints_set, n, m, 0)
    if puzzle_status in [CONSTRAINTS_INVALID, CONSTRAINTS_PARTIAL]:
        return None

    return picture

#print(solve_puzzle({(0, 3, 3), (1, 2, 5), (2, 0, 1), (0, 0, 0)}, 3, 4))

def _internal_how_many_solutions(picture, constraints_set: Set[Constraint], row_size, column_size, index, sol_count):
    """
    """
    if (row_size * column_size) == index: 
        return sol_count

    row, column = (index // (row_size+1)), (index % column_size)

    if UNDEF_CELL != picture[row][column]:
        return _internal_how_many_solutions(picture, constraints_set, row_size, column_size, index + 1, sol_count)

    for constraint_value in [BLACK_CELL, UNDEF_CELL]:
        if constraint_value is BLACK_CELL:
            new_constraint = (row, column, BLACK_CELL)
            constraints_set.add(new_constraint)
        result = solve_puzzle(constraints_set, row_size, column_size)
        if result is None:
            if constraint_value is BLACK_CELL:
                constraints_set.remove(new_constraint)
        else:
            sol_count += 1
            _internal_how_many_solutions(picture, constraints_set, row_size, column_size, index + 1, sol_count)

    return sol_count

def how_many_solutions(constraints_set: Set[Constraint], n: int, m: int) -> int:
    """
    """
    base_picture = _create_picture(constraints_set, n, m)
    solution_count = _internal_solve_puzzle_c(base_picture, constraints_set, n, m, 0, 0)
    return solution_count

print(how_many_solutions({(0, 2, 3), (1, 1, 4), (2, 2, 5)}, 3, 3))

def generate_puzzle(picture: Picture) -> Set[Constraint]:
    ...
