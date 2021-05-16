def main():
    h,w,d = map(int,input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    MAP = [0 for _ in range(h*w)]
    for i in range(h):
        for j in range(w):
            MAP[a[i][j]-1] = (i,j)
    cnt = []
    for i in range(h*w-d):
        x = MAP[i]
        y = MAP[i+d]
        cost = abs(x[0]-y[0]) + abs(x[1]-y[1])
        cnt.append(cost)
    ans = [0 for _ in range(h*w)]
    for i in range(h*w - d):
        ans[i+d] += ans[i] + cnt[i]

    q = int(input())
    for _ in range(q):
        l,r = map(int,input().split())
        print(ans[r-1] - ans[l-1])


if __name__ == "__main__":
    main()