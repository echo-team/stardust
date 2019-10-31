import arcade
import structure

from files.instruction import Instruction
from files.level_1_view import Lvl_1
from files.level_2_view import Lvl_2
from files.level_3_view import Lvl_3
from files.game_over_view import GameOverView
from files.victory_view import VictoryView

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
            'instruction': Instruction(),
            'level1': Lvl_1(),
            'level2': Lvl_2(),
            'level3': Lvl_3(),
            'gameover': GameOverView(),
            'victory': VictoryView()
        }

window = Window(SCREEN_WIDTH, SCREEN_HEIGHT)
window.total_score = 0
window.level = 1
window.screens['instruction'].show()
arcade.run()