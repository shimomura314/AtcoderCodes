import sys
input = sys.stdin.readline


def main():
    n = int(input())
    a = []
    b = []
    for _ in range(n):
        A,B = map(int,input().split())
        a.append(A)
        b.append(B)
    a.sort()
    b.sort()

    if n%2:
        print(b[n//2]-a[n//2]+1)
    else:
        print((b[n//2]+b[n//2-1]) - (a[n//2]+a[n//2-1])+1)


if __name__ == "__main__":
    main()