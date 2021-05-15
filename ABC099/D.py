import sys
from collections import defaultdict
from itertools import permutations
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7


def main():
    n,c = map(int,input().split())
    
    D = [list(map(int, input().split())) for _ in range(c)]
    a = [list(map(int, input().split())) for _ in range(n)]
    dic1 = defaultdict(int)
    dic2 = defaultdict(int)
    dic3 = defaultdict(int)
    for i in range(n):
        for j in range(n):
            if (i+j)%3 == 0:
                dic1[a[i][j]] += 1
            elif (i+j)%3 == 1:
                dic2[a[i][j]] += 1
            elif (i+j)%3 == 2:
                dic3[a[i][j]] += 1
    answer = 10**10
    if n == 1:
        for e in range(c):
            x = e
            temporary = 0
            for color1 in dic1:
                if color1 == x+1:
                    continue
                temporary += dic1[color1] * D[color1-1][x]
            answer = min(answer,temporary)
        print(answer)
        return
    for e in permutations(range(c),3):
        [x, y, z] = e
        temporary = 0
        for color1 in dic1:
            if color1 == x+1:
                continue
            temporary += dic1[color1] * D[color1-1][x]
        for color2 in dic2:
            if color2 == y+1:
                continue
            temporary += dic2[color2] * D[color2-1][y]
        for color3 in dic3:
            if color3 == z+1:
                continue
            temporary += dic3[color3] * D[color3-1][z]
        answer = min(answer,temporary)
    print(answer)            


if __name__ == "__main__":
    main()