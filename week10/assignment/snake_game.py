from typing import Optional
from game_display import GameDisplay

from snake import Snake
from common import Coordinate

class SnakeGame:

    def __init__(self) -> None:
        self.__key_clicked = None
        self._snake = Snake(Coordinate(4,4), 3)

    def read_key(self, key_clicked: Optional[str])-> None:
        self.__key_clicked = key_clicked

    def update_objects(self)-> None:
        print(self.__key_clicked)
        self._snake.move(self.__key_clicked)

    def draw_board(self, gd: GameDisplay) -> None:
        coords = self._snake.get_coordinates()
        for coordinate in coords:
            gd.draw_cell(coordinate.column, coordinate.row, "blue")

    def end_round(self) -> None:
        pass

    def is_over(self) -> bool:
        return False