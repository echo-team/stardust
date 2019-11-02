import arcade

from PIL import ImageFont
from Widgets.Menu import Menu
from Widgets.Highlight import Highlight


class MenuScreen(arcade.View):

    def __init__(self, window):
        font = ImageFont.truetype('../assets/fonts/source_code_pro.ttf', 15)
        itemWidth, itemHeight = font.getsize('Hight scores')
        itemHeight += 10

        font = ImageFont.truetype('../assets/fonts/lemon_milk.otf', 40)
        itemWidth, tmpHeight = font.getsize('STARUST')
        titleWidth, titleHeight = font.getsize('STAR')

        self.window = window
        windowWidth, windowHeight = window.get_size()

        self.titleFontSize = 40
        self.title = { 'x': (windowWidth - itemWidth) / 2, 'y': windowHeight - (windowHeight - titleHeight - itemHeight * 5) / 2 }
        self.titleText = 'STAR'
        self.subtitle = { 'x': self.title['x'] + titleWidth, 'y': self.title['y'] - titleHeight }
        self.subtitleText = 'DUST'

        self.focused = 0
        self.highlight = Highlight()

        self.items = [
            { 'name': 'Start', 'listener': self.start },
            { 'name': 'Continue', 'listener': self.resume },
            { 'name': 'High scores' },
            { 'name': 'Settings' },
            { 'name': 'Exit' }
        ]

        self.menu = Menu(self.title['x'], self.title['y'] - itemHeight - 20, itemWidth, itemHeight)
        for item in self.items:
            self.menu.addItem(item['name'])
        self.highlight.move(self.menu.items[0])

        self.previousScreen = None
    
    def resume(self):
        if self.previousScreen != None:
            self.window.show_view(self.previousScreen)
    
    def start(self):
        self.window.screens['instruction'].show()
    
    def show(self, previousScreen, victory = None):
        self.previousScreen = previousScreen
        self.window.show_view(self)

        if victory == None:
            self.titleText = 'STAR'
            self.subtitleText = 'DUST'
        elif victory:
            self.titleText = 'YOU'
            self.subtitleText = 'WIN'
        else:
            self.titleText = 'GAME'
            self.subtitleText = 'OVER'

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(
            self.titleText, self.title['x'], self.title['y'],
            arcade.color.WHITE, self.titleFontSize, font_name="../assets/fonts/lemon_milk.otf")
        arcade.draw_text(
            self.subtitleText, self.subtitle['x'], self.subtitle['y'],
            arcade.color.WHITE, self.titleFontSize, font_name="../assets/fonts/lemon_milk.otf")

        self.menu.draw()
        self.highlight.draw()
    
    def on_key_press(self, key, modifier):
        if key == arcade.key.UP:
            self.focused = (self.focused - 1) % len(self.items)
            self.highlight.move(self.menu.items[self.focused])
        elif key == arcade.key.DOWN:
            self.focused = (self.focused + 1) % len(self.items)
            self.highlight.move(self.menu.items[self.focused])
        elif key == arcade.key.ENTER:
            self.items[self.focused]['listener']()

    def on_mouse_motion(self, x, y, dx, dy):
        covered = self.highlight.mouseMove(x, y, self.menu.items)
        if covered != None:
            self.focused = covered[0]