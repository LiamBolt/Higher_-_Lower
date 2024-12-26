from art import logo, vs
from game_data import data

# Constants
MAX_INDEX = len(data) - 1
CONTINUE = 'y'
STOP = 'n'


# Game functions
def compare_user_guess(user_guess: str, score: int, compare_option: list,
                       against_option: list) -> int:
    """
    Compares the user's guess to determine if it's correct and updates the
    score.
    """
    if user_guess == 'a' and compare_option[1] > against_option[1]:
        print("Correct!")
        return score + 1
    elif user_guess == 'b' and compare_option[1] < against_option[1]:
        print("Correct!")
        return score + 1
    else:
        print("Wrong!")
    return score


def play_game() -> None:
    """
    Main game loop to play the higher or lower game.
    """
    compare_choice = 0
    against_choice = 1
    score = 0
    game_on = CONTINUE

    while game_on == CONTINUE:
        # Access dictionary values
        compare_option = list(data[compare_choice].values())
        against_option = list(data[against_choice].values())

        print("\nWelcome to the Higher or Lower Game!")
        print(logo)
        print(f"Compare A: {compare_option[0]}, {compare_option[2]}, "
              f"{compare_option[3]}")
        print(vs)
        print(f"Against B: {against_option[0]}, {against_option[2]}, "
              f"{against_option[3]}")
        print('\n')
        # Get user input
        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Update the score
        score = compare_user_guess(user_guess, score, compare_option,
                                   against_option)
        print(f"Your score: {score}")

        # Check if the user wants to continue
        game_on = input(f"Do you want to continue playing? Type '{CONTINUE}'"
                        f"to continue or '{STOP}' to stop: ").lower()

        if game_on == STOP:
            print(f"Your final score: {score}")
            break

        if against_choice == MAX_INDEX:
            print("We are working on adding more data. Thank you for playing!")
            break

        # Clear the screen (simulate)
        print("\n" * 20)

        # Update choices
        compare_choice += 1
        against_choice += 1


# Entry point
if __name__ == "__main__":
    play_game()
