import sys
sys.setrecursionlimit(10**8)


def main():
    h,w = map(int,input().split()) 
    s=[['$' for _ in range(w+2)]]
    for _ in range(h):
        s.append(['$'] + list(input()) + ['$'])
    s.append(['$' for _ in range(w+2)])
    ans = [['.' for _ in range(w)] for _ in range(h)]
    dx = [1,0,-1]
    dy = [1,0,-1]
    for i in range(h):
        for j in range(w):
            flag = 1
            for k in range(3):
                for l in range(3):
                    if s[i+dx[k]+1][j+dy[l]+1] == '.':
                        flag = 0
            if flag:
                ans[i][j]='#'
    for i in range(h):
        for j in range(w):
            flag = 1
            if s[i+1][j+1] == '#':
                for k in range(3):
                    for l in range(3):
                        if not (0 <= i+dx[k] < h and 0 <= j+dy[l] < w):
                            continue
                        if ans[i+dx[k]][j+dy[l]] == '#':
                            flag = 0
                if flag:
                    print('impossible')
                    return
    print('possible')
    for i in range(h):
        print(''.join(ans[i]))


if __name__ == "__main__":
    main()