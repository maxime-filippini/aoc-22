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
        items = re.findall("(\d+)-(\d+)", data)

        range_a, range_b = [
            set(range(int(item[0]), int(item[1])+1))
            for item in items
        ]

        if range_a.intersection(range_b):
            out += 1

    return out


if __name__ == "__main__":
    assert compute(read_data("04", "test.txt")) == 4
    print(compute(read_data("04", "input.txt")))
