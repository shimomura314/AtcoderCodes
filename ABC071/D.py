mod = 10**9+7

def main():
    n = int(input())
    s = [list(input()) for _ in range(2)]
    if s[0][0] == s[1][0]:
        answer = 3
        index = 1
        vertical = True
    else:
        answer = 6
        index = 2
        vertical = False
    while index < n:
        if s[0][index] == s[1][index]:
            if vertical:
                answer *= 2
            index += 1
            vertical = True
        else:
            if vertical:
                answer *= 2
            else:
                answer *= 3
            index += 2
            vertical = False
        answer %= mod
    print(answer)


if __name__ == "__main__":
    main()