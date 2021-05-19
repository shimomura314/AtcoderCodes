n = int(input())
ans = n
r = int(n**0.5) + 1
for i in range(r):
    i += 1
    if n%i == 0:
        ans = min( max(len(str(i)), len(str(n//i))), ans )
print(ans)