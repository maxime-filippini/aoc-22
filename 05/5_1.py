"""
    Day 5 of Advent of Code 2022
    Prompt: https://adventofcode.com/2022/day/5
"""

from aoc import read_data
import re

def compute(data):
    crate_lines, move_lines = data.split("\n\n")
    
    # Deal with crates
    crate_dict = {}
    for crate_line in crate_lines.split("\n")[:-1]:
        for i in range(0,len(crate_line),4):
            item = crate_line[i:i+3]
            if item.strip():
                i_crate = i // 4 + 1
                if i_crate not in crate_dict:
                    crate_dict[i_crate] = []
                crate_dict[i_crate].append(item[1:2])

    # Deal with moves
    regex = re.compile("move (\d+) from (\d+) to (\d+)")
    for move_line in move_lines.split("\n"):
        found = regex.findall(move_line)

        if found:
            to_move, src, dest = tuple(map(int, found[0]))
            
            crates = crate_dict[src][:int(to_move)]
            crate_dict[dest] = crates[::-1] + crate_dict[dest]
            crate_dict[src] = crate_dict[src][int(to_move):]

    out = [crate_dict[k][0] for k in sorted(crate_dict.keys()) if crate_dict[k]]
    return "".join(out)



if __name__ == "__main__":
    assert compute(read_data("05", "test.txt")) == "CMZ"
    print(compute(read_data("05", "input.txt")))
