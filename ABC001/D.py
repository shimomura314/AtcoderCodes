def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int,input().split('-'))))
        a[i][0] = (a[i][0]//5) * 5
        a[i][1] = ((a[i][1]+4)//5) * 5
        if a[i][1]%100 == 60:
            a[i][1] += 40
    a.sort()
    a.append([9999,9999])
    ans = []
    [s,e] = a[0]
    for i in range(n+1):
        if a[i][0] <=  e:
            e = max(e, a[i][1])
        else:
            ans.append([s,e])
            [s,e] = a[i]
    for i in range(len(ans)):
        print("%04d-%04d" %(ans[i][0],ans[i][1]))


if __name__ == "__main__":
    main()
