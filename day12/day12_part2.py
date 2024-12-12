grid = open("day12/day12_input.txt").read().strip().split("\n")

def rgb(r,g,b): return "\x1b[38;2;%i;%i;%im"%(r,g,b)

import random
def rrgb():
    return rgb(*map(int,random.randbytes(3)))

class UnionFindEntry:
    def __init__(self, y, x):
        self.parent = self
        self.set_size = 1

        self.perimeter = 0
        self.type = grid[y][x]

        self.has_perim = [False] * 4

        self.colour = rrgb()

        i = 0
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny = y + dy
            nx = x + dx

            if ny >= 0 and ny < len(grid) and nx >= 0 and nx < len(grid[0]):
                self.perimeter += self.type != grid[ny][nx]
                self.has_perim[i] = self.type != grid[ny][nx]
            else:
                self.perimeter += 1
                self.has_perim[i] = True

            i += 1

    def find(self):
        if self.parent == self:
            return self
        
        self.parent = self.parent.find()

        return self.parent
    
    def union(self, other, direction):
        pself = self.find()
        pother = other.find()

        if direction == 'x':
            if (self.has_perim[0] and other.has_perim[0]):
                self.find().perimeter -= 1
                # print(self.type, "0")
            if (self.has_perim[1] and other.has_perim[1]):
                self.find().perimeter -= 1
                # print(self.type, "1")


        elif direction == 'y':
            if (self.has_perim[2] and other.has_perim[2]):
                self.find().perimeter -= 1
                # print(self.type, "2")
            if (self.has_perim[3] and other.has_perim[3]):
                self.find().perimeter -= 1
                # print(self.type, "3")

        if pself == pother:
            return

        if pother.set_size > pself.set_size:
            pother.set_size += pself.set_size
            pother.perimeter += pself.perimeter

            pself.parent = pother
        else:
            pself.set_size += pother.set_size
            pself.perimeter += pother.perimeter

            pother.parent = pself

    def try_union(self, other, direction):
        if self.type == other.type:
            self.union(other, direction)

entries = []

for i, row in enumerate(grid):
    entry_row = []
    for j, col in enumerate(row):
        entry = UnionFindEntry(i, j)
        entry_row.append(entry)

        if j > 0:
            entry.try_union(entry_row[j - 1], 'x')
        
        if i > 0:
            entry.try_union(entries[i - 1][j], 'y')


    entries.append(entry_row)

cost = 0

for row in entries:
    for entry in row:
        if entry.parent == entry:
            cost += entry.perimeter * entry.set_size
            

        # print(entry.find().colour + entry.type, end="")

    # print()

# for row in entries:
#     for entry in row:
#         if entry.parent == entry:
#             print(f"Region of {entry.type}, perimeter {entry.perimeter}, area {entry.set_size}")

print(cost)

# for row in entries:
#     for entry in row:
#         print(bin(sum(1 << i if entry.has_perim[i] else 0 for i in range(4)))[2:], end=" ")

    # print()