k = int(input())
s = list(input())
t = list(input())
cnt = [k for _ in range(9)]
cnt_s = [0 for _ in range(9)]
cnt_t = [0 for _ in range(9)]
ans = 0
for i in range(4):
    s[i] = int(s[i])
    t[i] = int(t[i])
    cnt[s[i]-1] -= 1
    cnt[t[i]-1] -= 1
    cnt_s[s[i]-1] += 1
    cnt_t[t[i]-1] += 1

for x in range(1, 10):
    for y in range(1, 10):
        if cnt[x-1] == 0 or cnt[y-1] == 0:
            continue
        if x==y and cnt[x-1] < 2:
            continue
        point_s = 0
        point_t = 0
        for i in range(1, 10):
            if x != i:
                point_s += i*(10**cnt_s[i-1])
            else:
                point_s += i*(10**(cnt_s[i-1]+1))
            if y != i:
                point_t += i*(10**cnt_t[i-1])
            else:
                point_t += i*(10**(cnt_t[i-1]+1))
        if point_s > point_t:
            if x != y:
                ans += cnt[x-1] * cnt[y-1]
            else:
                ans += cnt[x-1] * (cnt[y-1]-1)

print(ans/((9*k-8)*(9*k-9)))