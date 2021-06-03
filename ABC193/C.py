from collections import Counter,defaultdict

n = int(input())
cnt = 0
dic = defaultdict(int)
for x in range(2, 10**5+1):
    for y in range(2, 100):
        if x**y > n:
            break
        if dic[x**y]==0:
            cnt += 1
            dic[x**y] += 1
print(n-cnt)