import bisect
from collections import Counter,defaultdict


def main():
    n = int(input())
    dp = [number for number in range(51)]
    for i in range(50):
        dp[i+1] += dp[i]

    prime_factorization = defaultdict(int)
    check = 2
    while(n!=1 and check <= int(n**0.5)+2):
        while n%check == 0:
            prime_factorization[check] += 1
            n /= check
        check += 1
    if n != 1:
        prime_factorization[n] += 1
    
    answer = 0
    for e in prime_factorization:
        answer += bisect.bisect_right(dp,prime_factorization[e]) - 1
    print(answer)
    
if __name__ == "__main__":
    main()