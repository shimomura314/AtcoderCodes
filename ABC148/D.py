def main():
    n = int(input())
    a = list(map(int,input().split()))
    answer = 0
    pre = 1
    for i in range(n):
        if a[i] == pre:
            pre += 1
            answer += 1
    if answer == 0:
        print(-1)
        return
    print(n-answer)


if __name__ == "__main__":
    main()