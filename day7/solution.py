from functools import cmp_to_key
import sys
from collections import Counter


def compare_same_kind(first_card: str, second_card: str) -> int:
    cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    for i in range(len(first_card)):
        if cards.index(first_card[i]) < cards.index(second_card[i]):
            return -1
        if cards.index(first_card[i]) > cards.index(second_card[i]):
            return 1
    raise Exception(first_card, second_card)


def get_card_rank(card: str) -> int:
    count = dict(Counter(card).most_common())
    if len(count) == 1:
        return 0
    if list(count.values()) == [4, 1]:
        return 1
    if list(count.values()) == [3, 2]:
        return 2
    if list(count.values()) == [3, 1, 1]:
        return 3
    if list(count.values()) == [2, 2, 1]:
        return 4
    if list(count.values()) == [2, 1, 1, 1]:
        return 5
    if list(count.values()) == [1, 1, 1, 1, 1]:
        return 6
    raise Exception(card, count.values())


@cmp_to_key
def compare(first_card: str, second_card: str) -> int:
    first_rank = get_card_rank(first_card)
    second_rank = get_card_rank(second_card)
    if first_rank - second_rank != 0:
        return first_rank - second_rank
    return compare_same_kind(first_card, second_card)


def part1(input_list: list[str]) -> int:
    hands = {}
    for line in input_list:
        hands[line.split(" ")[0]] = int(line.split(" ")[1])
    hands: dict[str, int] = {
        key: hands[key] for key in sorted(hands.keys(), key=compare, reverse=True)
    }

    result = 0
    for i, bet in enumerate(hands.values(), 1):
        result += i * bet

    return result


def compare_same_kind2(first_card: str, second_card: str) -> int:
    cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    for i in range(len(first_card)):
        if cards.index(first_card[i]) < cards.index(second_card[i]):
            return -1
        if cards.index(first_card[i]) > cards.index(second_card[i]):
            return 1
    raise Exception(first_card, second_card)


def get_card_rank2(card: str) -> int:
    count = dict(Counter(card).most_common())
    try:
        count[list(filter(lambda x: x != "J", count.keys()))[0]] += count["J"]
        count.pop("J", None)
    except:
        pass
    if len(count) == 1:
        return 0
    if list(count.values()) == [4, 1]:
        return 1
    if list(count.values()) == [3, 2]:
        return 2
    if list(count.values()) == [3, 1, 1]:
        return 3
    if list(count.values()) == [2, 2, 1]:
        return 4
    if list(count.values()) == [2, 1, 1, 1]:
        return 5
    if list(count.values()) == [1, 1, 1, 1, 1]:
        return 6
    raise Exception(card, count.values())


@cmp_to_key
def compare2(first_card: str, second_card: str) -> int:
    first_rank = get_card_rank2(first_card)
    second_rank = get_card_rank2(second_card)
    if first_rank - second_rank != 0:
        return first_rank - second_rank
    return compare_same_kind2(first_card, second_card)


def part2(input_list: list[str]) -> int:
    hands = {}
    for line in input_list:
        hands[line.split(" ")[0]] = int(line.split(" ")[1])
    hands = {
        key: hands[key] for key in sorted(hands.keys(), key=compare2, reverse=True)
    }

    result = 0
    for i, bet in enumerate(hands.values(), 1):
        result += i * bet

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
