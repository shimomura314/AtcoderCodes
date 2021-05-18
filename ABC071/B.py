s = list(input())
alpha = [chr(i) for i in range(97, 97+26)]
check = []
for c in alpha:
    if c not in s:
        check += [c]
if not check:
    print("None")
else:
    check.sort()
    print(check[0])