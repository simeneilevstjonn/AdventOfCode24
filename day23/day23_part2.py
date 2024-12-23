import networkx as nx

edges = [i.split("-") for i in open("day23/day23_input.txt").read().split("\n")]

graph = nx.Graph()

for u, v in edges:
    graph.add_edge(u, v)

cliques = nx.find_cliques(graph)

mq = max(cliques, key = len)

print(*sorted(mq), sep=",")