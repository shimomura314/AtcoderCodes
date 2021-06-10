from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))

dic = defaultdict(int)
ans = sum(a)
for i in range(n):
    dic[a[i]] += 1

q = int(input())
for _ in range(q):
    b,c = map(int,input().split())
    ans += dic[b]*(c-b)
    dic[c] += dic[b]
    dic[b] = 0
    print(ans)