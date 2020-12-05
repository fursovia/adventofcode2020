from dataclasses import dataclass
from typing import Optional, List


PASSES = [
    "BFFFBBFRRR",
    "FFFBBBFRRR",
    "BBFFBBFRLL",
]


MAPPINGS = {
    "F": 0,
    "B": 1,
    "L": 0,
    "R": 1
}
MAGIC_NUMBER = 8


@dataclass
class BoardingPass:
    bsp: str
    row: Optional[int] = None
    col: Optional[int] = None
    sid: Optional[int] = None

    def decode_seat(self, num_rows: int = 128, num_cols: int = 8) -> None:
        self.row = self.decode_idx(self.bsp[:7], num_rows)
        self.col = self.decode_idx(self.bsp[7:], num_cols)
        self.sid = self.row * MAGIC_NUMBER + self.col

    def decode_idx(self, sequence: str, num_idx: int) -> int:
        indices = list(range(num_idx))
        for char in sequence:
            center = len(indices) // 2
            indices = [indices[:center], indices[center:]][MAPPINGS[char]]

        return indices[0]

    def __post_init__(self):
        self.decode_seat()


passes = [BoardingPass(bp) for bp in PASSES]
assert max(bp.sid for bp in passes) == 820


def find_missing_seats(seats: List[int], num_rows: int = 128, num_cols: int = 8) -> List[int]:
    seats = set(seats)
    all_seats = []
    all_rows = []
    for i in range(num_rows):
        curr_row = []
        for j in range(num_cols):
            curr_row.append(i * MAGIC_NUMBER + j)
            all_seats.append(i * MAGIC_NUMBER + j)
        all_rows.append(set(curr_row))
    all_seats = set(all_seats)

    for row in all_rows:
        if all(idx not in seats for idx in row):
            for idx in row:
                all_seats.discard(idx)

    for seat in seats:
        all_seats.discard(seat)

    return list(all_seats)


with open("data/day05.txt") as f:
    passes = [BoardingPass(bp.strip()) for bp in f.readlines()]
    max_sid = max(bp.sid for bp in passes)
    print(max_sid)

    missing_seats = find_missing_seats([bp.sid for bp in passes])
    print(missing_seats)
