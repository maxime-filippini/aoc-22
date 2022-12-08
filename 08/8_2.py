"""
    Day 8 of Advent of Code 2022
    Prompt: https://adventofcode.com/2022/day/8
"""
from __future__ import annotations

from aoc import read_data
import numpy as np


def compute(data):
    lines = data.split("\n")
    mat = [list(map(int, x)) for x in lines]
    arr = np.array(mat)

    ni, nj = arr.shape

    all_out = []
    for i in range(1, ni - 1):
        for j in range(1, nj - 1):
            tree = arr[i, j]
            out = 1

            vecs = [
                arr[:i, j][::-1],  # row before,
                arr[i, :j][::-1],  # col before
                arr[i + 1 : ni, j],
                arr[i, j + 1 : nj],
            ]

            for vec in vecs:
                stop = np.cumprod(vec < tree)
                out *= np.sum(stop) + 1 * (stop.min() == 0)

            all_out.append(out)

    return max(all_out)


if __name__ == "__main__":
    assert compute(read_data("08", "test.txt")) == 8
    print(compute(read_data("08", "input.txt")))
