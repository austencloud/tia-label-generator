from reportlab.lib import colors
from categories import get_category_colors
from font_manager import FontManager
import random


class HeaderRenderer:
    HEADER_OFFSET = 10

    def __init__(self, canvas, layout):
        self.canvas = canvas
        self.layout = layout

    def draw(self, x, y, category, color_scheme):
        self.canvas.setFillColor(color_scheme["color"])
        self.canvas.rect(
            x + 3,
            y + self.layout.card_height - self.layout.header_height - 3,
            self.layout.card_width - 6,
            self.layout.header_height,
            fill=1,
            stroke=0,
        )
        font_name = FontManager.get_header_font(category)
        if " & " in category:
            parts = category.split(" & ")
            font_size = 8
            self.canvas.setFont(font_name, font_size)
            self.canvas.setFillColor(color_scheme["text_color"])
            header_mid = y + self.layout.card_height - (self.layout.header_height / 2)
            line1_y = header_mid + font_size * 0.6 - self.HEADER_OFFSET
            line2_y = header_mid - font_size * 0.6 - self.HEADER_OFFSET
            self.canvas.drawCentredString(
                x + self.layout.card_width / 2, line1_y, parts[0]
            )
            self.canvas.drawCentredString(
                x + self.layout.card_width / 2, line2_y, parts[1]
            )
        else:
            font_size = 9
            self.canvas.setFont(font_name, font_size)
            self.canvas.setFillColor(color_scheme["text_color"])
            text_y = (
                y
                + self.layout.card_height
                - (self.layout.header_height / 2)
                + (font_size / 3)
                - self.HEADER_OFFSET
            )
            self.canvas.drawCentredString(
                x + self.layout.card_width / 2, text_y, category
            )
