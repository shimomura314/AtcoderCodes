def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

n,x = map(int,input().split())
s = list(map(int,input().split()))

for i in range(n):
    s[i] -= x
answer = s[0]
for i in range(n-1):
    answer = gcd(answer,s[i+1])

if answer < 0:
    answer *= -1


print(answer)