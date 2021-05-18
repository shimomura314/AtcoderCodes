odd = list(input())
even = list(input())
answer = []
for num, e in enumerate(even):
    answer.append(odd[num])
    answer.append(e)
if num != len(odd)-1:
    answer.append(odd[-1])
print("".join(answer))