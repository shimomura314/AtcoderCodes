import bisect
mod = 10**9+7


def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    answer = 1
    cnt = 0
    l = 0
    r = n-1
    x = bisect.bisect_left(a,0)
    y = bisect.bisect_right(a,0)
    flag = 0
    if n == 1:
        print(a[0]%mod)
        return
    if n == 2:
        if k == 1:
            print((max(a[0],a[1]))%mod)
        else:
            print(a[0]*a[1]%mod)
        return
    if k == n:
        if x%2 == 0:
            flag = 1
    elif k == n-1:
        if x == n:
            if k%2 == 0:
                flag = 1
        else:
            if x%2 == 1:
                flag = 1
            else:
                if x != n:
                    flag = 1
    else:
        if x == n:
            if k%2 == 0:
                flag = 1
        else:
            flag = 1
    if flag:
        while True:
            if a[l+1] >= 0:
                answer *= a[r]
                answer %= mod
                cnt += 1
                r -= 1
            else:
                if a[l]*a[l+1] >= a[r]*a[r-1] and cnt < k-1:
                    answer *= a[l]
                    answer *= a[l+1]
                    answer %= mod
                    cnt += 2
                    l += 2
                else:
                    answer *= a[r]
                    answer %= mod
                    cnt += 1
                    r -= 1
            if cnt == k:
                break
        print(answer)
    else:
        if 0 in a:
            print(0)
            return
        for i in range(n):
            a[i] = abs(a[i])
        a.sort()
        for i in range(k):
            answer *= a[i]
            answer %= mod
        answer *= -1
        answer %= mod
        print(answer)


if __name__ == "__main__":
    main()