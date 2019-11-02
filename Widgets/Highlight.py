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
    
    def mouseMove(self, x, y, widgets):
        for index, widget in enumerate(widgets):
            if (widget.x <= x and widget.x + widget.width >= x and
                    widget.y <= y and widget.y + widget.height >= y):

                self.move(widget)
                return [index, widget]
        
        return None

    def draw(self):
        arcade.draw_text(
            '>', self.x, self.y,
            arcade.color.WHITE, self.fontSize,
            font_name = '../assets/fonts/source_code_pro.ttf')