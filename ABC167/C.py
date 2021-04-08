from itertools import combinations


def main():
    n,m,x = map(int,input().split())
    c = [list(map(int,input().split())) for _ in range(n)]
    answer = float('inf')

    for number in range(1, n+1):
        for e in combinations(range(n), number):
            cost = 0
            under = [0 for _ in range(m)]
            for f in e:
                cost += c[f][0]
                for i in range(m):
                    under[i] += c[f][i+1]
            if min(under) >= x:
                answer = min(answer,cost)
    if answer == float('inf'):
        print(-1)
    else:
        print(answer)

    
if __name__ == "__main__":
    main()