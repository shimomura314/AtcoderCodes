n = int(input())
ans = []
for x in range(1, int(n**0.5)+1):
    y = n//x
    ans.append( abs(x-y)+n-x*y )
print(min(ans))