import arcade

class Highlight:

    def __init__(self):
        self.x = 0
        self.y = 0

        self.fontSize = 15
        self.fontWeight = 15
    
    def move(self, widget):
        self.x = widget.x - 15
        self.y = widget.y + (widget.height - widget.fontSize) / 2
        print(self.x, self.y)

    def draw(self):
        arcade.draw_text(
            '>', self.x, self.y,
            arcade.color.WHITE, self.fontSize)