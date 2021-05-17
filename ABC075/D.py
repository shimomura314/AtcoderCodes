import sys
sys.setrecursionlimit(10**8)

def main():
    n,k = map(int,input().split())
    xy = []
    X = []
    Y = []
    for _ in range(n):
        x,y = map(int,input().split())
        xy.append((x,y))
        X.append(x)
        Y.append(y)
    answer = 10**20
    for i in range(n-1):
        for j in range(i+1,n):
            for a in range(n-1):
                for b in range(a+1,n):
                    xl,xr = X[i],X[j]
                    yd,yu = Y[a],Y[b]
                    if xl > xr:
                        xr,xl = xl,xr
                    if yd > yu:
                        yd,yu = yu,yd
                    area = (xr-xl)*(yu-yd)
                    if answer < area:
                        continue
                    cnt = 0
                    for c in range(n):
                        if xl <= xy[c][0] and xy[c][0] <= xr and yd <= xy[c][1] and xy[c][1] <= yu:
                            cnt += 1
                    if cnt >= k:
                        answer = min(answer,area)
    print(answer)


if __name__ == "__main__":
    main()