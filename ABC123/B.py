import math

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

orders = [a, b, c, d, e]
answer = 0

for order in orders:
    answer += 10*(math.ceil(order/10))

mod_minus = []
for order in orders:
    minus = 10 - order%10
    if minus == 10:
        mod_minus.append(0)    
    else:
        mod_minus.append(10 - order%10)

print(answer - max(mod_minus))