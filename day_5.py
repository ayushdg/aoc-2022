from collections import deque

from utils import time_func


@time_func
def python_soln(data_path):
    stacks_1 = [deque() for i in range(9)]
    with open(data_path, "r") as f:
        lines = f.readlines()

    stack_lines = lines[:8]
    move_lines = lines[10:]
    for line in stack_lines:
        for i in range(1, len(line), 4):
            if line[i] != " ":
                stacks_1[i // 4].appendleft(line[i])
    stacks_2 = [stack.copy() for stack in stacks_1]
    for line in move_lines:
        line = line.strip().split(" ")
        stack2_popped = []
        for i in range(int(line[1])):
            elem = stacks_1[int(line[3]) - 1].pop()
            stacks_1[int(line[5]) - 1].append(elem)
            stack2_popped.append(stacks_2[int(line[3]) - 1].pop())
        for elem in stack2_popped[::-1]:
            stacks_2[int(line[5]) - 1].append(elem)

    return (
        "".join([stacks_1[i].pop() for i in range(9)]),
        "".join([stacks_2[i].pop() for i in range(9)]),
    )


def main():
    data_path = "./data/day5.txt"

    print(python_soln(data_path))


if __name__ == "__main__":
    main()
