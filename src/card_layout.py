"""
Layout settings for display item cards
"""
from reportlab.lib.units import inch

class CardLayout:
    """
    Manages layout settings for the display cards including dimensions,
    spacing, and page arrangement.
    """
    
    def __init__(self):
        # Card dimensions - approximately 1/5 of letter width
        self.card_width = 1.7 * inch
        self.card_height = 1.2 * inch
        
        # Header section height
        self.header_height = 0.3 * inch
        
        # Layout settings
        self.cols = 5
        self.rows = 7
        self.cards_per_page = self.cols * self.rows
        
        # Spacing between cards
        self.card_spacing_x = 0.1 * inch
        self.card_spacing_y = 0.1 * inch
        
        # Calculate total grid dimensions with spacing
        self.grid_width = (self.cols * self.card_width) + ((self.cols - 1) * self.card_spacing_x)
        self.grid_height = (self.rows * self.card_height) + ((self.rows - 1) * self.card_spacing_y)
    
    def calculate_margins(self, page_width, page_height):
        """Calculate page margins to center the card grid."""
        margin_x = (page_width - self.grid_width) / 2
        margin_y = (page_height - self.grid_height) / 2
        return margin_x, margin_y
    
    def calculate_card_position(self, index, margin_x, margin_y, page_height):
        """Calculate the position of a card given its index and page margins."""
        page_index = index % self.cards_per_page
        col = page_index % self.cols
        row = page_index // self.cols
        
        # Calculate position with spacing
        x = margin_x + col * (self.card_width + self.card_spacing_x)
        y = page_height - margin_y - (row + 1) * self.card_height - row * self.card_spacing_y
        
        return x, y