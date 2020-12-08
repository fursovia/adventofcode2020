from typing import Optional
from copy import deepcopy

DATA = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


def get_acc_value(raw: str, return_none_on_infinite_loop: bool = False) -> Optional[int]:
    acc_value = 0

    instructions = raw.split("\n")
    visited = [False for _ in range(len(instructions))]

    i = 0
    while not all(visited) and i < len(instructions):

        if visited[i]:
            if return_none_on_infinite_loop:
                return None
            else:
                return acc_value
        else:
            visited[i] = True
            action, number = instructions[i].split()
            number = int(number)

            if action == "nop":
                i += 1
            elif action == "acc":
                acc_value += number
                i += 1
            elif action == "jmp":
                i += number

    return acc_value


acc_value = get_acc_value(DATA)
assert acc_value == 5


def find_replacement(raw: str) -> Optional[int]:
    instructions = raw.split("\n")

    replace_with = {"nop": "jmp", "jmp": "nop"}
    positions = {
        "nop": [i for i, instruction in enumerate(instructions) if "nop" in instruction],
        "jmp": [i for i, instruction in enumerate(instructions) if "jmp" in instruction]
    }

    for action, action_positions in positions.items():
        for i in action_positions:
            copied_instructions = deepcopy(instructions)
            copied_instructions[i] = copied_instructions[i].replace(action, replace_with[action])
            copied_instructions = "\n".join(copied_instructions)
            acc_value = get_acc_value(copied_instructions, True)
            if acc_value is not None:
                return acc_value

    return None


acc_value = find_replacement(DATA)
assert acc_value == 8


with open("data/day08.txt") as f:
    data = f.read()
    acc_value = get_acc_value(data)
    print(acc_value)

    acc_value = find_replacement(data)
    print(acc_value)
