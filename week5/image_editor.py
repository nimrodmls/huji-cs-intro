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
BLUE_GRAYSCALE_VALUE = 0.144

##############################################################################
#                                  Functions                                 #
##############################################################################


test_rgb_image = [[[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                  [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                  [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                  [[1, 2, 3], [1, 2, 3], [1, 2, 3]]]

img = load_image(r"C:\users\nimrod\downloads\images.jpg")

def separate_channels(image: ColoredImage) -> List[SingleChannelImage]:
    """
    """
    channel_list = [[], [], []]
    for row in image:
        red_row, green_row, blue_row = zip(*row)
        channel_list[RED_CHANNEL_INDEX].append(list(red_row))
        channel_list[GREEN_CHANNEL_INDEX].append(list(green_row))
        channel_list[BLUE_CHANNEL_INDEX].append(list(blue_row))

    return channel_list

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
    return (rgb_pixel[RED_CHANNEL_INDEX] * RED_GRAYSCALE_VALUE) + \
           (rgb_pixel[GREEN_CHANNEL_INDEX] * GREEN_GRAYSCALE_VALUE) + \
           (rgb_pixel[BLUE_CHANNEL_INDEX] * BLUE_GRAYSCALE_VALUE)

def RGB2grayscale(colored_image: ColoredImage) -> SingleChannelImage:
    """
    """
    return [[round(calc_grayscale_sum(pixel)) for pixel in row] for row in colored_image]

def blur_kernel(size: int) -> Kernel:
    """
    """
    return [[1/(size**2) for pixel in range(size)] for row in range(size)]

def apply_kernel_to_matrix(matrix, kernel):
    """
    same size
    """
    matrix_sum = 0
    kernel_center = round(len(matrix)/2)-1

    for row in zip(matrix, kernel):
        for pixel, kernel_cell in zip(*row):
            matrix_sum += (matrix[kernel_center][kernel_center] if pixel is None else pixel) * kernel_cell

    return matrix_sum

def get_padded_image(image, size):
    """
    """
    padded_image = copy.deepcopy(image)
    
    for row_index in range(len(image)):
        for column_pads in range(size):
            padded_image[row_index].insert(0, None) # Insert "left"
            padded_image[row_index].append(None) # Insert "right"

    for row_pads in range(size):
        row_pad = [None for row_len in range(len(image[0]) + size+1)]
        padded_image.insert(0, row_pad) # Insert "above"
        padded_image.append(row_pad) # Insert "below"

    return padded_image

def apply_kernel(image: SingleChannelImage, kernel: Kernel) -> SingleChannelImage:
    """
    """
    kernel_center = round(len(kernel)/2)
    padded_image = get_padded_image(image, kernel_center-1)
    
    manipulated_image = []
    for row_index in range(kernel_center, len(padded_image)):
        image_row = []

        for column_index in range(kernel_center, len(padded_image[row_index])):
            current_matrix = []

            for current_row in padded_image[row_index-kernel_center:row_index+kernel_center-1]:
                current_matrix.append(current_row[column_index-kernel_center:column_index+kernel_center-1])

            image_row.append(round(apply_kernel_to_matrix(current_matrix, kernel)))

        manipulated_image.append(image_row)

    return manipulated_image

nimg = combine_channels([apply_kernel(separate_channels(img)[0], blur_kernel(3)),
apply_kernel(separate_channels(img)[1], blur_kernel(3)),
apply_kernel(separate_channels(img)[2], blur_kernel(3))])
show_image(nimg)

def bilinear_interpolation(image: SingleChannelImage, y: float, x: float) -> int:
    pass


def resize(image: SingleChannelImage, new_height: int, new_width: int) -> SingleChannelImage:
    pass


def rotate_90(image: Image, direction: str) -> Image:
    pass


def get_edges(image: SingleChannelImage, blur_size: int, block_size: int, c: float) -> SingleChannelImage:
    pass


def quantize(image: SingleChannelImage, N: int) -> SingleChannelImage:
    pass


def quantize_colored_image(image: ColoredImage, N: int) -> ColoredImage:
    pass


if __name__ == '__main__':
    pass
