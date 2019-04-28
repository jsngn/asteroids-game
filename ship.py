# Author: Mien Nguyen
# Date: 04/27/2019
# Purpose: Create a Ship class for a version of the popular Asteroids game

from cs1lib import *

SHIP_INITIAL_X = 175  # Stores ship's initial x coordinate
SHIP_INITIAL_Y = 357  # Store's ship's initial y coordinate
SHIP_VELOC_X = 5  # Stores the x component of ship's velocity
SHIP_VELOC_Y = 5  # Stores the y component of ship's velocity


class Ship:
    def __init__(self):
        # Assigns ship's initial x and y coordinates to the appropriate instance variables
        self.ship_x = SHIP_INITIAL_X
        self.ship_y = SHIP_INITIAL_Y

        # Assigns ship's x and y velocity components to the appropriate instance variables
        self.ship_vx = SHIP_VELOC_X
        self.ship_vy = SHIP_VELOC_Y

        self.ship_body = load_image("Player.png")

    # Moves ship left by updating x coordinate
    def move_left(self):
        self.ship_x -= self.ship_vx

    # Moves ship right by updating x coordinate
    def move_right(self):
        self.ship_x += self.ship_vx

    # Restores ship's initial position
    def restore_ship_x(self):
        self.ship_x = SHIP_INITIAL_X

    # Draws ship at the right coordinates each frame
    def draw(self):
        draw_image(self.ship_body, self.ship_x, self.ship_y)
