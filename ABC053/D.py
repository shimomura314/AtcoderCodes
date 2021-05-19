from collections import defaultdict

def main():
    n = int(input())
    a = list(map(int,input().split()))
    dic = defaultdict(int)
    for e in a:
        dic[e] += 1
    count = 0
    for key in dic.values():
        count += key-1
    print(n - (count+count%2))


if __name__ == "__main__":
    main()