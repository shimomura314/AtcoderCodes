n = int(input())
a = list(map(int, input().split()))
winner = [[0, 0], [0, 0]]
for i in range(2**(n-1)):
    if winner[0][0] < a[i]:
        winner[0] = [a[i], i]
for i in range(2**(n-1), 2**n):
    if winner[1][0] < a[i]:
        winner[1] = [a[i], i]
if winner[0][0] < winner[1][0]:
    print(winner[0][1]+1)
else:
    print(winner[1][1]+1)