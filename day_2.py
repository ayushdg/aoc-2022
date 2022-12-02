import cudf
import pandas as pd

from utils import time_func


@time_func
def cudf_soln(data_path):
    df = cudf.read_csv(data_path, names=["opponent", "us"], sep=" ")
    # Rock -> A,X -> 1, Paper -> B,Y -> 2, Scissors -> C,Z -> 3
    df = df.replace(
        {"X": "1", "A": "1", "Y": "2", "B": "2", "Z": "3", "C": "3"}
    ).astype("int64")
    df["result"] = 0  # Loss
    df.result[df.us == df.opponent] = 3  # Draw
    df.result[
        ((df.us == 1) & (df.opponent == 3))
        | ((df.us == 2) & (df.opponent == 1))
        | ((df.us == 3) & (df.opponent == 2))
    ] = 6  # Win
    part_1 = df.us.sum() + df.result.sum()
    # Part 2 - The second column (us) is actually the intended result
    df["result"] = (df["us"] - 1) * 3  # Maps 1,2,3 to 0, 3, 6
    df["us"] = df["opponent"].copy()
    df.us[df.result == 0] = ((df.us + 1) % 3) + 1  # 1->3 2->1 3->2
    df.us[df.result == 6] = (df.us % 3) + 1  # 1->2 2->3 3->1
    part_2 = df.us.sum() + df.result.sum()
    return part_1, part_2


def main():
    data_path = "./data/day2.txt"

    print(cudf_soln(data_path))


if __name__ == "__main__":
    main()
