"""
    Day 11 of Advent of Code 2022
    Prompt: https://adventofcode.com/2022/day/11
"""
from __future__ import annotations

from aoc import read_data
import re

ROUNDS = 20


def parse(blocks):
    out = []
    for block in blocks:
        sp = block.split("\n")
        items = list(map(int, re.findall("\d+", sp[1])))
        op = eval("lambda old:" + sp[2][sp[2].find("=") + 1 :])

        div = int(sp[3].split(" ")[-1])
        dest_true = int(sp[4].split(" ")[-1])
        dest_false = int(sp[5].split(" ")[-1])

        out.append(
            {
                "items": items,
                "op": op,
                "div": div,
                "dest_true": dest_true,
                "dest_false": dest_false,
                "inspected": 0,
            }
        )
    return out


def compute(data):
    blocks = data.split("\n\n")
    monkeys = parse(blocks)
    out = []

    for r in range(ROUNDS):
        for monkey in monkeys:
            for item in monkey["items"]:
                worry = monkey["op"](item)
                worry = worry // 3
                test = (worry % monkey["div"]) == 0

                if test:
                    dest = monkey["dest_true"]
                else:
                    dest = monkey["dest_false"]

                monkey["items"] = monkey["items"][1:]
                monkeys[dest]["items"].append(worry)
                monkey["inspected"] += 1

    inspected_levels = sorted([m["inspected"] for m in monkeys], reverse=True)
    out = inspected_levels[0] * inspected_levels[1]
    return out


if __name__ == "__main__":
    assert compute(read_data("11", "test.txt")) == 10605
    print(compute(read_data("11", "input.txt")))
