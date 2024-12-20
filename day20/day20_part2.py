grid = [list(row) for row in open("day20/day20_dummy.txt").read().strip().split("\n")]

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


def dfsdiscover(y, x, dist, depth=0):
    if depth > 20:
        return
    if dist[y][x] < depth:
        return
    
    dist[y][x] = depth

    if depth > 0 and grid[y][x] != '#':
        return

    for ny, nx in [[y - 1, x], [y + 1, x], [y, x - 1], [y, x + 1]]:
        if inside(ny, nx):
            dfsdiscover(ny, nx, dist, depth + 1)


SAVE_THRESH = 50
above_thresh = 0

ot = []

def manhattan(y, x, i, j):
    return abs(y - i) + abs(x - j)

start_to_end_trace = traceto[sy][sx][::-1]

for i in range(len(start_to_end_trace) - 1):
    y, x = start_to_end_trace[i]

    for oy, ox in start_to_end_trace[i + 1:]:
        d = manhattan(y, x, oy, ox)
        if d > 20:
            continue
        
        dold = len(traceto[y][x])
        dnew = len(traceto[oy][ox]) + d

        delta = dold - dnew

        if delta > SAVE_THRESH:
            above_thresh += 1
            ot.append(delta)


       
for delta in sorted([*set(ot)]):
    print("There are", ot.count(delta), "cheats that save", delta, "picoseconds.")


print(above_thresh)



