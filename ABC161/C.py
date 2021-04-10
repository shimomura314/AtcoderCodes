def main():
    n,k = map(int,input().split())
    if n == k or n%k == 0:
        print(0)
        return
    n = n%k
    print(min(n,abs(n-k)))


if __name__ == "__main__":
    main()