s = list(input())
t = list(input())

answer = len(s)
for n in range(len(s)-len(t)+1):
    count = 0
    for i in range(len(t)):
        if s[n+i] != t[i]:
            count += 1

    answer = min(answer, count)

print(answer)
