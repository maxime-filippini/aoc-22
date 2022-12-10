"""
    Day 10 of Advent of Code 2022
    Prompt: https://adventofcode.com/2022/day/10
"""
from __future__ import annotations

from aoc import read_data

N_COLS = 40


def compute(data):
    lines = data.split("\n")

    X = 1
    out = []

    line_idx = 0
    cycle = 0
    to_add = None

    while line_idx < len(lines):
        line = lines[line_idx]
        pixel_x = cycle % 40

        if abs(pixel_x - X) <= 1:  # lit case
            out.append("#")
        else:
            out.append(".")

        if to_add is None:
            line_idx += 1

            if line.startswith("addx"):
                to_add = int(line[5:])

        else:
            X += to_add
            to_add = None

        cycle += 1

    n_rows = len(out) // N_COLS
    out = [
        "".join(out[i_row * N_COLS : (i_row + 1) * N_COLS]) for i_row in range(n_rows)
    ]
    return out


if __name__ == "__main__":
    expected = [
        "##..##..##..##..##..##..##..##..##..##..",
        "###...###...###...###...###...###...###.",
        "####....####....####....####....####....",
        "#####.....#####.....#####.....#####.....",
        "######......######......######......####",
        "#######.......#######.......#######.....",
    ]
    assert compute(read_data("10", "test.txt")) == expected
    for row in compute(read_data("10", "input.txt")):
        print(row)
