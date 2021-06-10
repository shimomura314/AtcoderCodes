n = int(input())
ans = []
n -= 1
while True:
    x = n%26
    n //= 26
    ans.append(chr(x+97))
    if n == 0:
        break
    n -= 1
ans.reverse()
print(''.join(ans))