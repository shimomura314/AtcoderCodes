def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    m = min(a,b,c,d,e)
    answer = n//m
    if n%m != 0:
        answer += 1
    print(answer+4)


if __name__ == "__main__":
    main()