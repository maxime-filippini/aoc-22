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
ROPE_LEN = 10


def move_knot(knot, parent):
    xk, yk = knot
    xp, yp = parent

    x_dist = xp - xk
    y_dist = yp - yk

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

        knot = xk + x_move, yk + y_move

    return knot


def compute(data):
    lines = data.split("\n")

    pos = {knot: START for knot in range(ROPE_LEN)}
    tail_visited = set([pos[ROPE_LEN - 1]])

    for line in lines:
        dir, amt = line.split(" ")
        mx, my = MOVE_DICT[dir]

        for _ in range(int(amt)):
            xh, yh = pos[0]
            pos[0] = xh + mx, yh + my

            for j in range(1, ROPE_LEN):
                pos[j] = move_knot(pos[j], pos[j - 1])

            tail_visited.add(pos[ROPE_LEN - 1])

    return len(tail_visited)


if __name__ == "__main__":
    assert compute(read_data("09", "test_2.txt")) == 36
    print(compute(read_data("09", "input.txt")))
