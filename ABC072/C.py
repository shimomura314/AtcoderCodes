n = int(input())
a = list(map(int,input().split()))
cnt = {}
for e in range(min(a)-1, max(a)+2):
    cnt[e] = 0
for e in a:
    if e in cnt:
        cnt[e] += 1
answer = 0
for i in a:
    if answer < cnt[i-1] + cnt[i] + cnt[i+1]:
        answer = cnt[i-1] + cnt[i] + cnt[i+1]
print(answer)