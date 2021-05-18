from collections import deque


def main():
    h,w = map(int,input().split())
    n = int(input())
    a = list(map(int,input().split()))
    answer = [[0 for _ in range(w)] for _ in range(h)]
    color = deque([])
    for i in range(n):
        for _ in range(a[i]):
            color.append(i+1)
    for i in range(h):
        if i%2 == 0:
            for j in range(w):
                answer[i][j] = color.pop()
        else:
            for j in range(w-1, -1, -1):
                answer[i][j] = color.pop()
    for i in range(h):
        print(*answer[i])


if __name__ == "__main__":
    main()