def main():
    n,k = map(int,input().split())
    s = list(int(input()) for _ in range(n))
    ans = 0
    right = 1
    length = 1
    index = 0
    mul = s[0]
    while index < n:
        while True:
            if right < n and mul*s[right] <= k:
                mul *= s[right]
                right += 1
                length = right-index
            else:
                break
        if s[index] <= mul <= k:
            ans = max(ans,length)
        if s[index] != 0:
            mul /= s[index]
            index += 1
        else:
            print(n)
            return
    print(ans)


if __name__ == "__main__":
    main()