n = int(input())
count = 0
for _ in range(n):
    x, y = list(map(int, input().split()))
    if x == y:
        count += 1
        if count == 3:
            print("Yes")
            exit()
    else:
        count = 0
print("No")