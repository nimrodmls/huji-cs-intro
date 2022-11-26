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

img = load_image(r"C:\users\nimrod\downloads\test2.jpg")
#show_image(img)
#show_image(combine_channels(separate_channels(img)))

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

#show_image(RGB2grayscale(img))

def blur_kernel(size: int) -> Kernel:
    """
    """
    return [[1/(size**2) for pixel in range(size)] for row in range(size)]

print(blur_kernel(3))

def apply_kernel_to_matrix(matrix, kernel):
    """
    same size
    """
    matrix_sum = 0
    for row in zip(matrix, kernel):
        for pixel, kernel_cell in zip(*row):
            matrix_sum += (pixel * kernel_cell)
    return matrix_sum

print(apply_kernel_to_matrix([[1,2,0], [2,2,0], [1,2,1]], [[0,0,0], [1,-1,0], [1,1,-1]]))

def is_padding_needed(image, size, row_index, pixel_index):
    """
    """
    horizontal_index = None
    if 0 > (pixel_index - size):
        horizontal_index = 0

    elif (len(image[row_index])-1) < (pixel_index + size):
        horizontal_index = pixel_index

    vertical_index = None
    if 0 > row_index-size:
        pass
    elif len(image)-1 == row_index:
        pass

    return horizontal_index, vertical_index

def get_padded_image(image, value, size):
    """
    """
    padded_image = list(image)
    for row_pads in range(size):
        row_pad = [value for row_len in range(len(image[0]))]
        padded_image.insert(0, row_pad) # Insert "above"
        padded_image.append(row_pad) # Insert "below"
    
    for row_index in range(len(image)):
        for column_pads in range(size):
            padded_image[row_index].insert(0, value) # Insert "left"
            padded_image[row_index].append(value) # Insert "right"

    return padded_image

print(get_padded_image(test_rgb_image, 5, 1))

def apply_kernel(image: SingleChannelImage, kernel: Kernel) -> SingleChannelImage:
    """
    """
    padded_image = list(image)
    for row_index in range(len(image)):

        padded_image

        for pixel_index in range(len(image[row_index])):

            current_pixel = image[row_index][pixel_index]

            horizontal_index, vertical_index = is_padding_needed(image, round(len(kernel)/2)-1, row_index, pixel_index)

            if None != horizontal_index:
                for times in range(abs(pixel_index-len(kernel))):
                    padded_image[row_index].insert(0, current_pixel)




            cell = image[row_index][column_index]

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
