import arcade
import structure

from MenuScreen import MenuScreen

# TODO: remove for Linux
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Window(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.screens = {
            'menu': MenuScreen(self)
        }
        self.screens['current'] = self.screens['menu']

    def on_draw(self):
        arcade.start_render()
        self.screens['current'].draw()
        arcade.finish_render()
    
    def on_key_press(self, key, modifiers):
        self.screens['current'].keypress(key, modifiers)
    
    def on_mouse_motion(self, x, y, dx, dy):
        self.screens['current'].mousemove(x, y, dx, dy)

window = Window(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()

