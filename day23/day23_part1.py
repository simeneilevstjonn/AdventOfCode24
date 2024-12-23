import networkx as nx

edges = [i.split("-") for i in open("day23/day23_input.txt").read().split("\n")]

graph = nx.Graph()

for u, v in edges:
    graph.add_edge(u, v)

cnt = 0

for clique in nx.enumerate_all_cliques(graph):
    if len(clique) < 3:
        continue

    if len(clique) > 3:
        break

    bt = sum(i[0] == 't' for i in clique)

    cnt += bt > 0

print(cnt)