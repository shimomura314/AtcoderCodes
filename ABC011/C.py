def main():
    n = int(input())
    ng = [int(input()) for _ in range(3)]
    a = []
    if n in ng:
        print("NO")
        return
    cnt = 0
    while n > 0:
        if n-3 not in ng:
            n -= 3
        elif n-2 not in ng:
            n -= 2
        elif n-1 not in ng:
            n -= 1
        else:
            print("NO")
            return
        cnt += 1
        if cnt > 100:
            print('NO')
            return
    print('YES')


if __name__ == "__main__":
    main()