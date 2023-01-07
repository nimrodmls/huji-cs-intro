import argparse
import game_utils
from snake_game import SnakeGame
from game_display import GameDisplay

def main_loop(gd: GameDisplay, args: argparse.Namespace) -> None:

    # INIT OBJECTS
    game = SnakeGame(args.apples)
    gd.show_score(0)
    # END OF ROUND 0
    while not game.is_over():
        # DRAW BOARD
        game.draw_board(gd)
        # CHECK KEY CLICKS
        key_clicked = gd.get_key_clicked()
        game.read_key(key_clicked)
        # UPDATE OBJECTS
        game.update_objects()
        # WAIT FOR NEXT ROUND:
        game.end_round()
        gd.end_round()

if __name__ == "__main__":
    print("You should run:\n"
          "> python game_display.py")