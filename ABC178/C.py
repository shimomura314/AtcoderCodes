mod = 10**9
n = int(input())
answer = pow(10, n-2, mod)
answer *= n*(n-1)//2
answer %= mod
print(answer)
