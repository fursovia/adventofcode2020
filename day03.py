from typing import NamedTuple, Tuple, List
import operator
from functools import reduce


FOREST = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
ANGLE = (1, 3)


class Forest(NamedTuple):
    num_rows: int
    num_cols: int
    trees: List[Tuple[int, int]]
    trajectory_angle: Tuple[int, int]
    starting_point: Tuple[int, int] = (0, 0)

    def is_encountered(self, x: int, y: int) -> bool:
        return (x, y % self.num_cols) in self.trees

    def get_trajectory(self):
        trajectory: List[Tuple[int, int]] = [self.starting_point]
        while True:
            new_point = (trajectory[-1][0] + self.trajectory_angle[0], trajectory[-1][1] + self.trajectory_angle[1])
            trajectory.append(new_point)
            if new_point[0] >= (self.num_rows - 1):
                break

        return trajectory

    @classmethod
    def from_rows(cls, rows: List[str], trajectory_angle: Tuple[int, int]) -> "Forest":
        num_rows = len(rows)
        num_cols = len(rows[0])

        trees = []
        for i, row in enumerate(rows):
            for j, coordinate in enumerate(row):
                if coordinate == "#":
                    # (row, col)
                    trees.append((i, j))

        return cls(num_rows=num_rows, num_cols=num_cols, trees=trees, trajectory_angle=trajectory_angle)


def get_num_encountered(rows: List[str], angle: Tuple[int, int]) -> int:
    forest = Forest.from_rows(rows, angle)
    trajectory = forest.get_trajectory()
    encountered = [forest.is_encountered(*coord) for coord in trajectory]
    return sum(encountered)


assert get_num_encountered(FOREST.split("\n"), ANGLE) == 7

ANGLES = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

nums = []
for angle in ANGLES:
    nums.append(get_num_encountered(FOREST.split("\n"), angle))

assert reduce(operator.mul, nums, 1) == 336


with open("data/day03.txt") as f:
    rows = f.read().split("\n")
    num_encountered = get_num_encountered(rows, ANGLE)
    print(num_encountered)

    nums = []
    for angle in ANGLES:
        nums.append(get_num_encountered(rows, angle))

    print(reduce(operator.mul, nums, 1))
