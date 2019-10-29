import arcade
import random
import os
from files.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SPRITE_SCALING_COIN, SPRITE_SCALING_PLAYER, MOVEMENT_SPEED
from files.coin import Coin
from files.level_2_view import Lvl_2

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

class Lvl_1(arcade.View):

    def __init__(self):
        super().__init__()

        self.time_taken = 0
        self.frame_count = 0

        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player info
        self.player_sprite = arcade.Sprite("sprites/tyan.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0
        self.player_list.append(self.player_sprite)
        self.score = 0
        self.level = 1

        # Create the coins
        for i in range(20):
            # Create the coin instance
            coin = Coin("sprites/hooi_dlya_tyan.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            coin.change_x = random.randrange(-3, 4)
            coin.change_y = random.randrange(-3, 4)

            # Add the coin to the lists
            self.coin_list.append(coin)


    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK_OLIVE)
        # Don't show the mouse cursor
        self.window.set_mouse_visible(False)

    def on_draw(self):
        arcade.start_render()

        self.coin_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 10, arcade.color.WHITE, 14)
        output = f"Level: {self.level}"
        arcade.draw_text(output, 10, 25, arcade.color.WHITE, 14)

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

        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the
        # score.
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1

        if len(self.coin_list) == 0 and self.level == 1:
            self.level += 1
            lvl2 = Lvl_2(self.score)
            self.window.show_view(lvl2)

