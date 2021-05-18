mod = 10**9+7


def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))
    X = 0
    Y = 0
    cntX, cntY = n-1, m-1
    for i in range(n-1,-1,-1):
        X += x[i]*cntX
        X %= mod
        cntX -= 2
    for i in range(m-1,-1,-1):
        Y += y[i]*cntY
        Y %= mod
        cntY -= 2
    print((X*Y)%mod)


if __name__ == "__main__":
    main()