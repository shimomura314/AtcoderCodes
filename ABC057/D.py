import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 170141183460469231731687303715884105727 


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
    return x


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


def main():
    n,a,b = map(int,input().split())
    v = list(map(int,input().split()))
    v.sort(reverse=True)
    sumation = 0
    for i in range(a):
        sumation += v[i]
    print(sumation/a)
    left = 0
    right = n-1
    for i in range(a-1,n-1):
        if v[i] != v[i+1]:
            right = i
            break
    for i in range(a-1,0,-1):
        if v[i] != v[i-1]:
            left = i
            break
    number = right - left + 1
    ans = 0
    if v[a-1] != v[0]:
        print(nCk(number, a-left))
        return
    if v[0] == v[a-1]:
        for e in range(a, min(b+1,number+1)):
            ans += nCk(number, e)
        print(ans)
    else:
        print(nCk(number,a-left+1))


if __name__ == "__main__":
    main()