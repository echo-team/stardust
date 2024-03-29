import arcade
import structure

from constants import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE

from Screens.instruction import Instruction
from Screens.level_1_view import Lvl_1
from Screens.level_2_view import Lvl_2
from Screens.level_3_view import Lvl_3
from Screens.MenuScreen import MenuScreen

# TODO: remove for Linux
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

class Window(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.screens = {
            'instruction': Instruction(),
            'level1': Lvl_1(),
            'level2': Lvl_2(),
            'level3': Lvl_3(),
            'menu': MenuScreen(self)
        }

window = Window(SCREEN_WIDTH, SCREEN_HEIGHT)
window.total_score = 0
window.level = 1
window.screens['menu'].show(None)
arcade.run()
