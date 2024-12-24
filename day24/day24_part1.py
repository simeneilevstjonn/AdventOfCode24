initials, edges = open("day24/day24_input.txt").read().strip().split("\n\n")

class Node:
    def __init__(self, key):
        self.value = None
        self.key = key

        self.edges = []

    def add_edge(self, coorigin, destination, operator):
        self.edges.append((coorigin, destination, operator))

    def do_op(self, other, op):
        OPS = {
            "AND": lambda x, y : x.value & y.value,
            "OR": lambda x, y : x.value | y.value,
            "XOR": lambda x, y : x.value ^ y.value 
        }

        return OPS[op](self, other)

    def set_value(self, value):
        self.value = value

        for coorigin, destination, operator in self.edges:
            if destination.value is not None or coorigin.value is None:
                continue

            destination.set_value(self.do_op(coorigin, operator))


nodes = {}

def get_or_make_node(key):
    if key in nodes:
        return nodes[key]
    
    nodes[key] = Node(key)

    return nodes[key]


for el in edges.split("\n"):
    f0, o, f1, _, d = el.split()
    
    f0 = get_or_make_node(f0)
    f1 = get_or_make_node(f1)
    d = get_or_make_node(d)

    f0.add_edge(f1, d, o)
    f1.add_edge(f0, d, o)


for init in initials.split("\n"):
    node, value = init.split()
    node = node[:-1]
    value = int(value)

    get_or_make_node(node).set_value(value)

out = 0

for node in nodes.values():
    if node.key[0] == 'z':
        pos = int(node.key[1:])

        assert node.value is not None

        out |= (node.value << pos)

print(out)