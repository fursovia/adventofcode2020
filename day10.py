from dataclasses import dataclass
from typing import List, Dict, Optional
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
        adapters = list(map(int, raw.split("\n")))
        adapters = [0] + adapters + [max(adapters) + 3]
        adapters = sorted(adapters)
        return cls(adapters=adapters)

    def get_differences(self) -> Dict[int, int]:

        differences = defaultdict(int)
        for i in range(1, len(self.adapters)):
            diff = self.adapters[i] - self.adapters[i - 1]
            differences[diff] += 1

        return dict(differences)


def get_num_paths(sorted_adapters: List[int], cached_num_paths: Optional[Dict[int, int]] = None) -> int:

    if cached_num_paths is None:
        cached_num_paths = dict()

    num_paths = 0
    first_element = sorted_adapters[0]

    if len(sorted_adapters) == 1:
        cached_num_paths[first_element] = 1
        return 1

    if first_element in cached_num_paths:
        return cached_num_paths[first_element]

    for i in range(1, min(4, len(sorted_adapters))):
        if (sorted_adapters[i] - first_element) <= 3:
            num_paths += get_num_paths(sorted_adapters[i:], cached_num_paths)

    cached_num_paths[first_element] = num_paths
    return num_paths


chain = Chain.from_str(DATA_SMALL)
assert chain.get_differences() == {1: 7, 3: 5}
assert get_num_paths(chain.adapters) == 8

chain = Chain.from_str(DATA_LARGE)
assert chain.get_differences() == {1: 22, 3: 10}
assert get_num_paths(chain.adapters) == 19208


with open("data/day10.txt") as f:
    data = f.read()

# part 1
chain = Chain.from_str(data)
differences = chain.get_differences()
print(differences[1] * differences[3])

# part 2
print(get_num_paths(chain.adapters))
