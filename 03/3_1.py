"""
    Day 3 of Advent of Code 2022
    Prompt: https://adventofcode.com/2022/day/3
"""

from aoc import read_data
from string import ascii_letters

def compute(data):
    def compute_priority(letter):
        return ascii_letters.find(letter) + 1

    split = data.split("\n")
    
    out = 0
    for rucksack in split:
        n = len(rucksack)
        half = int(n/2)
        h1, h2 = rucksack[:half], rucksack[half:]

        overlap = set(h1).intersection(h2)

        for item in overlap:
            out += compute_priority(item)

    return out


if __name__ == "__main__":
    assert compute(read_data(3, "test.txt")) == 157
    print(compute(read_data(3, "input.txt")))
