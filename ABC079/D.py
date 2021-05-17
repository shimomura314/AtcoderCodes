from collections import defaultdict


def main(): 
    h,w = map(int,input().split())
    d = []
    for _ in range(10):
        d.append(list(map(int,input().split())))
    n = 10
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    a = []
    for _ in range(h):
        a.append(list(map(int,input().split())))

    ans = 0
    for i in range(h):
        for j in range(w):
            if a[i][j] == -1:
                continue
            ans += d[a[i][j]][1]
    print(ans)


if __name__ == "__main__":
    main()