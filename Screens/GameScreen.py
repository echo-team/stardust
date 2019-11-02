import arcade

class GameScreen(arcade.View):

    def show_menu_if_esc(self, key, previousScreen):
        if key == arcade.key.ESCAPE:
            arcade.get_window().screens['menu'].show(previousScreen)