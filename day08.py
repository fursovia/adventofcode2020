

DATA = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


def get_acc_value(raw: str) -> int:
    acc_value = 0

    instructions = raw.split("\n")
    visited = [False for _ in range(len(instructions))]

    i = 0
    while not all(visited):

        if visited[i]:
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


acc_value = get_acc_value(DATA)
assert acc_value == 5


with open("data/day08.txt") as f:
    data = f.read()
    acc_value = get_acc_value(data)
    print(acc_value)
