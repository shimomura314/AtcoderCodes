def main():
    n,m = map(int,input().split())
    x,y = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    now = 0
    indexa = 0
    indexb = 0
    ans = 0
    while True:
        while indexa!=n:
            if a[indexa] >= now:
                now = a[indexa]+x
                break
            else:
                indexa += 1
        while indexb != m:
            if b[indexb] >= now:
                now = b[indexb]+y
                break
            else:
                indexb += 1
        if indexa == n or indexb == m:
            print(ans)
            return
        ans += 1


if __name__ == "__main__":
    main()