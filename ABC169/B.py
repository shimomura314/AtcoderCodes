def main():
    n = int(input())
    a = list(map(int,input().split()))
    answer = 1
    a.sort()

    for i in range(n):
        if a[i] == 0:
            print(0)
            return
        answer *= a[i]
        if answer > 10**18:
            print(-1)
            return
    print(answer)


if __name__ == "__main__":
    main()