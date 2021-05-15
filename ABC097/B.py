n = int(input())
b = []
for i in range(30):
    i += 2
    s = i*i
    while s <= 1000:
        b.append(s)
        s = s*i
answer = 1
for i in range(len(b)):
    if b[i] <= n and answer < b[i]:
        answer = b[i]
print(answer)