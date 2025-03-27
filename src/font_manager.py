"""
Font management for display cards
"""

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


class FontManager:
    """
    Handles font registration and management for the display cards.
    """

    @staticmethod
    def register_fonts():
        """Register all required fonts for the display cards."""
        try:
            # Register DejaVu font family
            pdfmetrics.registerFont(TTFont("DejaVuSans", "DejaVuSans.ttf"))
            pdfmetrics.registerFont(TTFont("DejaVuSans-Bold", "DejaVuSans-Bold.ttf"))
            pdfmetrics.registerFont(
                TTFont("DejaVuSans-Oblique", "DejaVuSans-Oblique.ttf")
            )
            pdfmetrics.registerFont(
                TTFont("DejaVuSans-BoldOblique", "DejaVuSans-BoldOblique.ttf")
            )
            pdfmetrics.registerFont(TTFont("DejaVuSerif", "DejaVuSerif.ttf"))
            pdfmetrics.registerFont(TTFont("DejaVuSerif-Bold", "DejaVuSerif-Bold.ttf"))

            print("✅ Fonts registered successfully.")
        except Exception as e:
            print(f"⚠️ Warning: Could not register DejaVu fonts ({e})")
            print("📝 Using standard fonts instead.")

    @staticmethod
    def get_header_font(category):
        """Get the appropriate header font for a category."""
        # This could be expanded to use different fonts for different categories
        return "DejaVuSans-Bold"

    @staticmethod
    def get_item_font(category):
        """Get the appropriate item name font for a category."""
        # This could be expanded to use different fonts for different categories
        return "DejaVuSans-Bold"
