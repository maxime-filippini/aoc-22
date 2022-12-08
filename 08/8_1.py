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
    inner_arr = arr[1:-1, 1:-1]

    def check_inner_vis(inner_arr, arr_compare, axis, post_op=lambda x: x):
        curr_max = np.maximum.accumulate(arr_compare, axis=axis)
        check = inner_arr > curr_max
        return post_op(check)

    v = (
        check_inner_vis(inner_arr=inner_arr, arr_compare=arr[1:-1, :-2], axis=1),
        check_inner_vis(
            inner_arr=np.fliplr(inner_arr),
            arr_compare=np.fliplr(arr[1:-1, 2:]),
            axis=1,
            post_op=np.fliplr,
        ),
        check_inner_vis(
            inner_arr=inner_arr,
            arr_compare=arr[:-2, 1:-1],
            axis=0,
        ),
        check_inner_vis(
            inner_arr=np.flipud(inner_arr),
            arr_compare=np.flipud(arr[2:, 1:-1]),
            axis=0,
            post_op=np.flipud,
        ),
    )

    out = np.full_like(inner_arr, False)

    for v_ in v:
        out = np.logical_or(out, v_)

    return out.sum() + 4 * arr.shape[0] - 4


if __name__ == "__main__":
    assert compute(read_data("08", "test.txt")) == 21
    print(compute(read_data("08", "input.txt")))
