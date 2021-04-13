from collections import defaultdict


def main():
    n,m = map(int,input().split())
    dic = defaultdict(int)
    x = 0
    y = 0
    for _ in range(m):
        ps = list(input().split())
        ps[0] = int(ps[0])
        if ps[1] == 'WA':
            dic[ps[0]] += 1
        elif ps[1] == 'AC' and dic[ps[0]]<10**6:
            x += 1
            y += dic[ps[0]]
            dic[ps[0]] = 10**6
    print(x, y)



if __name__ == "__main__":
    main()