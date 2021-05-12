s = list(input())
answer = 10000
for i in range(len(s)-2):
    n = int(''.join(s[i:i+3]))
    if answer > abs(n-753):
        answer = abs(n-753)
print(answer)