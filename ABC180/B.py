n = int(input())
x = list(map(int,input().split()))
a,b,c = 0,0,0
for i in range(n):
    x[i] = abs(x[i])
print(sum(x))
for i in range(n):
    a += x[i]**2
a = a**0.5
print(a)
print(max(x))