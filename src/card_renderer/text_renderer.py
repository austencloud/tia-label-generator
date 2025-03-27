from reportlab.lib import colors
from categories import get_category_colors
from font_manager import FontManager
import random


class TextRenderer:
    def __init__(self, canvas, layout):
        self.canvas = canvas
        self.layout = layout

    def draw(self, x, y, item_name, fun_fact, color_scheme):
        # Calculate content area dimensions
        content_area_start = y + self.layout.header_height + 5
        content_area_height = self.layout.card_height - self.layout.header_height - 15

        # Set up for item name
        self.canvas.setFillColor(colors.black)
        item_font_name = FontManager.get_item_font("default")
        item_font_size = 10

        # Wrap item name text
        item_lines = self._wrap_text(
            item_name, item_font_name, item_font_size, self.layout.card_width - 16
        )

        # Set up for fun fact
        fact_font_name = FontManager.get_fact_font("default")
        fact_font_size = 7

        # Wrap fun fact text
        fact_lines = self._wrap_text(
            fun_fact, fact_font_name, fact_font_size, self.layout.card_width - 20
        )

        # Calculate spacing
        item_line_height = item_font_size * 1.3
        fact_line_height = fact_font_size * 1.2
        spacing_between = 5  # Space between item name and fun fact

        # Calculate total height needed
        total_item_height = len(item_lines) * item_line_height
        total_fact_height = len(fact_lines) * fact_line_height
        total_height = total_item_height + spacing_between + total_fact_height

        # Calculate center of content area
        content_center_y = content_area_start + (content_area_height / 2)

        # Vertical positioning offset to fit both elements
        vertical_offset = -15

        # Calculate starting Y position for item name
        item_start_y = (
            content_center_y + (total_height / 2) - item_line_height + vertical_offset
        )

        # Draw item name
        for i, line in enumerate(item_lines):
            self.canvas.setFont(item_font_name, item_font_size)
            line_y = item_start_y - (i * item_line_height)
            self.canvas.drawCentredString(x + self.layout.card_width / 2, line_y, line)

        # Calculate starting Y position for fun fact
        fact_start_y = (
            item_start_y - (len(item_lines) * item_line_height) - spacing_between
        )

        # Draw fun fact in italics
        self.canvas.setFillColor(
            colors.Color(0.3, 0.3, 0.3)
        )  # Slightly lighter color for facts
        for i, line in enumerate(fact_lines):
            self.canvas.setFont(
                fact_font_name + "-Oblique", fact_font_size
            )  # Use italic font
            line_y = fact_start_y - (i * fact_line_height)
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
