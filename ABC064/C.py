n = int(input())
a = list(map(int,input().split()))
color = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(n):
    if a[i] >= 3200:
        color[8] += 1
    else:
        color[(a[i]//400)] = 1 
ans = sum(color) - color[-1]
Max = ans+color[8]
if ans == 0:
    ans = 1
print(ans, Max)