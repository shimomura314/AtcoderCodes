n = int(input())

answer = 0
for a in range(1, n):
    answer += n//a
    if n%a == 0:
        answer -= 1
print(answer)
