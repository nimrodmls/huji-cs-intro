
import math

from typing import Optional
from game_display import GameDisplay, WIDTH, HEIGHT
from game_utils import get_random_apple_data

from snake import Snake
from common import Coordinate, BaseGameObject
from board import Board, OutOfBounds
from apple import Apple
from wall import Wall

class SnakeGame:

    def __init__(self, total_apples: int) -> None:
        self.__key_clicked = None
        self._snake = Snake(Coordinate(4,4))
        self._board = Board(self._snake, Coordinate(HEIGHT, WIDTH))
        self._board.add_game_object(Apple(Coordinate(0, 5)))
        self._board.add_game_object(Apple(Coordinate(1, 5)))
        self._board.add_game_object(Apple(Coordinate(2, 5)))
        self._board.add_game_object(Wall(Coordinate(20, 20), "Up"))
        self._total_apples = total_apples
        self._current_apples = 0
        self._score = 0
        self._is_over = False

    def read_key(self, key_clicked: Optional[str])-> None:
        self.__key_clicked = key_clicked

    def _interaction_callback(self, source: BaseGameObject, dest: BaseGameObject) -> None:
        """
        """
        if type(dest) is Apple and type(source) is Snake:
            self.add_points()
            self._board.remove_game_object(dest)
            self._current_apples -= 1
            self._snake.expand(3)
        
        if (type(dest) is Snake or dest is OutOfBounds) and type(source) is Snake:
            self.set_is_over()

    def add_points(self):
        """
        """
        self._score += math.floor(math.sqrt(len(self._snake)))

    def update_objects(self)-> None:
        print(len(self._snake))
        self._snake.change_direction(self.__key_clicked)
        self._board.move_game_objects(self._interaction_callback)

        # Adding walls if missing any
        # Adding apples if missing
        if self._total_apples != self._current_apples:
            self._board.add_game_object(
                Apple(Coordinate.from_legacy_coordinate(get_random_apple_data())))
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