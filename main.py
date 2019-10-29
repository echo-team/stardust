import arcade
from files.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE
from files.instruction import Instruction


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu_view = Instruction()
    window.total_score = 0
    window.level = 1
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()