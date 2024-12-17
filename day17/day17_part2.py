import re

a, b, c, *ops = map(int, re.findall("\\d+", open("day17/day17_input.txt").read()))

def simulate(opidx, a):
    if opidx < 0:
        return a

    bmod8 = ops[opidx]
    found = 0
    for bposs in range(8):
        awouldbe = (a << 3) | bposs

        b = bposs
        b ^= 2
        c = awouldbe >> b
        b ^= 3
        b ^= c

        if b % 8 == bmod8:
            # a = awouldbe
            found += 1

            rtn = simulate(opidx - 1, awouldbe)
            if rtn != -1:
                return rtn
            
    return -1

print(simulate(len(ops) - 1, 0))