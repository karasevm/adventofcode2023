import sys
import re


def part1(input_list: list[str]) -> int:
    result = 0
    for line in input_list:
        tmp_line = re.findall(r"\d", line)
        result += int("".join([tmp_line[0], tmp_line[-1]]))
    return result


def part2(input_list: list[str]) -> int:
    result = 0
    for line in input_list:
        tmp_digit = ["0", "0"]
        matches = re.finditer(
            r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line
        )
        tmp_line = [match.group(1) for match in matches]
        if len(tmp_line[0]) != 1:
            match tmp_line[0]:
                case "one":
                    tmp_digit[0] = "1"
                case "two":
                    tmp_digit[0] = "2"
                case "three":
                    tmp_digit[0] = "3"
                case "four":
                    tmp_digit[0] = "4"
                case "five":
                    tmp_digit[0] = "5"
                case "six":
                    tmp_digit[0] = "6"
                case "seven":
                    tmp_digit[0] = "7"
                case "eight":
                    tmp_digit[0] = "8"
                case "nine":
                    tmp_digit[0] = "9"
        else:
            tmp_digit[0] = tmp_line[0]
        if len(tmp_line[-1]) != 1:
            match tmp_line[-1]:
                case "one":
                    tmp_digit[1] = "1"
                case "two":
                    tmp_digit[1] = "2"
                case "three":
                    tmp_digit[1] = "3"
                case "four":
                    tmp_digit[1] = "4"
                case "five":
                    tmp_digit[1] = "5"
                case "six":
                    tmp_digit[1] = "6"
                case "seven":
                    tmp_digit[1] = "7"
                case "eight":
                    tmp_digit[1] = "8"
                case "nine":
                    tmp_digit[1] = "9"
        else:
            tmp_digit[1] = tmp_line[-1]
        result += int("".join(tmp_digit))
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
