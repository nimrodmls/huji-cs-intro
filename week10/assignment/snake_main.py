import argparse
import game_utils
from snake_game import SnakeGame
from game_display import GameDisplay

from common import Coordinate
from board import Board
from snake import Snake

def _initialize_game(args: argparse.Namespace) -> SnakeGame:
    """
    """
    board = Board(Coordinate(args.height, args.width))
    
    # If game is not on debug mode, create the snake
    snake = None
    if not args.debug:
        snake = Snake(Coordinate(args.height//2, args.width//2))

    return SnakeGame(board, snake, args.apples, args.walls, args.rounds)

def main_loop(gd: GameDisplay, args: argparse.Namespace) -> None:

    # INIT OBJECTS
    game = _initialize_game(args)
    gd.show_score(0)
    # DRAW BOARD
    game.draw_board(gd)    
    # END OF ROUND 0
    while not game.is_over():
        # CHECK KEY CLICKS
        key_clicked = gd.get_key_clicked()
        game.read_key(key_clicked)
        # UPDATE OBJECTS
        game.update_objects()
        # DRAW BOARD
        game.draw_board(gd)
        # WAIT FOR NEXT ROUND:
        game.end_round()
        gd.end_round()

if __name__ == "__main__":
    print("You should run:\n"
          "> python game_display.py")