def main():
    n,m = map(int,input().split())
    if n == 1 and m == 1:
        print(1)
        return
    if n == 1 or m == 1:
        print(n*m - 2)
        return
    print((n-2)*(m-2))


if __name__ == "__main__":
    main()