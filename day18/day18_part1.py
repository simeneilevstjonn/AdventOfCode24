import sys
sys.setrecursionlimit(10000000)

corruptions = [[int(i) for i in j.split(",")] for j in open("day18/day18_input.txt").read().strip().split("\n")]

GRID_DIM = 71
LIMIT = 1024


blocked = [[False] * GRID_DIM for _ in range(GRID_DIM)]
dist = [[2147483647] * GRID_DIM for _ in range(GRID_DIM)]


for x, y in corruptions[:LIMIT]:
    blocked[x][y] = True

    
# for row in blocked:
#     print(*[".#"[i] for i in row], sep="")

dist[0][0] = 0

def dfs(x, y):  
    for nx, ny in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
        if ny < 0  or ny >= GRID_DIM or nx < 0 or nx >= GRID_DIM:
            continue

        if blocked[nx][ny]:
            continue

        if dist[nx][ny] - 1 > dist[x][y]:
            dist[nx][ny] = dist[x][y] + 1
            dfs(nx, ny)

dfs(0, 0)

print(dist[-1][-1])