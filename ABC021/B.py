def main():
    n = int(input())
    x,y = map(int,input().split())
    k = int(input())
    a = list(map(int,input().split()))
    a.append(x)
    a.append(y)
    if len(a) == len(list(set(a))):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()