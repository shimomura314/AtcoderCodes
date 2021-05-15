s = list(input())
t = list(input())
n = len(s)
answer = "No"
for i in range(n):
    for j in range(n-1):
        s[n-1-j], s[n-2-j] = s[n-2-j], s[n-1-j]
    if s == t:
        answer = "Yes"
print(answer)