n = int(input())
answer = n
for num in range(1, n+1):
    if "7" in str(num):
        answer -= 1
    else:
        while num:
            if num % 8 == 7:
                answer -= 1
                break
            num //= 8
print(answer)
