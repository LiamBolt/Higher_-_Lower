"""
Higher Lower Game
A game where players guess which Ugandan celebrity has more social media
followers.
"""

from game import play_game


def main():
    """Main entry point for the game."""
    try:
        play_game()
    except KeyboardInterrupt:
        print("\nGame terminated by user. Thanks for playing!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please report this issue on GitHub.")


if __name__ == "__main__":
    main()
