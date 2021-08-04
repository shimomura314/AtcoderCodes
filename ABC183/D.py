n, w = map(int, input().split())

plan = [0] * (2*10**5+1)
for _ in range(n):
    s, t, p = map(int, input().split())
    plan[s] += p
    plan[t] -= p
for i in range(2*10**5):
    plan[i+1] += plan[i]

if max(plan) > w:
    print("No")
else:
    print("Yes")