def main():
    n,k,c = map(int,input().split())
    s = list(input())
    circle = []
    for i in range(n):
        if s[i] == 'o':
            circle.append(i)
    pre_number = -c-10
    count = 0
    front = []
    for i in range(len(circle)):
        if pre_number+c < circle[i]:
            front.append(i)
            pre_number = circle[i]
            count += 1
            if count == k:
                break
    pre_number = n+c+10
    count = 0
    back = []
    for i in range(len(circle)-1,-1,-1):
        if pre_number-c > circle[i]:
            back.append(i)
            pre_number = circle[i]
            count += 1
            if count == k:
                break
    back.sort()
    for i in range(k):
        if back[i] == front[i]:
            print(circle[front[i]]+1)


if __name__ == "__main__":
    main()