
import math

from typing import Optional
from game_display import GameDisplay, WIDTH, HEIGHT
from game_utils import get_random_apple_data, get_random_wall_data

from snake import Snake
from common import Coordinate, BaseGameObject
from board import Board
from apple import Apple
from wall import Wall

class SnakeGame:

    def __init__(self, total_apples: int, total_walls: int) -> None:
        self.__key_clicked = None
        self._snake = None #Snake(Coordinate(4,4))
        self._board = Board(None, Coordinate(HEIGHT, WIDTH))
        self._total_apples = total_apples
        self._current_apples = 0
        self._total_walls = total_walls
        self._current_walls = 0
        self._score = 0
        self._is_over = False

    def read_key(self, key_clicked: Optional[str])-> None:
        self.__key_clicked = key_clicked
    
    def _out_of_bounds_callback(self, source: BaseGameObject, off_board: bool) -> None:
        """
        """
        if type(source) is Wall and off_board:
            # Wall is completely off the board, we should remove it
            self._board.remove_game_object(source)
            self._current_walls -= 1

        if type(source) is Snake:
            self.set_is_over()

    def _interaction_callback(self, source: BaseGameObject, dest: BaseGameObject) -> None:
        """
        """
        if type(dest) is Apple and type(source) is Snake:
            self.add_points()
            self._board.remove_game_object(dest)
            self._current_apples -= 1
            self._snake.expand(3)

        if type(dest) is Apple and type(source) is Wall:
            self._board.remove_game_object(dest)
            self._current_apples -= 1

        if type(dest) is Snake and type(source) is Wall:
            dest.split(source.get_coordinates()[0])

        # Ending the game if the snake hits a wall, or hit itself
        if (type(dest) is Snake or type(dest) is Wall) and type(source) is Snake:
            self.set_is_over()

    def add_points(self):
        """
        """
        self._score += math.floor(math.sqrt(len(self._snake)))

    def update_objects(self)-> None:
        if self._snake is not None:
            self._snake.change_direction(self.__key_clicked)
        self._board.move_game_objects(self._interaction_callback, 
                                      self._out_of_bounds_callback)

        # Adding walls if missing any
        if self._total_walls > self._current_walls:
            x_coord, y_coord, direction = get_random_wall_data()
            if self._board.add_game_object(
                Wall(Coordinate.from_legacy_coordinate((x_coord, y_coord)), direction)):
                self._current_walls += 1

        # Adding apples if missing
        if self._total_apples > self._current_apples:
            if self._board.add_game_object(
                Apple(Coordinate.from_legacy_coordinate(get_random_apple_data()))):
                self._current_apples += 1

    def draw_board(self, gd: GameDisplay) -> None:
        self._board.draw_board(gd)
        gd.show_score(self._score)

    def end_round(self) -> None:
        pass

    def set_is_over(self):
        self._is_over = True

    def is_over(self) -> bool:
        return self._is_over