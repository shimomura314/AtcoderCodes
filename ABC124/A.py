x,y = map(int,input().split())	
if x == y:
    print(2*x)
else:
    print(2*max(x,y)-1)