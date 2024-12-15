grid, moves = open("day15/day15_input.txt").read().strip().split("\n\n")

grid = [[i for i in row] for row in grid.split("\n")]

moves = moves.replace("\n", "")

def move(from_y, from_x, dy, dx):
    ny = from_y + dy
    nx = from_x + dx

    if grid[ny][nx] == '#':
        return False
    elif grid[ny][nx] == '.':
        grid[ny][nx], grid[from_y][from_x] = grid[from_y][from_x], grid[ny][nx]
        return True
    
    if move(ny, nx, dy, dx):
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
        if col == 'O':
            score += i * 100 + j




print(score)