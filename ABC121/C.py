n,m = map(int,input().split())	
price_number = [0 for _ in range(n)]
for i in range(n):
    price_number[i] = list(map(int,input().split()))	
price_number.sort()
price = 0
index = 0

while m > 0:
    if m >= price_number[index][1]:
        price += price_number[index][0]*price_number[index][1]
        m -= price_number[index][1]
        index += 1
    else:
        price += price_number[index][0]*m
        break

print(price)