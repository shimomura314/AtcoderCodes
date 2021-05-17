n = list(input())
pm = ["+", "-"]

for op1 in pm:
    for op2 in pm:
        for op3 in pm:
            s = n[0] + op1 + n[1] + op2 + n[2] + op3 + n[3]
            if eval(s) == 7:
                print(s + "=7")
                exit()