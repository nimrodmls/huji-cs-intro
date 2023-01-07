from typing import Optional
from game_display import GameDisplay, WIDTH, HEIGHT

from snake import Snake
from common import Coordinate, BaseGameObject
from board import Board
from apple import Apple

class SnakeGame:

    def __init__(self) -> None:
        self.__key_clicked = None
        self._snake = Snake(Coordinate(4,4), 3)
        self._board = Board(self._snake, Coordinate(HEIGHT, WIDTH))
        self._cnt = 0
        self._expansions = 0
        self._score = 0
        self._is_over = False

    def read_key(self, key_clicked: Optional[str])-> None:
        self.__key_clicked = key_clicked

    def _interaction_callback(self, source: BaseGameObject, dest: BaseGameObject) -> None:
        """
        """
        if type(source) is Snake and type(dest) is Apple:
            self._score += 1

    def update_objects(self)-> None:
        if (self._cnt % 20) == 0:
            print("Expanding")
            #self._expansions += 1
            
        if self._expansions > 0:
            if self._snake.move(self.__key_clicked, expand=True):
                self._expansions -= 1
        else:
            #self._snake.move(self.__key_clicked)
            if not self._board.move_snake(self.__key_clicked, False, None):
                self._is_over = True
        self._cnt += 1

    def draw_board(self, gd: GameDisplay) -> None:
        self._board.draw_board(gd)

    def end_round(self) -> None:
        pass

    def is_over(self) -> bool:
        return self._is_over