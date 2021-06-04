def divisor(n: int):
    divisors = []
    for integer in range(1, int(n**0.5)+1):
        if not n % integer:
            divisors.append(integer)
            divisors.append(n//integer)
    divisors.sort()
    return divisors


def main():
    n = int(input())
    divisors = divisor(n)
    divisors = list(set(divisors))
    divisors.sort()
    for e in divisors:
        print(e)


if __name__ == "__main__":
    main()