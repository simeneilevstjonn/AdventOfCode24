grid = open("day10/day10_input.txt", "r").read().strip().split("\n")

grid = [[int(i) for i in row] for row in grid]

def dfs_climb(height, y, x, vis):
    if vis[y][x]:
        return 0
    
    vis[y][x] = True

    if height == 9:
        return 1
    
    peaks = 0

    if y > 0 and grid[y - 1][x] - 1 == height:
        peaks += dfs_climb(height + 1, y - 1, x, vis)

    if x > 0 and grid[y][x - 1] - 1 == height:
        peaks += dfs_climb(height + 1, y, x - 1, vis)

    if x < len(grid[0]) - 1 and grid[y][x + 1] - 1 == height:
        peaks += dfs_climb(height + 1, y, x + 1, vis)

    if y < len(grid) - 1 and grid[y + 1][x] - 1 == height:
        peaks += dfs_climb(height + 1, y + 1, x, vis)

    return peaks

s = 0

for i, row in enumerate(grid):
    for j, h in enumerate(row):
        if h == 0:
            vis = [[False] * len(grid[0]) for _ in grid]
            sc = dfs_climb(0, i, j, vis)
            # print(f"trailhead at {i}, {j} has score {sc}")
            s += sc

print(s)