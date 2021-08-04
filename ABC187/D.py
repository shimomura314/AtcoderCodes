n = int(input())
ab = []
aoki = 0
takahashi = 0
for _ in range(n):
    a, b = map(int, input().split())
    aoki += a
    ab.append([2*a+b, a, b])

answer = 0
ab.sort()
ab.reverse()
while aoki >= takahashi:
    _, a, b = ab[answer]
    aoki -= a
    takahashi += a+b
    answer += 1
print(answer)
