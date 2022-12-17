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
    row_cells_left = picture[row][col:]
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

picture = [[-1, 0, 1, -1], [0, 1, -1, 1], [1, 0, 1, 0]] 

def min_seen_cells(picture: Picture, row: int, col: int) -> int:
    """
    """
    return _seen_cells(picture, row, col, count_undef=False)

print(min_seen_cells(picture, 1, 1))

def check_constraints(picture: Picture, constraints_set: Set[Constraint]) -> int:
    ...


def solve_puzzle(constraints_set: Set[Constraint], n: int, m: int) -> Optional[Picture]:
    ...


def how_many_solutions(constraints_set: Set[Constraint], n: int, m: int) -> int:
    ...


def generate_puzzle(picture: Picture) -> Set[Constraint]:
    ...
