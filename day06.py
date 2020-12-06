from collections import Counter, defaultdict
from typing import List, DefaultDict

DATA = """abc

a
b
c

ab
ac

a
a
a
a

b"""


Answers = DefaultDict[str, str]


def get_answer(raw: str) -> Answers:
    answer = defaultdict(lambda: "no")
    for char in set(raw.replace("\n", "")):
        answer[char] = "yes"
    return answer


def get_answer2(raw: str) -> Answers:
    answer = defaultdict(lambda: "no")
    num_people = len(raw.split("\n"))
    for char in set(raw.replace("\n", "")):
        if raw.count(char) == num_people:
            answer[char] = "yes"
    return answer


def count_answers(answers: List[Answers]) -> int:
    values = []
    for ans in answers:
        values.extend(list(ans.values()))
    counter = Counter(values)
    return counter["yes"]


answers = [get_answer(raw) for raw in DATA.split("\n\n")]
assert count_answers(answers) == 11

answers2 = [get_answer2(raw) for raw in DATA.split("\n\n")]
assert count_answers(answers2) == 6


with open("data/day06.txt") as f:
    data = f.read()
    answers = [get_answer(raw) for raw in data.split("\n\n")]
    print(count_answers(answers))

    answers2 = [get_answer2(raw) for raw in data.split("\n\n")]
    print(count_answers(answers2))
