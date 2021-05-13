def main():
    n = int(input())
    xyh=[]
    for _ in range(n):
        x,y,h = map(int,input().split())
        xyh.append([x,y,h])
    xyh.sort(key=lambda x: x[2], reverse=True)
    for xc in range(101):
        for yc in range(101):
            x = xyh[0][0]
            y = xyh[0][1]
            h = xyh[0][2]
            d = abs(xc-x) + abs(yc-y)
            H = h+d
            for i in range(1,n):
                x = xyh[i][0]
                y = xyh[i][1]
                h = xyh[i][2]
                d = abs(xc-x) + abs(yc-y)
                if h != max(0, H-d):
                    break
                if i == n-1:
                    print(xc, yc, H)
                    return


if __name__ == "__main__":
    main()