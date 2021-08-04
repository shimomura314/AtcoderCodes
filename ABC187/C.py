n = int(input())
s = [str(input()) for _ in range(n)]
dic = {}
for e in s:
    if e in dic.keys():
        continue
    if "!" + e in dic.keys():
        print(e)
        exit()
    dic[e] = 1
    if "!" in e:
        e = e[1:]
        if e in dic.keys():
            print(e)
            exit()
print("satisfiable")