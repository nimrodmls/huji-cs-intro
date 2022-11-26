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

def apply_kernel(image: SingleChannelImage, kernel: Kernel) -> SingleChannelImage:
    """
    """
    


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
