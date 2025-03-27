from reportlab.lib import colors
from categories import get_category_colors
from font_manager import FontManager
import random
class PatternRenderer:
    def __init__(self, canvas):
        self.canvas = canvas

    def draw(self, x, y, width, height, pattern_color):
        self.canvas.saveState()
        self.canvas.setFillColor(pattern_color)
        spacing = 12
        dot_size = 1
        for i in range(int(width / spacing) + 1):
            for j in range(int(height / spacing) + 1):
                offset_x = random.uniform(-1, 1)
                offset_y = random.uniform(-1, 1)
                dot_x = x + (i * spacing) + offset_x
                dot_y = y + (j * spacing) + offset_y
                if dot_x > x and dot_x < x + width and dot_y > y and dot_y < y + height:
                    self.canvas.circle(dot_x, dot_y, dot_size, fill=1, stroke=0)
        self.canvas.restoreState()
