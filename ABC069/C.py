def main():
    n = int(input())
    a = list(map(int,input().split()))
    count2 = 0
    count4 = 0
    for e in a:
        if e%2 == 0:
            count2 += 1
        if e%4 == 0:
            count4 += 1
    if n == 3 and count4:
        print("Yes")
        return
    if count2 == n:
        print("Yes")
        return
    if count4 >= n-count2:
        print("Yes")
        return
    if n%2 and n//2 == count4:
        print("Yes")
        return
    print("No")


if __name__ == "__main__":
    main()