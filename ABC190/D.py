def divisor(n: int):
    divisors = []
    for integer in range(1, int(n**0.5)+1):
        if not n % integer:
            divisors.append(integer)
            divisors.append(n//integer)
    divisors.sort()
    return divisors


n = int(input())
divisors = divisor(2*n)
answer = 0
for integer in divisors:
    pair = 2*n // integer
    a2 = pair + 1 - integer
    if a2 % 2 == 0:
        answer += 1
print(answer)