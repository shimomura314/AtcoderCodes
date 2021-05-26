def main():
    n=int(input())
    s=list(input())
    if n == 1:
        if s == ["b"]:
            print(0)
            return
        else:
            print(-1)
            return
    cnt=0
    while True:
        N=len(s)
        if s == ["b"]:
            print(cnt)
            return
        if N%6 == 3:
            if s[0] == "a" and s[N-1] == "c":
                s.pop(N-1)
                s.pop(0)
                cnt+=1
            else:
                print(-1)
                return
        elif N%6 == 5:
            if s[0] == "c" and s[N-1] == "a":
                s.pop(N-1)
                s.pop(0)
                cnt+=1
            else:
                print(-1)
                return
        elif N%6 == 1:
            if s[0] == "b" and s[N-1] == "b":
                s.pop(N-1)
                s.pop(0)
                cnt+=1
            else:
                print(-1)
                return
        else:
            print(-1)
            return     


if __name__  ==  "__main__":
    main()