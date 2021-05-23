from collections import defaultdict
import sys
sys.setrecursionlimit(10**8)
mod = 10**9+7


def main():
    n,a = map(int,input().split())
    k = int(input())
    b = list(map(int,input().split()))
    dic = defaultdict(int)
    lap_1st = []
    lap_2nd = []
    while dic[a] == 0:
        lap_1st.append(a)
        dic[a] = 1
        a = b[a-1]
    while dic[a] == 1:
        lap_2nd.append(a)
        dic[a] = 2
        a = b[a-1]
    l1 = len(lap_1st)
    l2 = len(lap_2nd)
    if k <= l1-1:
        print(lap_1st[k])
        return
    index = k - l1 - ((k-l1)//l2)*l2
    if index == l2:
        index = 0
    print(lap_2nd[index])


if __name__ == "__main__":
    main()