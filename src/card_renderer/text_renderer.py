from reportlab.lib import colors
from categories import get_category_colors
from font_manager import FontManager
import random


class TextRenderer:
    def __init__(self, canvas, layout):
        self.canvas = canvas
        self.layout = layout

    def draw(self, x, y, item_name, color_scheme):
        self.canvas.setFillColor(colors.black)
        font_name = FontManager.get_item_font("default")
        font_size = 10
        lines = self._wrap_text(
            item_name, font_name, font_size, self.layout.card_width - 16
        )
        line_height = font_size * 1.3
        total_text_height = len(lines) * line_height

        # Calculate content area dimensions
        content_area_start = y + self.layout.header_height + 5
        content_area_height = self.layout.card_height - self.layout.header_height - 15

        # Calculate center of content area
        content_center_y = content_area_start + (content_area_height / 2)

        # Add a downward offset (negative value moves down)
        vertical_offset = -20  # Adjust this value to control how much to lower the text

        # Calculate starting Y position with offset
        start_y = (
            content_center_y
            + (total_text_height / 2)
            - (line_height / 2)
            + vertical_offset
        )

        # Draw each line
        for i, line in enumerate(lines):
            self.canvas.setFont(font_name, font_size)
            line_y = start_y - (i * line_height)
            self.canvas.drawCentredString(x + self.layout.card_width / 2, line_y, line)

    def _wrap_text(self, text, font_name, font_size, max_width):
        words = text.split()
        lines = []
        current_line = ""
        for word in words:
            test_line = current_line + (" " if current_line else "") + word
            width = self.canvas.stringWidth(test_line, font_name, font_size)
            if width <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)
        return lines
