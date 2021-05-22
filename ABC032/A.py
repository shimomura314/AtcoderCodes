def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
def lcm(a, b):
    return((a*b)//gcd(a,b))


def main():
    a = int(input())
    b = int(input())
    n = int(input())
    c = lcm(a,b)
    if n%c == 0:
        print(n)
    else:
        print(c+c*(n//c))


if __name__ == "__main__":
    main()