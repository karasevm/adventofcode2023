from collections import defaultdict
import sys
from math import gcd


class Node:
    def set_l(self, child: str):
        self.left = child

    def set_r(self, child: str):
        self.right = child


def part1(input_list: list[str]) -> int:
    tree = defaultdict(Node)
    tree["AAA"] = Node()
    for line in input_list[2:]:
        children = line.split("(")[1][:-1].split(", ")
        for child in children:
            tree[child] = Node()
    for line in input_list[2:]:
        parent = line[:3]
        children = line.split("(")[1][:-1].split(", ")
        tree[parent].set_l(children[0])
        tree[parent].set_r(children[1])

    instructions = input_list[0]
    i = 0
    curr_node = "AAA"
    while curr_node != "ZZZ":
        if instructions[i % len(instructions)] == "L":
            curr_node = tree[curr_node].left
        else:
            curr_node = tree[curr_node].right
        i += 1
    return i


def part2(input_list: list[str]) -> int:
    tree = defaultdict(Node)
    for line in input_list[2:]:
        children = line.split("(")[1][:-1].split(", ")
        for child in children:
            tree[child] = Node()
    for line in input_list[2:]:
        parent = line[:3]
        children = line.split("(")[1][:-1].split(", ")
        tree[parent].set_l(children[0])
        tree[parent].set_r(children[1])

    instructions = input_list[0]
    i = 0
    print(list(filter(lambda x: x[2] == "A", tree.keys())))
    curr_nodes = list(filter(lambda x: x[2] == "A", tree.keys()))
    loop_steps = defaultdict(int)
    while len(loop_steps.keys()) != len(curr_nodes):
        if instructions[i % len(instructions)] == "L":
            for j in range(len(curr_nodes)):
                curr_nodes[j] = tree[curr_nodes[j]].left
                if curr_nodes[j][2] == "Z":
                    loop_steps[curr_nodes[j]] = i + 1
        else:
            for j in range(len(curr_nodes)):
                curr_nodes[j] = tree[curr_nodes[j]].right
                if curr_nodes[j][2] == "Z":
                    loop_steps[curr_nodes[j]] = i + 1
        i += 1

    result = 1
    for step in loop_steps.values():
        result = result * step // gcd(result, step)
    return result


if __name__ == "__main__":
    try:
        f = open(sys.argv[1], "r")
    except IOError:
        print("Error opening the file, try again")
        sys.exit(1)
    with f:
        lines = f.readlines()
        f.close()
        lines = [line.rstrip() for line in lines]
        print(f"Part 1 answer: {part1(lines)} Part 2 answer: {part2(lines)}")
