import sys
from collections import defaultdict
sys.setrecursionlimit(10**8)
mod = 10**9+7


def prime_factorization_dict(n: int): 
    prime_factors = defaultdict(int)
    integer = 2
    while n != 0 and integer <= int(n**0.5)+1:
        while not n%integer:
            prime_factors[integer] += 1
            n //= integer
        integer += 1
    if n != 1:
        prime_factors[n] += 1
    return prime_factors


def main():
    n = int(input())
    prime_factors = defaultdict(int)
    for number in range(1, n+1):
        integer = 2
        while number != 0 and integer <= int(number**0.5)+1:
            while not number%integer:
                prime_factors[integer] += 1
                number //= integer
            integer += 1
        if number != 1:
            prime_factors[number] += 1

    answer = 1
    for value in prime_factors.values():
        answer *= value + 1
        answer %= mod
    print(answer)


if __name__ == "__main__":
    main()