"""
    Day 13 of Advent of Code 2022
    Prompt: https://adventofcode.com/2022/day/13
"""
from __future__ import annotations

from aoc import read_data
from itertools import zip_longest


def compare(it1, it2):
    if isinstance(it1, int):
        if isinstance(it2, int):
            return it1 - it2
        elif isinstance(it2, list):
            it1 = [it1]

    elif isinstance(it1, list):
        if isinstance(it2, int):
            it2 = [it2]

    else:
        raise AssertionError("???")

    # Compare lists
    comp = 0
    for subit1, subit2 in zip_longest(it1, it2, fillvalue=None):
        if subit2 is None:
            return 1

        if subit1 is None:
            return -1

        comp = compare(subit1, subit2)

        if comp != 0:
            return comp

    return comp


def compute(data):
    blocks = data.split("\n\n")

    out = 0
    for idx, block in enumerate(blocks):
        pkt1, pkt2 = block.split("\n")
        pkt1, pkt2 = eval(pkt1), eval(pkt2)

        comp = compare(pkt1, pkt2)
        out += int(comp < 0) * (idx + 1)

        print(idx + 1, comp < 0)

    return out


if __name__ == "__main__":
    assert compute(read_data("13", "test.txt")) == 13
    print(compute(read_data("13", "input.txt")))
