x,y = map(int,input().split())
a = 0
for i in range(y-x-1):
   a += i+1
print(a-x)