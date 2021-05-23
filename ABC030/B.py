n,m = map(int,input().split()) 
a = 6*m
b = 30*n + 0.5*m
c = abs(a-b)%360
print( min(c, abs(360-c)) )