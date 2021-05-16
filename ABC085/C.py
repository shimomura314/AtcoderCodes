n,y = map(int,input().split())
y //= 1000

if n*10 == y:
    print(n, 0, 0)
    exit()
if n*10 < y:
    print(-1, -1, -1)
    exit()

for number10 in range(y//10 + 1):
    for number5 in range((y-number10*10)//5 + 1):
        number1 = y - number10*10 - number5*5
        if number10 + number5 + number1 == n:
            print(number10, number5, number1)
            exit()

print(-1, -1, -1)