import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7


def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2]!=1:
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
    a = n-k
    b = k
    for i in range(1,a+b+1):
        res = res*i%mod
    for i in range(1,a+1):
        res = res*mod_inv(i,mod)%mod
    for i in range(1,b+1):                                 
        res = res*mod_inv(i,mod)%mod
    return res


def nHr(n,r):
    return nCk(n+r-1,r)


def div3(x):
    div = defaultdict(int)
    check = 2
    while(x!=1 and check <= int(x**0.5)+2):
        while x%check == 0:
            div[check] += 1
            x //= check
        check += 1
    if x != 1:
        div[x] += 1
    return div

def main():
    n,m = map(int,input().split())
    div = div3(m)
    ans = 1
    for e in div:
        ans = (ans * nHr(n,div[e])) % mod
    print(ans)


if __name__ == "__main__":
    main()