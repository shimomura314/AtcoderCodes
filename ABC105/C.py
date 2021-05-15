n = int(input())
answer = []
if n == 0:
    answer += [0]
while n != 0:
    if n%(-2) == 0:
        answer += [0]
        n = n//-2
    else:
        answer += [1]
        n = (n-1)//-2

answer.reverse()
answer = ''.join(map(str, answer))
print(answer)