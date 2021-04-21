def main():
    n = int(input())
    a = list(map(int,input().split()))
    count = 0
    for i in range(n):
        if a[i] < 0:
            a[i] *= -1
            count += 1
    a.sort()
    print(sum(a)) if count%2==0 else print(sum(a)-2*a[0])


if __name__ == "__main__":
    main()