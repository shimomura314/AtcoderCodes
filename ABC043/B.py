s = list(input())
t = []
for i in range(len(s)):
    if s[i] == "B":
        if len(t) > 0:
            t = t[:-1]
    else:
        t.append(s[i])

print("".join(t))