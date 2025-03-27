from reportlab.lib import colors
from categories import get_category_colors
from font_manager import FontManager
import random


class AccentRenderer:
    def __init__(self, canvas):
        self.canvas = canvas

    def draw(self, x, y, width, height, color, size=6):
        self.canvas.saveState()
        self.canvas.setStrokeColor(color)
        self.canvas.setLineWidth(1)
        self.canvas.line(x + 3, y + height - 3, x + 3 + size, y + height - 3)
        self.canvas.line(x + 3, y + height - 3, x + 3, y + height - 3 - size)
        self.canvas.line(
            x + width - 3, y + height - 3, x + width - 3 - size, y + height - 3
        )
        self.canvas.line(
            x + width - 3, y + height - 3, x + width - 3, y + height - 3 - size
        )
        self.canvas.line(x + 3, y + 3, x + 3 + size, y + 3)
        self.canvas.line(x + 3, y + 3, x + 3, y + 3 + size)
        self.canvas.line(x + width - 3, y + 3, x + width - 3 - size, y + 3)
        self.canvas.line(x + width - 3, y + 3, x + width - 3, y + 3 + size)
        self.canvas.restoreState()
