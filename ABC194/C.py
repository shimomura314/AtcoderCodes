def main():
    n = int(input())
    a = list(map(int,input().split()))
    sumation = sum(a)
    sumation_square = 0
    for i in range(n):
        sumation_square += a[i]**2
    
    print(n*sumation_square - sumation**2)


if __name__ == "__main__":
    main()