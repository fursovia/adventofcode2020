import string
from collections import namedtuple, Counter, defaultdict
from typing import Dict, List, DefaultDict

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


ALPHABET = list(string.ascii_lowercase)

# Answers = namedtuple("Answers", fields=ALPHABET, defaults=("no",) * len(ALPHABET))
Answers = DefaultDict[str, str]


def get_answer(raw: str) -> Answers:
    answer = defaultdict(lambda: "no")
    for char in set(raw.replace("\n", "")):
        answer[char] = "yes"
    return answer


def count_answers(answers: List[Answers]) -> int:
    values = []
    for ans in answers:
        values.extend(list(ans.values()))
    counter = Counter(values)
    return counter["yes"]


answers = [get_answer(raw) for raw in DATA.split("\n\n")]
num_yes = count_answers(answers)
assert num_yes == 11


with open("data/day06.txt") as f:
    data = f.read()
    answers = [get_answer(raw) for raw in data.split("\n\n")]
    num_yes = count_answers(answers)
    print(num_yes)

