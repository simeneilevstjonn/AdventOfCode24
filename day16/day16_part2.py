from heapq import heappush, heappop

grid = [list(row) for row in open("day16/day16_input.txt").read().strip().split("\n")]

for i, row in enumerate(grid):
    if "E" in row:
        ey = i
        ex = row.index("E")
    
    if "S" in row:
        sy = i
        sx = row.index("S")

def add_dir(y, x, dir):
    if dir == 0:
        return [y, x + 1]
    elif dir == 1:
        return [y + 1, x]
    elif dir == 2:
        return [y, x - 1]
    elif dir == 3:
        return [y - 1, x]
    
def inside(y, x):
    return y >= 0 and x >= 0 and y < len(grid) and x < len(grid[0])

def tracedup(trace):
    return [t[::] for t in trace]

distto = [[[2147483647] * 4 for _ in row] for row in grid]
inbestpath = [[False for _ in row] for row in grid]

heap = [[0, sy, sx, 0, []]]

while heap:
    score, y, x, direction, trace = heappop(heap)

    if score > distto[y][x][direction]:
        continue

    distto[y][x][direction] = score

    trace.append([y, x, direction])

    if y == ey and x == ex and score == min(distto[ey][ex]):
        for y, x, direction in trace:
            inbestpath[y][x] = True


    for i in range(-1, 3):
        nd = (direction + i) % 4
        ny, nx = add_dir(y, x, nd)

        nscore = score + 1 + 1000 * abs(i)

        if inside(ny, nx) and distto[ny][nx][nd] >= nscore and not grid[ny][nx] == "#" and not [ny, nx, nd] in trace:
            heappush(heap, [nscore, ny, nx, nd, tracedup(trace)])

print(sum(sum(r) for r in inbestpath))

# for i, row in enumerate(grid):
#     for j, col in enumerate(row):
#         if inbestpath[i][j]:
#             print("O", end="")
#         else:
#             print(col, end="")

#     print()