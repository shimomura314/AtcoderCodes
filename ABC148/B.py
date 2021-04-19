def main():
    n = int(input())
    [s, t] = list(input().split())
    
    answer = []
    for i in range(n):
        answer.append(s[i])
        answer.append(t[i])
    print(''.join(answer))


if __name__ == "__main__":
    main()