from itertools import combinations


def main():
    answer = 10**10
    n,a,b,c = map(int,input().split())
    l = list(int(input()) for _ in range(n))
    for an in range(1, n-1):
        for use_a in combinations(range(n), an):
            tank = []
            for j in range(n):
                if j not in use_a:
                    tank.append(j)
            for bn in range(1,n-an):
                for use_b in combinations(tank, bn):
                    tank1 = []
                    for j in tank:
                        if j not in use_b:
                            tank1.append(j)
                    for cn in range(1,n-an-bn+1):
                        for use_c in combinations(tank1, cn):
                            a_pre = 0
                            b_pre = 0
                            c_pre = 0
                            for i in use_a:
                                a_pre += l[i]
                            for i in use_b:
                                b_pre += l[i]
                            for i in use_c:
                                c_pre += l[i]
                            count = 0
                            count += ( len(use_a)+len(use_b)+len(use_c)-3 )*10 + abs(a_pre-a)+abs(c_pre-c)+abs(b_pre-b)
                            if answer > count:
                                answer = count
    print(answer)


if __name__ == "__main__":
    main()