n = int(input())
length = len(str(n))
ans = 0
for i in range(length, -1, -1):
    if i%2 != 0 or i == 0:
        continue
    elif i==length:
        b = n%(10**(i//2))
        a = (n-b)//(10**(i//2))

        ans += (a-(10**(i//2-1)))
        if a <= b:
            ans += 1
    else:
        ans += (10**(i//2))*0.9
print(int(ans))