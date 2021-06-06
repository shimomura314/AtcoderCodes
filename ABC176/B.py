n = int(input())
a = list(map(int,list(str(n))))
if sum(a)%9 == 0:
    print('Yes')
    exit()  
print('No')