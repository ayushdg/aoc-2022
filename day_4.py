import cudf

from utils import time_func


def item_to_priority(item):
    item = ord(item)
    return item - ord("a") + 1 if item >= ord("a") else item - ord("A") + 27


@time_func
def cudf_soln(data_path):
    df = cudf.read_csv(data_path, sep=",", names=["elf1", "elf2"])
    elf1 = df.elf1.str.split("-", expand=True).astype("int64")
    elf2 = df.elf2.str.split("-", expand=True).astype("int64")
    part_1 = ((elf1[0] >= elf2[0]) & (elf1[1] <= elf2[1])) | ((elf1[0] <= elf2[0]) & (elf1[1] >= elf2[1]))
    part_2 = ~((elf2[1] < elf1[0]) | (elf1[1] < elf2[0]))
    return part_1.sum(), part_2.sum()


def main():
    data_path = "./data/day4.txt"

    print(cudf_soln(data_path))


if __name__ == "__main__":
    main()
