"""
Card renderer for display item cards
"""
import random
from reportlab.lib import colors
from categories import get_category_colors
from font_manager import FontManager

class CardRenderer:
    """
    Renders beautiful display cards with enhanced visual elements.
    """
    
    def __init__(self, canvas, layout):
        self.canvas = canvas
        self.layout = layout
    
    def draw_card(self, x, y, category, item_name):
        """Draw a complete card with all visual elements."""
        # Get color scheme for this category
        color_scheme = get_category_colors(category)
        
        # Draw shadow beneath card
        self._draw_card_shadow(
            x + 2, y - 2, 
            self.layout.card_width, 
            self.layout.card_height,
            color_scheme["border_color"]
        )
        
        # Draw card background with gradient
        self._draw_card_background(x, y, color_scheme)
        
        # Draw subtle pattern overlay
        self._draw_subtle_pattern(
            x + 5, y + 5, 
            self.layout.card_width - 10, 
            self.layout.card_height - 10,
            color_scheme["pattern_color"]
        )
        
        # Draw category header
        self._draw_category_header(x, y, category, color_scheme)
        
        # Draw decorative divider
        self._draw_decorative_divider(
            x + 5, 
            y + self.layout.card_height - self.layout.header_height - 5,
            self.layout.card_width - 10,
            color_scheme["border_color"]
        )
        
        # Draw item name
        self._draw_item_name(x, y, item_name, color_scheme)
        
        # Draw corner accents
        self._draw_corner_accents(
            x, y, 
            self.layout.card_width, 
            self.layout.card_height,
            color_scheme["border_color"]
        )
    
    def _draw_card_shadow(self, x, y, width, height, shadow_color, radius=5, opacity=0.3):
        """Draw a shadow effect beneath the card."""
        shadow_color = colors.Color(
            shadow_color.red,
            shadow_color.green,
            shadow_color.blue,
            opacity
        )
        
        self.canvas.saveState()
        self.canvas.setFillColor(shadow_color)
        self.canvas.roundRect(
            x, y, width, height, radius, fill=1, stroke=0
        )
        self.canvas.restoreState()
    
    def _draw_card_background(self, x, y, color_scheme):
        """Draw card background with gradient and border."""
        # Draw gradient background
        self._draw_gradient_background(
            x + 1, y + 1,
            self.layout.card_width - 2,
            self.layout.card_height - 2,
            color_scheme["gradient_start"],
            color_scheme["gradient_end"]
        )
        
        # Draw card border
        self.canvas.setStrokeColor(color_scheme["border_color"])
        self.canvas.setLineWidth(1.5)
        self.canvas.roundRect(
            x, y, 
            self.layout.card_width, 
            self.layout.card_height,
            radius=5, fill=0, stroke=1
        )
    
    def _draw_gradient_background(self, x, y, width, height, start_color, end_color, steps=12):
        """Draw a vertical gradient background."""
        for i in range(steps):
            ratio = i / float(steps - 1)
            r = start_color.red + (end_color.red - start_color.red) * ratio
            g = start_color.green + (end_color.green - start_color.green) * ratio
            b = start_color.blue + (end_color.blue - start_color.blue) * ratio
            current_color = colors.Color(r, g, b)
            
            self.canvas.setFillColor(current_color)
            segment_height = height / steps
            self.canvas.rect(
                x, y + (i * segment_height),
                width, segment_height + 0.5,  # Slight overlap to avoid gaps
                fill=1, stroke=0
            )
    
    def _draw_subtle_pattern(self, x, y, width, height, pattern_color):
        """Draw a subtle dot pattern for texture."""
        self.canvas.saveState()
        self.canvas.setFillColor(pattern_color)
        
        # Draw a grid of small dots
        spacing = 12
        dot_size = 1
        
        for i in range(int(width / spacing) + 1):
            for j in range(int(height / spacing) + 1):
                # Add some random offset for a more natural look
                offset_x = random.uniform(-1, 1)
                offset_y = random.uniform(-1, 1)
                
                dot_x = x + (i * spacing) + offset_x
                dot_y = y + (j * spacing) + offset_y
                
                # Only draw if within bounds
                if dot_x > x and dot_x < x + width and dot_y > y and dot_y < y + height:
                    self.canvas.circle(dot_x, dot_y, dot_size, fill=1, stroke=0)
        
        self.canvas.restoreState()
    
    def _draw_category_header(self, x, y, category, color_scheme):
        """Draw the category header with text."""
        # Draw header background
        self.canvas.setFillColor(color_scheme["color"])
        self.canvas.rect(
            x + 3, 
            y + self.layout.card_height - self.layout.header_height - 3,
            self.layout.card_width - 6, 
            self.layout.header_height,
            fill=1, stroke=0
        )
        
        # Determine text position and style based on category length
        font_name = FontManager.get_header_font(category)
        
        # Handle two-part category names (with "&")
        if " & " in category:
            parts = category.split(" & ")
            
            # Use smaller font for two lines
            font_size = 8
            self.canvas.setFont(font_name, font_size)
            self.canvas.setFillColor(color_scheme["text_color"])
            
            # Calculate vertical positions to better center within the header
            header_mid = y + self.layout.card_height - (self.layout.header_height / 2)
            line1_y = header_mid + font_size * 0.6  # Position first line above center
            line2_y = header_mid - font_size * 0.6  # Position second line below center
            
            # Draw first part
            self.canvas.drawCentredString(
                x + self.layout.card_width / 2,
                line1_y,
                parts[0]
            )
            
            # Draw second part
            self.canvas.drawCentredString(
                x + self.layout.card_width / 2,
                line2_y,
                parts[1]
            )
        else:
            # Single line category - center exactly in the middle of the header
            font_size = 9
            self.canvas.setFont(font_name, font_size)
            self.canvas.setFillColor(color_scheme["text_color"])
            
            # Calculate vertical position to center in header (adjusting for baseline)
            text_y = y + self.layout.card_height - (self.layout.header_height / 2) + (font_size / 3)
            
            self.canvas.drawCentredString(
                x + self.layout.card_width / 2,
                text_y,
                category
            )
    def _draw_decorative_divider(self, x, y, width, color):
        """Draw a decorative divider between header and content."""
        self.canvas.saveState()
        
        # Draw main line
        self.canvas.setStrokeColor(color)
        self.canvas.setLineWidth(0.8)
        self.canvas.line(x + 10, y, x + width - 10, y)
        
        # Draw small circles at ends
        self.canvas.setFillColor(color)
        self.canvas.circle(x + 10, y, 1.5, fill=1, stroke=0)
        self.canvas.circle(x + width - 10, y, 1.5, fill=1, stroke=0)
        
        self.canvas.restoreState()
    
    def _draw_item_name(self, x, y, item_name, color_scheme):
        """Draw the item name, handling multiline text if needed."""
        self.canvas.setFillColor(colors.black)
        
        # Get appropriate font
        font_name = FontManager.get_item_font("default")
        font_size = 10
        
        # Wrap text if needed
        lines = self._wrap_text(
            item_name, font_name, font_size, 
            self.layout.card_width - 16
        )
        
        # Calculate line height based on font size
        line_height = font_size * 1.3
        
        # Calculate total height of text block
        total_text_height = len(lines) * line_height
        
        # Calculate center of the available area for item name
        content_area_start = y + self.layout.header_height + 5  # Header + divider space
        content_area_height = self.layout.card_height - self.layout.header_height - 15
        content_center_y = content_area_start + (content_area_height / 2)
        
        # Calculate starting Y position to center text block
        start_y = content_center_y + (total_text_height / 2) - (line_height / 2)
        
        # Draw each line
        for i, line in enumerate(lines):
            self.canvas.setFont(font_name, font_size)
            
            line_y = start_y - (i * line_height)
            
            self.canvas.drawCentredString(
                x + self.layout.card_width / 2,
                line_y,
                line
            )
    def _wrap_text(self, text, font_name, font_size, max_width):
        """Break text into lines that fit within max_width."""
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
    
    def _draw_corner_accents(self, x, y, width, height, color, size=6):
        """Draw corner accents on the card."""
        self.canvas.saveState()
        self.canvas.setStrokeColor(color)
        self.canvas.setLineWidth(1)
        
        # Top-left corner
        self.canvas.line(x + 3, y + height - 3, x + 3 + size, y + height - 3)
        self.canvas.line(x + 3, y + height - 3, x + 3, y + height - 3 - size)
        
        # Top-right corner
        self.canvas.line(x + width - 3, y + height - 3, x + width - 3 - size, y + height - 3)
        self.canvas.line(x + width - 3, y + height - 3, x + width - 3, y + height - 3 - size)
        
        # Bottom-left corner
        self.canvas.line(x + 3, y + 3, x + 3 + size, y + 3)
        self.canvas.line(x + 3, y + 3, x + 3, y + 3 + size)
        
        # Bottom-right corner
        self.canvas.line(x + width - 3, y + 3, x + width - 3 - size, y + 3)
        self.canvas.line(x + width - 3, y + 3, x + width - 3, y + 3 + size)
        
        self.canvas.restoreState()