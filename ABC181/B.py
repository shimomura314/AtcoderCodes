n = int(input())
answer = 0
for _ in range(n):
    a, b = map(int, input().split())
    answer += (a+b)*(b-a+1) // 2
print(answer)
