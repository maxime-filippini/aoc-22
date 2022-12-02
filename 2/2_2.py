"""
    Day 2 of Advent of Code 2022
    Prompt: https://adventofcode.com/2022/day/2
"""

from pathlib import Path

def read_data(file_name):
    with open(Path(__file__).parent / file_name, "r") as f:
        data = f.read()
    return data

def compute(data):
    win_score_dict = {
        "X": 0,
        "Y": 3,
        "Z": 6,
    }  

    score_dict = {
        "A": {"X": 3, "Y": 1, "Z": 2},
        "B": {"X": 1, "Y": 2, "Z": 3},
        "C": {"X": 2, "Y": 3, "Z": 1}
    }

    split = data.split("\n")

    out = []

    for round in split:
        win_score = 0
        them, lose = round.split(" ")
        
        my_score = score_dict[them][lose]
        win_score = win_score_dict[lose]
        
        out.append(my_score + win_score)

    return sum(out)


if __name__ == "__main__":
    assert compute(read_data("test.txt")) == 12
    print(compute(read_data("input.txt")))
