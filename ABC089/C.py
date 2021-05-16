n = int(input())
count = [0]*5
for _ in range(n):
    s = list(input())
    if s[0] == "M":
        count[0] += 1
    if s[0] == "A":
        count[1] += 1
    if s[0] == "R":
        count[2] += 1
    if s[0] == "C":
        count[3] += 1
    if s[0] == "H":
        count[4] += 1

ans = 0
for i in range(3):
    for j in range(i+1, 4):
        for k in range(j+1, 5):
            ans += count[i]*count[j]*count[k]
print(ans)