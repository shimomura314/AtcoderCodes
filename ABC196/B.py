x = str(input())
if '.' not in x:
    print(x)
    exit()
print(int(x.split(".")[0]))