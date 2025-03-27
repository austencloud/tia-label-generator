from reportlab.lib import colors
from categories import get_category_colors
from font_manager import FontManager
import random
class ShadowRenderer:
    def __init__(self, canvas):
        self.canvas = canvas

    def draw(self, x, y, width, height, shadow_color, radius=5, opacity=0.3):
        shadow_color = colors.Color(
            shadow_color.red, shadow_color.green, shadow_color.blue, opacity
        )
        self.canvas.saveState()
        self.canvas.setFillColor(shadow_color)
        self.canvas.roundRect(x, y, width, height, radius, fill=1, stroke=0)
        self.canvas.restoreState()
