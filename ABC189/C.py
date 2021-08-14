n = int(input())
a = list(map(int, input().split()))

answer = 0
for left in range(n):
    x = a[left]
    if answer > x*(n-left):
        break
    for right in range(left, n):
        if answer > x*(n-left):
            break
        x = min(x, a[right])
        answer = max(answer, x*(right-left+1))
print(answer)