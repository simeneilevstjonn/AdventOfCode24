import re
from math import lcm
import numpy as np

data = [map(int, re.findall("\\d+", lines)) for lines in open("day13/day13_input.txt").read().strip().split("\n\n")]

total_cost = 0

def int_and_round(number):
    return int(np.round(number))

for ax, ay, bx, by, px, py in data:
    px += 10000000000000
    py += 10000000000000

    A = np.array([[ax, bx], [ay, by]])
    B = np.array([px, py])

    a_times, b_times = map(int_and_round, np.linalg.solve(A, B))

    if a_times * ax + b_times * bx == px and a_times * ay + b_times * by == py:
        total_cost += b_times + 3 * a_times
        # print("Completed one")
    # else:
        # print("not possible")


print(total_cost)
            