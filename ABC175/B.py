n = int(input())
l = list(map(int,input().split()))
l.sort()
answer = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1,n):
            if l[i] == l[j] or l[j] == l[k]:
                continue
            if l[i]+l[j] > l[k]:
                answer += 1
print(answer)