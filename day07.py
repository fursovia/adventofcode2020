from typing import Dict, Set, Optional, Union, Tuple
from collections import defaultdict

DATA = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

DATA2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

AdjList = Dict[str, Union[Set[str], Set[Tuple[int, str]]]]


def get_adj_list(raw: str, include_numbers: bool = False) -> AdjList:
    adj_list = defaultdict(set)

    for rule in raw.split("\n"):
        vertex, nodes = rule.split(" bags contain ")

        if not nodes.startswith("no other"):
            for node in nodes.split(","):
                splitted = node.split()
                num = int(splitted[0])
                node = " ".join(splitted[1:3])

                if include_numbers:
                    adj_list[vertex].add((num, node))
                else:
                    adj_list[vertex].add(node)
        else:
            adj_list[vertex] = set()

    return dict(adj_list)


def get_all_parents(graph: AdjList, start: str, visited: Optional[Set[str]] = None):
    if visited is None:
        visited = set()
    visited.add(start)

    for vertex, nodes in graph.items():
        if start in nodes:
            get_all_parents(graph, vertex, visited)

    return visited


def get_num_bags(graph: AdjList, start: str, num_bags: Optional[int] = None):

    num_bags = num_bags or 0

    for num, node in graph[start]:
        num_bags += num
        num_bags += num * get_num_bags(graph, node, 0)

    return num_bags


adj_list = get_adj_list(DATA)
assert len(get_all_parents(adj_list, "shiny gold")) - 1 == 4

adj_list = get_adj_list(DATA, include_numbers=True)
num_bags = get_num_bags(adj_list, "shiny gold")
assert num_bags == 32


adj_list = get_adj_list(DATA2, include_numbers=True)
num_bags = get_num_bags(adj_list, "shiny gold")
assert num_bags == 126


with open("data/day07.txt") as f:
    data = f.read()
    adj_list = get_adj_list(data)
    print(len(get_all_parents(adj_list, "shiny gold")) - 1)

    adj_list = get_adj_list(data, include_numbers=True)
    num_bags = get_num_bags(adj_list, "shiny gold")
    print(num_bags)
