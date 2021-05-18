import sys, math
input = sys.stdin.readline

def main():
    n,a,b = map(int,input().split())
    h = [int(input()) for _ in range(n)]
    ok = max(h)
    ng = 0
    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        cnt = 0
        for i in range(n):
            cnt += max(0, math.ceil((h[i]-mid*b)/(a-b)))
        if cnt <= mid:
            ok = mid
        else:
            ng = mid
    print(ok)


if __name__ == "__main__":
    main()