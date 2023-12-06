import sys
import re

def part1(input_list: list[str]) -> int:
    result = 1
    pairs = []
    times = re.findall(r"\d+", input_list[0])
    distances = re.findall(r"\d+", input_list[1])
    
    for i in range(len(times)):
        pairs.append((int(times[i]), int(distances[i])))
    for pair in pairs:
        time, distance = pair
        win_count = 0
        for i in range(time):
            tmp_distance = i * (time - i)
            if tmp_distance > distance:
                win_count += 1
        result *= win_count

    return result



def part2(input_list: list[str]) -> int:
    result = 1
    time = int(''.join(re.findall(r"\d+", input_list[0])))
    distance = int(''.join(re.findall(r"\d+", input_list[1])))

    win_count = 0
    for i in range(time):
        tmp_distance = i * (time - i)
        if tmp_distance > distance:
            win_count += 1
    result *= win_count

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
        print(
        f"Part 1 answer: {part1(lines)} Part 2 answer: {part2(lines)}")
