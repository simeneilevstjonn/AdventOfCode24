grid, moves = open("day15/day15_input.txt").read().strip().split("\n\n")

grid = [[i for i in row.replace("#","##").replace("O","[]").replace(".","..").replace("@","@.")] for row in grid.split("\n")]

moves = moves.replace("\n", "")

def move(from_y, from_x, dy, dx, dry=False):
    ny = from_y + dy
    nx = from_x + dx

    if grid[ny][nx] == '#':
        return False
    elif grid[ny][nx] == '.':
        if not dry:
            grid[ny][nx], grid[from_y][from_x] = grid[from_y][from_x], grid[ny][nx]
        return True
    
    if dy == 0 or not (grid[ny][nx] in "[]"):
        if move(ny, nx, dy, dx):
            if not dry:
                grid[ny][nx], grid[from_y][from_x] = grid[from_y][from_x], grid[ny][nx]
            return True
    else:
        dir = 1 if grid[ny][nx] == "[" else -1
        if move(ny, nx, dy, dx, dry=True) and move(ny, nx + dir, dy, dx, dry=True):
            if not dry:
                move(ny, nx, dy, dx)
                move(ny, nx + dir, dy, dx)
                grid[ny][nx], grid[from_y][from_x] = grid[from_y][from_x], grid[ny][nx]
            return True
                    
    return False
    

robot_y = 0
robot_x = 0

for i, row in enumerate(grid):
    try:
        robot_x = row.index('@')
        robot_y = i
        break
    except:
        pass

print(robot_y, robot_x)

for m in moves:
    if m == "<":
        if move(robot_y, robot_x, 0, -1):
            robot_x -= 1
    elif m == ">":
        if move(robot_y, robot_x, 0, 1):
            robot_x += 1
    elif m == "^":
        if move(robot_y, robot_x, -1, 0):
            robot_y -= 1
    elif m == "v":
        if move(robot_y, robot_x, 1, 0):
            robot_y += 1

score = 0

for i, row in enumerate(grid):
    print("".join(row))
    for j, col in enumerate(row):
        if col == '[':
            score += i * 100 + j




print(score)