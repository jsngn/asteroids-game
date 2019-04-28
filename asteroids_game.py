# Author: Mien Nguyen
# Date: 04/27/2019
# Purpose: Create a version of the popular Asteroids game
# Disclaimer: I did not write the cs1lib.py module used in this program. All graphics done by Seth Serrano.
# Note: cs1lib.py is NEEDED for this game to run. Find it at: https://www.cs.dartmouth.edu/~cs1/install-win/cs1lib.py

from cs1lib import *
from ship import Ship
from bullet import Bullet
from rocks import Rocks


# Makes background black
def draw_bg():
    set_clear_color(0, 0, 0)
    clear()


# Handles the bullets' movement
def move_bullets():
    i = 0
    while i < len(bullet_list):  # Loops through every bullet in list of bullets/bullets shot that haven't left window
        bullet_list[i].draw()  # Draws the bullet
        bullet_list[i].update_location()  # Updates the location of the bullet for the next frame to make bullet move up

        # Deletes bullets that have left the screen from the list of bullets
        if bullet_list[i].bullet_y < BULLETS_MAX_D:
            del bullet_list[i]
        else:
            i += 1


# Adds falling rocks to the window
def draw_rocks():
    global add_rock

    if len(rock_list) < ROCKS_MAX_N:  # Only adds rocks when number of existing rocks/in rocks list is less than 5

        c = 0
        while c < ROCKS_ADD_N:  # Adds 3 rocks

            add_rock = True  # Updates to False if the rock can't be added because of its position
            rock = Rocks()  # Creates an object of Rocks class which is the rock

            # Compares x coordinate of new rock to all rocks in list of rocks to ensure that the new rock is not added
            # if it's not far away enough from the other rocks in terms of x coordinate
            i = 0
            while i < len(rock_list):
                if rock_list[i].rock_x - ROCKS_INTER_DISTANCE <= rock.rock_x <= rock_list[i].rock_x \
                        + ROCKS_INTER_DISTANCE:
                    add_rock = False
                i += 1

            # Only adds new rock if its x coordinate is far enough away from other rocks
            if add_rock:
                rock_list.append(rock)
                c += 1


# Handles the rocks' movement
def move_rocks():
    global lives

    i = 0
    while i < len(rock_list):  # Loops through every rock in list of rocks
        rock_list[i].draw()  # Draws the rock
        rock_list[i].update_location()  # Updates the location of the rock to make rock move down

        # When rock has moved beyond the point where player can still shoot it down...
        if rock_list[i].rock_y > ROCKS_MAX_D:
            del rock_list[i]  # ... deletes rock from list
            lives -= LIVES_DECR  # ... decreases player's lives by 1
            check_lose()  # ... check if player has lost
        else:
            i += 1


# Handles the destruction of the rocks by bullets
def destroy_rocks():
    global score, delete_bullet

    # Loops through every bullet in the bullets list
    i = 0
    while i < len(bullet_list):
        j = 0
        delete_bullet = False  # Boolean updates to True if the bullet must be deleted
        while j < len(rock_list):  # Loops through every rock in rocks list
            # If bullet hits rock...
            if bullet_list[i].bullet_y < rock_list[j].rock_y + ROCKS_HITBOX_Y and \
                    rock_list[j].rock_x <= bullet_list[i].bullet_x <= rock_list[j].rock_x + ROCKS_HITBOX_X:
                del rock_list[j]  # ... deletes rock from rocks list
                score += SCORE_INCR  # ... increases player's score by 1
                delete_bullet = True  # ... updates this Boolean to True
            else:
                j += 1

        # Delete the bullet from bullets list if it's hit a rock
        if delete_bullet:
            del bullet_list[i]
        else:
            i += 1


# Handles key presses
def key_pressed(key):
    global ship_shooting, ship_move_left, ship_move_right, start_game

    # Sets the ship's movement to left if "a" pressed
    if key == "a":
        ship_move_left = True

    # Sets the ship's movement to right if "d" pressed
    if key == "d":
        ship_move_right = True

    # Sets ship's state to shooting if space bar pressed
    if key == " ":
        ship_shooting = True

    # Sets game's state to start if "s" pressed
    if key == "s":
        start_game = True


# Handles key releases
def key_released(key):
    global ship_shooting, ship_move_left, ship_move_right

    # Stops ship's movement from being set to left if "a" released
    if key == "a":
        ship_move_left = False
    # Stops ship's movement from being set to right if "d" released
    if key == "d":
        ship_move_right = False
    # Stops ship's state from being set to shooting if space bar released
    if key == " ":
        ship_shooting = False


# Checks whether player has lost the game
def check_lose():
    global lose_game, start_game, player_score

    # If lives equals zero
    if lives == MIN_LIVES:
        lose_game = True  # Sets game's state to lost
        start_game = False  # Sets game's state to not started
        player_score = score  # Stores the player's score


# Resets the game when game is lost
def reset_game():
    global score, lives

    score = INITIAL_SCORE  # Resets score to 0
    lives = MAX_LIVES  # Resets lives to 3

    ship.restore_ship_x()  # Resets ship's position to initial position

    # Deletes every rock in rocks list
    i = 0
    while i < len(rock_list):
        del rock_list[i]

    # Deletes every bullet in bullets list
    j = 0
    while j < len(bullet_list):
        del bullet_list[j]


# Displays graphical components and text where necessary, and calls the appropriate functions for game to function
def asteroids_game():

    draw_bg()  # Redraws black background every frame for animation to work

    set_stroke_color(0.98, 0.24, 0.95)  # Sets text color to pink
    set_font("Impact")
    draw_text("Score: " + str(score), 3, 20)  # Displays score in top left corner
    draw_text("Lives: " + str(lives), 3, 40)  # Displays lives below score

    ship.draw()

    if not start_game:
        if lose_game:  # If game's state is not started and player lost, displays the following message...
            draw_text("You lost! Press 's' to try again.", 90, 190)
            draw_text("Score: " + str(player_score), 165, 230)  # ... and player's score
            reset_game()  # ... and resets game
        else:  # If game's state is not started and player hasn't lost, displays instructions
            draw_text("Press 'a' 'd' to move left & right, space to shoot.", 20, 150)
            draw_text("Only 20 bullets can be on the screen at any time.", 15, 190)
            draw_text("Fire economically!", 125, 230)
            draw_text("Press 's' to start.", 135, 270)
    else:  # If game's state is started...
        # ... moves ship right if ship's state is set to moving right and ship hasn't hit right boundary
        if ship_move_right and ship.ship_x < SHIP_RIGHT_BOUNDARY:
            ship.move_right()

        # ... moves ship left if ship's state is set to moving left and ship hasn't hit left boundary
        if ship_move_left and ship.ship_x > SHIP_LEFT_BOUNDARY:
            ship.move_left()

        # ... shoots bullet from ship and adds bullet to bullets list if ship's state is shooting and there are less
        # than 20 bullets on window (ie only 20 bullets allowed on window at any one time)
        if ship_shooting and len(bullet_list) < BULLETS_MAX_N:
            bullet = Bullet(ship.ship_x + BULLETS_SHOOT_X, ship.ship_y)
            bullet_list.append(bullet)

        move_bullets()

        draw_rocks()
        move_rocks()
        destroy_rocks()


ship = Ship()  # Creates an object of class Ship

bullet_list = []  # Creates an empty list of bullets

rock_list = []  # Creates an empty list of rocks


INITIAL_SCORE = 0  # Stores the initial score
SCORE_INCR = 1  # Stores the increase in score each time player shoots a rock
MAX_LIVES = 3  # Stores the maximum lives the player has
MIN_LIVES = 0  # Stores the minimum lives the player has
LIVES_DECR = 1  # Stores the decrease in lives each time a rock isn't shot down

SHIP_RIGHT_BOUNDARY = 365  # Stores the x coordinate of the right boundary where ship can move to
SHIP_LEFT_BOUNDARY = -10  # Stores the x coordinate of the left boundary where ship can move to

BULLETS_MAX_N = 20  # Stores the maximum number of bullets on window at any one time
BULLETS_SHOOT_X = 20  # Stores distance between edge & center of ship image to ensure bullets shot from ship's center
BULLETS_MAX_D = 0  # Stores x coordinate of maximum boundary bullets can move to before they are deleted from list

ROCKS_MAX_N = 5  # Stores the maximum number of rocks to exist in game at any one time
ROCKS_ADD_N = 3  # Stores the number of rocks to be added when rocks can be added
ROCKS_INTER_DISTANCE = 15  # Stores the lower, non-inclusive limit for distance between the rocks
ROCKS_MAX_D = 335  # Stores x coordinate of maximum boundary rocks can move to before they can no longer be shot down
ROCKS_HITBOX_Y = 20  # Stores minimum distance from top edge of rock image which bullet must move to to destroy rock
ROCKS_HITBOX_X = 25  # Stores maximum distance from left edge of rock image which bullet must be within to destroy rock

lose_game = False  # Updates to True when player loses game
start_game = False  # Updates to True when player starts or restarts game

score = INITIAL_SCORE  # Keeps track of player's current score, initially set to 0
player_score = INITIAL_SCORE  # Stores the player's score after they've lost, initially set to 0
lives = MAX_LIVES  # Keeps track of player's lives, initially set to 3

ship_shooting = False  # Updates to True when space bar pressed
ship_move_left = False  # Updates to True when "a" pressed
ship_move_right = False  # Updates to True when "d" pressed

delete_bullet = False  # Updates to True when a bullet in the bullets list must be deleted

add_rock = True  # Updates to False when a new rock can't be added to rocks list

# Starts animating the game
start_graphics(asteroids_game, key_press=key_pressed, key_release=key_released)
