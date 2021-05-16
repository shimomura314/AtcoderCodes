def main():
    n = int(input())
    ans = []
    csf = []
    for _ in range(n-1):
        csf.append(list(map(int,input().split())))
        ans.append(csf[-1][1])
    csf.append([0,0,0])
    ans.append(0)
    for i in range(n-1):
        for j in range(i+1):
            if ans[j] >= csf[i][1] and ans[j]%csf[i][2] == 0:
                ans[j] += csf[i][0]
            elif ans[j] >= csf[i][1]:
                ans[j] += csf[i][2] - ans[j]%csf[i][2]
                ans[j] += csf[i][0]
            else:
                ans[j] = csf[i][0] + csf[i][1]
    print(*ans)


if __name__ == "__main__":
    main()