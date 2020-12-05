from dataclasses import dataclass
from typing import Optional


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


@dataclass
class BoardingPass:
    bsp: str
    row: Optional[int] = None
    col: Optional[int] = None
    sid: Optional[int] = None

    def decode_seat(self, num_rows: int = 128, num_cols: int = 8) -> None:
        self.row = self.decode_idx(self.bsp[:7], num_rows)
        self.col = self.decode_idx(self.bsp[7:], num_cols)
        self.sid = self.row * 8 + self.col

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


with open("data/day05.txt") as f:
    passes = [BoardingPass(bp.strip()) for bp in f.readlines()]
    max_sid = max(bp.sid for bp in passes)
    print(max_sid)
