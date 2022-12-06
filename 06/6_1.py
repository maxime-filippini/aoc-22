"""
    Day 6 of Advent of Code 2022
    Prompt: https://adventofcode.com/2022/day/6
"""

from aoc import read_data
import re


def compute(data):
    for i in range(len(data) - 4):
        word = data[i : i + 4]
        if len(set(word)) == 4:
            return i + 4


if __name__ == "__main__":
    assert compute(read_data("06", "test.txt")) == 7
    print(compute(read_data("06", "input.txt")))
