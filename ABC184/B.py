n, x = map(int, input().split())
s = str(input())
for e in s:
    if e == "o":
        x += 1
    else:
        x -= 1
        if x < 0:
            x = 0
print(x)
