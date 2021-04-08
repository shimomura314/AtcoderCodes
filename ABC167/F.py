def main():
    n = int(input())
    s = [list(input()) for _ in range(n)]
    left_count = []
    right_count = []
    leftright_count = []

    min_left,min_right = 10**6,10**6
    for i in range(n):
        t = s[i]
        flag = 0
        l = 0
        r = 0
        for j in range(len(t)):
            if not flag and t[j] == ')':
                r += 1
            elif t[j] == '(':
                flag = 1
                l += 1
            else:
                l -= 1
                if l == 0:
                    flag = 0
        if r == 0 and l == 0:
            continue
        if r == 0:
            left_count.append(l)
        elif l == 0:
            right_count.append(r)
        else:
            leftright_count.append([l,r])
            min_left = min(min_left,l)
            min_right = min(min_right,r)
    L,R = sum(left_count),sum(right_count)
    if not leftright_count:
        if L == R:
            print('Yes')
            return
        else:
            print('No')
            return
    if not (left_count and right_count):
        print('No')
        return
    box1 = []
    box2 = []
    for i in range(len(leftright_count)):
        if L >= leftright_count[i][1] and leftright_count[i][1] <= leftright_count[i][0]:
            L += leftright_count[i][0] - leftright_count[i][1]
        elif leftright_count[i][1] <= leftright_count[i][0]:
            box1.append(leftright_count[i])
        else:
            box2.append(leftright_count[i])
    for i in range(len(box1)):
        L -= box1[i][1]
        if L < 0:
            print('No')
            return
        L += box1[i][0]
    for i in range(len(box2)):
        L -= box2[i][1]
        if L < 0:
            print('No')
            return
        L += box2[i][0]
    if L == R:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()