import re

robots = [map(int, re.findall("-?\\d+", row)) for row in open("day14/day14_input.txt").read().strip().split("\n")]

WIDTH = 101
HEIGHT = 103
# WIDTH = 11
# HEIGHT = 7
SIMULATE_TIME = 100


grid = [[0] * WIDTH for _ in range(HEIGHT)]

for rx, ry, vx, vy in robots:
    rx += vx * SIMULATE_TIME
    rx %= WIDTH
    ry += vy * SIMULATE_TIME
    ry %= HEIGHT

    grid[ry][rx] += 1

q1 = sum(sum(row[:WIDTH//2]) for row in grid[:HEIGHT//2])
q2 = sum(sum(row[:WIDTH//2]) for row in grid[-HEIGHT//2+1:])
q3 = sum(sum(row[-WIDTH//2+1:]) for row in grid[:HEIGHT//2])
q4 = sum(sum(row[-WIDTH//2+1:]) for row in grid[-HEIGHT//2+1:])

# for row in grid[:HEIGHT//2]:
#     print("".join([str(i) if i > 0 else "." for i in row[:WIDTH//2]]))
# print()

# for row in grid[:HEIGHT//2]:
#     print("".join([str(i) if i > 0 else "." for i in row[-WIDTH//2+1:]]))
# print()

# for row in grid[-HEIGHT//2+1:]:
#     print("".join([str(i) if i > 0 else "." for i in row[:WIDTH//2]]))
# print()

# for row in grid[-HEIGHT//2+1:]:
#     print("".join([str(i) if i > 0 else "." for i in row[-WIDTH//2+1:]]))
# print()



# print(q1, q2, q3, q4)

# for r in grid:
#     print("".join([str(i) if i > 0 else "." for i in r]))

p = q1 * q2 * q3 * q4
print(p)