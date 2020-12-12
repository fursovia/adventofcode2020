from dataclasses import dataclass
from typing import List, Tuple
from collections import OrderedDict


RAW = """F10
N3
F7
R90
F11"""


CARDINAL_MAPPING = OrderedDict(
    {
        "N": (0, +1),
        "E": (-1, 0),
        "S": (0, -1),
        "W": (+1, 0),
    }
)
DIRECTIONS = list(CARDINAL_MAPPING.values())


@dataclass
class Navigation:
    actions: List[str]
    current_direction: Tuple[int, int] = (-1, 0)
    current_position: Tuple[int, int] = (0, 0)

    def move(self):
        for action in self.actions:
            value = int(action[1:])
            if action.startswith("R") or action.startswith("L"):
                self.change_direction(action)
                continue
            elif action.startswith("F"):
                direction = self.current_direction
            else:
                direction = CARDINAL_MAPPING[action[0]]

            to_step = tuple(di * value for di in direction)
            self.current_position = tuple(map(sum, zip(self.current_position, to_step)))

    def change_direction(self, action: str):
        turn, degrees = action[0], int(action[1:])
        assert turn == "L" or turn == "R"
        num_rotations = int(degrees / 90)
        if turn == "L":
            num_rotations = -num_rotations

        current_index = DIRECTIONS.index(self.current_direction)
        self.current_direction = DIRECTIONS[(current_index + num_rotations) % 4]

    def get_distance(self) -> int:
        return abs(self.current_position[0]) + abs(self.current_position[1])


navigation = Navigation(RAW.split("\n"))
navigation.move()
assert navigation.get_distance() == 25


with open("data/day12.txt") as f:
    data = f.read().split("\n")

navigation = Navigation(data)
navigation.move()
distance = navigation.get_distance()
print(distance)
