n = int(input())
l = list(map(int,input().split()))	
answer = "Yes"
for i in range(n):
    if sum(l)-2*l[i] <= 0:
        answer = "No"
print(answer)