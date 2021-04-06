def main():
    n = int(input())
    a = [0 for _ in range(n+1)]
    for i in range(n):
        a[i] = 1/((n-i)/n)
    print(sum(a)-1)


if __name__ == "__main__":
    main()