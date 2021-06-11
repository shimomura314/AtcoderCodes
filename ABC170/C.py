x,n = map(int,input().split())
l = list(map(int,input().split()))
for i in range(200):
    if x-i not in l:
        print(x-i)
        exit()
    if x+i not in l:
        print(x+i)
        exit()