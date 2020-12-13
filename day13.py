from typing import List, Tuple, Optional


def parse_bus_with_shift(raw: str) -> List[Tuple[int, int]]:
    return [(i, int(bus)) for i, bus in enumerate(raw.split(",")) if bus != "x"]


TIMESTAMP = 939
BUSES = "7,13,x,x,59,x,31,19"
BUSES_WITH_SHIFT = parse_bus_with_shift(BUSES)
BUSES = [int(bus) for bus in BUSES.split(",") if bus != "x"]


def find_delay(timestamp: int, bus_id: int) -> int:

    remainder = timestamp % bus_id
    if remainder == 0:
        return 0

    return bus_id - remainder


def find_best_bus_times_delay(timestamp: int, buses: List[int]) -> int:
    delays = {}
    for bus_id in buses:
        delay = find_delay(timestamp, bus_id)
        delays[bus_id] = delay

    best_bus, best_delay = min(delays.items(), key=lambda x: x[1])
    return best_bus * best_delay


assert find_best_bus_times_delay(TIMESTAMP, BUSES) == 295


def find_earliest_timestamp_brute_force(buses_with_shift: List[Tuple[int, int]], first_to_try: Optional[int] = None) -> int:
    buses = [x[1] for x in buses_with_shift]
    shifts = [x[0] for x in buses_with_shift]

    max_shift, max_bus = max(buses_with_shift, key=lambda x: x[1])
    index_to_remove = buses.index(max_bus)

    shifts = [shift - max_shift for shift in shifts]
    first_shift = shifts[0]

    shifts.pop(index_to_remove)
    buses.pop(index_to_remove)

    timestamp = first_to_try or max_bus
    while True:

        if all((timestamp + shift) % bus == 0 for shift, bus in zip(shifts, buses)):
            return timestamp + first_shift

        timestamp += max_bus


earliest_timestamp = find_earliest_timestamp_brute_force(BUSES_WITH_SHIFT)
assert earliest_timestamp == 1068781

for timestamp, raw in (
    (3417, "17,x,13,19"),
    (754018, "67,7,59,61"),
    (779210, "67,x,7,59,61"),
    (1261476, "67,7,x,59,61"),
    (1202161486, "1789,37,47,1889")
):
    buses_with_shift = parse_bus_with_shift(raw)
    assert find_earliest_timestamp_brute_force(buses_with_shift) == timestamp


with open("data/day13.txt") as f:
    data = f.readlines()


timestamp = int(data[0].strip())
buses = [int(bus) for bus in data[1].strip().split(",") if bus != "x"]
print(find_best_bus_times_delay(timestamp, buses))


buses_with_shift = parse_bus_with_shift(data[1].strip())
max_bus = max(x[1] for x in buses_with_shift)
LARGE_NUMBER = 100000000000000
first_to_try = LARGE_NUMBER - LARGE_NUMBER % max_bus
print(find_earliest_timestamp_brute_force(buses_with_shift, first_to_try))
