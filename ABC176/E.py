from collections import defaultdict

def main():
    h,w,m = map(int,input().split())
    dich = {}
    dicw = {}
    a = {}
    for _ in range(m):
        x,y = map(int,input().split())
        if x in dich.keys():
            dich[x] += 1
        else:
            dich[x] = 1
        if y in dicw.keys():
            dicw[y] += 1
        else:
            dicw[y] = 1
        a[(x,y)] = 1
    ansh = 0
    keyh = []
    answ = 0
    keyw = []
    for key in dich.keys():
        if ansh < dich[key]:
            ansh = dich[key]
            keyh = [key]
        elif ansh == dich[key]:
            keyh.append(key)
    for key in dicw.keys():
        if answ < dicw[key]:
            answ = dicw[key]
            keyw = [key]
        elif answ == dicw[key]:
            keyw.append(key)
    b = {}
    for key in keyw:
        b[key] = 1

    for key in keyh:
        for KEY in b.keys():
            if not (key, KEY) in a:
                print(ansh+answ)
                return

    print(ansh+answ-1)


if __name__ == "__main__":
    main()