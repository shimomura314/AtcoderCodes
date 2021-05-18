n = int(input())
a = [int(input()) for _ in range(n)]
# for i in range(n):
    # a[i]=int(input())
if sum(a)%10 != 0:
    print(sum(a))
    exit()
a.sort()
for i in range(n):
    if (sum(a)-a[i])%10 != 0:
        print(sum(a)-a[i])
        exit()
print(0)