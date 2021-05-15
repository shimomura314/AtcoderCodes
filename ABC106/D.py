def main():
    n,m,Q = map(int,input().split())
    answer = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        l,r = map(int,input().split())
        r -= 1
        answer[r][0] += 1
        if l != n:
            answer[r][l] -= 1
    for i in range(n):
        for j in range(1,n):
            answer[i][j] += answer[i][j-1]
    for i in range(n):
        for j in range(1,n):
            answer[j][i] += answer[j-1][i]
    for _ in range(Q):
        p,q = map(int,input().split())
        print(answer[q-1][p-1])


if __name__ == "__main__":
    main()