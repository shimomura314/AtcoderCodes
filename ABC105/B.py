n = int(input())
answer = "No"
for i in range(n//7+1):
    if (n-i*7)%4 == 0:
        answer = "Yes"
        break
print(answer)