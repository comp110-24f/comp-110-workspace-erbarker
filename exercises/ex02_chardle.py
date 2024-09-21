"""EX02 - Chardle - A cute step toward Wordle"""

__author__ = "730648018"


def input_word() -> str:
    choose_word: str = input("Enter a 5-character word: ")
    if len(choose_word) != 5:
        print("Error: Word must cotnain 5 characters.")
        exit()
        return choose_word
    else:
        return choose_word


def input_letter() -> str:
    choose_letter: str = input("Enter a single character: ")
    if len(choose_letter) != 1:
        print("Error: Character must be a single character.")
        exit()
        return choose_letter
    else:
        return choose_letter


def contains_char(word: str, letter: str) -> None:
    count: int = 0
    print("Searching for " + str(letter) + " in " + str(word))
    if word[0] == letter:
        print(str(letter) + " found at index 0")
        count += 1
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
    if count == 0:
        print("No instances of " + str(letter) + " found in " + str(word))
    if count != 0:
        print(str(count) + " instances of " + str(letter) + " found in " + str(word))


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
