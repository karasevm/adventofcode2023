import sys

def part1(input_list: list[str]) -> int:
    seeds = [int(x) for x in input_list[0].split(": ")[1].split(" ")]

    for i in range(len(input_list)):
        # print(i)
        if len(input_list[i]) > 0 and input_list[i][-1] == ":":
            for j in range(i, len(input_list)):
                if input_list[j] == "":
                    for l in range(len(seeds)):
                        seed = seeds[l]
                        for k in range(i + 1, j):
                            params = [int(x) for x in input_list[k].split(" ")]
                            if seed in range(params[1], params[1] + params[2]):
                                seeds[l] = seed - params[1] + params[0]
                    break
    return min(seeds)


def part2(input_list: list[str]) -> int:
    seeds = [int(x) for x in input_list[0].split(": ")[1].split(" ")]
    for i in range(0, len(seeds), 2):
        seeds[i + 1] = seeds[i] + seeds[i + 1]
    for i in range(len(input_list)):
        if len(input_list[i]) > 0 and input_list[i][-1] == ":":
            for j in range(i, len(input_list)):
                if input_list[j] == "":
                    modified_seeds = []  # seeds that are modified (NOT JUST CUT)
                    for k in range(i + 1, j):
                        params = [int(x) for x in input_list[k].split(" ")]
                        for l in range(
                            0, len(seeds), 2
                        ):  # we have 4 cases (seed fits in op, seed start gets cut off, seed end gets cut off, or seed gets cut off from both sides)
                            if (
                                seeds[l] >= params[1]
                                and seeds[l + 1] <= params[1] + params[2]
                            ):  # seed fits, no seed modification
                                modified_seeds.append(seeds[l] - params[1] + params[0])
                                modified_seeds.append(
                                    seeds[l + 1] - params[1] + params[0]
                                )

                                seeds[l] = -1
                                seeds[l + 1] = -1

                            if params[1] in range(
                                seeds[l] + 1, seeds[l + 1] - 1
                            ):  # start is cut off
                                if params[1] + params[2] in range(
                                    seeds[l] + 1, seeds[l + 1] - 1
                                ):  # and end is cut off
                                    seed_start = seeds[l]
                                    seed_end = seeds[l + 1]

                                    # preserve the start
                                    seeds[l] = seed_start
                                    seeds[l + 1] = params[1] - 1

                                    # add new
                                    modified_seeds.append(params[0])
                                    modified_seeds.append(params[0] + params[2])

                                    # preserve the end
                                    seeds.append(params[1] + params[2])
                                    seeds.append(seed_end)

                                else:  # end is okay
                                    seed_start = seeds[l]
                                    seed_end = seeds[l + 1]

                                    # preserve the start
                                    seeds[l] = seed_start
                                    seeds[l + 1] = params[1] - 1

                                    # add new
                                    modified_seeds.append(params[0])
                                    modified_seeds.append(
                                        seed_end - params[1] + params[0]
                                    )

                            elif params[1] + params[2] in range(
                                seeds[l] + 1, seeds[l + 1] - 1
                            ):  # start is okay and end is cut off
                                seed_start = seeds[l]
                                seed_end = seeds[l + 1]

                                # preserve the end
                                seeds[l] = params[1] + params[2]
                                seeds[l + 1] = seed_end

                                # add new
                                modified_seeds.append(
                                    seed_start - params[1] + params[0]
                                )
                                modified_seeds.append(params[0] + params[2])

                        seeds = list(filter(lambda x: x != -1, seeds))
                    seeds.extend(modified_seeds)
                    break
    return min(seeds)


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
