from typing import NamedTuple, Tuple, List


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


forest = Forest.from_rows(FOREST.split("\n"), ANGLE)
trajectory = forest.get_trajectory()
num_encountered = sum([forest.is_encountered(*coord) for coord in trajectory])
assert num_encountered == 7


with open("data/day03.txt") as f:
    rows = f.read().split("\n")
    forest = Forest.from_rows(rows, ANGLE)
    trajectory = forest.get_trajectory()
    encountered = [forest.is_encountered(*coord) for coord in trajectory]
    num_encountered = sum(encountered)
    print(num_encountered)


