class DividerRenderer:
    def __init__(self, canvas):
        self.canvas = canvas

    def draw(self, x, y, width, color):
        self.canvas.saveState()
        self.canvas.setStrokeColor(color)
        self.canvas.setLineWidth(0.8)
        self.canvas.line(x + 10, y, x + width - 10, y)
        self.canvas.setFillColor(color)
        self.canvas.circle(x + 10, y, 1.5, fill=1, stroke=0)
        self.canvas.circle(x + width - 10, y, 1.5, fill=1, stroke=0)
        self.canvas.restoreState()
