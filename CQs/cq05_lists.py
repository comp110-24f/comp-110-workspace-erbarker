"""Mutating functions."""

__author__ = "730648018"


def manual_append(a: list[int], mutate: int) -> None:
    a.append(mutate)


def double(b: list[int]) -> None:
    index: int = 0
    while index < len(b):
        b[index] *= 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
