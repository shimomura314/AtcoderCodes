n = int(input())
Lucas = [0]*(n+1)
Lucas[0] = 2
Lucas[1] = 1
for i in range(n-1):
    Lucas[i+2] = Lucas[i+1] + Lucas[i]
print(Lucas[n])