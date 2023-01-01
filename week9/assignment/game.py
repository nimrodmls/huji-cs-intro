#################################################################
# FILE : game.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex9 2023
# DESCRIPTION: Implementing the main program for Rush Hour Game
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

# External imports
import sys
from helper import load_json

# Internal imports
from car import Car
from board import Board

CAR_CONFIG_LENGTH_INDEX = 0
CAR_CONFIG_LOC_INDEX = 1
CAR_CONFIG_ORIENTATION_INDEX = 2


class Game:
    """
    Add class description here
    """

    CAR_MOVE_NAME_INDEX = 0
    CAR_MOVE_KEY_INDEX = 1
    CAR_MOVE_DESCRIPTION_INDEX = 2

    INPUT_CAR_NAME_INDEX = 0
    INPUT_CAR_DIRECTION_INDEX = 1

    EXIT_INPUT = "!"

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self._board = board

    def _new_turn_prompt(self):
        """
        """
        print(self._board)
        print("[!] Possible moves for current turn: ")
        for move in self._board.possible_moves():
            print("\t[>] {name},{key} - {description}".format(
                name=move[Game.CAR_MOVE_NAME_INDEX],
                key=move[Game.CAR_MOVE_KEY_INDEX],
                description=move[Game.CAR_MOVE_DESCRIPTION_INDEX]
            ))

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        self._new_turn_prompt()
        user_input = input("[!] Enter the move (or ! to exit): ")
        if Game.EXIT_INPUT == user_input:
            print("[!] Exiting Game...")
            return False

        ready_input = user_input.split(',')
        # If the user input is bad, let it be received again
        if 2 != len(ready_input):
            print("[!] Invalid input! Make sure you follow the car,direction style.")
            return True # This is intentional, we don't want the game to exit

        # Making sure the user direction input is okay,
        #   this is actually checked in board in some way, but the instructions
        #   are quite unclear about those validations
        user_direction = ready_input[Game.INPUT_CAR_DIRECTION_INDEX]
        if user_direction not in ['u', 'r', 'd', 'l']:
            print("[!] Invalid direction! Make sure it is a valid direction!")
            return True
        
        # Trying to actually move the car
        if not self._board.move_car(ready_input[Game.INPUT_CAR_NAME_INDEX], user_direction):
            print ("[!] Moving the car has failed")
            return True

        return True

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        while self._board.cell_content(self._board.target_location()) is None:
            # Checking if the user requested to exit prematurely,
            #   if so return at that moment
            if not self.__single_turn():
                return

        print(self._board)
        print("[!] The game has been won!")      

def _add_cars_to_board(board, car_config):
    """
    """
    for car_name in car_config:
        # Checking that car name is valid
        if car_name not in ['Y', 'B', 'O', 'G', 'W', 'R']:
            return False

        # Checking car length validity
        car_length = car_config[car_name][CAR_CONFIG_LENGTH_INDEX]
        if car_length not in range(2,5):
            return False

        # Location validity is checked within board
        car_location = car_config[car_name][CAR_CONFIG_LOC_INDEX]
        
        # Checking orientation validity
        car_orientation = car_config[car_name][CAR_CONFIG_ORIENTATION_INDEX]
        if car_orientation not in [Car.HORIZONTAL_ORIENTATION, Car.VERTICAL_ORIENTATION]:
            return False

        # Trying to add the car to the board
        current_car = Car(car_name, car_length, car_location, car_orientation)
        if not board.add_car(current_car):
            return False

    return True

def main(json_path):
    """
    The primary function for initializing the game objects and running the game.
    """
    board = Board()
    car_config = load_json(json_path)
    if not _add_cars_to_board(board, car_config):
        print("[!] Error - Car config invalid, make sure cars don't overlap and are named properly")

    game = Game(board)
    game.play()

if __name__== "__main__":
    if 2 != len(sys.argv):
        print("[!] Error - Expected JSON Config Path; {exec} [json_path]".format(exec=sys.argv[0]))
    else:
        main(sys.argv[1])
