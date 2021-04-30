def main():
    x,y,z,K = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)

    que = []
    for i in range(x):
        for j in range(y):
            for k in range(z):
                if (i+1)*(j+1)*(k+1) > K:
                    break
                else:
                    que.append(a[i] + b[j] + c[k])
    que.sort(reverse=True)
    for i in range(K):
        print(que[i])


if __name__ == "__main__":
    main()