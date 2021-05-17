x,t = map(int,input().split())
answer = x - t
if answer < 0:
    answer = 0
print(answer)