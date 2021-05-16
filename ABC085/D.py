def main():
    n,h = map(int,input().split())
    B = []
    a_max = 0
    for _ in range(n):
        a,b = map(int,input().split())
        B.append(b)
        a_max = max(a_max, a)
    b_upper = [b for b in B if b > a_max]
    b_upper.sort(reverse=True)
    answer = 0
    temp = 0
    for b in b_upper:
        temp += b
        answer += 1
        if temp >= h:
            return print(answer)
    answer += (h-temp) // a_max
    if (h-temp)%a_max:
        answer += 1
    print(answer)


if __name__ == "__main__":
    main()