stones = [int(i) for i in open("day11/day11_input.txt").read().split()]

def recurse_count(stones, depth):
    # print(f"At depth {depth} stone arrangement is {stones}")
    if depth == 0:
        return len(stones)
    
    newstones = []

    for stone in stones:
        if stone == 0:
            newstones.append(1)
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            a = s[:len(s)//2]
            b = s[len(s)//2:]

            newstones.append(int(a))
            newstones.append(int(b))
        else:
            newstones.append(stone * 2024)

    return recurse_count(newstones, depth - 1)


print(sum(recurse_count([stone], 25) for stone in stones))
        