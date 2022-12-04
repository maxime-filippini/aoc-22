"""
    Day 4 of Advent of Code 2022
    Prompt: https://adventofcode.com/2022/day/4
"""

from aoc import read_data
import re

def compute(data):
    split = data.split("\n")
    
    out = 0
    for data in split:
        items = re.findall("\d+", data)
        items = [int(item) for item in items]

        if (items[0] - items[2]) * (items[1] - items[3]) <= 0:
            out += 1

    return out


if __name__ == "__main__":
    assert compute(read_data("04", "test.txt")) == 2
    print(compute(read_data("04", "input.txt")))
