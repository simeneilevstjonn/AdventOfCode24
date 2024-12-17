import re

a, b, c, *ops = map(int, re.findall("\\d+", open("day17/day17_input.txt").read()))

pc = 0

outs = []

while pc < len(ops):
    op = ops[pc] 
    pc += 1

    literal = ops[pc]
    pc += 1

    combo = [0, 1, 2, 3, a, b, c, 7][literal]

    print(f"\nPC = {pc - 2}, operation {op}, literal {literal}, combo {combo}")

    if op == 0:
        a //= (1 << combo)
    elif op == 1:
        b ^= literal
    elif op == 2:
        b = combo % 8
    elif op == 3:
        if a:
            pc = literal
    elif op == 4:
        b ^= c
    elif op == 5:
        outs.append(combo % 8)
    elif op == 6:
        b = a // (1 << combo)
    elif op == 7:
        c = a // (1 << combo)

print(*outs, sep=",")