import math
import sys
sys.setrecursionlimit(10**8)
mod = 10**9+7


def main():
    x = list(input())
    m = int(input())
    for i in range(len(x)):
        x[i] = int(x[i])
    if len(x) == 1:
        if x[0] <= m:
            print(1)
            return
        else:
            print(0)
            return
    if len(x) == 2:
        bigger = m//x[0]
        smaller = max(x)+1
        if m < bigger*x[0] + x[1]:
            bigger -= 1
        if m < smaller*x[0] + x[1]:
            print(0)
            return
        if bigger < smaller:
            print(0)
            return
        print(bigger-smaller+1)
        return
    if len(x) == 3:
        f = math.sqrt(m/(x[0]))
        if int(f) == f:
            bigger = int(f)
        else:
            bigger = int(math.floor(f))
        smaller = max(x)+1
        while m < (bigger*bigger)*x[0] + bigger*x[1] + x[2]:
            bigger -= 1
        if m < (smaller*smaller)*x[0] + smaller*x[1] + x[2]:
            print(0)
            return
        if bigger < smaller:
            print(0)
            return
        print(bigger-smaller+1)
        return

    smaller = max(x)+1
    ans = 0
    while True:
        value = 0
        for i in range(len(x)):
            value += x[i]*(smaller**(len(x)-i-1))
            if value > m:
                print(ans)
                return
        smaller += 1
        ans += 1


if __name__ == "__main__":
    main()