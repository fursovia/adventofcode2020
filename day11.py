from dataclasses import dataclass
from typing import List
from copy import deepcopy


DATA = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""


@dataclass
class SeatLayout:
    seats: List[List[str]]
    num_updates: int = 0

    @classmethod
    def from_str(cls, raw: str) -> "SeatLayout":
        seats = []
        for line in raw.split("\n"):
            seats.append(list(line))
        return cls(seats=seats)

    def update_state(self) -> None:

        updates = {}
        for i in range(len(self.seats)):
            for j in range(len(self.seats[0])):
                curr_value = self.seats[i][j]

                if curr_value == ".":
                    continue

                num_occupied = 0
                for k in range(max(i - 1, 0), min(i + 2, len(self.seats))):
                    for m in range(max(j - 1, 0), min(j + 2, len(self.seats[0]))):
                        if not (k == i and j == m):
                            neigh_value = self.seats[k][m]
                            if neigh_value == "#":
                                num_occupied += 1

                if num_occupied == 0 and curr_value == "L":
                    updates[(i, j)] = "#"
                elif num_occupied >= 4 and curr_value == "#":
                    updates[(i, j)] = "L"
                else:
                    continue

        for (i, j), val in updates.items():
            self.seats[i][j] = val

    def update_state2(self) -> None:

        updates = {}
        for i in range(len(self.seats)):
            for j in range(len(self.seats[0])):
                num_occupied = 0
                curr_value = self.seats[i][j]

                if curr_value == ".":
                    continue

                # to the right
                for m in range(j + 1, len(self.seats[0])):
                    neigh_value = self.seats[i][m]
                    if neigh_value != ".":
                        if neigh_value == "#":
                            num_occupied += 1
                        break

                # to the left
                for m in range(j - 1, -1, -1):
                    neigh_value = self.seats[i][m]
                    if neigh_value != ".":
                        if neigh_value == "#":
                            num_occupied += 1
                        break

                # to the upwards
                for k in range(i - 1, -1, -1):
                    neigh_value = self.seats[k][j]
                    if neigh_value != ".":
                        if neigh_value == "#":
                            num_occupied += 1
                        break

                # to the bottom
                for k in range(i + 1, len(self.seats)):
                    neigh_value = self.seats[k][j]
                    if neigh_value != ".":
                        if neigh_value == "#":
                            num_occupied += 1
                        break
                # ←↑
                for l in range(min(j, i)):
                    neigh_value = self.seats[i - l - 1][j - l - 1]
                    if neigh_value != ".":
                        if neigh_value == "#":
                            num_occupied += 1
                        break

                # →↑
                for l in range(min(len(self.seats[0]) - j - 1, i)):
                    neigh_value = self.seats[i - l - 1][j + l + 1]
                    if neigh_value != ".":
                        if neigh_value == "#":
                            num_occupied += 1
                        break

                # →↓
                for l in range(min(len(self.seats[0]) - j - 1, len(self.seats) - i - 1)):
                    neigh_value = self.seats[i + l + 1][j + l + 1]
                    if neigh_value != ".":
                        if neigh_value == "#":
                            num_occupied += 1
                        break

                # ←↓
                for l in range(min(j, len(self.seats) - i - 1)):
                    neigh_value = self.seats[i + l + 1][j - l - 1]
                    if neigh_value != ".":
                        if neigh_value == "#":
                            num_occupied += 1
                        break

                if num_occupied == 0 and curr_value == "L":
                    updates[(i, j)] = "#"
                elif num_occupied >= 5 and curr_value == "#":
                    updates[(i, j)] = "L"
                else:
                    continue

        self.num_updates += 1
        for (i, j), val in updates.items():
            self.seats[i][j] = val

    def count_occupied(self) -> int:
        num_occupied = 0
        for line in self.seats:
            num_occupied += sum(seat == "#" for seat in line)
        return num_occupied

    def __repr__(self) -> str:
        data = ["".join(line) for line in self.seats]
        return "\n".join(data)


def find_occupied_seats_at_equilibrium(raw: str, part_two: bool = False) -> int:
    seat_layout = SeatLayout.from_str(raw)
    previous_seats = None

    while previous_seats != seat_layout.seats:
        previous_seats = deepcopy(seat_layout.seats)
        if part_two:
            seat_layout.update_state2()
        else:
            seat_layout.update_state()

    return seat_layout.count_occupied()


num_occupied = find_occupied_seats_at_equilibrium(DATA)
assert num_occupied == 37

num_occupied = find_occupied_seats_at_equilibrium(DATA, True)
assert num_occupied == 26


with open("data/day11.txt") as f:
    data = f.read()


num_occupied = find_occupied_seats_at_equilibrium(data)
print(num_occupied)


num_occupied = find_occupied_seats_at_equilibrium(data, True)
print(num_occupied)
