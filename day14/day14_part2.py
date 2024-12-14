import re

robots = [[*map(int, re.findall("-?\\d+", row))] for row in open("day14/day14_input.txt").read().strip().split("\n")]

WIDTH = 101
HEIGHT = 103

its = 1
while True:
    grid = [[0] * WIDTH for _ in range(HEIGHT)]
    i = 0
    for rx, ry, vx, vy in robots:
        rx += vx
        rx %= WIDTH
        ry += vy
        ry %= HEIGHT

        robots[i][0] = rx
        robots[i][1] = ry

        i += 1

        grid[ry][rx] += 1

    m = sum(sum(i for i in row if i > 1) for row in grid)

    if m:
        its += 1
        continue

    for r in grid:
        print("".join([str(i) if i > 0 else "." for i in r]))

    print(its)
    its += 1

    print()
    print()
    input()