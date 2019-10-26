import arcade

class MenuItem:

    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.fontSize = 15
        self.fontWeight = 0
    
    def draw(self):
        arcade.draw_text(
            self.text, self.x, self.y + (self.height - self.fontSize) / 2,
            arcade.color.WHITE,
            self.fontSize, self.fontWeight, 'left', 'arial')

class Menu:

    def __init__(self, x, y, itemWidth, itemHeight):
        self.x = x
        self.y = arcade.get_window().get_size()[1] - y
        self.itemWidth = itemWidth
        self.itemHeight = itemHeight
        self.items = []
    
    def addItem(self, text):
        item = MenuItem(
            self.x,
            self.y - self.itemHeight * len(self.items),
            self.itemWidth,
            self.itemHeight,
            text)
        self.items.append(item)
    
    def draw(self):
        for item in self.items:
            item.draw()
