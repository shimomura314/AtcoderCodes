n = int(input())
a = list(map(int, input().split()))
answer = 10**10

for bit in range(1, 2**(len(a)-1)):

    borders = []
    for number in range(len(a)-1):
        if number ^ bit:
            borders.append(number)

    print(borders)

    temp = 0
    for i in range(len(borders)-1):
        temp_or = 0
        for e in a[borders[i]:borders[i+1]]:
            temp_or |= e
        temp ^= temp_or

    answer = min(answer, temp)

print(answer)
