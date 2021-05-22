def main():
    s = list(input())
    t = int(input())
    x,y = 0,0
    cnt = 0
    for i in range(len(s)):
        if s[i] == "U":
            y += 1
        elif s[i] == "D":
            y -= 1
        elif s[i] == "L":
            x -= 1
        elif s[i] == "R":
            x += 1
        else:
            cnt += 1
    d = abs(x)+abs(y)
    if t == 1:
        print(d + cnt)
    else:
        if d > cnt:
            print(d-cnt)
        else:
            print((d+cnt)%2)


if __name__ == "__main__":
    main()