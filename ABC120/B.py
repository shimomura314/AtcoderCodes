from math import gcd

a,b,k = map(int,input().split())
count = 1

answer = gcd(a,b)
n = answer
if not(k==1):
    for i in range(n):
        c = n-i-1
        if a%c == 0 and b%c == 0:
            answer = n-i-1
            count += 1
        if count == k:
            break

print(answer)