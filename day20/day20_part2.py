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



atomic_cheats = [[[] for _ in r] for r in grid]

for i, (y, x) in enumerate(traceto[sy][sx]):
   print("processing", y, x)
   dist = [[2147483647] * len(r) for r in grid]

   dfsdiscover(y, x, dist, 0)

   for k, (drow, grow) in enumerate(zip(dist, grid)):
       for j, (dc, gc) in enumerate(zip(drow, grow)):
            if gc == "#" or dc == 2147483647:
                continue

            distto = len(traceto[k][j]) - 1

            distbetween = i - distto

            delta = distbetween - dc

            if delta > 0:
                atomic_cheats[y][x].append([k, j, dc])
            
#            distto = len(traceto[k][j]) - 1

#            distbetween = i - distto

#            delta = distbetween - dc

#            above_thresh += delta >= SAVE_THRESH

#            if delta >= SAVE_THRESH:
#                ot.append(delta)


def cheat_combine(y, x, out_cheats = [], depth_left=20, length_add=0):
    def append_or_update(y, x, l):
        found = False
        for i in range(len(out_cheats)):
            if out_cheats[i][0] == y and out_cheats[i][1] == x:
                found = True
                out_cheats[i][2] = min(out_cheats[i][2], l)
                break

        if not found:
            out_cheats.append([y, x, l])

        

    for cy, cx, length in atomic_cheats[y][x]:
        if length < depth_left:
            append_or_update(cy, cx, length + length_add)

            cheat_combine(cy, cx, out_cheats, depth_left - length, length + length_add)

    return out_cheats

SAVE_THRESH = 50
above_thresh = 0

ot = []

for i, (y, x) in enumerate(traceto[sy][sx]):
    for cy, cx, length in cheat_combine(y, x):
        dist_between = i - (len(traceto[cy][cx]) - 1)
        
        delta = dist_between - length

        if delta >= SAVE_THRESH:
            ot.append(delta)
            above_thresh += 1

       
# print(ot)

for delta in sorted([*set(ot)]):
    print("There are", ot.count(delta), "cheats that save", delta, "picoseconds.")


print(above_thresh)



