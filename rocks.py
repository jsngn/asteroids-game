# Author: Mien Nguyen
# Date: 04/27/2019
# Purpose: Create a Rocks class for a version of the popular Asteroids game

from cs1lib import *
from random import randint

ROCKS_MAX_X = 380  # Stores the maximum x coordinate where rocks are created
ROCKS_MIN_X = 20  # Stores the minimum x coordinate where rocks are created
ROCKS_MAX_Y = 0  # Stores the maximum y coordinate where rocks are created
ROCKS_MIN_Y = -200  # Stores the minimum y coordinate where rocks are created
ROCKS_VELOC = 2  # Stores the rock's velocity (y component only)


class Rocks:
    def __init__(self):
        # Randomly picks the coordinates where the rocks are created
        self.rock_x = randint(ROCKS_MIN_X, ROCKS_MAX_X)
        self.rock_y = randint(ROCKS_MIN_Y, ROCKS_MAX_Y)

        self.rock_vy = ROCKS_VELOC

        # Picks which rock image the rock has randomly
        self.rock_type = randint(1, 5)
        if self.rock_type == 1:
            self.rock_body = load_image("Rock_1.png")
        elif self.rock_type == 2:
            self.rock_body = load_image("Rock_2.png")
        elif self.rock_type == 3:
            self.rock_body = load_image("Rock_3.png")
        elif self.rock_type == 4:
            self.rock_body = load_image("Rock_4.png")
        else:
            self.rock_body = load_image("Rock_5.png")

    # Moves rock downward by its velocity value each time
    def update_location(self):
        self.rock_y += self.rock_vy

    # Draws rock at the right coordinates each frame
    def draw(self):
        draw_image(self.rock_body, self.rock_x, self.rock_y)
