def main():
    n,k = map(int,input().split())
    answer = [1 for _ in range(n)]
    for _ in range(k):
        d = int(input())
        a = list(map(int,input().split()))
        for i in range(d):
            answer[a[i]-1] = 0
    print(sum(answer))    


if __name__ == "__main__":
    main()