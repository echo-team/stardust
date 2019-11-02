import arcade
import random
import os
import math
import time
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, SPRITE_SCALING_COIN, SPRITE_SCALING_PLAYER, MOVEMENT_SPEED
from Coin_Folder.coin import Coin
from Coin_Folder.bonus_coin import Bonus_Coin

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)


class Lvl_2(arcade.View):

    def __init__(self):
        super().__init__()

        self.time_taken = 0
        self.frame_count = 0

        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bonus_coin_list = arcade.SpriteList()

        # Set up the player info
        self.player_sprite = arcade.Sprite("../assets/images/tyan.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0
        self.player_list.append(self.player_sprite)
        self.score = 0
        self.level = 2
        self.hp = 3
        self.time = time.time()
        self.time2 = 0

        # Create the coins
        for i in range(25):
            # Create the coin instance
            coin = Coin("../assets/images/hooi_dlya_tyan.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            coin.change_x = random.randrange(-3, 4)
            coin.change_y = random.randrange(-3, 4)

            # Add the coin to the lists
            self.coin_list.append(coin)

        for i in range(4):
            # Create the coin instance
            bonus_coin = Bonus_Coin("../assets/images/bonus_hooi.png", SPRITE_SCALING_COIN)

            # Position the center of the circle the coin will orbit
            bonus_coin.circle_center_x = random.randrange(SCREEN_WIDTH)
            bonus_coin.circle_center_y = random.randrange(SCREEN_HEIGHT)

            # Random radius from 10 to 200
            bonus_coin.circle_radius = random.randrange(10, 200)

            # Random start angle from 0 to 2pi
            bonus_coin.circle_angle = random.random() * 2 * math.pi

            self.bonus_coin_list.append(bonus_coin)

    def show(self, score):
        self.score = score
        arcade.get_window().show_view(self)
        
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK_OLIVE)
        # Don't show the mouse cursor
        self.window.set_mouse_visible(False)

    def on_draw(self):
        arcade.start_render()

        self.coin_list.draw()
        self.player_list.draw()
        self.bonus_coin_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 10, arcade.color.WHITE, 14)
        output = f"Level: {self.level}"
        arcade.draw_text(output, 10, 25, arcade.color.WHITE, 14)
        output = f"HP: {self.hp}"
        arcade.draw_text(output, 10, 40, arcade.color.WHITE, 14)
        output = f"Time left: {10 - self.time2}"
        arcade.draw_text(output, 10, 55, arcade.color.WHITE, 14)


    def on_mouse_motion(self, x, y, dx, dy):

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_key_press(self, key, modifiers):
        # Called whenever the user presses a key.
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        # Called whenever a user releases a key.
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0

    def on_update(self, delta_time: float):
        self.time_taken += delta_time

        self.time2 = int(time.time() - self.time)

        # Move the player
        self.player_sprite.center_y += self.player_sprite.change_y
        self.player_sprite.center_x += self.player_sprite.change_x

        # See if the player hit the edge of the screen. If so, change direction
        if self.player_sprite.center_x < 55:
            self.player_sprite.center_x = 55

        if self.player_sprite.center_x > SCREEN_WIDTH - 55:
            self.player_sprite.center_x = SCREEN_WIDTH - 55

        if self.player_sprite.center_y < 55:
            self.player_sprite.center_y = 55

        if self.player_sprite.center_y > SCREEN_HEIGHT - 55:
            self.player_sprite.center_y = SCREEN_HEIGHT - 55

        self.coin_list.update()
        self.player_list.update()
        self.bonus_coin_list.update()

        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the
        # score.
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1

        bonus_coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bonus_coin_list)

        for bonus_coin in bonus_coin_hit_list:
            bonus_coin.remove_from_sprite_lists()
            self.hp += 1

        if self.time2 == 10:
            self.window.screens['level3'].show(self.score)