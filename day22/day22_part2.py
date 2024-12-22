secrets = [*map(int, open("day22/day22_input.txt").read().split())]

def next_secret(secret):
    secret ^= (secret << 6)
    secret %= 16777216

    secret ^= (secret >> 5)
    secret %= 16777216

    secret ^= (secret << 11)
    secret %= 16777216

    return secret

sums = 0

sequences = []

for secret in secrets:
    # print("Secret", secret, end=", new is: ")
    seq = [secret % 10]
    for _ in range(2000):
        secret = next_secret(secret)
        seq.append(secret % 10)

    sequences.append(seq)

    # print(secret)

allkeys = set()

all_delta_seqs = []

for sequence in sequences:
    delta_seqs = {}

    for i in range(len(sequence) - 4):
        pseq = sequence[i:i+5]
        assert len(pseq) == 5

        deltaseq = [0] * 4
        for j in range(len(pseq) - 1):
            deltaseq[j] = pseq[j + 1] - pseq[j]

        key = str(deltaseq)

        price = pseq[-1]

        if key in delta_seqs:
            continue
        else:
            delta_seqs[key] = price

        allkeys.add(key)

    all_delta_seqs.append(delta_seqs)

maxval = 0
maxkey = ""

for key in allkeys:
    cur_val = 0
    for ds in all_delta_seqs:
        if key in ds:
            cur_val += ds[key]
    
    if cur_val > maxval:
        maxval = cur_val
        maxkey = key

print(maxval)
print(maxkey)