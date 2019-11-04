import arcade
import os
import math

from constants import SCREEN_WIDTH, SCREEN_TITLE, SCREEN_HEIGHT, SPRITE_SCALING_PLAYER, SPRITE_SCALING_LASER_BOSS, \
    SPRITE_SCALING_BOSS, SPRITE_SCALING_COIN, SPRITE_SCALING_LASER, MOVEMENT_SPEED, \
    BULLET_SPEED, BOSS_BULLET_SPEED
from Screens.GameScreen import GameScreen

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

class Lvl_3(GameScreen):

    def __init__(self):
        super().__init__()
    
    def init(self, bullet_amount, hp):
        self.time_taken = 0
        self.frame_count = 0

        self.player_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.boss_list = arcade.SpriteList()
        self.bullet_boss_list = arcade.SpriteList()

        # Set up the player info
        self.player_sprite = arcade.Sprite("../assets/images/rocket.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0
        self.player_list.append(self.player_sprite)
        self.bullet_amount = bullet_amount
        self.boss_hp = 20
        self.hp = hp
        self.level = 3

        # Create the boss
        boss = arcade.Sprite("../assets/images/ufo.png", SPRITE_SCALING_BOSS)
        boss.center_x = SCREEN_WIDTH / 2
        boss.center_y = SCREEN_HEIGHT - boss.height / 4
        self.boss_list.append(boss)
    
    def show(self, bullet_amount, hp):
        self.init(bullet_amount, hp)
        arcade.get_window().show_view(self)

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

        # Don't show the mouse cursor
        self.window.set_mouse_visible(False)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.player_list.draw()
        self.bullet_list.draw()
        self.boss_list.draw()
        self.bullet_boss_list.draw()

        # Put the text on the screen.
        output = f"Bullets: {self.bullet_amount}"
        arcade.draw_text(output, 10, 10, arcade.color.WHITE, 14, font_name='../assets/fonts/source_code_pro.ttf')
        output = f"Level: {self.level}"
        arcade.draw_text(output, 10, 25, arcade.color.WHITE, 14, font_name='../assets/fonts/source_code_pro.ttf')
        output = f"HP: {self.hp}"
        arcade.draw_text(output, 10, 40, arcade.color.WHITE, 14, font_name='../assets/fonts/source_code_pro.ttf')
        output = f"Boss's hp: {self.boss_hp}"
        arcade.draw_text(output, 10, 55, arcade.color.WHITE, 14, font_name='../assets/fonts/source_code_pro.ttf')

    def on_mouse_motion(self, x, y, dx, dy):

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_mouse_press(self, x, y, button, modifiers):

        bullet = arcade.Sprite("../assets/images/bullet.png", SPRITE_SCALING_LASER)
        bullet.center_x = self.player_sprite.center_x
        bullet.center_y = self.player_sprite.center_y
        bullet.change_y = BULLET_SPEED
        self.bullet_amount -= 1
        self.bullet_list.append(bullet)

    def on_key_press(self, key, modifiers):
        super().show_menu_if_esc(key, self)

        # Called whenever the user presses a key.
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.SPACE and self.level == 3:
            bullet = arcade.Sprite("../assets/images/boss_bullet.png", SPRITE_SCALING_LASER)
            bullet.center_x = self.player_sprite.center_x
            bullet.center_y = self.player_sprite.center_y + 30
            bullet.change_y = BULLET_SPEED
            self.bullet_amount -= 1
            self.bullet_list.append(bullet)

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

        self.player_list.update()

        self.frame_count += 1

        # Loop through each enemy that we have
        for boss in self.boss_list:

            # First, calculate the angle to the player. We could do this
            # only when the bullet fires, but in this case we will rotate
            # the enemy to face the player each frame, so we'll do this
            # each frame.

            # Position the start at the enemy's current location
            start_x = boss.center_x
            start_y = boss.center_y

            # Get the destination location for the bullet
            dest_x = self.player_sprite.center_x
            dest_y = self.player_sprite.center_y

            # Do math to calculate how to get the bullet to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the bullet will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Set the enemy to face the player.
            boss.angle = math.degrees(angle) + 90

            # Shoot every 60 frames change of shooting each frame
            if self.frame_count % 60 == 0:
                bullet_boss = arcade.Sprite("../assets/images/boss_bullet.png", SPRITE_SCALING_LASER_BOSS)
                bullet_boss.center_x = start_x
                bullet_boss.center_y = start_y

                # Angle the bullet sprite
                bullet_boss.angle = math.degrees(angle) + 90

                # Taking into account the angle, calculate our change_x
                # and change_y. Velocity is how fast the bullet travels.
                bullet_boss.change_x = math.cos(angle) * BOSS_BULLET_SPEED
                bullet_boss.change_y = math.sin(angle) * BOSS_BULLET_SPEED

                self.bullet_boss_list.append(bullet_boss)

        # Get rid of the bullet when it flies off-screen

        bullet_boss_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bullet_boss_list)
        for bullet_boss in bullet_boss_hit_list:
            self.hp -=1
            bullet_boss.remove_from_sprite_lists()

        self.bullet_boss_list.update()

        bullet_player_hit_list = arcade.check_for_collision_with_list(boss, self.bullet_list)

        for bullet in bullet_player_hit_list:
            self.boss_hp -= 1
            bullet.remove_from_sprite_lists()

        self.bullet_list.update()
        
        if self.hp == 0 or self.bullet_amount == 0:
            self.window.screens['menu'].show(None, victory = False)

        if self.boss_hp == 0:
            self.window.screens['menu'].show(None, victory = True, score = self.hp)
        