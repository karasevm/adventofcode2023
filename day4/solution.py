from collections import defaultdict
import sys


def part1(input_list: list[str]) -> int:
    result = 0
    for line in input_list:
        line = line.split(": ")[1]
        winning_numbers = line.split(" | ")[0]
        my_numbers = line.split(" | ")[1]
        winning_set = set()
        my_set = set()
        for number in winning_numbers.split(" "):
            if number != "":
                winning_set.add(int(number))
        for number in my_numbers.split(" "):
            if number != "":
                my_set.add(int(number))
        if len(winning_set & my_set) > 0:
            result += 2 ** (len(winning_set & my_set) - 1)

    return result


def part2(input_list: list[str]) -> int:
    result = 0
    card_count = defaultdict(lambda: 1)
    for i, line in enumerate(input_list):
        line = line.split(": ")[1]
        winning_numbers = line.split(" | ")[0]
        my_numbers = line.split(" | ")[1]
        winning_set = set()
        my_set = set()
        for number in winning_numbers.split(" "):
            if number != "":
                winning_set.add(int(number))
        for number in my_numbers.split(" "):
            if number != "":
                my_set.add(int(number))
        if len(winning_set & my_set) > 0:
            for j in range(i + 1, i + len(winning_set & my_set) + 1):
                card_count[j] += card_count[i]
    for i in range(len(input_list)):
        result += card_count[i]
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
