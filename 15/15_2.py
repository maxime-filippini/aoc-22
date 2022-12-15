"""
    Day 15 of Advent of Code 2022
    Prompt: https://adventofcode.com/2022/day/15
"""
from __future__ import annotations

import re
from aoc import read_data
import numpy as np

RE_COORD = re.compile(r"=(-?\d+)")


def compute(data, bounds):
    items = data.split("\n")
    sensors = {}

    for item in items:
        xs, ys, xc, yc = list(map(int, RE_COORD.findall(item)))
        sensors[(xs, ys)] = xc, yc

    beacons = set(sensors.values())

    lb, ub = bounds

    # New strategy - Only check the outer edge + 1
    for sensor, closest_beacon in sensors.items():
        xs, ys = sensor
        xc, yc = closest_beacon

        dc = abs(xc - xs) + abs(yc - ys)

        for i in range(dc):
            for x, y in [
                (xs + i + 1, ys + dc - i),
                (xs - i - 1, ys + dc - i),
                (xs + i, ys - dc + i - 1),
                (xs - i, ys - dc + i - 1),
            ]:

                if x < lb or y < lb or x > ub or y > ub:
                    continue

                if (x, y) in beacons:
                    continue

                for other_sensor, other_closest_beacon in sensors.items():
                    xso, yso = other_sensor
                    xco, yco = other_closest_beacon

                    dcand = abs(xso - x) + abs(yso - y)
                    do = abs(xso - xco) + abs(yso - yco)

                    # if overlap, not a beacon
                    if dcand <= do:
                        break

                else:
                    return x * 4_000_000 + y

    raise AssertionError("???")


if __name__ == "__main__":
    assert compute(read_data("15", "test.txt"), bounds=(0, 20)) == 56000011
    print(compute(read_data("15", "input.txt"), bounds=(0, 4_000_000)))
