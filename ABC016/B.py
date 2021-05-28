a,b,c = map(int,input().split())

if (b==0 and a==c) or (a==0 and b==c):
    print("?")
elif a+b == c:
    print("+")
elif a-b == c:
    print("-")
else:
    print("!")