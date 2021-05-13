def divisor(n: int):
    divisors = [1]
    for integer in range(1, int(n**0.5)+1):
        if not n % integer:
            divisors.append(integer)
            divisors.append(n//integer)
    divisors.sort()
    return divisors


def main():
    n,m = map(int,input().split())
    divisors = divisor(m)
    for i in range(len(divisors)):
        if divisors[len(divisors)-1-i] <= m//n:
            print(divisors[len(divisors)-1-i])
            return


if __name__ == "__main__":
    main()