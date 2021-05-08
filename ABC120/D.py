def find(x):
    if par[x] == x:
        return x
    else:
        par[x]=find(par[x])
        return par[x]


def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        answer.append(0)
        return
    answer.append( num[x]*num[y] )
    z = num[x]+num[y]
    num[x] = z
    num[y] = z
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

def same(x,y):
    return find(x)==find(y)


def main():
    n,m = map(int,input().split()) 

    global par, rank, num, answer
    par = [i for i in range(n)]  # 親
    rank = [0 for _ in range(n)] # 木の深さ
    num = [1 for _ in range(n)] # 木の大きさ
    answer = []
    ab = []
    for _ in range(m):
        a,b = map(int, input().split())
        ab.append((a-1,b-1))
    for i in range(m-1,-1,-1):
        unite(ab[i][0], ab[i][1])
    
    p = (n*(n-1)) // 2
    x = []
    for i in range(m):
        x.append(p)
        p -= answer[i]
        if p < 0:
            p = 0
    x.reverse()
    
    for i in range(m):
        print(x[i])


if __name__ == "__main__":
    main()