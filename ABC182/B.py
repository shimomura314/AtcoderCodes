n = int(input())
a = list(map(int, input().split()))

answer = 0
max_GCD = 0

for k in range(2, 1000):
    temp = 0
    for e in a:
        if e % k == 0:
            temp += 1
    if temp > max_GCD:
        max_GCD = temp
        answer = k
print(answer)
