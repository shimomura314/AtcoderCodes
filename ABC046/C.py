def main():
    n = int(input())
    answer = 0
    t_number,a_number = map(int,input().split())
    for _ in range(n-1):
        t,a = map(int,input().split())
        if t_number%t:
            t_multi = t_number//t + 1
        else:
            t_multi = t_number//t
        if a_number%a:
            a_multi = a_number//a + 1
        else:
            a_multi = a_number//a
        t_number, a_number = t*max(t_multi, a_multi), a*max(t_multi, a_multi)
    print(t_number + a_number)


if __name__ == "__main__":
    main()