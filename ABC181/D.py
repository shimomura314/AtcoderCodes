from collections import defaultdict

s = str(input())

if len(s) < 3:
    if int(s)%8 == 0:
        print("Yes")
        exit()
    if len(s) == 2:
        if (int(s[1])*10 + int(s[0])) % 8 == 0:
            print("Yes")
            exit()
    print("No")
    exit()

dict_s = defaultdict(int)
for e in s:
    dict_s[e] += 1
for multi in range(8, 1000, 8):
    dict_8 = defaultdict(int)
    multi = "%03d" % multi
    for e in multi:
        dict_8[e] += 1

    flag = True
    for key in dict_8.keys():
        if dict_8[key] > dict_s[key]:
            flag = False

    if flag:
        print("Yes")
        exit()

print("No")
