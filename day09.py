from dataclasses import dataclass
from typing import List
from functools import lru_cache


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


@lru_cache(maxsize=None)
def sumup_numbers(*values: int) -> int:
    return sum(values)


@dataclass
class XMAS:
    preamble: List[int]
    offset: int = 0

    def get_possible_sums(self) -> List[int]:
        sums = []

        for i in range(self.offset, len(self.preamble)):
            for j in range(self.offset + 1, len(self.preamble)):
                if j > i:
                    # TODO: instead of lru_cache I should just skip (i, j) pairs I've already calculated
                    sums.append(sumup_numbers(self.preamble[i], self.preamble[j]))

        self.offset += 1
        return sums

    def update_and_check_preamble(self, value: int):
        self.preamble += [value]


def parse_data(raw: str) -> List[int]:
    return list(map(int, raw.split("\n")))


def get_invalid_sum(numbers: List[int], preamble_length: int) -> int:
    xmas = XMAS(numbers[:preamble_length])

    for number in numbers[preamble_length:]:
        possible_sums = set(xmas.get_possible_sums())
        if number not in possible_sums:
            return number
        else:
            xmas.update_and_check_preamble(number)

    raise ValueError


data = parse_data(DATA)
invalid_sum = get_invalid_sum(data, 5)
assert invalid_sum == 127


def find_sumup_combination(values: List[int], sumup_value: int) -> List[int]:
    batch_size = 2

    while batch_size <= len(values):
        for i in range(len(values)):
            curr_values = values[i: i + batch_size]
            if sumup_numbers(*curr_values) == sumup_value:
                return curr_values

        batch_size += 1

    raise ValueError


contiguous_range = find_sumup_combination(data[:data.index(invalid_sum)], invalid_sum)
assert sumup_numbers(min(contiguous_range), max(contiguous_range)) == 62


with open("data/day09.txt") as f:
    data = parse_data(f.read())
    invalid_sum = get_invalid_sum(data, 25)
    print(invalid_sum)

    contiguous_range = find_sumup_combination(data[:data.index(invalid_sum)], invalid_sum)
    print(sumup_numbers(min(contiguous_range), max(contiguous_range)))
