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
    play_dict = {
        "A": {"X": 3, "Y": 6, "Z": 0},
        "B": {"X": 0, "Y": 3, "Z": 6},
        "C": {"X": 6, "Y": 0, "Z": 3},
    }

    score_dict = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }  

    split = data.split("\n")

    out = []

    for round in split:
        them, me = round.split(" ")

        my_score = score_dict[me]
        win_score = play_dict[them][me]
        
        out.append(my_score + win_score)

    return sum(out)


if __name__ == "__main__":
    assert compute(read_data("test.txt")) == 15
    print(compute(read_data("input.txt")))
