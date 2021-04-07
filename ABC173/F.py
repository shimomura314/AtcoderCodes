n = int(input())
answer = n*(n+1)*(n+2)//6

for i in range(n-1):
    u = list(map(int,input().split()))
    answer -= min(u)*(n-max(u)+1)

print(answer)