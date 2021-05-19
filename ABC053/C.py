x = int(input())
if x % 11:
    print(2*(x//11) + (x%11)//7 + 1)
else:
    print(2*(x//11) + (x%11)//7)