"""Basic syntax of lists"""

my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor

# Add an item to the list
my_numbers.append(1.5)
my_numbers.append(2.3)

# Create an already populated list
game_points: list[int] = [102, 86, 94]

# Subscription notation/Indexing
# print(game_points[2])
last_game: int = game_points[2]

# Modifying by index (because lists are mutable)
game_points[1] = 72

# Getting the length
len(game_points)

# Removing an item
game_points.pop(1)


def display(input: list[int]) -> None:
    index: int = 0
    while index < len(input):
        print(list[index])
        index += 1


display(input=game_points)
