s = list(input())
answer = "yes"
if len(s) != len(list(set(s))):
    answer = "no"
print(answer)