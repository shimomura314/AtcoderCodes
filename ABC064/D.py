def main():
    n = int(input())
    s = input()
    r,l = 0,0
    for i in range(n):
        if s[i] == '(':
            r += 1
        elif s[i] == ')':
            if r == 0:
                l += 1
            else:
                r -= 1

    ans = []
    for i in range(l):
        ans.append('(')
    for i in range(n):
        ans.append(s[i])
    for i in range(r):
        ans.append(')')
    print("".join(ans))


if __name__ == "__main__":
    main()