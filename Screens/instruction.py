import arcade
import os

from PIL import ImageFont
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from Screens.GameScreen import GameScreen

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

class Instruction(GameScreen):

    def __init__(self):
        super().__init__()

        font = ImageFont.truetype('../assets/fonts/source_code_pro.ttf', 15)
        text_width, text_height = font.getsize('Press mouse\'s button or space to shoot')

        self.text = [
            'Use mouse or arrows to move',
            'Press mouse\'s button or space to shoot',
            'Press Esc to pause',
            'Press Enter to continue'
        ]
        self.text_pos = {
            'x': (SCREEN_WIDTH - text_width) / 2,
            'y': (SCREEN_HEIGHT - (text_height + 5) * len(self.text)) / 2,
            'delta': 20
        }

    def show(self):
        arcade.get_window().show_view(self)

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        for index in range(len(self.text)):
            arcade.draw_text(
                self.text[index],
                self.text_pos['x'], SCREEN_HEIGHT - self.text_pos['y'] - index * self.text_pos['delta'],
                arcade.color.WHITE, font_size=15, font_name='../assets/fonts/source_code_pro.ttf')

    def on_key_press(self, key, modifiers):
        super().show_menu_if_esc(key, self)

        if key == arcade.key.ENTER:
            self.window.screens['level1'].show()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        self.window.screens['level1'].show()
