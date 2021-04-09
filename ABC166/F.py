def main():
    n,a,b,c = map(int,input().split())
    S = []
    answer = []
    for i in range(n):
        s = input()
        S.append(s)
    for i in range(n):
        s = S[i]
        if s == 'AB':
            if a == 0 and b == 0:
                print('No')
                return
            if a == 0:
                a += 1
                b -= 1
                answer.append('A')
            elif b == 0:
                a -= 1
                b += 1
                answer.append('B')
            elif a == 1 and b == 1 and i < n-1 and s != S[i+1]:
                if S[i+1] == 'AC':
                    a += 1
                    b -= 1
                    answer.append('A')
                else:
                    b += 1
                    a -= 1
                    answer.append('B')
            else:
                if a > b:
                    a -= 1
                    b += 1
                    answer.append('B')
                else:
                    a += 1
                    b -= 1
                    answer.append('A')
        if s == 'AC':
            if a == 0 and c == 0:
                print('No')
                return
            if a == 0:
                a += 1
                c -= 1
                answer.append('A')
            elif c == 0:
                a -= 1
                c += 1
                answer.append('C')
            elif a == 1 and c == 1 and i < n-1 and s != S[i+1]:
                if S[i+1] == 'AB':
                    a += 1
                    c -= 1
                    answer.append('A')
                else:
                    c += 1
                    a -= 1
                    answer.append('C')
            else:
                if a > c:
                    a -= 1
                    c += 1
                    answer.append('C')
                else:
                    a += 1
                    c -= 1
                    answer.append('A')
        if s == 'BC':
            if c == 0 and b == 0:
                print('No')
                return
            if b == 0:
                b += 1
                c -= 1
                answer.append('B')
            elif c == 0:
                b -= 1
                c += 1
                answer.append('C')
            elif b == 1 and c == 1 and i < n-1 and s != S[i+1]:
                if S[i+1] == 'AB':
                    b += 1
                    c -= 1
                    answer.append('B')
                else:
                    c += 1
                    b -= 1
                    answer.append('C')
            else:
                if b > c:
                    b -= 1
                    c += 1
                    answer.append('C')
                else:
                    b += 1
                    c -= 1
                    answer.append('B')
    print('Yes')
    for i in range(n):
        print(answer[i])


if __name__ == "__main__":
    main()