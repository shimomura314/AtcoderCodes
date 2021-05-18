import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


def lcm(a, b):
    return((a*b)//gcd(a,b))


def main():
    n = int(input())
    t = [int(input()) for _ in range(n)]
    ans = 1
    for i in range(n):
        ans = lcm(ans, t[i])
    print(ans)


if __name__ == "__main__":
    main()