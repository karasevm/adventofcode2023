import sys


def line_is_bad(line: list[str]) -> bool:
    for turn in line:
        turn = turn.split(", ")
        for color in turn:
            if (
                (color.split(" ")[1] == "red" and int(color.split(" ")[0]) <= 12)
                or (color.split(" ")[1] == "green" and int(color.split(" ")[0]) <= 13)
                or (color.split(" ")[1] == "blue" and int(color.split(" ")[0]) <= 14)
            ):
                continue
            return True
    return False


def part1(input_list: list[str]) -> int:
    result = 0
    for i, line in enumerate(input_list):
        line = line.split(": ")[1]
        line = line.split("; ")
        if not line_is_bad(line):
            result += i + 1

    return result


def part2(input_list: list[str]) -> int:
    result = 0
    for line in input_list:
        max_blue = 0
        max_green = 0
        max_red = 0
        line = line.split(": ")[1]
        line = line.split("; ")
        for turn in line:
            turn = turn.split(", ")
            for color in turn:
                if color.split(" ")[1] == "red":
                    max_red = max(max_red, int(color.split(" ")[0]))
                if color.split(" ")[1] == "green":
                    max_green = max(max_green, int(color.split(" ")[0]))
                if color.split(" ")[1] == "blue":
                    max_blue = max(max_blue, int(color.split(" ")[0]))
        result += max_red * max_blue * max_green

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
