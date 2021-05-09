def main():
    a,b,q = map(int,input().split())
    s = tuple(int(input()) for _ in range(a))
    t = tuple(int(input()) for _ in range(b))
    x = tuple(int(input()) for _ in range(q))
    for i in range(q):
        start = x[i]
        n = len(s)
        ok = -1
        ng = n
        while abs(ok-ng) > 1:
            mid = (ok+ng) // 2
            if s[mid] < start:
                ok = mid
            else:
                ng = mid
        index_s = ok
        n = len(t)
        ok = -1
        ng = n
        while abs(ok-ng) > 1:
            mid = (ok+ng) // 2
            if t[mid] < start:
                ok = mid
            else:
                ng = mid
        index_t = ok
        a1 = 10**11
        b1 = 10**11
        c1 = 10**11
        d1 = 10**11
        if index_t+1 < b and index_s+1 < a:
            d1 = abs(max(s[index_s+1],t[index_t+1]) - start)
        if index_s >= 0 and index_t+1 < b:
            a1 = min(abs(start - s[index_s]) + abs(s[index_s] - t[index_t+1]), abs(start - t[index_t+1]) + abs(s[index_s] - t[index_t+1]) )  
        if index_t >= 0 and index_s+1 < a:
            b1 = min(abs(start - t[index_t]) + abs(s[index_s+1] - t[index_t]),abs(start - s[index_s+1]) + abs(s[index_s+1] - t[index_t]))
        if index_s >= 0 and index_t >= 0:
            c1 = abs(start - min(s[index_s],t[index_t]))
        print(min(a1,b1,c1,d1))

if __name__ == "__main__":
    main()