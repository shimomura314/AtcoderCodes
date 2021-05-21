def main():
    n,q = map(int,input().split())  
    ans = [0 for _ in range(n)]
    for _ in range(q):
        l,r,t = map(int,input().split())
        for i in range(l-1,r):
            ans[i] = t
    for i in range(n):
        print(ans[i])


if __name__ == "__main__":
    main()
