def main():
    n,m = map(int,input().split())
    h = list(map(int,input().split()))
    g = [[] for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)
    answer = 0
    for i in range(n):
        flag = 1
        for j in range(len(g[i])):
            if h[i] <= h[g[i][j]]:
                flag = 0
        if flag:
            answer += 1
    print(answer)


if __name__ == "__main__":
    main()