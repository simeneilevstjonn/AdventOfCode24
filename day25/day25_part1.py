schematics = open("day25/day25_input.txt").read().strip().split("\n\n")

keys = [*filter(lambda x : x[0] == '.', schematics)]
locks = [*filter(lambda x : x[0] == '#', schematics)]

def non_overlap(key, lock):
    for k, l in zip(key, lock):
        if k == l and k == "#":
            return False
        
    return True

nonoverlapping = 0


for key in keys:
    for lock in locks:
        nonoverlapping += non_overlap(key, lock)

print(nonoverlapping)