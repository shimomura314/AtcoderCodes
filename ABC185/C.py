mod = 170141183460469231731687303715884105727


def extgcd(a, b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2] != 1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    return [w[0],w[1]]


def mod_inv(a,m):
    x = extgcd(a,m)[0]
    return ( m + x%m ) % m


def nCk(n,k):
    res = 1
    a=n-k
    b=k
    for i in range(1,a+b+1):
        res = res*i%mod
    for i in range(1,a+1):
        res = res*mod_inv(i,mod)%mod
    for i in range(1,b+1):                                 
        res = res*mod_inv(i,mod)%mod
    return res


L = int(input())
print(nCk(L-1, 11))