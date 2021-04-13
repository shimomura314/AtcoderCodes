def disk(p1,p2,p3):
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    a2 = (x2 - x3) **2 + (y2 -y3) ** 2 
    b2 = (x1 - x3) **2 + (y1 -y3) ** 2
    c2 = (x2 - x1) **2 + (y2 -y1) ** 2
    area = ((x2 - x1) * (y3 -y1) - (x3 -x1) * (y2- y1)) / 2
    if area == 0:
        return (0,0),10**5
    x = (a2*(b2+c2-a2)*x1 + b2*(c2+a2-b2)*x2 +c2*(a2+b2-c2)*x3) / (16*area*area)
    y = (a2*(b2+c2-a2)*y1 + b2*(c2+a2-b2)*y2 +c2*(a2+b2-c2)*y3) / (16*area*area) 
    r = ((x1 - x ) ** 2 + (y1 - y) ** 2)**.5
    return (x,y), r


def circumcircle():
    n = int(input())
    l = [tuple(map(int, input().split())) for _ in range(n)]
    ans = 10**5
    dist = lambda p,q: ((p[0]-q[0])**2 + (p[1]-q[1])**2)**.5
    check = lambda c,d: all(dist(c,p)<=d for p in l)
    for i in range(n-1):
        for j in range(i+1,n):
            c = ((l[i][0]+l[j][0])/2, (l[i][1]+l[j][1])/2)
            d = dist(l[i],l[j])/2
            if check(c,d) and d < ans:
                ans = d
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                c,d = disk(l[i],l[j],l[k])
                if check(c,d) and d < ans:
                    ans = d
    print(ans)


def main():
    circumcircle()


if __name__ == "__main__":
    main()


