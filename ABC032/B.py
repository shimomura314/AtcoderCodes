s = list(input())
n = int(input())
if len(s)<n:
    print(0)
    exit()

ans = 0
c = {}
for i in range(len(s)-n+1):
    if "".join(s[i:i+n]) not in c:
        c["".join(s[i:i+n])] = 1
        ans += 1
    else:
        continue

print(ans)