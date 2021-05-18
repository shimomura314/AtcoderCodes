n,T = map(int,input().split())
t = list(map(int,input().split()))
answer = T
for i in range(1, n):
    answer += max(0, min(T, t[i]-t[i-1]))
print(answer)