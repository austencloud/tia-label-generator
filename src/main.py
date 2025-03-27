"""
Main entry point for the display item card generator
"""
from display_card_generator import DisplayCardGenerator

def main():
    """Run the display item card generator."""
    print("📝 Starting Display Item Card Generator")
    generator = DisplayCardGenerator()
    generator.generate_cards()
    print("✅ Done!")

if __name__ == "__main__":
    main()
