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

visited = [[[False] * 4 for _ in row] for row in grid]

heap = [[0, sy, sx, 0]]

while heap:
    score, y, x, direction = heappop(heap)

    if visited[y][x][direction]:
        continue

    if y == ey and x == ex:
        print(score)
        break

    visited[y][x][direction] = True

    for i in range(-1, 3):
        nd = (direction + i) % 4
        ny, nx = add_dir(y, x, nd)

        if inside(ny, nx) and not visited[ny][nx][nd] and not grid[ny][nx] == "#":
            heappush(heap, [score + 1 + 1000 * abs(i), ny, nx, nd])

