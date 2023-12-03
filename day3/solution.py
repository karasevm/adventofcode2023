import sys


def part1(input_list: list[str]) -> int:
    result = 0
    not_symbols = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."])
    digits = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    visited = set()
    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            if (i, j) in visited:
                continue
            if input_list[i][j] in digits:
                for offset in [
                    (0, 1),
                    (1, 1),
                    (1, 0),
                    (1, -1),
                    (0, -1),
                    (-1, -1),
                    (-1, 0),
                    (-1, 1),
                ]:
                    try:
                        di, dj = offset
                        if input_list[i + di][j + dj] not in not_symbols:
                            start = j
                            end = j
                            while start - 1 >= 0 and input_list[i][start - 1] in digits:
                                start -= 1
                            while (
                                end + 1 < len(input_list[i])
                                and input_list[i][end + 1] in digits
                            ):
                                end += 1
                            result += int(input_list[i][start : end + 1])
                            for v in range(start, end + 1):
                                visited.add((i, v))
                            break
                    except:
                        pass

    return result


def part2(input_list: list[str]) -> int:
    result = 0
    digits = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    visited = set()
    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            if input_list[i][j] == "*":
                part_numbers = []
                for offset in [
                    (0, 1),
                    (1, 1),
                    (1, 0),
                    (1, -1),
                    (0, -1),
                    (-1, -1),
                    (-1, 0),
                    (-1, 1),
                ]:
                    try:
                        di, dj = offset
                        if input_list[i + di][j + dj] in digits:
                            if (i + di, j + dj) in visited:
                                continue
                            start = j + dj
                            end = j + dj
                            while (
                                start - 1 >= 0
                                and input_list[i + di][start - 1] in digits
                            ):
                                start -= 1
                            while (
                                end + 1 < len(input_list[i])
                                and input_list[i + di][end + 1] in digits
                            ):
                                end += 1
                            part_numbers.append(
                                int(input_list[i + di][start : end + 1])
                            )
                            for v in range(start, end + 1):
                                visited.add((i + di, v))
                    except:
                        pass
                if len(part_numbers) == 2:
                    result += part_numbers[0] * part_numbers[1]
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
