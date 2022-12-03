"""
    Day 3 of Advent of Code 2022
    Prompt: https://adventofcode.com/2022/day/3
"""

from aoc import read_data
from string import ascii_letters

def compute(data):
    def compute_priority(letter):
        return ascii_letters.find(letter) + 1

    out = 0
    split = data.split("\n")
    elf_groups = zip(split[::3], split[1::3], split[2::3])

    for elf_group in elf_groups:
        e1, e2, e3 = elf_group
        badges = list(set(e1).intersection(e2).intersection(e3))
        
        if len(badges) > 1:
            print(badges)
            raise AssertionError

        badge = badges[0]
        out += compute_priority(badge)

    return out



if __name__ == "__main__":
    assert compute(read_data(3, "test.txt")) == 70
    print(compute(read_data(3, "input.txt")))
