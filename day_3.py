import cudf

from utils import time_func


def item_to_priority(item):
    item = ord(item)
    return item - ord("a") + 1 if item >= ord("a") else item - ord("A") + 27


@time_func
def python_soln(data_path):
    part_1 = 0
    part_2 = 0
    group_items = []
    with open(data_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            comp1 = set(line[: len(line) // 2])
            comp2 = set(line[(len(line) // 2) :])
            wrong_item = item_to_priority(comp1.intersection(comp2).pop())
            part_1 += wrong_item
            group_items.append(set(line))
            if len(group_items) == 3:
                badge_prio = item_to_priority(set.intersection(*group_items).pop())
                part_2 += badge_prio
                group_items = []

    return part_1, part_2


def main():
    data_path = "./data/day3.txt"

    print(python_soln(data_path))


if __name__ == "__main__":
    main()
