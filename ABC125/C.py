def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


def main():
    n = int(input())
    a = list(map(int,input().split()))
    L = [a[0] for _ in range(n)]
    R = [a[n-1] for _ in range(n)]
    for i in range(1,n):
        L[i] = gcd(L[i-1], a[i])
    for i in range(1,n):
        R[i] = gcd(R[i-1], a[n-1-i])
    R.reverse()
    LR = []
    for i in range(1,n-1):
        LR.append( gcd(L[i-1], R[i+1]) )
    if LR == []:
        print( max(L[n-2], R[1]) )
    else:
        print( max(max(LR), L[n-2], R[1]) )


if __name__ == "__main__":
    main()