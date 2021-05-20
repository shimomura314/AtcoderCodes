l,s = map(int,input().split())
count = 0
if s < l:
    l = s

for i in range(l+1):
    for j in range(l+1):
        if s-i-j <= l and s-i-j >= 0:
            count += 1
print(count)