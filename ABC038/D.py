import sys
import bisect
sys.setrecursionlimit(10**8)


def LIS(a):
    lis = [a[0]]
    for i in range(len(a)):
        if a[i] > lis[-1]:
            lis.append(a[i])
        else:
            lis[bisect.bisect_left(lis,a[i])] = a[i]
    return len(lis)


def main():
    n = int(input())
    wh = []
    for _ in range(n):
        w,h = map(int,input().split())
        wh.append((w,h))
    wh = sorted(wh, key = lambda x: (x[0],-x[1]))
    a = []
    for i in range(n):
        a.append(wh[i][1])
    print(LIS(a))


if __name__ == "__main__":
    main()