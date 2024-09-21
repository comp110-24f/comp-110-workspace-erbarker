"""Practicing with conditionals"""


def less_than_10(num: int) -> None:
    """Tell us if num < 10"""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:  # check if this is true
        print("small number!")  # "then" block
    else:
        print("big number!")
    print("This is the end of the function!")


# less_than_10(num=7)


def wake_up(alarm: bool) -> str:
    """Return a message based on if alarm is going off."""
    if alarm is True:
        return "Wake up! Go to Comp 110!"
    else:
        return "Kepp sleeping. You deserve it. :)"


# print(wake_up(alarm=True))


def check_first_letter(word: str, letter: str) -> str:
    """Checks if letter is first character of word."""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"

    # print(check_first_letter(word="happy", letter="s"))

    def get_weather_report() -> str:
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather")
    return weather
