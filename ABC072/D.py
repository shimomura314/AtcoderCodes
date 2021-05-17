def main():
    n = int(input())
    a = list(map(int,input().split()))
    cnt = 0
    index = 0
    while index < n:
        if a[index] == index+1:
            cnt += 1
            index += 2
        else:
            index += 1
    print(cnt)


if __name__ == "__main__":
    main()