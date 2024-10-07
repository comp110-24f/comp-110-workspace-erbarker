"""Editing Lists"""

__author__ = "730648018"


def all(list_1: list[int], num: int) -> bool:
    if len(list_1) == 0:
        return False
        # If the list is empty, return False
    for i in range(len(list_1)):
        # len(list_1) so the algorithm can work for a list of any length
        # for i in range will step through every index to check if num matches at that position
        if list_1[i] != num:
            return False
            # Return false if not every number matches the specified integer num
    return True
    # Returns True if all numbers match the indicated number "num"


def max(list_2: list[int]) -> int:
    if len(list_2) == 0:
        raise ValueError("max() arg is an empty List")
        # If the list is empty, max should result in a ValueError
    largest_num: int = list_2[0]
    # Establishes a variable that is modified every time a larger number is encountered
    for index in range(0, len(list_2)):
        # Iterates through the list starting from the first element
        if list_2[index] > largest_num:
            # If the element is greater than the current value for largest number...
            largest_num = list_2[index]
            # ...update largest number to that
    return largest_num
    # After checking every item in the list, return the largest


def is_equal(list_3: list[int], list_4: list[int]) -> bool:
    for index in range(len(list_3)):
        # Iterates through items at each index in the list
        if list_3[index] != list_4[index]:
            return False
            # If the values aren't equal for one particular index, return False
    return True


def extend(list_5: list[int], list_6: list[int]) -> None:
    for element in list_6:
        list_5.append(element)
        # Edit list_5 by adding each element from list_6 onto the existing list
