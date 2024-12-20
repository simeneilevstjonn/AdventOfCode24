grid = [list(row) for row in open("day20/day20_input.txt").read().strip().split("\n")]

for i, row in enumerate(grid):
    if "E" in row:
        ey = i
        ex = row.index("E")
    
    if "S" in row:
        sy = i
        sx = row.index("S")
    
def inside(y, x):
    return y >= 0 and x >= 0 and y < len(grid) and x < len(grid[0])

traceto = [[[] for _ in r] for r in grid]

queue = [[ey, ex, []]]

while queue:
    y, x, trace = queue.pop(0)

    trace.append([y,x])

    if len(traceto[y][x]) > 0 and len(traceto[y][x]) <= len(trace):
        continue

    traceto[y][x] = trace

    for ny, nx in [[y - 1, x], [y + 1, x], [y, x - 1], [y, x + 1]]:
        if not inside(ny, nx) or (len(traceto[ny][nx]) > 0 and len(traceto[ny][nx]) + 1 <= len(trace)) or grid[ny][nx] == '#':
            continue

        queue.append([ny, nx, trace[::]])

# print(len(traceto[sy][sx]))

def dfs_find_all(y, x, steps=2):
    if steps == 0:
        if traceto[y][x]:
            return [len(traceto[y][x])]
        else:
            return []

    rtn = []

    for ny, nx in [[y - 1, x], [y + 1, x], [y, x - 1], [y, x + 1]]:
        if not inside(ny, nx):
            continue
    
        rtn += dfs_find_all(ny, nx, steps - 1)

    return rtn

SAVE_THRESH = 100
above_thresh = 0

for i, (y, x) in enumerate(traceto[sy][sx]):
    all = dfs_find_all(y, x)


    # if lowest > i + 1:
    #     print("Lowest is greater, skipping")
    #     continue

    for lowest in all:
        delta = i - lowest - 1
        # if delta > 0:
            # print("Cheating from", y, x, "dist", i, "would be from dist", lowest - 1)
            # print("Delta would then be", delta)

        above_thresh += delta >= SAVE_THRESH

print(above_thresh)



