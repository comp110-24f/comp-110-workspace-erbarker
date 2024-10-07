"""Writing for Loops"""

pets: list[str] = ["Louie", "Bo", "Bear"]
# Tell every pet they're a good boy!
for pet in pets:
    print(f"Good boy, {pet}!")


names: list[str] = ["Alyssa", "Janet", "Vrinda"]
# Print each index: name
for index in range(0, len(names)):
    print(str(index) + ": " + names[index])
