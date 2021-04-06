def main():
    n = int(input())
    a, b = [],[]
    answer = float('inf')
    for _ in range(n):
        x,y = map(int,input().split())
        a.append(x)
        b.append(y)
    
    for i in range(n):
        for j in range(n):
            if i == j:
                answer = min(answer, a[i]+b[i])
            else:
                answer = min(answer, max(a[i],b[j]))
    print(answer)


if __name__ == "__main__":
    main()