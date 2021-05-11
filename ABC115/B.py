n = int(input())
answer = 0
m = 0
for _ in range(n):
    a = int(input())
    answer += a
    m = max(m,a)
print(answer-m//2)