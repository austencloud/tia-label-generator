"""
Main generator class for display item cards
"""
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from card_layout import CardLayout
from card_renderer.card_renderer import CardRenderer
from font_manager import FontManager
from items import ITEMS
from title_page_renderer import TitlePageRenderer

class DisplayCardGenerator:
    """
    Main class for generating the display item cards PDF.
    Coordinates the layout, rendering, and PDF creation process.
    """
    
    def __init__(self, output_file="display_item_cards.pdf"):
        """Initialize the generator with output file and components."""
        self.output_file = output_file
        self.page_width, self.page_height = letter
        
        # Register fonts
        FontManager.register_fonts()
        
        # Create layout
        self.layout = CardLayout()
        
        # Create canvas
        self.canvas = canvas.Canvas(output_file, pagesize=letter)
        
        # Create renderers
        self.card_renderer = CardRenderer(self.canvas, self.layout)
        self.title_page_renderer = TitlePageRenderer(self.canvas)
    
    def generate_cards(self):
        """Generate the complete PDF with title page and cards."""
        # Create title page
        self.title_page_renderer.draw_title_page()
        self.canvas.showPage()
        
        # Calculate margins
        margin_x, margin_y = self.layout.calculate_margins(
            self.page_width, self.page_height
        )
        
        # Generate all cards
        for i, (category, item) in enumerate(ITEMS):
            # Calculate position
            x, y = self.layout.calculate_card_position(
                i, margin_x, margin_y, self.page_height
            )
            
            # Draw card
            self.card_renderer.draw_card(x, y, category, item)
            
            # Start a new page after filling the current page
            if (i + 1) % self.layout.cards_per_page == 0 and i < len(ITEMS) - 1:
                self.canvas.showPage()
        
        # Close the last page if there are remaining cards
        if len(ITEMS) % self.layout.cards_per_page != 0:
            self.canvas.showPage()
        
        # Save the PDF
        self.canvas.save()
        print(f"✨ Display item cards saved to: {os.path.abspath(self.output_file)}")
