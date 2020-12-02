from typing import List

DATA = [
    1721,
    979,
    366,
    299,
    675,
    1456
]


def multiple_2020_sumup(data: List[int]) -> int:

    for i in range(len(data)):
        for j in range(len(data)):
            if i > j:
                sumup = data[i] + data[j]
                if sumup == 2020:
                    return data[i] * data[j]

    raise ValueError('did not find any')


assert multiple_2020_sumup(DATA) == 514579


def multiple3_2020_sumup(data: List[int]) -> int:

    for i in range(len(data)):
        for j in range(len(data)):
            for k in range(len(data)):
                if i > j > k:
                    sumup = data[i] + data[j] + data[k]
                    if sumup == 2020:
                        return data[i] * data[j] * data[k]

    raise ValueError('did not find any')


assert multiple3_2020_sumup(DATA) == 241861950


with open('day01/data.txt') as f:
    competition_data = f.readlines()
    competition_data = list(map(int, competition_data))
    print(multiple_2020_sumup(competition_data))
    print(multiple3_2020_sumup(competition_data))
