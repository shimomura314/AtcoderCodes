mod = 10**9 + 7

n = int(input())
a = list(map(int, input().split()))

answer = 0
sumation = sum(a)

for i in range(n-1):
    sumation -= a[i]
    answer += a[i]*sumation
    answer %= mod

print(answer)
