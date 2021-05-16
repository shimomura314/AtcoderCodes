a,b = map(int,input().split())
count = 0

for i in range(a,b+1):
    s = list(str(i))
    flag = 1
    for j in range(len(s)//2):
        if s[j] != s[len(s)-1-j]:
            flag = 0
            break
    count += flag

print(count)