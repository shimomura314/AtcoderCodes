def main():
    t = int(input())
    n = int(input())
    a = list(map(int,input().split())) 
    m = int(input())
    b = list(map(int,input().split())) 
    if n < m:
        print("no")
        return
    ab = []
    remain = 0
    done = []
    for i in range(n):
        ab.append([a[i], "a"])
    for i in range(m):
        ab.append([b[i], "b"])
    ab.sort()
    for i in range(len(ab)):
        while True:
            if i < len(ab) and len(done)>0 and ab[i][0]>done[0]:
                done.pop(0)
                remain -= 1
            else:
                break
        if ab[i][1] == "a":
            remain += 1
            done.append(ab[i][0]+t)
        if ab[i][1] == "b":
            if remain == 0:
                print("no")
                return
            remain -= 1
            done.pop(0)
    print("yes") 


if __name__ == "__main__":
    main()