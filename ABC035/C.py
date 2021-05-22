def main():
    n,q = map(int,input().split())
    cnt = [0 for _ in range(n+1)]
    ans=[]
    for _ in range(q):
        l,r = map(int,input().split())
        cnt[l-1] += 1
        cnt[r] += 1
    x = 0
    for i in range(n):
        x = (x+cnt[i])%2
        ans.append(str(x))
    print("".join(ans))


if __name__ == "__main__":
    main()