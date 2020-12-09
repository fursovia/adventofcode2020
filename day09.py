from dataclasses import dataclass
from typing import List, Optional


DATA = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


@dataclass
class XMAS:
    preamble: List[int]
    offset: int = 0

    def get_possible_sums(self, sums: Optional[List[int]] = None) -> List[int]:
        sums = sums or []

        for i in range(self.offset, len(self.preamble)):
            for j in range(self.offset + 1, len(self.preamble)):
                if j > i:
                    sums.append(self.preamble[i] + self.preamble[j])

        self.offset += 1
        return sums

    def update_and_check_preamble(self, value: int):
        self.preamble += [value]


def get_invalid_sum(raw: str, preamble_length: int) -> int:
    numbers = list(map(int, raw.split("\n")))
    xmas = XMAS(numbers[:preamble_length])

    for number in numbers[preamble_length:]:
        possible_sums = set(xmas.get_possible_sums())
        if number not in possible_sums:
            return number
        else:
            xmas.update_and_check_preamble(number)

    raise ValueError


invalid_sum = get_invalid_sum(DATA, 5)
assert invalid_sum == 127


with open("data/day09.txt") as f:
    data = f.read()
    invalid_sum = get_invalid_sum(data, 25)
    print(invalid_sum)
