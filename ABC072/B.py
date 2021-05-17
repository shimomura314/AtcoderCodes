s = list(input())
answer = []
for i in range(len(s)//2+len(s)%2):
    answer += s[2*i]
print(''.join(answer))