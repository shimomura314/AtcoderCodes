import copy


def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = copy.copy(a)
    a.sort()
    for i in range(n):
        if b[i] <= a[(n//2)-1]:
            print(a[(n//2)])
        else:
            print(a[(n//2)-1])


if __name__ == "__main__":
    main()