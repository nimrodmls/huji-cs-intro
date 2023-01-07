from typing import Optional
from game_display import GameDisplay, WIDTH, HEIGHT

from snake import Snake
from common import Coordinate
from board import Board

class SnakeGame:

    def __init__(self) -> None:
        self.__key_clicked = None
        self._snake = Snake(Coordinate(4,4), 3)
        self._board = Board(self._snake, Coordinate(HEIGHT, WIDTH))
        self._cnt = 0
        self._expansions = 0

    def read_key(self, key_clicked: Optional[str])-> None:
        self.__key_clicked = key_clicked

    def update_objects(self)-> None:
        if (self._cnt % 20) == 0:
            print("Expanding")
            #self._expansions += 1
            
        if self._expansions > 0:
            if self._snake.move(self.__key_clicked, expand=True):
                self._expansions -= 1
        else:
            #self._snake.move(self.__key_clicked)
            self._board.move_snake(self.__key_clicked, False, None)
        self._cnt += 1

    def draw_board(self, gd: GameDisplay) -> None:
        self._board.draw_board(gd)

    def end_round(self) -> None:
        pass

    def is_over(self) -> bool:
        return False