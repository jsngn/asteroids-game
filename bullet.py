# Author: Mien Nguyen
# Date: 04/27/2019
# Purpose: Create a Bullet class for a version of the popular Asteroids game

from cs1lib import *

BULLETS_VELOC = 5  # Stores the bullets' velocity (y component only)

class Bullet:
    def __init__(self, bullet_x, bullet_y):
        # Instance variables for the coordinates take the value passed to parameters
        self.bullet_x = bullet_x
        self.bullet_y = bullet_y

        self.bullet_vy = BULLETS_VELOC

        self.bullet_body = load_image("Bullet.png")

    # Moves the bullet upward
    def update_location(self):
        self.bullet_y -= self.bullet_vy

    # Draws the bullet at the right coordinates each frame
    def draw(self):
        draw_image(self.bullet_body, self.bullet_x, self.bullet_y)
