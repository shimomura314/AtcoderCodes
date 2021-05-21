def main():
    n = int(input())
    a = list(map(int,input().split()))
    cnt = 0
    ans = 0
    for i in range(n-1):
        if a[i] < a[i+1]:
            cnt+=1
        else:
            ans += ( cnt * (cnt+1) )//2
            cnt = 0
    ans += (cnt*(cnt+1)) // 2
    print(ans + n)   


if __name__ == "__main__":
    main()