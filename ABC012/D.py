import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


def warshall_floyd():
    n,w = map(int,input().split())
    d = [[10**10 for i in range(n)] for i in range(n)] 

    for i in range(w):
        x,y,z = map(int,input().split())
        x -= 1
        y -= 1
        d[x][y] = z
        d[y][x] = z
    for i in range(n):
        d[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    m = float('inf')
    for i in range(n):
        m = min( m,max(d[i]) )
    print(m)


def main(): 
    warshall_floyd()


if __name__ == "__main__":
    main()