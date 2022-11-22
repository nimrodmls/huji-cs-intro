#################################################################
# FILE : image_editor.py
# WRITER : your_name , your_login , your_id
# EXERCISE : intro2cs ex5 2022-2023
# DESCRIPTION: A simple program that...
# STUDENTS I DISCUSSED THE EXERCISE WITH: Bugs Bunny, b_bunny.
#								 	      Daffy Duck, duck_daffy.
# WEB PAGES I USED: www.looneytunes.com/lola_bunny
# NOTES: ...
#################################################################

##############################################################################
#                                   Imports                                  #
##############################################################################
from ex5_helper import *
from typing import Optional

##############################################################################
#                                  Functions                                 #
##############################################################################


def separate_channels(image: ColoredImage) -> List[SingleChannelImage]:
    ...


def combine_channels(channels: List[SingleChannelImage]) -> ColoredImage:
    ...


def RGB2grayscale(colored_image: ColoredImage) -> SingleChannelImage:
    ...


def blur_kernel(size: int) -> Kernel:
    ...


def apply_kernel(image: SingleChannelImage, kernel: Kernel) -> SingleChannelImage:
    ...


def bilinear_interpolation(image: SingleChannelImage, y: float, x: float) -> int:
    ...


def resize(image: SingleChannelImage, new_height: int, new_width: int) -> SingleChannelImage:
    ...


def rotate_90(image: Image, direction: str) -> Image:
    ...


def get_edges(image: SingleChannelImage, blur_size: int, block_size: int, c: float) -> SingleChannelImage:
    ...


def quantize(image: SingleChannelImage, N: int) -> SingleChannelImage:
    ...


def quantize_colored_image(image: ColoredImage, N: int) -> ColoredImage:
    ...


if __name__ == '__main__':
    ...
