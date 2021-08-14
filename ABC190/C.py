n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
cd = [list(map(int, input().split())) for _ in range(k)]

answer = 0
for conditions in range(2**k):
    disks = [False] * n
    for person in range(k):
        condition = conditions >> person
        disks[cd[person][condition % 2]-1] = True

    temp = 0
    for a, b in ab:
        if disks[a-1] and disks[b-1]:
            temp += 1
    answer = max(answer, temp)
print(answer)