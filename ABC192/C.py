def main():
    n,k = map(int,input().split())
    for _ in range(k):
        sorted_number = sorted(list(str(n)))
        reversed_number = list(reversed(sorted(list(str(n)))))
        n = int(''.join(reversed_number)) - int(''.join(sorted_number))
    print(n)


if __name__ == "__main__":
    main()