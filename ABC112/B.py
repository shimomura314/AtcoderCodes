n,t = map(int,input().split())
ct = sorted([list(map(int, input().split())) for _ in range(n)])
m = 1001
for i in range(n):
    if ct[i][1] <=t:
        m = min(m,ct[i][0])
if(m == 1001):
    print("TLE")
else:
    print(m)