import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))

    tuple_x = {}
    tuple_y = defaultdict(int)
    for i in range(m):
        tuple_x[a[i]] = 1
        tuple_y[a[i]] += 1
    for i in range(m+1):
        if i not in tuple_x.keys():
            ans = i
            break
    for i in range(m, n):
        tuple_y[a[i-m]] -= 1
        tuple_y[a[i]] += 1
        if tuple_y[a[i-m]] == 0:
            tuple_y.pop(a[i-m])
            ans = min(ans, a[i-m])
    print(ans)


if __name__ == "__main__":
    main()