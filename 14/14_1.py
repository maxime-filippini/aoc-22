"""
    Day 14 of Advent of Code 2022
    Prompt: https://adventofcode.com/2022/day/14
"""
from __future__ import annotations

from aoc import read_data

N_SAND = 24


def parse(data):
    all_rocks = set()

    rocks_data = data.split("\n")

    for rock_data in rocks_data:
        coords = [tuple(map(int, item.split(","))) for item in rock_data.split(" -> ")]

        for c_start, c_end in zip(coords[:-1], coords[1:]):
            xs, ys = c_start
            xe, ye = c_end

            for x in range(min(xs, xe), max(xs, xe) + 1):
                for y in range(min(ys, ye), max(ys, ye) + 1):
                    all_rocks.add((x, y))

    return all_rocks


def compute(data):
    rocks = parse(data)
    max_y = max(r[1] for r in rocks)

    start = (500, 0)
    occupied = rocks

    n_dropped = 0
    while True:
        is_dropped = False
        x, y = start

        while not is_dropped:
            next_pos = next(
                pos
                for pos in [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1), (x, y)]
                if pos not in occupied
            )

            if y > max_y:
                return n_dropped

            # Drop case
            if next_pos == (x, y):
                is_dropped = True
                n_dropped += 1
                occupied.add((x, y))

            else:
                x, y = next_pos


if __name__ == "__main__":
    assert compute(read_data("14", "test.txt")) == 24
    print(compute(read_data("14", "input.txt")))
