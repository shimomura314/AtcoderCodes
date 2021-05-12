def function(x, e):
    return len(list(filter(lambda y:y>=x-1,e)))


def main():
    n = int(input())
    e = [0 for _ in range(n+1)]
    for i in range(2,n+1):
        x = i
        for j in range(2,i+1):
            while x % j == 0:
                e[j] += 1
                x //= j
    print( function(75, e) + function(25, e)*(function(3, e)-1) + function(15, e)*(function(5, e)-1) + function(5, e)*(function(5, e)-1)*(function(3, e)-2)//2)


if __name__ == "__main__":
    main()