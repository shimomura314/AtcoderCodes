import sys
import bisect
input = sys.stdin.readline

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    check = {}
    for i in a:
        if not (i in check):
            check[i] = 1
        elif check[i] == 1:
            check[i] = 0
        elif check[i] == 0:
            check[i] = 1
    ans = 0
    for i in check:
        if check[i] == 1:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()