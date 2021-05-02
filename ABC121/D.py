def function(x):
    ans = 0
    if x%4 == 0:
        return 0^x
    elif x%4 == 1:
        return 1
    elif x%4 == 2:
        return 1^x
    elif x%4 == 3:
        return 0


def main():
    a,b = map(int,input().split())
    a -= 1
    print(function(a)^function(b))


if __name__ == "__main__":
    main()