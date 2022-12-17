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
Constraint = Tuple[int, int, int]


def max_seen_cells(picture: Picture, row: int, col: int) -> int:
    ...


def min_seen_cells(picture: Picture, row: int, col: int) -> int:
    ...


def check_constraints(picture: Picture, constraints_set: Set[Constraint]) -> int:
    ...


def solve_puzzle(constraints_set: Set[Constraint], n: int, m: int) -> Optional[Picture]:
    ...


def how_many_solutions(constraints_set: Set[Constraint], n: int, m: int) -> int:
    ...


def generate_puzzle(picture: Picture) -> Set[Constraint]:
    ...
