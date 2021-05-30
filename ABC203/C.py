
n, k = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(n)]
ab.sort()
money = k
position = 0
for i in range(n):
    position += money
    if position < ab[i][0]:
        print(position)
        exit()
    money = ab[i][1]
print(position+money)