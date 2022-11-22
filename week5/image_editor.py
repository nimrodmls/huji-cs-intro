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

def get_channel(image):
    """
    """
    for row 

def separate_channels(image: ColoredImage) -> List[SingleChannelImage]:
    """
    """
    red_channel = []
    blue_channel = []
    green_channel = []
    for row in image:
        for pixel in row:
            red_channel

    return [[[] for pixel in row] for row in image]
            

def combine_channels(channels: List[SingleChannelImage]) -> ColoredImage:
    pass


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
    ...pass


def quantize(image: SingleChannelImage, N: int) -> SingleChannelImage:
    pass


def quantize_colored_image(image: ColoredImage, N: int) -> ColoredImage:
    pass


if __name__ == '__main__':
    pass
