import arcade
import os
#from files.instruction import Instruction


file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

class VictoryView(arcade.View):

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Congrats", 240, 400, arcade.color.WHITE, 54)
        arcade.draw_text("Click to return to menu", 310, 300, arcade.color.WHITE, 24)

    def on_key_press(self, key, modifiers: int):
        instr = Instruction()
        if key == arcade.key.ENTER:
            self.window.show_view(instr)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        instr = Instruction()
        self.window.show_view(instr)