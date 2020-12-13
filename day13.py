from typing import List


TIMESTAMP = 939
BUSES = "7,13,x,x,59,x,31,19"
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


with open("data/day13.txt") as f:
    data = f.readlines()


timestamp = int(data[0].strip())
buses = [int(bus) for bus in data[1].strip().split(",") if bus != "x"]
print(find_best_bus_times_delay(timestamp, buses))
