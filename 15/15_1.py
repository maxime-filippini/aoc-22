"""
    Day 15 of Advent of Code 2022
    Prompt: https://adventofcode.com/2022/day/15
"""
from __future__ import annotations

import re
from aoc import read_data


RE_COORD = re.compile(r"=(-?\d+)")


def compute(data, y):
    items = data.split("\n")
    sensors = {}

    for item in items:
        xs, ys, xc, yc = list(map(int, RE_COORD.findall(item)))
        sensors[(xs, ys)] = xc, yc

    max_d = max(abs(xs - ys) + abs(xc - yc) for (xs, ys), (xc, yc) in sensors.items())

    min_b_x = min(v[0] for v in sensors.values())
    max_b_x = max(v[0] for v in sensors.values())

    out = 0
    for x in range(min_b_x - max_d, max_b_x + max_d + 1):  # too naive
        for (xs, ys), (xc, yc) in sensors.items():
            d_sensor_beacon = abs(xs - xc) + abs(ys - yc)
            d_compare = abs(x - xs) + abs(y - ys)

            if d_compare <= d_sensor_beacon and (x, y) != (xc, yc):
                out += 1
                break

    return out


if __name__ == "__main__":
    assert compute(read_data("15", "test.txt"), y=10) == 26
    print(compute(read_data("15", "input.txt"), y=2_000_000))
