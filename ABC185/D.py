n,m = map(int, input().split())
a = list(map(int, input().split()))
if m == 0:
    print(1)
    exit()
a.sort()
margins = []
for i in range(m):
    if i == 0:
        if a[i]-1:
            margins.append(a[i]-1)
        continue
    if a[i]-a[i-1]-1:
        margins.append(a[i]-a[i-1]-1)
    if i == m-1:
        if n-a[i]:
            margins.append(n-a[i])
    # print(margins)
if margins == []:
    print(0)
    exit()
margins.sort()
k = margins[0]
answer = 0
for e in margins:
    answer += e//k
    if e%k:
        answer += 1

print(answer)
