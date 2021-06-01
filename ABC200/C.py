from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))
dic = defaultdict(int)
ans = 0
for i in range(n):
    ans += dic[a[i]%200]
    dic[a[i]%200] += 1
print(ans)