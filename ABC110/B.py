n,m,X,Y = map(int,input().split())
x = list(map(int,input().split()))	
y = list(map(int,input().split()))	
answer = "War"
for Z in range(X+1,Y+1):
    if max(x) < Z <= min(y):
        answer = "No War"
        break
print(answer)