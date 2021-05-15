s = list(input())
k = int(input())
answer = "1"

k = min(k, len(s))

for i in range(k):
    if answer == "1" and s[i] != "1":
        answer = s[i]

print(answer)