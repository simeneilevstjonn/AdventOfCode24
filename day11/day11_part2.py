# import networkx

stone_list = [int(i) for i in open("day11/day11_input.txt").read().split()]

stones = {}

ITERATION_COUNT = 75

def childdup(children):
    return [a[::] for a in children]

class Stone:
    def __init__(self, value):
        self.value = value

        self.proc_queue = [0] * (ITERATION_COUNT + 1)

        self.children = []
        self.children_proced = False
        self.has_inbound = False

    def make_children_recursive(self):
        if self.children_proced:
            return self.children

        # if stack and self == stack[0]:
        #     self.children_proced = True
        #     self.children = []
        #     return self.children
        
        # if len(stack) > 100:
        #     return []
        
        # stack.append(self)

        

        if self.value == 0:
            if 1 not in stones:
                stones[1] = Stone(1)
                stones[1].make_children_recursive()
            # self.children = childdup(stones[1].make_children_recursive())
            # for i in range(len(self.children)):
            #     self.children[i][0] += 1
            
            self.children = [[1, stones[1]]]

        elif len(str(self.value)) % 2 == 0:
            s = str(self.value)
            a = int(s[:len(s)//2])
            b = int(s[len(s)//2:])

            if a not in stones:
                stones[a] = Stone(a)
                stones[a].make_children_recursive()

            if b not in stones:
                stones[b] = Stone(b)
                stones[b].make_children_recursive()

            self.children = [[1,stones[a]], [1,stones[b]]]
            stones[a].has_inbound = True
            stones[b].has_inbound = True

        else:
            v = self.value * 2024

            if v not in stones:
                stones[v] = Stone(v)
                stones[v].make_children_recursive()
            # for i in range(len(self.children)):
            #     self.children[i][0] += 1

            self.children = [[1, stones[v]]]

        self.children_proced = True
        return self.children

    def proc_index(self, index):
        noreach = True

        # print("procing node", self.value, "at time", index)

        if not self.proc_queue[index] or not self.children_proced:
            # print("early return")
            return 0
        
        # print("procing node", self.value, "at time", index)

        for timeto, child in self.make_children_recursive():
            # print("has child", child.value, "timeto",timeto)
            if index >= timeto:
                # print("Can reach child", child.value, "time will be", index - timeto, "upon arrival, adding", self.proc_queue[index])
                child.proc_queue[index - timeto] += self.proc_queue[index]
                noreach = False
        # print()
        if noreach:
            # print("noreach!!, returning", self.proc_queue[index], "\n\n")
            return self.proc_queue[index]
        else:
            return 0


for stone in stone_list:
    if stone not in stones:
        stones[stone] = Stone(stone)
        stones[stone].make_children_recursive()

    stones[stone].proc_queue[ITERATION_COUNT] += 1
    stones[stone].has_inbound = True



# print("proceed all nodes")
print("length is", len(stones))

# keys = list(stones.keys())

# for k in keys:
#     if not stones[k].has_inbound:
#         stones.pop(k)

# print("length is", len(stones))

# g = networkx.DiGraph()

# for stone in stones.values():
#     for child in stone.children:
#         # g.add_edge(stone.value, child[1].value)
#         g.add_weighted_edges_from([(stone.value, child[1].value, child[0])])

# print("trying to draw")

# networkx.draw(g)
# import matplotlib.pyplot as plt

# plt.show()
s = 0
for i in list(range(ITERATION_COUNT + 1))[::-1]:
    for stone in stones.values():
        s += stone.proc_index(i)

print(s)