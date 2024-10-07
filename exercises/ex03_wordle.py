"""Let's play Wordle!"""

__author__ = "730648018"


def input_guess(secret_word_len: int) -> str:
    choose_word: str = input(f"Enter a {secret_word_len} character word: ")
    # prompt should change depending on the number of characters the secret code has
    while True:
        if len(choose_word) == secret_word_len:
            return choose_word
        else:
            choose_word = input(f"That wasn't {secret_word_len} chars! Try again: ")
            # if the length is not right, the user gets a second chance


"""Checking for letter matches"""


def contains_char(secret_word: str, char_guess: str) -> bool:
    assert len(char_guess) == 1
    # ensures char_guess is a single character always
    index: int = 0
    while index < len(secret_word):
        # ensures that the while loop stops if index is too high
        if secret_word[index] == char_guess:
            return True
        index += 1
        # index must increase inside of the while loop so it progresses and doesn't run indefinitely
    return False


"""Comparing the guess and secret word"""


def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    # constants for emoji representation
    index: int = 0
    answer: str = ""
    # answer variable is important so that the emojis print in succession instead of individual lines
    while index < len(guess):
        # len(guess) so that the secret word can be a flexible number of letters
        if guess[index] == secret[index]:
            # if the character is correct and in the correct location, it's a green box
            answer += GREEN_BOX
        elif contains_char(secret, guess[index]) == True:
            # a yellow box is printed if contains_char is True at any position
            answer += YELLOW_BOX
        else:
            answer += WHITE_BOX
            # letters nowhere in the secret code get a white box
        index += 1
        # moves to the next character so each index is accounted for
    return answer


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn_count: int = 1
    # turn count starts at one with a permanent max of 6
    winner: bool = False
    # tracks whether turns should continue increasing or if the player has won
    while turn_count <= 6 and not winner:
        # turns continue unless they run out or you win
        print(f"=== Turn {turn_count}/6 ===")
        guess: str = input_guess(len(secret))
        # call to input_guess so the guess is the right number of characters
        result: str = emojified(guess, secret)
        # call to emojified to print the emoji representation of the boolean
        print(result)
        if guess == secret:
            winner = True
        else:
            turn_count += 1
            # turns only increase if the player has yet to win (until max of 6)
    if winner:
        print(f"You won in {turn_count}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
