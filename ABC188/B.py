n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sumation = 0
for x, y in zip(a, b):
    sumation += x*y
if sumation == 0:
    print("Yes")
else:
    print("No")