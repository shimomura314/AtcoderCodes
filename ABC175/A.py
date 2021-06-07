s = list(input())
answer = 0
if s[0] == "R":
    answer = 1
if s[1] == "R":
    answer += 1
else:
    if answer == 1:
        print(1)
        exit()
    else:
        pass
if s[2] == "R":
    answer += 1
print(answer)