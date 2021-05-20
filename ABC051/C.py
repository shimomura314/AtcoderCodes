sx,sy,tx,ty = map(int,input().split())
x = tx-sx
y = ty-sy
ans = []
for i in range(y):
    ans.append("U")
for i in range(x):
    ans.append("R")
for i in range(y):
    ans.append("D")
for i in range(x+1):
    ans.append("L")
for i in range(y+1):
    ans.append("U")
for i in range(x+1):
    ans.append("R")
ans.append("D")
ans.append("R")
for i in range(y+1):
    ans.append("D")
for i in range(x+1):
    ans.append("L")
ans.append("U")
print(''.join(ans))