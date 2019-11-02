import arcade

from PIL import ImageFont
from Widgets.Menu import Menu
from Widgets.Highlight import Highlight


class MenuScreen(arcade.View):

    def __init__(self, window):
        font = ImageFont.truetype('arial.ttf', 15)
        itemWidth, itemHeight = font.getsize('Hight scores')
        itemHeight += 10

        self.focused = 0
        self.highlight = Highlight()

        self.window = window
        windowWidth, windowHeight = window.get_size()

        self.items = ['Start', 'Continue', 'High scores', 'Settings', 'Exit']
        self.menu = Menu((windowWidth - itemWidth) / 2, (windowHeight - itemHeight * 5) / 2, itemWidth, itemHeight)
        for item in self.items:
            self.menu.addItem(item)
        
        self.highlight.move(self.menu.items[0])
    
    def show(self):
        self.window.show_view(self)

    def on_draw(self):
        arcade.start_render()
        self.menu.draw()
        self.highlight.draw()
    
    def on_key_press(self, key, modifier):
        if key == arcade.key.UP:
            self.focused = (self.focused - 1) % len(self.items)
            self.highlight.move(self.menu.items[self.focused])
        elif key == arcade.key.DOWN:
            self.focused = (self.focused + 1) % len(self.items)
            self.highlight.move(self.menu.items[self.focused])

    def on_mouse_motion(self, x, y, dx, dy):
        covered = self.highlight.mouseMove(x, y, self.menu.items)
        if covered != None:
            self.focused = covered[0]