import cudf
import pandas as pd

from utils import time_func


def df_soln(df):
    df["elf_id"] = df["calories"].isna().cumsum()
    df = df.groupby("elf_id").calories.sum().nlargest(3)
    part_1 = df.iloc[0]
    part_2 = df.sum()
    return part_1, part_2


@time_func
def cudf_soln(data_path):
    df = cudf.read_csv(data_path, skip_blank_lines=False, names=["calories"])
    return df_soln(df)


@time_func
def pandas_soln(data_path):
    df = pd.read_csv(data_path, skip_blank_lines=False, names=["calories"])
    return df_soln(df)


@time_func
def python_soln(data_path):
    elf_calories = []
    current_calories = 0
    with open(data_path, mode="r") as f:
        for line in f.readlines():
            if line.strip():
                calorie = int(line.strip())
                current_calories += calorie
            else:
                elf_calories.append(current_calories)
                current_calories = 0
    elf_calories.sort()
    part_1 = elf_calories[-1]
    part_2 = sum(elf_calories[-3:])
    return part_1, part_2


def main():
    data_path = "./data/day1.txt"

    print(python_soln(data_path))
    print(cudf_soln(data_path))
    print(pandas_soln(data_path))


if __name__ == "__main__":
    main()
