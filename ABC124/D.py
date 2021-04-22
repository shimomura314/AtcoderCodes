def main():
    n,k = map(int,input().split())
    s = list(input())
    t = [0]
    for i in range(n-1):
        if s[i] != s[i+1]:
            t.append(i+1)
    length = len(t)
    if length < 2*k - 1:
        print(n)
        return
    for i in range(2*length + 4):
        t.append(n)

    answer = 0
    if s[0] == '1':
        for i in range(length):
            if 2*k+2*i+1 >= len(t):
                break
            answer = max(answer, t[2*k+2*i+1] - t[2*i])
    else:
        answer = t[2*k]
        for i in range(length):
            if 2*k + 2*i + 2 >= len(t):
                break
            answer = max(answer, t[2*k+2*i+2] - t[2*i+1])
    print(answer)


if __name__ == "__main__":
    main()