import sys
import math
sys.setrecursionlimit(10**8)

def f(t, a, b, c):
    x = c*t*math.pi
    return a*t + b*math.sin(x)


def main():
    a,b,c = map(int,input().split())
    ok = 0
    ng = 10**4
    mid = (ok+ng)/2
    while abs(f(ok, a, b, c)-100)>10**(-7):
        mid = (ok+ng) / 2
        if f(mid, a, b, c) > 100:
            ng = mid
        elif f(mid, a, b, c) < 100:
            ok = mid
        else:
            print(mid)
            return
    print(ok)


if __name__ == "__main__":
    main()