s = input()
answer = []
for e in s:
    if not e in ["a", "i", "u", "e", "o"]:
        answer.append(e)
print("".join(answer))