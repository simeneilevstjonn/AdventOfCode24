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

for secret in secrets:
    print("Secret", secret, end=", new is: ")
    for _ in range(2000):
        secret = next_secret(secret)
    print(secret)

    sums += secret

print(sums)