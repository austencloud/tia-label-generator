
from reportlab.lib import colors
from categories import get_category_colors
from font_manager import FontManager
import random
class BackgroundRenderer:
    def __init__(self, canvas, layout):
        self.canvas = canvas
        self.layout = layout

    def draw(self, x, y, color_scheme):
        self._draw_gradient_background(x + 1, y + 1, self.layout.card_width - 2, self.layout.card_height - 2, color_scheme["gradient_start"], color_scheme["gradient_end"])
        self.canvas.setStrokeColor(color_scheme["border_color"])
        self.canvas.setLineWidth(1.5)
        self.canvas.roundRect(x, y, self.layout.card_width, self.layout.card_height, radius=5, fill=0, stroke=1)

    def _draw_gradient_background(self, x, y, width, height, start_color, end_color, steps=12):
        for i in range(steps):
            ratio = i / float(steps - 1)
            r = start_color.red + (end_color.red - start_color.red) * ratio
            g = start_color.green + (end_color.green - start_color.green) * ratio
            b = start_color.blue + (end_color.blue - start_color.blue) * ratio
            current_color = colors.Color(r, g, b)
            self.canvas.setFillColor(current_color)
            segment_height = height / steps
            self.canvas.rect(x, y + (i * segment_height), width, segment_height + 0.5, fill=1, stroke=0)

