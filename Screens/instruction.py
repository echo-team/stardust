import arcade
import os

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from Screens.GameScreen import GameScreen

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

class Instruction(GameScreen):

    def show(self):
        arcade.get_window().show_view(self)

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        pos_x = SCREEN_WIDTH / 5
        pos_y = SCREEN_HEIGHT / 2 + 60
        arcade.draw_text("Use mouse or arrows to move", pos_x, pos_y, arcade.color.WHITE, font_size=14)
        arcade.draw_text("Press mouse's button or space to shoot", pos_x, pos_y - 20, arcade.color.WHITE, font_size=14)
        arcade.draw_text("Press Esc to pause", pos_x, pos_y - 40, arcade.color.WHITE, font_size=14)
        arcade.draw_text("Press Enter to continue", pos_x, pos_y - 100, arcade.color.WHITE, font_size=14)

    def on_key_press(self, key, modifiers):
        super().show_menu_if_esc(key)

        if key == arcade.key.ENTER:
            self.window.screens['level1'].show()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        self.window.screens['level1'].show()
