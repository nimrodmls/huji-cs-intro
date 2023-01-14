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
    The primary game functionality for Rush Hour.
    The game rules are that the board is 7x7, exit cell is in (3,7),
    with cars permitted to go either left, right, up or down.
    The permitted cars are Y(ellow), B(lue), O(range), G(reen), W(hite), R(ed).
    Once a car in horizontal orientation arrives to the target cell, the game
    is stopped. User is permitted to stop the game beforehand.
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
        Prints the board, along with information about the possible
        movements of the cars on board.
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
        Does a single turn for the user.
        The user is prompted with the details of the car movements, and is
        requested with directions for a car on the board.
        Whether the input is valid or invalid, the function returns True, signals
        to the caller that the game shall continue.
        If the user requested the game to exit, the function returns False.
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

        # Making sure the car name is OK, it may be possible that the car is
        #   added by a mysterious way into the board, but it's not valid according
        #   to the game rules, so we don't allow it.
        user_car_name = ready_input[Game.INPUT_CAR_NAME_INDEX]
        if user_car_name not in ['Y', 'B', 'O', 'G', 'W', 'R']:
            print("[!] Invalid car name! Make sure you name a valid car!")
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

def _add_car_to_board(board, car_name, car_config):
    """
    Adding a car, according to the given configuration, to the board.
    If the car does not comply with the game rules, the addition fails 
    and False is returned. Otherwise True. 
    """
    # Checking that car name is valid
    if car_name not in ['Y', 'B', 'O', 'G', 'W', 'R']:
        return False

    # Checking car length validity
    car_length = car_config[CAR_CONFIG_LENGTH_INDEX]
    if car_length not in range(2,5):
        return False

    # Location validity is checked within board
    car_location = car_config[CAR_CONFIG_LOC_INDEX]
    
    # Checking orientation validity
    car_orientation = car_config[CAR_CONFIG_ORIENTATION_INDEX]
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
    All the cars from the configuration are added, this is best effort.
    If no cars comply with the game rules, the game finishes instantly.
    
    :param json_path: The path on the filesystem for the JSON configuration.
    """
    board = Board()
    car_config = load_json(json_path)

    result = False
    # Adding all cars to the board
    for car_name in car_config:
        if _add_car_to_board(board, car_name, car_config[car_name]):
            result = True # We successfully added a car to the board, 
                          # the game can start even if some failed
            
    if not result:
        print("[!] Car configuration is invalid, game cannot start!")
        return

    # Starting the game
    game = Game(board)
    game.play()

if __name__== "__main__":
    # Checking if we received a single argument
    if 2 != len(sys.argv):
        print("[!] Error - Expected JSON Config Path; {exec} [json_path]".format(exec=sys.argv[0]))
    else:
        main(sys.argv[1])
