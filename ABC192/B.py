def main():
    s = list(input())
    flag = True
    for i in range(len(s)):
        n = ord(s[i])
        if i%2 == 0 and 65 <= n <= 90:
            flag = False
            break
        if i%2 == 1 and 97 <= n <= 122:
            flag = False
            break
    print('Yes') if flag else print('No')


if __name__ == "__main__":
    main()