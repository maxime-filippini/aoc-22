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


def recursion(curr_node, end, map_elev, unvisited, distances):
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
            map_elev=map_elev,
            unvisited=unvisited,
            distances=distances,
        )

    return unvisited, distances


def compute(data):
    rows = data.split("\n")

    parsed = {(j, i): cell for i, row in enumerate(rows) for j, cell in enumerate(row)}
    map_elev = {k: get_elev(v) for k, v in parsed.items()}
    distances = {node: float("inf") for node in parsed.keys()}

    starts = [k for k, v in parsed.items() if v == "S" or v == "a"]
    end = next(k for k, v in parsed.items() if v == "E")

    out = []

    for i, curr_start in enumerate(starts):
        print(f"{i} / {len(starts)}")

        unvisited = set(parsed.keys())
        distances[curr_start] = 0

        unvisited, distances = recursion(
            curr_node=curr_start,
            end=end,
            map_elev=map_elev,
            unvisited=unvisited,
            distances=distances,
        )

        out.append(distances[end])

    return min(out)


if __name__ == "__main__":
    assert compute(read_data("12", "test.txt")) == 29
    print(compute(read_data("12", "input.txt")))
