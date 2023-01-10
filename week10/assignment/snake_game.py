#################################################################
# FILE : snake_game.py
# WRITERS : Nimrod M. ; Dor K.
# EXERCISE : intro2cs1 ex10 2023
# DESCRIPTION: Implements the primary game functionality
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

# External imports
import math
from typing import Optional
from game_display import GameDisplay
from game_utils import get_random_apple_data, get_random_wall_data

# Internal imports
from common import Coordinate, BaseGameObject, SnakeException, Direction
from snake import Snake
from board import Board
from apple import Apple
from wall import Wall

class GameOverException(SnakeException):
    """
    Raised mainly from inner functions of SnakeGame
    in order to signal that the game should end.
    """
    pass

class SnakeGame:
    """
    The primary game object for Snake
    """

    def __init__(
            self, 
            board: Board,
            snake: Optional[Snake],
            max_apples: int, 
            max_walls: int,
            max_rounds: int) -> None:
        """
        Creates a new Snake Game with the given Board and Snake.
        max_apples and max_walls specify the maximum amount of 
            apples and walls to be on the wall at a given time.
        max_rounds specifies when the game will terminate automatically
            if it didn't terminate naturally.
        """
            
        self._new_direction = None
        self._snake = snake
        self._board = board

        # Apple info
        self._max_apples = max_apples
        self._current_apples = 0

        # Wall info
        self._max_walls = max_walls
        self._current_walls = 0
        self._score = 0
        self._is_over = False
        self._current_round = 0
        self._max_rounds = max_rounds

        # If we received a snake object add it to the board
        if self._snake is not None:
            self._board.add_game_object(self._snake)

        # Edge case: Adding apples and walls on the Snake itself will cause
        #   them not to generate in the first round
        self._add_apples_and_walls()

    def set_snake_direction(self, direction: Optional[Direction])-> None:
        """
        Setting the moving direction of the snake.
        """
        self._new_direction = direction
    
    def add_points(self):
        """
        Adding to the score tally.
        The points are calculated by the floor of the 
            square root of the snake's current length.
        """
        self._score += math.floor(math.sqrt(len(self._snake)))

    def update_objects(self)-> bool:
        """
        """
        try:
            # Changing the direction of the snake if we have a snake
            if self._snake is not None:
                self._snake.change_direction(self._new_direction)

            self._board.move_game_objects(self._interaction_callback, 
                                        self._out_of_bounds_callback)

            self._add_apples_and_walls()

        # If any SnakeException received we end the game properly
        #   any other exception is passed on
        except SnakeException: 
            self._set_is_over()
            return False

        return True

    def _out_of_bounds_callback(self, source: BaseGameObject, off_board: bool) -> None:
        """
        Deals with all interactions of game objects and the game board.
        Called from within Board.
        """
        if type(source) is Wall and off_board:
            # Wall is completely off the board, we should remove it
            self._board.remove_game_object(source)
            self._current_walls -= 1

        if type(source) is Snake:
            # The snake met with the board boundries, we end the game
            raise GameOverException

    def _interaction_callback(self, source: BaseGameObject, dest: BaseGameObject) -> None:
        """
        Deals with all interactions of the game objects with one another.
        Called from within Board.
        """
        if type(dest) is Apple and type(source) is Snake:
            # The snake with an apple, remove it, 
            #   increment the score and expand the snake
            self.add_points()
            self._board.remove_game_object(dest)
            self._current_apples -= 1
            self._snake.expand(3)

        if type(dest) is Apple and type(source) is Wall:
            # The wall met with an apple, destroy it
            self._board.remove_game_object(dest)
            self._current_apples -= 1

        if type(dest) is Snake and type(source) is Wall:
            # The wall met with a snake, split the snake
            # If the split left the snake with 0 or 1 cells,
            #   the game ends
            dest.split(source.get_coordinates()[0])

        # Ending the game if the snake hits a wall, or hit itself
        if (type(dest) is Snake or type(dest) is Wall) and type(source) is Snake:
            raise GameOverException

    def _wall_move_callback(self):
        """
        Deals with the conditions for the wall to move.
        Currently the wall moves if and only if the round is even number.
        """
        return 0 == (self._current_round % 2)

    def _add_apples_and_walls(self):
        """
        Adds apples and walls to the wall, if any are missing.
        The coordinates for each are generated randomly, if the
            generated coordinates overlap with any other object on the game
            board the addition fails and it is not tried again
        """
        # Adding walls if missing any
        if self._max_walls > self._current_walls:
            x_coord, y_coord, direction = get_random_wall_data()
            if self._board.add_game_object(
                Wall(Coordinate.from_legacy_coordinate((x_coord, y_coord)), 
                     direction,
                     self._wall_move_callback)):
                self._current_walls += 1

        # Adding apples if missing
        if self._max_apples > self._current_apples:
            if self._board.add_game_object(
                Apple(Coordinate.from_legacy_coordinate(get_random_apple_data()))):
                self._current_apples += 1

    def draw_board(self, gui: GameDisplay) -> None:
        """
        Drawing the current board on the screen and setting the score value
        """
        self._board.draw_board(gui)
        gui.show_score(self._score)

    def end_round(self) -> None:
        """
        Finishing the current round
        Placing apples and walls if needed, and incrementing the round counter
        """
        self._current_round += 1

    def _set_is_over(self) -> None:
        """
        Setting the is_over flag, signaling that the game should end
        """
        self._is_over = True

    def is_over(self) -> bool:
        """
        Returns if any of the end conditions were satisfied.
        Possible ending routes:
            1) The max round has been reached.
            2) The Snake met with a wall or the board boundries
            3) The Snake was split to an invalid length (currently 1 or 0)
        """
        return self._is_over or (self._current_round > self._max_rounds if self._max_rounds != -1 else False)