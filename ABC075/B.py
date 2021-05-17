h,w = map(int,input().split())	
s = [list(input()) for _ in range(h)]
dx = [-1, 0, 1]
dy = [-1, 0, 1]

for row in range(h):
    for column in range(w):
        if s[row][column] == "#":
            continue
        count = 0
        for x in dx:
            for y in dy:
                if not (0 <= row+x < h and 0 <= column+y < w):
                    continue
                if s[row+x][column+y] == "#":
                    count += 1
        s[row][column] = count

for i in range(h):
    print(''.join(map(str,s[i])))