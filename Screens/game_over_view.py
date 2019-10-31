import arcade
import os
#from files.instruction import Instruction

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

class GameOverView(arcade.View):

    def show(self):
        arcade.get_window().show_view(self)

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Game Over", 240, 400, arcade.color.WHITE, 54)
        arcade.draw_text("Click to restart", 310, 300, arcade.color.WHITE, 24)

    def on_key_press(self, key, modifiers: int):
        if key == arcade.key.ENTER:
            self.window.screens['instruction'].show()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        self.window.screens['instruction'].show()