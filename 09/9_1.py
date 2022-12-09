"""
    Day 9 of Advent of Code 2022
    Prompt: https://adventofcode.com/2022/day/9
"""
from __future__ import annotations

from aoc import read_data

MOVE_DICT = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}

START = (0, 0)


def compute(data):
    lines = data.split("\n")

    tail = START
    head = START
    visited = set([tail])

    for line in lines:
        dir, amt = line.split(" ")
        mx, my = MOVE_DICT[dir]

        xh, yh = head
        xt, yt = tail

        for _ in range(int(amt)):
            head = xh + mx, yh + my
            xh, yh = head

            x_dist = xh - xt
            y_dist = yh - yt

            should_move = max(abs(x_dist), abs(y_dist)) > 1

            if should_move:
                if abs(x_dist) > 0:
                    x_move = x_dist / abs(x_dist)
                else:
                    x_move = 0

                if abs(y_dist) > 0:
                    y_move = y_dist / abs(y_dist)
                else:
                    y_move = 0

                tail = xt + x_move, yt + y_move
                xt, yt = tail

                visited.add(tail)
    return len(visited)


if __name__ == "__main__":
    assert compute(read_data("09", "test_1.txt")) == 13
    print(compute(read_data("09", "input.txt")))
