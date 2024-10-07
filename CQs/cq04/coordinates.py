"""Importing functions"""

__author__ = "730648018"


def get_coords(xs: str, ys: str) -> None:
    xsindex: int = 0
    while xsindex < len(xs):
        ysindex: int = 0
        while ysindex < len(ys):
            print("(" + xs[xsindex] + "," + ys[ysindex] + ")")
            ysindex += 1
        xsindex += 1
