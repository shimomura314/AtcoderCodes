s = list(input())
o0, o1, e0, e1 = 0,0,0,0

for i in range(len(s)//2):
    if s[i*2] == "0":
        o0 += 1
    elif s[i*2] == "1":
        o1 += 1
    if s[i*2+1] == "0":
        e0 += 1
    elif s[i*2+1] == "1":
        e1 += 1
if len(s)%2 == 1:
    if s[len(s)-1] == "0":
        o0 += 1
    else:
        o1 += 1

print( min( o1+e0, e1+o0 ) )