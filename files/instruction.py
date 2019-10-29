import arcade
import os
from files.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from files.level_1_view import Lvl_1

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

class Instruction(arcade.View):

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

    def on_key_press(self, key, modifiers: int):
        lvl1 = Lvl_1()
        if key == arcade.key.ENTER:
            self.window.show_view(lvl1)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = Lvl_1()
        self.window.show_view(game_view)
