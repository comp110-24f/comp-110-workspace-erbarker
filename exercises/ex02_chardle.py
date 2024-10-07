"""EX02 - Chardle - A cute step toward Wordle"""

__author__ = "730648018"


def input_word() -> str:
    choose_word: str = input("Enter a 5-character word: ")
    if len(choose_word) != 5:
        # the word chosen must be 5 letters, or it will result in an error message.
        print("Error: Word must contain 5 characters.")
        exit()  # exits the program BEFORE it returns something so contains_char isn't run.
        return choose_word
    else:
        return choose_word


def input_letter() -> str:
    choose_letter: str = input("Enter a single character: ")
    if len(choose_letter) != 1:
        # the letter chosen must be a single character, or it will result in an error message.
        print("Error: Character must be a single character.")
        exit()  # exits the program BEFORE it returns something so contains_char isn't run.
        return choose_letter
    else:
        return choose_letter


def contains_char(word: str, letter: str) -> None:
    count: int = 0  # count starts at zero in case the character is never found.
    print("Searching for " + str(letter) + " in " + str(word))
    # Searching for statement before the if so it doesn't print multiple times if the letter appears multiple times.
    if word[0] == letter:
        print(str(letter) + " found at index 0")
        count += 1  # count increases every time the if boolean results in True.
    if word[1] == letter:
        print(str(letter) + " found at index 1")
        count += 1
    if word[2] == letter:
        print(str(letter) + " found at index 2")
        count += 1
    if word[3] == letter:
        print(str(letter) + " found at index 3")
        count += 1
    if word[4] == letter:
        print(str(letter) + " found at index 4")
        count += 1
    if count == 0:  # when the count is 0, none of the if statements were True.
        print("No instances of " + str(letter) + " found in " + str(word))
    if count == 1:
        # count increases for every instance so by the end, it should be the total- if the count is one, instance is singular.
        print("1 instance of " + str(letter) + " found in " + str(word))
    if count != 0 and count != 1:
        # if count is more than one, instances is plural.
        print(str(count) + " instances of " + str(letter) + " found in " + str(word))


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
