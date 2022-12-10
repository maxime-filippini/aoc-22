"""
    Day 10 of Advent of Code 2022
    Prompt: https://adventofcode.com/2022/day/10
"""
from __future__ import annotations

from aoc import read_data

SAMPLES = [20, 60, 100, 140, 180, 220]


def compute(data):
    lines = data.split("\n")

    X = 1
    out = []

    line_idx = 0
    cycle = 1
    to_add = None

    while line_idx < len(lines):
        line = lines[line_idx]
        out.append(cycle * X)

        if to_add is None:
            line_idx += 1

            if line.startswith("addx"):
                to_add = int(line[5:])

        else:
            X += to_add
            to_add = None

        print(f"{cycle=}, {X=}, signal={cycle*X}")
        cycle += 1

    return sum([out[s - 1] for s in SAMPLES])


if __name__ == "__main__":
    assert compute(read_data("10", "test.txt")) == 13140
    print(compute(read_data("10", "input.txt")))
