s = list(map(int,input().split()))	
k = int(input())
s.sort()
print( s[2]*(2**k) + s[0]+ s [1])