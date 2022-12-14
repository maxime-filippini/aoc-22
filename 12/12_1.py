"""
    Day 12 of Advent of Code 2022
    Prompt: https://adventofcode.com/2022/day/12
"""
from __future__ import annotations

from aoc import read_data
import sys

sys.setrecursionlimit(10000)


def get_elev(letter):
    if letter == "E":
        return ord("z")
    elif letter == "S":
        return ord("a")
    return ord(letter)


def get_neighbors(node, map_elev):
    out = set()
    x, y = node
    elev = map_elev[node]

    for cand_node in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if map_elev.get(cand_node) and (map_elev[cand_node] <= elev + 1):
            out.add(cand_node)
    return out


def compute(data):
    rows = data.split("\n")

    parsed = {(j, i): cell for i, row in enumerate(rows) for j, cell in enumerate(row)}
    map_elev = {k: get_elev(v) for k, v in parsed.items()}
    distances = {node: float("inf") for node in parsed.keys()}

    start = next(k for k, v in parsed.items() if v == "S")
    end = next(k for k, v in parsed.items() if v == "E")

    unvisited = set(parsed.keys())
    distances[start] = 0

    def recursion(curr_node, end, unvisited, distances):
        neighbors = get_neighbors(
            node=curr_node,
            map_elev=map_elev,
        )

        next_nodes = set(neighbors).intersection(unvisited)

        # Update distances
        for next_node in next_nodes:
            if distances[next_node] > distances[curr_node] + 1:
                distances[next_node] = distances[curr_node] + 1

        # Mark current node as visited
        unvisited.remove(curr_node)

        # Recursive bit
        if unvisited:
            min_distance_node = min(unvisited, key=lambda node: distances[node])
            unvisited, distances = recursion(
                curr_node=min_distance_node,
                end=end,
                unvisited=unvisited,
                distances=distances,
            )

        return unvisited, distances

    while end in unvisited:
        unvisited, distances = recursion(
            curr_node=start, end=end, unvisited=unvisited, distances=distances
        )

    return distances[end]


if __name__ == "__main__":
    assert compute(read_data("12", "test.txt")) == 31
    print(compute(read_data("12", "input.txt")))
