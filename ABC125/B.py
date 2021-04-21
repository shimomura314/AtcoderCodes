n = int(input())
v = list(map(int,input().split()))	
c = list(map(int,input().split()))	
answer = 0
for i in range(n):
    answer += max(0, v[i]-c[i])
print(answer)