from typing import Dict, Set, Optional
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

AdjList = Dict[str, Set[str]]


def get_adj_list(raw: str) -> AdjList:
    adj_list = defaultdict(set)

    for rule in raw.split("\n"):
        vertex, nodes = rule.split(" bags contain ")

        if not nodes.startswith("no other"):
            for node in nodes.split(","):
                node = " ".join(node.split()[1:3])
                adj_list[vertex].update([node])
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


adj_list = get_adj_list(DATA)
assert len(get_all_parents(adj_list, "shiny gold")) - 1 == 4

with open("data/day07.txt") as f:
    data = f.read()
    adj_list = get_adj_list(data)
    print(len(get_all_parents(adj_list, "shiny gold")) - 1)
