"""
    Day 7 of Advent of Code 2022
    Prompt: https://adventofcode.com/2022/day/7
"""
from __future__ import annotations

from aoc import read_data
import re
from dataclasses import dataclass, field


def find_smallest_folder(threshold, all_sizes):
    above_threshold = [v for v in all_sizes.values() if v >= threshold]
    min_ = min(above_threshold)
    return min_


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    name: str
    files: list[File] = field(default_factory=list)
    dirs: dict[str, Directory] = field(default_factory=dict)
    parent: Directory = None

    @property
    def size(self):
        return sum([f.size for f in self.files]) + sum(
            [d.size for d in self.dirs.values()]
        )

    @property
    def full_path(self):
        out = ""

        if self.parent:
            out = self.parent.full_path + "/"

        out += self.name
        return out

    def get_total_below_x(self, threshold, out=0):
        for dir in self.dirs.values():
            out = dir.get_total_below_x(threshold=threshold, out=out)

        if self.size < threshold:
            out += self.size

        return out

    def get_all_sizes(self, all_sizes=None):
        if all_sizes is None:
            all_sizes = {}

        for dir in self.dirs.values():
            all_sizes = dir.get_all_sizes(all_sizes)

        all_sizes[self.full_path] = self.size
        return all_sizes

    def add_child(self, dir: Directory):
        dir.parent = self
        self.dirs[dir.name] = dir


def compute(data):
    root_dir = Directory(name="/")
    current_dir = root_dir

    lines = data.split("\n")
    curr_line_idx = 1

    while curr_line_idx < len(lines):
        curr_line = lines[curr_line_idx]

        if curr_line.startswith("$ cd"):
            path = curr_line[5:]

            if path == "..":
                current_dir = current_dir.parent
            else:
                current_dir = current_dir.dirs[path]

            curr_line_idx += 1

        elif curr_line == "$ ls":
            curr_line_idx += 1
            curr_line = lines[curr_line_idx]

            while not curr_line.startswith("$"):
                if curr_line.startswith("dir"):
                    dir_name = curr_line[4:]
                    if dir_name not in current_dir.dirs:
                        current_dir.add_child(Directory(name=dir_name))

                else:
                    size, name = curr_line.split(" ")
                    current_dir.files.append(File(name=name, size=int(size)))

                curr_line_idx += 1

                if curr_line_idx >= len(lines):
                    break

                curr_line = lines[curr_line_idx]

    return find_smallest_folder(
        threshold=30000000 - (70000000 - root_dir.size),
        all_sizes=root_dir.get_all_sizes(),
    )


if __name__ == "__main__":
    assert compute(read_data("07", "test.txt")) == 24933642
    print(compute(read_data("07", "input.txt")))
