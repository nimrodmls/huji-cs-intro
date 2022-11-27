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

img = load_image(r"C:\users\nimro\downloads\temp2.jpg")

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
            if 1 == kernel_length:
                kernel_length = 3

            for current_row in padded_image[row_index:row_index+kernel_length]:
                current_matrix.append(current_row[column_index:column_index+kernel_length])

            image_row.append(round(apply_kernel_to_matrix(current_matrix, kernel)))

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

#gray_img = RGB2grayscale(img)
#show_image(gray_img)
#new_img = resize(gray_img, 500, 500)
#show_image(new_img)

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
    threshold = []
    blurred_image = apply_kernel(image, blur_kernel(blur_size))
    for row_index in range(len(blurred_image)):
        for pixel_index in range(len(blurred_image[row_index])):
            r = block_size // 2
            current_sum = blurred_image[row_index-r:row_index+r+1][pixel_index-r:pixel_index+r+1]
            threshold[row_index][pixel_index] = (current_sum/9) - c
    return threshold

def quantize(image: SingleChannelImage, N: int) -> SingleChannelImage:
    pass


def quantize_colored_image(image: ColoredImage, N: int) -> ColoredImage:
    pass


if __name__ == '__main__':
    pass
