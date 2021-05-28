n = int(input())
n = 2025-n
for i in range(1, n+1):
    for j in range(n+1):
        if i < 10 and j < 10 and i*j == n:
            ans = []
            ans.append(str(i))
            ans.append("x")
            ans.append(str(j))
            print(" ".join(ans))