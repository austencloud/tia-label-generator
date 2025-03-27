"""
Title page renderer for display item cards
"""
import random
from reportlab.lib import colors
from reportlab.lib.units import inch
from categories import CATEGORIES

class TitlePageRenderer:
    """
    Creates an attractive title page for the display item cards PDF.
    """
    
    def __init__(self, canvas):
        self.canvas = canvas
        self.page_width, self.page_height = self.canvas._pagesize
    
    def draw_title_page(self):
        """Draw the complete title page."""
        # Draw background
        self._draw_gradient_background()
        
        # Draw subtle pattern
        self._draw_subtle_pattern()
        
        # Draw title
        self._draw_title()
        
        # Draw color legend
        self._draw_color_legend()
        
        # Draw decorative elements
        self._draw_decorative_elements()
    
    def _draw_gradient_background(self):
        """Draw a gradient background for the entire page."""
        start_color = colors.Color(0.95, 0.95, 1.0)  # Light blue-gray
        end_color = colors.Color(1.0, 1.0, 1.0)      # White
        steps = 20
        
        for i in range(steps):
            ratio = i / float(steps - 1)
            r = start_color.red + (end_color.red - start_color.red) * ratio
            g = start_color.green + (end_color.green - start_color.green) * ratio
            b = start_color.blue + (end_color.blue - start_color.blue) * ratio
            current_color = colors.Color(r, g, b)
            
            self.canvas.setFillColor(current_color)
            segment_height = self.page_height / steps
            self.canvas.rect(
                0, i * segment_height,
                self.page_width, segment_height + 1,  # Slight overlap
                fill=1, stroke=0
            )
    
    def _draw_subtle_pattern(self):
        """Draw a subtle dot pattern on the title page."""
        pattern_color = colors.Color(0.5, 0.5, 0.8, 0.05)
        self.canvas.setFillColor(pattern_color)
        
        # Draw a grid of small dots
        spacing = 15
        dot_size = 1.2
        
        for i in range(int(self.page_width / spacing) + 1):
            for j in range(int(self.page_height / spacing) + 1):
                # Add some random offset for a more natural look
                offset_x = random.uniform(-2, 2)
                offset_y = random.uniform(-2, 2)
                
                dot_x = (i * spacing) + offset_x
                dot_y = (j * spacing) + offset_y
                
                self.canvas.circle(dot_x, dot_y, dot_size, fill=1, stroke=0)
    
    def _draw_title(self):
        """Draw title and subtitle text."""
        # Title
        self.canvas.setFillColor(colors.Color(0.3, 0.3, 0.5))
        self.canvas.setFont("DejaVuSans-Bold", 28)
        title = "Display Item Cards"
        title_width = self.canvas.stringWidth(title, "DejaVuSans-Bold", 28)
        
        # Add title with shadow effect
        self.canvas.setFillColor(colors.Color(0.3, 0.3, 0.5, 0.3))
        self.canvas.drawString(
            (self.page_width - title_width) / 2 + 2, 
            self.page_height - 2 * inch - 2, 
            title
        )
        
        self.canvas.setFillColor(colors.Color(0.3, 0.3, 0.5))
        self.canvas.drawString(
            (self.page_width - title_width) / 2, 
            self.page_height - 2 * inch, 
            title
        )
        
        # Subtitle
        self.canvas.setFont("DejaVuSans", 16)
        self.canvas.setFillColor(colors.Color(0.4, 0.4, 0.6))
        subtitle = "The Insect Asylum Collection"
        subtitle_width = self.canvas.stringWidth(subtitle, "DejaVuSans", 16)
        self.canvas.drawString(
            (self.page_width - subtitle_width) / 2, 
            self.page_height - 2.5 * inch, 
            subtitle
        )
        
        # Draw decorative line under subtitle
        self.canvas.setStrokeColor(colors.Color(0.4, 0.4, 0.6))
        self.canvas.setLineWidth(1)
        line_width = 3 * inch
        self.canvas.line(
            (self.page_width - line_width) / 2, 
            self.page_height - 2.7 * inch,
            (self.page_width + line_width) / 2, 
            self.page_height - 2.7 * inch
        )
    
    def _draw_color_legend(self):
        """Draw a color legend showing category colors."""
        # Legend title
        legend_y = self.page_height - 4 * inch
        self.canvas.setFont("DejaVuSans-Bold", 14)
        self.canvas.setFillColor(colors.Color(0.3, 0.3, 0.5))
        legend_title = "Category Guide"
        self.canvas.drawCentredString(
            self.page_width / 2,
            legend_y + 25,
            legend_title
        )
        
        # Draw categories in a grid (2 columns)
        categories = list(CATEGORIES.items())
        
        # Calculate layout
        box_size = 0.25 * inch
        spacing_y = 0.45 * inch
        spacing_x = 3 * inch
        cols = 2
        rows = (len(categories) + cols - 1) // cols  # Ceiling division
        
        # Starting position
        start_x = self.page_width / 2 - spacing_x * 0.8
        start_y = legend_y - 20
        
        # Draw each category
        for i, (cat_name, cat_data) in enumerate(categories):
            col = i % cols
            row = i // cols
            
            x = start_x + col * spacing_x
            y = start_y - row * spacing_y
            
            # Draw color sample with gradient
            self._draw_category_sample(x, y, box_size, cat_data)
            
            # Draw category name
            self.canvas.setFillColor(colors.black)
            self.canvas.setFont("DejaVuSans", 10)
            self.canvas.drawString(
                x + box_size + 8, 
                y - 3, 
                cat_name
            )
    
    def _draw_category_sample(self, x, y, size, cat_data):
        """Draw a sample of the category color with gradient."""
        # Check if we have gradient colors in cat_data
        if "gradient_start" in cat_data and "gradient_end" in cat_data and "border_color" in cat_data:
            # Draw border
            self.canvas.setStrokeColor(cat_data["border_color"])
            self.canvas.setLineWidth(1)
            self.canvas.roundRect(
                x, y - size, size, size, 
                radius=2, stroke=1, fill=0
            )
            
            # Draw gradient sample
            steps = 8
            step_height = size / steps
            
            for i in range(steps):
                ratio = i / float(steps - 1)
                r = cat_data["gradient_start"].red + (cat_data["gradient_end"].red - cat_data["gradient_start"].red) * ratio
                g = cat_data["gradient_start"].green + (cat_data["gradient_end"].green - cat_data["gradient_start"].green) * ratio
                b = cat_data["gradient_start"].blue + (cat_data["gradient_end"].blue - cat_data["gradient_start"].blue) * ratio
                current_color = colors.Color(r, g, b)
                
                self.canvas.setFillColor(current_color)
                self.canvas.rect(
                    x + 1, y - size + 1 + (i * step_height),
                    size - 2, step_height,
                    fill=1, stroke=0
                )
        else:
            # Fallback to solid color if gradient colors not available
            self.canvas.setFillColor(cat_data["color"])
            self.canvas.roundRect(
                x, y - size, size, size,
                radius=2, fill=1, stroke=0
            )
    
    def _draw_decorative_elements(self):
        """Draw decorative elements on the title page."""
        # Draw corners
        corner_size = 30
        self.canvas.setStrokeColor(colors.Color(0.4, 0.4, 0.6))
        self.canvas.setLineWidth(1.5)
        
        # Top-left corner
        self.canvas.line(40, self.page_height - 40, 40 + corner_size, self.page_height - 40)
        self.canvas.line(40, self.page_height - 40, 40, self.page_height - 40 - corner_size)
        
        # Top-right corner
        self.canvas.line(self.page_width - 40, self.page_height - 40, self.page_width - 40 - corner_size, self.page_height - 40)
        self.canvas.line(self.page_width - 40, self.page_height - 40, self.page_width - 40, self.page_height - 40 - corner_size)
        
        # Bottom-left corner
        self.canvas.line(40, 40, 40 + corner_size, 40)
        self.canvas.line(40, 40, 40, 40 + corner_size)
        
        # Bottom-right corner
        self.canvas.line(self.page_width - 40, 40, self.page_width - 40 - corner_size, 40)
        self.canvas.line(self.page_width - 40, 40, self.page_width - 40, 40 + corner_size)
        
        # Add some information at the bottom
        self.canvas.setFont("DejaVuSans", 9)
        self.canvas.setFillColor(colors.Color(0.5, 0.5, 0.7))
        
        footer_text = "Created with Display Item Card Generator"
        self.canvas.drawCentredString(
            self.page_width / 2, 
            1.0 * inch, 
            footer_text
        )