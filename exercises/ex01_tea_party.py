"""Throwing a tea party"""

__author__ = "730648018"


def main_planner(guests: int) -> None:
    """Main function calls all other functions"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))
    return


# When str() wasn't before each + int, there was an error message b/c you can't add a str and an int. str + str = str.
# "Tea Bags:", etc. to get printed labels for each result, not just a number.
# (guests) b/c main_planner input is guests instead of people- only one input for all 3.
# keyword return to get the function to return something. When return was before the first line/all, the following 3 wouldn't appear. Return goes last so it doesn't stop reading the other lines of print.


def tea_bags(people: int) -> int:
    """# tea bags needed based on # guests"""
    return people * 2


def treats(people: int) -> int:
    """#treats based on # guests"""
    return int(tea_bags(people=people) * 1.5)


# 3 treats per person, 1.5 treats per tea bag. int() b/c just the 1.5 returns a float.
# office hours- must use keyword argument. people needs to equal something, since we don't know the value do people=people


def cost(tea_count: int, treat_count: int) -> float:
    """Cost of tea bags and treats"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
