x,y,a,b = map(int,input().split())
ans = 0
while x < y:
    if x*(a-1) <= b:
        x *= a
        ans += 1
    else:
        z = (y-x)//b
        if (y-x)%b == 0:
            z -= 1
        ans += z
        break

if x < y:
    print(ans)
else:
    print(ans-1)