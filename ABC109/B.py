n = int(input())
said = {}
answer = "Yes"
s = input()
said[s] =  1
pre_word = s
for _ in range(n-1):
    s = input()
    if s not in said:
        if pre_word[len(pre_word)-1] == s[0]:
            said[s]=1
            pre_word = s
        else:
            answer = "No"
            break
    else:
        answer = "No"
        break


print(answer)