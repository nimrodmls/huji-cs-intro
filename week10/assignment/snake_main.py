#################################################################
# FILE : snake_main.py
# WRITERS : Nimrod M. ; Dor K.
# EXERCISE : intro2cs1 ex10 2023
# DESCRIPTION: Runs the Snake Game
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

# External imports
import argparse
from game_display import GameDisplay

# Internal imports
from snake_game import SnakeGame
from common import Coordinate
from board import Board
from snake import Snake

def _initialize_game(args: argparse.Namespace) -> SnakeGame:
    """
    Initializing the game with the given arguments.
    """
    board = Board(Coordinate(args.height, args.width))
    
    # If game is not on debug mode, create the snake
    snake = None
    if not args.debug:
        snake = Snake(Coordinate(args.height//2, args.width//2))

    return SnakeGame(board, snake, args.apples, args.walls, args.rounds)

def main_loop(gd: GameDisplay, args: argparse.Namespace) -> None:
    """
    Runs the Snake Game with the given arguments and Game Display.
    """
    game = _initialize_game(args)
    gd.show_score(0)

    # ROUND 0 STARTS HERE
    # No movements are made in the round 0
    game.draw_board(gd)    
    game.end_round()
    gd.end_round()
    # ROUND 0 ENDS HERE

    # Begin primary game loop
    while not game.is_over():
        
        # Changing the direction of the snake if necessary
        game.set_snake_direction(gd.get_key_clicked())
        # Updating the objects on the game board
        game.update_objects()
        
        # Round finalization
        # Drawing the board and ending the round
        game.draw_board(gd)
        game.end_round()
        gd.end_round()

if __name__ == "__main__":
    print("You should run:\n"
          "> python game_display.py")