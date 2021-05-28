import copy

def main():
    n,m = map(int,input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)
    
    for i in range(n):
        if len(g[i]) == 0:
            print(0)
            continue
        cnt = 0
        check = copy.copy(g[i])
        check.append(i)
        for e in g[i]:
            for d in g[e]:
                if d != i and (d not in g[i]) and (d not in check):
                    check.append(d)
                    cnt += 1
        print(cnt)


if __name__ == "__main__":
    main()