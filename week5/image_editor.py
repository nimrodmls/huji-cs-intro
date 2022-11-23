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
#                                  Functions                                 #
##############################################################################

RED_CHANNEL_INDEX = 0
BLUE_CHANNEL_INDEX = 1
GREEN_CHANNEL_INDEX = 2

test_rgb_image = [[[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                  [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                  [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                  [[1, 2, 3], [1, 2, 3], [1, 2, 3]]]

def separate_channels(image: ColoredImage) -> List[SingleChannelImage]:
    """
    """
    channel_list = [[], [], []]
    for row in image:
        red_row = []
        blue_row = []
        green_row = []
        
        for pixel in row:
            red_row.append(pixel[RED_CHANNEL_INDEX])
            blue_row.append(pixel[BLUE_CHANNEL_INDEX])
            green_row.append(pixel[GREEN_CHANNEL_INDEX])

        channel_list[RED_CHANNEL_INDEX].append(red_row)
        channel_list[BLUE_CHANNEL_INDEX].append(blue_row)
        channel_list[GREEN_CHANNEL_INDEX].append(green_row)

    return channel_list

def combine_channels(channels: List[SingleChannelImage]) -> ColoredImage:
    """
    """
    image = []
    for row in \
        zip(channels[RED_CHANNEL_INDEX], 
            channels[BLUE_CHANNEL_INDEX], 
            channels[GREEN_CHANNEL_INDEX]):
        current_row = []
        for pixel in zip(*row):
            current_row.append(list(pixel))
        image.append(current_row)

    return image

print(combine_channels(separate_channels(test_rgb_image)))

def RGB2grayscale(colored_image: ColoredImage) -> SingleChannelImage:
    pass


def blur_kernel(size: int) -> Kernel:
    pass


def apply_kernel(image: SingleChannelImage, kernel: Kernel) -> SingleChannelImage:
    pass


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
