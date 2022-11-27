#################################################################
# FILE : image_editor.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs ex5 2022-2023
# DESCRIPTION: TBA
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

##############################################################################
#                                   Imports                                  #
##############################################################################
from ex5_helper import *
from typing import Optional
import copy
import math
import sys

##############################################################################
#                                  Constants                                 #
##############################################################################

# Indices of each channel in an RGB Pixel
RED_CHANNEL_INDEX = 0
GREEN_CHANNEL_INDEX = 1
BLUE_CHANNEL_INDEX = 2

# Values for the grayscale summation of RGB Pixel
RED_GRAYSCALE_VALUE = 0.299
GREEN_GRAYSCALE_VALUE = 0.587
BLUE_GRAYSCALE_VALUE = 0.114

# Commands
QUIT_COMMAND_VALUE = 8

##############################################################################
#                                  Functions                                 #
##############################################################################

def separate_channels(image: ColoredImage) -> List[SingleChannelImage]:
    """
    """
    channels = [[] for channel in range(len(image[0][0]))]

    for row in image:
        channel_row = list(zip(*row))
        for channel in range(len(channel_row)):
            channels[channel].append(list(channel_row[channel]))

    return channels

def combine_channels(channels: List[SingleChannelImage]) -> ColoredImage:
    """
    """
    image = []
    for row in zip(*channels):
        current_row = []
        for pixel in zip(*row):
            current_row.append(list(pixel))
        image.append(current_row)

    return image

def calc_grayscale_sum(rgb_pixel):
    """
    """
    sum_value = (rgb_pixel[RED_CHANNEL_INDEX] * RED_GRAYSCALE_VALUE) + \
                (rgb_pixel[GREEN_CHANNEL_INDEX] * GREEN_GRAYSCALE_VALUE) + \
                (rgb_pixel[BLUE_CHANNEL_INDEX] * BLUE_GRAYSCALE_VALUE)
    if 255 < sum_value:
        sum_value = 255
    elif 0 > sum_value:
        sum_value = 0
    return sum_value

def RGB2grayscale(colored_image: ColoredImage) -> SingleChannelImage:
    """
    """
    return [[round(calc_grayscale_sum(pixel)) for pixel in row] for row in colored_image]

def blur_kernel(size: int) -> Kernel:
    """
    """
    return [[1/(size**2)]*size]*size

def apply_kernel_to_matrix(matrix, kernel):
    """
    same size
    """
    matrix_sum = 0
    kernel_center = int((len(kernel)-1)/2)
    kernel_center = kernel_center if 0 != kernel_center else 1

    for row in zip(matrix, kernel):
        for pixel, kernel_cell in zip(*row):
            matrix_sum += (matrix[kernel_center][kernel_center] if pixel is None else pixel) * kernel_cell

    matrix_sum = round(matrix_sum)
    # Checkng if the sum is going out of bounds
    if 0 > matrix_sum:
        matrix_sum = 0
    elif 255 < matrix_sum:
        matrix_sum = 255

    return matrix_sum

def get_padded_image(image, size):
    """
    """
    padded_image = copy.deepcopy(image)

    if 0 == size:
        size = 1
    
    for row_pads in range(size):
        padded_image.insert(0, [None for row_len in range(len(image[0]))]) # Insert "above"
        padded_image.append([None for row_len in range(len(image[0]))]) # Insert "below"

    for row_index in range(len(padded_image)):
        for column_pads in range(size):
            padded_image[row_index].insert(0, None) # Insert "left"
            padded_image[row_index].append(None) # Insert "right"

    return padded_image

def apply_kernel(image: SingleChannelImage, kernel: Kernel) -> SingleChannelImage:
    """
    """
    padded_image = get_padded_image(image, int((len(kernel)-1)/2))
    
    manipulated_image = []
    for row_index in range(len(image)):
        image_row = []

        for column_index in range(len(image[row_index])):
            current_matrix = []

            kernel_length = len(kernel)
            if 1 == len(kernel):
                image_row.append(image[row_index][column_index] * kernel[0][0])
            else:
                for current_row in padded_image[row_index:row_index+kernel_length]:
                    current_matrix.append(current_row[column_index:column_index+kernel_length])

                image_row.append(apply_kernel_to_matrix(current_matrix, kernel))

        manipulated_image.append(image_row)

    return manipulated_image

def bilinear_interpolation(image: SingleChannelImage, y: float, x: float) -> int:
    """
    """
    delta_x = x%1 if x < 1 else 1
    delta_y = y%1 if y < 1 else 1

    a = image[math.floor(y)][math.floor(x)]
    b = image[math.ceil(y)][math.floor(x)]
    c = image[math.floor(y)][math.ceil(x)]
    d = image[math.ceil(y)][math.ceil(x)]
    
    return round((a*(1-delta_x)*(1-delta_y)) + \
                (b*delta_y*(1-delta_x)) + \
                (c*delta_x*(1-delta_y)) + \
                (d*delta_x*delta_y))

def resize(image: SingleChannelImage, new_height: int, new_width: int) -> SingleChannelImage:
    """
    """
    new_image = [[0 for columns in range(new_width)] for rows in range(new_height)]

    # Taking care of all pixels
    for row_index in range(len(new_image)):
        for pixel_index in range(len(new_image[row_index])):
            new_image[row_index][pixel_index] = \
                bilinear_interpolation(image, 
                                       (row_index/(len(new_image)-1))*(len(image)-1), 
                                       (pixel_index/(len(new_image[row_index])-1)*(len(image[0])-1)))

    # Giving the corners a special treatment
    new_image[0][0] = image[0][0]
    new_image[0][len(new_image[0])-1] = image[0][len(image[0])-1]
    new_image[len(new_image)-1][0] = image[len(image)-1][0]
    new_image[len(new_image)-1][len(new_image[0])-1] = image[len(image)-1][len(image[0])-1]

    return new_image

def rotate_90(image: Image, direction: str) -> Image:
    """
    """
    new_image = []
    for combination in zip(*image):
        current = list(combination)
        if 'R' == direction:
            current.reverse()
            new_image.append(current)
        if 'L' == direction:
            new_image.insert(0, current)

    return new_image

def get_edges(image: SingleChannelImage, blur_size: int, block_size: int, c: float) -> SingleChannelImage:
    """
    """
    edges_image = []
    blurred_image = apply_kernel(image, blur_kernel(blur_size))
    thresholds_image = apply_kernel(blurred_image, blur_kernel(block_size))

    for row in zip(thresholds_image, blurred_image):
        current_row = []

        for threshold_pixel, blurred_pixel in zip(*row):
            if threshold_pixel - c > blurred_pixel:
                current_row.append(0)
            else:
                current_row.append(255)
        
        edges_image.append(current_row)

    return edges_image

def quantize(image: SingleChannelImage, N: int) -> SingleChannelImage:
    """
    """
    return [[round(math.floor(pixel*(N/256))*(255/(N-1))) for pixel in row] for row in image]


def quantize_colored_image(image: ColoredImage, N: int) -> ColoredImage:
    """
    """
    all_channels = separate_channels(image)
    return combine_channels([quantize(all_channels[RED_CHANNEL_INDEX], N),
                            quantize(all_channels[GREEN_CHANNEL_INDEX], N),
                            quantize(all_channels[BLUE_CHANNEL_INDEX], N)])

def handle_command_line():
    """
    """
    if 2 != len(sys.argv):
        print("[!] Too many parameters received. Usage: image_editor.py {image_path}")
        return

    return sys.argv[1]

def _get_number_input(msg, is_integer=True, is_odd=False):
    """
    """
    user_input = input(msg)
    if (not user_input.isdecimal()) and is_integer and ("0" != user_input):
        print("[!] Received a non-integer")
        return None
    else:
        user_input = int(user_input)
        if 0 == user_input%2 and is_odd:
            print("[!] Received an even integer, it should be odd")
            return None

    if not is_integer:
        try:
            user_input = float(user_input)
        except ValueError:
            print("[!] Received invalid floating-point number")
            return None

    return user_input

def grayscale_command(image):
    """
    """
    # Checking if there is only a single channel, if so, it's a grayscale
    if list != type(image[0][0]):
        print("[!] Image is already grayscaled. Returning to Menu.")
        return image

    return RGB2grayscale(image)

def blur_command(image):
    """
    """
    pass

def resize_command(image):
    """
    """
    pass

def rotate_command(image):
    """
    """
    pass

def edges_command(image):
    """
    """
    pass

def quantize_command(image):
    """
    """
    pass

def show_image_command(image):
    """
    """
    show_image(image)
    return image

def execute_command(image):
    """
    """
    commands = {
        1: RGB2grayscale,
        2: blur_command,
        3: resize_command,
        4: rotate_command,
        5: edges_command,
        6: quantize_command,
        7: show_image_command,
        8: None
    }

    user_command = None
    while not (user_command in commands.keys()):
        print("Available commands:\n \
              1: Grayscaling\n \
              2: Blurring\n \
              3: Resizing\n \
              4: Rotating\n \
              5: Edged Image\n \
              6: Quantizing\n \
              7: Show Image\n \
              8: Quit Program")
        user_input = input("Choose a command (1-8): ")
        if user_input.isdecimal():
            user_command = int(user_input)    
            if not (user_command in commands.keys()):
                print("[!] Invalid command number - Only 1-8 available")
        else:
            print("[!] Invalid command - Only numbers 1-8 are available")
        
    if QUIT_COMMAND_VALUE == user_command:
        return None

    return commands[user_command](image)

def main():
    """
    """
    image_path = handle_command_line()
    current_image = load_image(image_path)

    while current_image is not None:
        current_image = execute_command(current_image)

if __name__ == '__main__':
    """
    """
    main()