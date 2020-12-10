from dataclasses import dataclass
from typing import List, Dict
from collections import defaultdict


DATA_SMALL = """16
10
15
5
1
11
7
19
6
12
4"""

DATA_LARGE = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""


@dataclass
class Chain:
    adapters: List[int]

    @classmethod
    def from_str(cls, raw: str) -> "Chain":
        return cls(adapters=list(map(int, raw.split("\n"))))

    def get_differences(self) -> Dict[int, int]:
        sorted_adapters = sorted(self.adapters)
        # charging outlet
        sorted_adapters.insert(0, 0)

        differences = defaultdict(int)
        for i in range(1, len(self.adapters) + 1):
            diff = sorted_adapters[i] - sorted_adapters[i - 1]
            differences[diff] += 1

        # built-in joltage adapter
        differences[3] += 1
        return dict(differences)


chain = Chain.from_str(DATA_SMALL)
assert chain.get_differences() == {1: 7, 3: 5}


chain = Chain.from_str(DATA_LARGE)
assert chain.get_differences() == {1: 22, 3: 10}


with open("data/day10.txt") as f:
    data = f.read()

chain = Chain.from_str(data)
differences = chain.get_differences()
print(differences[1] * differences[3])