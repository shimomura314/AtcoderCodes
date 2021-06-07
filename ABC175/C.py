x,k,d = map(int,input().split())
if abs(x) > k*d:
    print(abs(abs(x)-k*d))
    exit()
cnt = abs(x)//d
k -= cnt
if k%2 == 0:
    print(abs(x)-d*cnt)
else:
    print(d-(abs(x)-d*cnt))