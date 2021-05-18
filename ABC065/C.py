mod=10**9+7

def factorial(x): #階乗計算
    n = 1
    for i in range(x):
        n *= i+1
        n %= mod
    return n


def main():
    n,m = map(int,input().split())    
    if abs(n-m) > 1:
        print(0)
    else:
        a = max(n,m)
        b = min(n,m)
        if a > b:
            print( (factorial(a)*factorial(b)) % mod )
        else:
            ans = (factorial(a)**2) % mod
            print( (2*ans) % mod )


if __name__ == "__main__":
    main()