def f(x,y,ax,ay,bx,by):
    if ax == bx:
        if x > ax:
            return 1
        return -1
    if y > ((by-ay)/(bx-ax))*(x-ax)+ay:
        return 1
    return -1


def main():
    ax,ay,bx,by = map(int,input().split())
    n = int(input())
    point = []
    for _ in range(n):
        point.append(tuple(map(int,input().split())))
    count = 0
    for i in range(n):
        if f(point[i][0],point[i][1],ax,ay,bx,by) * f(point[(i+1)%n][0],point[(i+1)%n][1],ax,ay,bx,by) == -1:
            if f(ax,ay,point[i][0],point[i][1],point[(i+1)%n][0],point[(i+1)%n][1]) * f(bx,by,point[i][0],point[i][1],point[(i+1)%n][0],point[(i+1)%n][1]) == -1:
                count += 1
    print(count//2 + 1)


if __name__ == "__main__":
    main()