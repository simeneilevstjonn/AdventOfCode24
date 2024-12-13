import re

data = [map(int, re.findall("\\d+", lines)) for lines in open("day13/day13_input.txt").read().strip().split("\n\n")]

total_cost = 0

for ax, ay, bx, by, px, py in data:
    maxb = max(px // bx, py // by)

    for b_times in [*range(maxb + 1)][::-1]:
        remx = px - b_times * bx
        remy = py - b_times * by

        if remx % ax == 0 and remy % ay == 0 and remx // ax == remy // ay:
            total_cost += b_times + 3 * (remx // ax)
            break


print(total_cost)
            