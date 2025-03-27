"""
Scavenger Hunt List Generator for The Insect Asylum Collection

This script generates a professionally designed PDF scavenger hunt checklist
that coordinates with the display card system.
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    Paragraph,
    Spacer,
    SimpleDocTemplate,
    Table,
    TableStyle,
    Image,
)

# Define categories with their color schemes based on your existing colors
CATEGORIES = {
    "Minerals & Fossils": {
        "color": colors.Color(0.4, 0.4, 0.8),  # Blue-purple
        "emoji": "🔵",
        "items": [
            "Dinosaur fossil",
            "Blue calcite",
            "Honey calcite",
            "Labradorite",
            "Spectralite",
            "Red ammonite",
            "Purple agate",
            "Hourglass selenite",
            "Desert Rose Crystal",
            "Wulfenite crystal",
        ],
    },
    "Shells & Marine": {
        "color": colors.Color(0.2, 0.7, 0.7),  # Turquoise
        "emoji": "🔷",
        "items": [
            "Yellow dog conch shell",
            "Butter clam shell",
            "Brooch clamshell",
            "Conch shell eggs",
            "Horseshoe crab",
            "Shark jaw",
        ],
    },
    "Plant Materials": {
        "color": colors.Color(0.3, 0.7, 0.4),  # Green
        "emoji": "🟢",
        "items": [
            "Sugar pinecones",
            "Pine cones",
            "Bottle tree seed pods",
            "Moss",
            "Okra seed pods",
            "Driftwood",
            "Foxtails",
        ],
    },
    "Preserved Specimens": {
        "color": colors.Color(0.8, 0.7, 0.2),  # Amber
        "emoji": "🟡",
        "items": [
            "Duckling",
            "Mummified Duckling",
            "Chipmunk",
            "Opossum",
            "Chameleon",
            "Snakeskin",
            "Chick",
            "Weasel",
            "Fox head",
            "Chinese water dragon",
        ],
    },
    "Animal Parts": {
        "color": colors.Color(0.7, 0.5, 0.3),  # Brown
        "emoji": "🟤",
        "items": [
            "Macaw feathers",
            "Goose feathers",
            "Turtle shell",
            "Bird's nest",
            "Wasp nest",
            "Cobra skin",
            "Butterfly & Moth Wings",
            "Snake shed",
            "Beaver paw",
            "Rabbit pelt",
            "Coyote tail",
            "Raccoon pelt",
            "Bobcat Hyde",
            "Raccoon tail",
            "Silver Fox hide",
            "Faun hide",
            "Woodboring Jewel Beatles",
        ],
    },
    "Bones & Skulls": {
        "color": colors.Color(0.7, 0.7, 0.7),  # Gray
        "emoji": "⚪",
        "items": [
            "Giraffe vertebrae",
            "Beaver skull",
            "Beaver jaw",
            "Fox skull",
            "Hip bone",
            "Raccoon skull",
            "Deer jaw",
            "Deer bones",
            "Deer antler",
            "Fishbone tail",
            "Python vertebrae",
            "Moose tooth",
        ],
    },
    "Resin Replicas": {
        "color": colors.Color(0.9, 0.7, 0.4),  # Light orange
        "emoji": "🟠",
        "items": [
            "Madagascar hissing cockroach",
            "Beaver teeth",
            "Beaver paw",
            "Iguana head",
            "Iguana foot",
        ],
    },
    "Miscellaneous": {
        "color": colors.Color(0.5, 0.5, 0.5),  # Neutral gray
        "emoji": "⚫",
        "items": ["Arrowheads", "Clay bowl"],
    },
}


def draw_gradient_background(
    canvas, x, y, width, height, start_color, end_color, steps=20
):
    """Draw a gradient background"""
    for i in range(steps):
        ratio = i / float(steps - 1)
        r = start_color.red + (end_color.red - start_color.red) * ratio
        g = start_color.green + (end_color.green - start_color.green) * ratio
        b = start_color.blue + (end_color.blue - start_color.blue) * ratio
        current_color = colors.Color(r, g, b)
        canvas.setFillColor(current_color)
        segment_height = height / steps
        canvas.rect(
            x, y + (i * segment_height), width, segment_height + 0.5, fill=1, stroke=0
        )


def draw_checkbox(canvas, x, y, size=12):
    """Draw a checkbox"""
    canvas.setStrokeColor(colors.black)
    canvas.setLineWidth(0.5)
    canvas.rect(x, y, size, size, fill=0, stroke=1)


def draw_category_header(canvas, x, y, category, emoji, color_scheme, width):
    """Draw a category header with gradient background"""
    # Define colors
    start_color = colors.Color(
        color_scheme.red * 1.2, color_scheme.green * 1.2, color_scheme.blue * 1.2
    )
    end_color = colors.Color(
        color_scheme.red * 0.8, color_scheme.green * 0.8, color_scheme.blue * 0.8
    )

    # Draw background
    header_height = 28
    draw_gradient_background(canvas, x, y, width, header_height, start_color, end_color)

    # Draw category name
    canvas.setFillColor(
        colors.white
        if color_scheme.red + color_scheme.green + color_scheme.blue < 1.5
        else colors.black
    )
    canvas.setFont("Helvetica-Bold", 14)
    text_y = y + header_height - 10
    canvas.drawString(x + 10, text_y, f"{emoji}  {category}")

    # Draw accent corners
    canvas.setStrokeColor(
        colors.white
        if color_scheme.red + color_scheme.green + color_scheme.blue < 1.5
        else colors.black
    )
    canvas.setLineWidth(1)
    corner_size = 8

    # Top-left
    canvas.line(
        x + 4, y + header_height - 4, x + 4 + corner_size, y + header_height - 4
    )
    canvas.line(
        x + 4, y + header_height - 4, x + 4, y + header_height - 4 - corner_size
    )

    # Top-right
    canvas.line(
        x + width - 4,
        y + header_height - 4,
        x + width - 4 - corner_size,
        y + header_height - 4,
    )
    canvas.line(
        x + width - 4,
        y + header_height - 4,
        x + width - 4,
        y + header_height - 4 - corner_size,
    )

    # Bottom-left
    canvas.line(x + 4, y + 4, x + 4 + corner_size, y + 4)
    canvas.line(x + 4, y + 4, x + 4, y + 4 + corner_size)

    # Bottom-right
    canvas.line(x + width - 4, y + 4, x + width - 4 - corner_size, y + 4)
    canvas.line(x + width - 4, y + 4, x + width - 4, y + 4 + corner_size)

    return y + header_height


def draw_pattern(canvas, x, y, width, height, color, opacity=0.05):
    """Draw a subtle pattern"""
    pattern_color = colors.Color(color.red, color.green, color.blue, opacity)
    canvas.saveState()
    canvas.setFillColor(pattern_color)

    import random

    spacing = 15
    dot_size = 0.8

    for i in range(int(width / spacing) + 1):
        for j in range(int(height / spacing) + 1):
            offset_x = random.uniform(-1.5, 1.5)
            offset_y = random.uniform(-1.5, 1.5)
            dot_x = x + (i * spacing) + offset_x
            dot_y = y + (j * spacing) + offset_y
            if dot_x > x and dot_x < x + width and dot_y > y and dot_y < y + height:
                canvas.circle(dot_x, dot_y, dot_size, fill=1, stroke=0)

    canvas.restoreState()


def create_scavenger_hunt_pdf(output_filename="insect_asylum_scavenger_hunt.pdf"):
    # Set up the document
    width, height = letter
    c = canvas.Canvas(output_filename, pagesize=letter)

    # Draw page background
    c.setFillColor(colors.Color(0.98, 0.98, 1.0))
    c.rect(0, 0, width, height, fill=1, stroke=0)

    # Draw subtle pattern on background
    draw_pattern(c, 0, 0, width, height, colors.Color(0.3, 0.3, 0.5))

    # Draw decorative corners
    corner_size = 30
    c.setStrokeColor(colors.Color(0.4, 0.4, 0.6))
    c.setLineWidth(1.5)

    # Top-left corner
    c.line(40, height - 40, 40 + corner_size, height - 40)
    c.line(40, height - 40, 40, height - 40 - corner_size)

    # Top-right corner
    c.line(width - 40, height - 40, width - 40 - corner_size, height - 40)
    c.line(width - 40, height - 40, width - 40, height - 40 - corner_size)

    # Bottom-left corner
    c.line(40, 40, 40 + corner_size, 40)
    c.line(40, 40, 40, 40 + corner_size)

    # Bottom-right corner
    c.line(width - 40, 40, width - 40 - corner_size, 40)
    c.line(width - 40, 40, width - 40, 40 + corner_size)

    # Draw title
    title = "The Insect Asylum Collection"
    subtitle = "Specimen Scavenger Hunt"

    c.setFont("Helvetica-Bold", 24)
    c.setFillColor(colors.Color(0.3, 0.3, 0.5))
    title_width = c.stringWidth(title, "Helvetica-Bold", 24)
    c.drawString((width - title_width) / 2, height - 1.3 * inch, title)

    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(colors.Color(0.4, 0.4, 0.6))
    subtitle_width = c.stringWidth(subtitle, "Helvetica-Bold", 18)
    c.drawString((width - subtitle_width) / 2, height - 1.7 * inch, subtitle)

    # Draw a decorative line
    c.setStrokeColor(colors.Color(0.4, 0.4, 0.6))
    c.setLineWidth(1)
    line_width = 5 * inch
    c.line(
        (width - line_width) / 2,
        height - 1.9 * inch,
        (width + line_width) / 2,
        height - 1.9 * inch,
    )

    # Draw instructions
    c.setFont("Helvetica", 11)
    c.setFillColor(colors.black)
    instructions = "Explore our collection and check off each fascinating specimen as you find it! Items are color-coded by category to help guide your search."
    instructions_width = c.stringWidth(instructions, "Helvetica", 11)

    # If instructions are too long for one line, split them
    if instructions_width > width - 2 * inch:
        words = instructions.split()
        line1 = []
        line2 = []
        current_width = 0
        for word in words:
            word_width = c.stringWidth(word + " ", "Helvetica", 11)
            if current_width + word_width < width - 2 * inch:
                line1.append(word)
                current_width += word_width
            else:
                line2.append(word)

        line1_text = " ".join(line1)
        line2_text = " ".join(line2)

        line1_width = c.stringWidth(line1_text, "Helvetica", 11)
        line2_width = c.stringWidth(line2_text, "Helvetica", 11)

        c.drawString((width - line1_width) / 2, height - 2.2 * inch, line1_text)
        c.drawString((width - line2_width) / 2, height - 2.4 * inch, line2_text)

        y_start = height - 2.7 * inch
    else:
        c.drawString(
            (width - instructions_width) / 2, height - 2.2 * inch, instructions
        )
        y_start = height - 2.5 * inch

    # Calculate layout
    margin = 1 * inch
    content_width = width - 2 * margin

    # For a two-column layout
    column_width = (content_width - 0.5 * inch) / 2
    left_column_x = margin
    right_column_x = margin + column_width + 0.5 * inch

    # Draw categories and items
    current_y = y_start
    right_column_start_y = y_start

    # Track which categories go in which column
    total_items = sum(len(cat_data["items"]) for cat_data in CATEGORIES.values())
    items_per_column = total_items / 2

    current_column_items = 0
    current_x = left_column_x

    # Draw categories
    for category, cat_data in CATEGORIES.items():
        # Check if we need to switch to the right column
        if current_column_items > items_per_column and current_x == left_column_x:
            current_column_items = 0
            current_x = right_column_x
            current_y = right_column_start_y

        # Draw category header
        header_y = draw_category_header(
            c,
            current_x,
            current_y,
            category,
            cat_data["emoji"],
            cat_data["color"],
            column_width,
        )
        current_y = header_y + 5

        # Draw items with checkboxes
        for item in cat_data["items"]:
            draw_checkbox(c, current_x + 15, current_y, 12)
            c.setFont("Helvetica", 10)
            c.setFillColor(colors.black)
            c.drawString(current_x + 32, current_y + 2, item)
            current_y += 18
            current_column_items += 1

        # Add some space after each category
        current_y += 10

    # Draw footer with total count
    total_items = sum(len(cat_data["items"]) for _, cat_data in CATEGORIES.items())
    footer_y = 1.0 * inch

    c.setFont("Helvetica-Oblique", 11)
    c.setFillColor(colors.Color(0.3, 0.3, 0.5))
    footer_text = (
        f"How many specimens can you find? Record your total here: ____ / {total_items}"
    )
    footer_width = c.stringWidth(footer_text, "Helvetica-Oblique", 11)
    c.drawString((width - footer_width) / 2, footer_y, footer_text)

    social_text = "Share your discovery journey with us on social media using #InsectAsylumCollection"
    social_width = c.stringWidth(social_text, "Helvetica-Oblique", 11)
    c.drawString((width - social_width) / 2, footer_y - 20, social_text)

    # Save the document
    c.save()
    print(f"✨ Scavenger hunt PDF saved to: {output_filename}")


if __name__ == "__main__":
    create_scavenger_hunt_pdf()
