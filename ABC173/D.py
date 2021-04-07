from collections import deque


def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(reverse = True)
    
    que = deque()
    answer = 0
    que.append(a[0])
    for i in range(1,n):
        answer += que.popleft()
        que.append(a[i])
        que.append(a[i])
    print(answer)


if __name__ == "__main__":
    main()