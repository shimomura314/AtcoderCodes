s = list(input())
r, b, answer = 0, 0, 0

for i in range(len(s)):
    if b == 0 and s[i] == "0":
        r += 1
    elif r == 0 and s[i] == "1":
        b += 1
    elif b>0 and s[i] == "0":
        b -= 1
        answer += 2
    elif r>0 and s[i] == "1" :
        r -= 1
        answer += 2

print(answer)