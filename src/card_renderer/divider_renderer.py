class DividerRenderer:
    # Add an offset to move the divider down
    DIVIDER_OFFSET = 5  # 10 pixels down

    def __init__(self, canvas):
        self.canvas = canvas

    def draw(self, x, y, width, color):
        # Apply the offset to lower the divider position
        offset_y = y - self.DIVIDER_OFFSET
        
        self.canvas.saveState()
        self.canvas.setStrokeColor(color)
        self.canvas.setLineWidth(0.8)
        
        # Draw the line with offset
        self.canvas.line(x + 10, offset_y, x + width - 10, offset_y)
        
        # Draw the circles with offset
        self.canvas.setFillColor(color)
        self.canvas.circle(x + 10, offset_y, 1.5, fill=1, stroke=0)
        self.canvas.circle(x + width - 10, offset_y, 1.5, fill=1, stroke=0)
        
        self.canvas.restoreState()