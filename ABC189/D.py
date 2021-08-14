n = int(input())
s = [str(input()) for _ in range(n)]
n0, n1 = 1, 1
for i in range(n):
    if s[i] == "AND":
        n0, n1 = n0*2 + n1, n1
    else:
        n0, n1 = n0, n0 + n1*2
print(n1)
