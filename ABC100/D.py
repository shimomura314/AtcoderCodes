import sys
import numpy as np
input = sys.stdin.readline


def main():
    n,m = map(int,input().split())
    xyz = [[] for _ in range(8)]
    pm = [
        [ 1, 1, 1],
        [ 1, 1,-1],
        [ 1,-1, 1],
        [-1, 1, 1],
        [ 1,-1,-1],
        [-1, 1,-1],
        [-1,-1, 1],
        [-1,-1,-1]
        ]
    pm = np.array(pm)
    for _ in range(n):
        x,y,z = map(int,input().split())
        for i in range(8):
            k = np.array([x,y,z])
            xyz[i].append(sum(pm[i]*k))
    answer = -10**20
    for i in range(8):
        X = xyz[i]
        X.sort(reverse=True)
        count = 0
        for j in range(m):
            count += X[j]
        answer = max(answer, count)
    print(answer)


if __name__ == "__main__":
    main()