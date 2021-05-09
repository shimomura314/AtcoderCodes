def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    x = [0 for _ in range(41)]
    y = [0 for _ in range(41)]
    index = 0
    while k > 0:
        x[index] += k%2
        k //= 2
        index += 1
    for i in range(n):
        index = 0
        while a[i] > 0:
            y[index] += a[i]%2
            a[i] //= 2
            index += 1
    answer = 0
    key1 = 0
    key2 = 0
    for i in range(40,-1,-1):
        flag = (y[i] >= (n/2))
        if x[i]>0 or y[i]>0:
            key2 = 1
        if x[i] == 1 and flag and key2 and (not key1):
            key1 = True
            answer += pow(2,i)*y[i]
        elif key2:
            if flag or (x[i] == 0 and (not key1)):
                answer += pow(2,i)*y[i]
            else:
                answer += pow(2,i)*(n-y[i])
    print(answer)


if __name__ == "__main__":
    main()