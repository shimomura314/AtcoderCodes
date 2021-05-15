def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    x = a[n-1]
    m = x
    y = 0
    for i in range(n-1):
        if abs(a[i]-x//2) < m:
            m = abs(a[i]-x/2)
            y = a[i]
    print(x,y)


if __name__ == "__main__":
    main()