n = int(input())
a = [int(input()) for _ in range(n)]
cnt = 0
push = 1
for i in range(n):
    push = a[push-1]
    cnt += 1
    if push == 2:
        print(cnt)
        exit()
print(-1)