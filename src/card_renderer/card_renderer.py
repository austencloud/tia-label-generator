from reportlab.lib import colors
from background_renderer import BackgroundRenderer
from card_renderer.accent_renderer import AccentRenderer
from card_renderer.divider_renderer import DividerRenderer
from card_renderer.header_renderer import HeaderRenderer
from card_renderer.pattern_renderer import PatternRenderer
from card_renderer.shadow_renderer import ShadowRenderer
from card_renderer.text_renderer import TextRenderer
from categories import get_category_colors
from font_manager import FontManager
import random

class CardRenderer:
    def __init__(self, canvas, layout):
        self.canvas = canvas
        self.layout = layout
        self.shadow_renderer = ShadowRenderer(canvas)
        self.background_renderer = BackgroundRenderer(canvas, layout)
        self.pattern_renderer = PatternRenderer(canvas)
        self.header_renderer = HeaderRenderer(canvas, layout)
        self.divider_renderer = DividerRenderer(canvas)
        self.text_renderer = TextRenderer(canvas, layout)
        self.accent_renderer = AccentRenderer(canvas)

    def draw_card(self, x, y, category, item_name):
        color_scheme = get_category_colors(category)
        self.shadow_renderer.draw(x + 2, y - 2, self.layout.card_width, self.layout.card_height, color_scheme["border_color"])
        self.background_renderer.draw(x, y, color_scheme)
        self.pattern_renderer.draw(x + 5, y + 5, self.layout.card_width - 10, self.layout.card_height - 10, color_scheme["pattern_color"])
        self.header_renderer.draw(x, y, category, color_scheme)
        self.divider_renderer.draw(x + 5, y + self.layout.card_height - self.layout.header_height - 5, self.layout.card_width - 10, color_scheme["border_color"])
        self.text_renderer.draw(x, y, item_name, color_scheme)
        self.accent_renderer.draw(x, y, self.layout.card_width, self.layout.card_height, color_scheme["border_color"])









