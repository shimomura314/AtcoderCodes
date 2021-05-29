from itertools import combinations


def main():
    n,m = map(int,input().split())
    ab = []
    for _ in range(m):
        a,b = map(int,input().split())
        ab.append((a-1,b-1))
    for num in range(n,1,-1):
        for com in combinations(range(n),num):
            flag = 0
            for pair in combinations(com,2):
                if (pair[0],pair[1]) not in ab:
                    flag = 1
                    break
            if flag == 0:
                print(num)
                return
    print(1)


if __name__ == "__main__":
    main()
