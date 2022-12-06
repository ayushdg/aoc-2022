from utils import time_func


@time_func
def python_soln(data_path):
    with open(data_path, "r") as f:
        line = f.readline()
    part_1 = 0
    part_2 = 0
    for i in range(0, len(line) - 3):
        if len(set(line[i : i + 4])) == 4:
            part_1 = i + 4
            break
    for i in range(0, len(line) - 13):
        if len(set(line[i : i + 14])) == 14:
            part_2 = i + 14
            break
    return part_1, part_2


def main():
    data_path = "./data/day6.txt"

    print(python_soln(data_path))


if __name__ == "__main__":
    main()
