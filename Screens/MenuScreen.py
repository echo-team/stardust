from PIL import ImageFont
from Menu import Menu


class MenuScreen:

    def __init__(self, window):
        font = ImageFont.truetype('arial.ttf', 15)
        itemWidth, itemHeight = font.getsize('Hight scores')
        itemHeight += 10

        self.window = window
        windowWidth, windowHeight = window.get_size()

        self.menu = Menu((windowWidth - itemWidth) / 2, (windowHeight - itemHeight * 5) / 2, itemWidth, itemHeight);
        self.menu.addItem('Start')
        self.menu.addItem('Continue')
        self.menu.addItem('Hight scores')
        self.menu.addItem('Settings')
        self.menu.addItem('Exit')

    def draw(self):
        self.menu.draw()
