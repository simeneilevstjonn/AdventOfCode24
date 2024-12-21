from heapq import heappop, heappush

codes = open("day21/day21_input.txt").read().strip().split("\n")

keypad_vertices = []

def layer_to_coords(layer):
    return [
        [0, 1],
        [1, 2],
        [1, 1],
        [1, 0],
        [0, 2]
    ][layer]

def coords_to_layer(coords):
    return [
        [0, 1],
        [1, 2],
        [1, 1],
        [1, 0],
        [0, 2]
    ].index(coords)


def manhattan(y, x, i, j):
    return abs(y - i) + abs(x - j)

class KeypadVertex:
    def __init__(self, y, x, layer, depth):
        self.y = y
        self.x = x
        self.layer = layer
        self.depth = depth

        self.value = [
            " ^A",
            "<v>",
        ][y][x]

        self.edges = []

    def djikstra_reset(self):
        self.distance = 0
        self.visited = False

    def __lt__(self, other):
        return False

    def init_edges(self):
        # layers: 0: up, 1: right, 2: down, 3: left, 4: activate

        if self.layer == 0:
            if self.y > 0 and not (self.y == 1 and self.x == 0):
                self.edges.append([1, keypad_vertices[self.depth][self.y - 1][self.x][self.layer]])
        elif self.layer == 1:
            if self.x < 2:
                self.edges.append([1, keypad_vertices[self.depth][self.y][self.x + 1][self.layer]])
        elif self.layer == 2:
            if self.y < 1:
                self.edges.append([1, keypad_vertices[self.depth][self.y + 1][self.x][self.layer]])
        elif self.layer == 3:
            if self.x > 0 and not (self.y == 0 and self.x == 1):
                self.edges.append([1, keypad_vertices[self.depth][self.y][self.x - 1][self.layer]])

        for other_layer in range(5):
            if other_layer == self.layer:
                continue
            
            if self.depth == 0:
                self.edges.append([manhattan(*layer_to_coords(self.layer), *layer_to_coords(other_layer)), keypad_vertices[self.depth][self.y][self.x][other_layer]])
            else:
                d = numpad_layer_trans[self.layer][other_layer]
                self.edges.append([d, keypad_vertices[self.depth][self.y][self.x][other_layer]])


NUMBER_OF_INTERMEDIATE_NUMPADS = 25

keypad_vertices = [[[[KeypadVertex(i, j, k, d) for k in range(5)] for j in range(3)] for i in range(2)] for d in range(NUMBER_OF_INTERMEDIATE_NUMPADS - 1)]

for layer in range(NUMBER_OF_INTERMEDIATE_NUMPADS - 1):
    keypad_vertices_as_list = []

    for plane in keypad_vertices[layer]:
        for row in plane:
            for col in row:
                col.init_edges()
                keypad_vertices_as_list.append(col)

    numpad_layer_trans = [[2147483647] * 5 for _ in range(5)]

    def keypad_djikstra(f, to):
        heap = [[0, f]]

        while heap:
            dist, vertex = heappop(heap)

            if vertex.visited:
                continue

            vertex.distance = dist
            vertex.visited = True

            if vertex == to:
                return dist

            for el, et in vertex.edges:
                if et.visited:
                    continue

                
                heappush(heap, [dist + el, et])

        assert False

    for first in keypad_vertices_as_list:
        if first.layer != 4 or first.value == " ":
            continue
        for second in keypad_vertices_as_list:
            if first == second or second.layer != 4 or second.value == " ":
                continue

            for v in keypad_vertices_as_list:
                v.djikstra_reset()

            l = keypad_djikstra(first, second)

            numpad_layer_trans[coords_to_layer([first.y, first.x])][coords_to_layer([second.y, second.x])] = l



numpad_vertices = []


class NumpadVertex:
    def __init__(self, y, x, layer):
        self.y = y
        self.x = x
        self.layer = layer

        self.value = [
            "789",
            "456",
            "123",
            " 0A"
        ][y][x]

        self.edges = []

    def djikstra_reset(self):
        self.distance = 0
        self.visited = False

    def __lt__(self, other):
        return False

    def init_edges(self):
        # layers: 0: up, 1: right, 2: down, 3: left, 4: activate

        if self.layer == 0:
            if self.y > 0:
                self.edges.append([1, numpad_vertices[self.y - 1][self.x][self.layer]])
        elif self.layer == 1:
            if self.x < 2:
                self.edges.append([1, numpad_vertices[self.y][self.x + 1][self.layer]])
        elif self.layer == 2:
            if self.y < 3 and not (self.x == 0 and self.y == 2):
                self.edges.append([1, numpad_vertices[self.y + 1][self.x][self.layer]])
        elif self.layer == 3:
            if self.x > 0 and not (self.y == 3 and self.x == 1):
                self.edges.append([1, numpad_vertices[self.y][self.x - 1][self.layer]])

        for other_layer in range(5):
            if other_layer == self.layer:
                continue

            self.edges.append([numpad_layer_trans[self.layer][other_layer], numpad_vertices[self.y][self.x][other_layer]])

numpad_vertices = [[[NumpadVertex(i, j, k) for k in range(5)] for j in range(3)] for i in range(4)]

numpad_vertices_as_list = []

for plane in numpad_vertices:
    for row in plane:
        for col in row:
            col.init_edges()
            numpad_vertices_as_list.append(col)

def numpad_vertex_djikstra(f, to):
    for v in numpad_vertices_as_list:
        v.djikstra_reset()

    heap = [[0, f]]

    while heap:
        dist, vertex = heappop(heap)

        if vertex.visited:
            continue

        vertex.visited = True
        vertex.distance = dist

        if vertex == to:
            return dist

        for el, et in vertex.edges:
            if et.visited:
                continue

            heappush(heap, [dist + el, et])

    assert False

complex = 0

def code_to_vertex(code):
    if code == '7':
        return numpad_vertices[0][0][4]
    elif code == '8':
        return numpad_vertices[0][1][4]
    elif code == '9':
        return numpad_vertices[0][2][4]
    elif code == '4':
        return numpad_vertices[1][0][4]
    elif code == '5':
        return numpad_vertices[1][1][4]
    elif code == '6':
        return numpad_vertices[1][2][4]
    elif code == '1':
        return numpad_vertices[2][0][4]
    elif code == '2':
        return numpad_vertices[2][1][4]
    elif code == '3':
        return numpad_vertices[2][2][4]
    elif code == '0':
        return numpad_vertices[3][1][4]
    elif code == 'A':
        return numpad_vertices[3][2][4]        

for code in codes:
    last = code_to_vertex('A')

    count = 0

    for c in code:
        v = code_to_vertex(c)

        count += numpad_vertex_djikstra(last, v) + 1

        last = v

    complex += count * int(code[:-1])

print(complex)