n = int(input())
answer = 0
for _ in range(n):
    xu = input().split()
    if xu[1] == "JPY":
        answer += int(xu[0])
    else:
        answer += float(xu[0])*380000
print(answer)