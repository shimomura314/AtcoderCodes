import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


def main(): 
    n = int(input())
    hs = [tuple(map(int,input().split())) for _ in range(n)]

    ok = 10**16
    ng = 0
    while ok-ng > 1:
        mid = (ok+ng)//2
        box = []
        for i in range(n):
            x = (mid-hs[i][0]) // hs[i][1]
            box.append(x)
        box.sort()
        flag = False
        for i in range(n):
            if box[i] < i:
                ng = mid
                flag = True
        if not flag:
            ok = mid
    print(ok)


if __name__ == "__main__":
    main()