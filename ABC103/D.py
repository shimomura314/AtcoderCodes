def main():
    n,m = map(int,input().split())
    ab = []
    for _ in range(m):
        ab.append(list(map(int,input().split())))
    ab.sort()
    Right = ab[0][1]
    count = 1
    for i in range(m):
        if ab[i][1] < Right:
            Right = ab[i][1]
        if Right <= ab[i][0]:
            count += 1
            Right = ab[i][1]
    print(count)


if __name__ == "__main__":
    main()