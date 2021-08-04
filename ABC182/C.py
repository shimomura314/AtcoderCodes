from itertools import combinations

n = str(input())

multis = []
for num in range(1, len(n)+1):
    for pair in combinations(n, num):
        x = int("".join(pair))
        if x % 3 == 0:
            multis.append(x)

if multis == []:
    print(-1)
    exit()

multis.sort()
print(len(n)-len(str(multis[-1])))
