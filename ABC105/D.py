from collections import defaultdict


def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    answer = 0
    count = 0
    dictionary = defaultdict(int)
    dictionary[count] += 1
    for i in range(n):
        count += a[i]
        count %= m
        dictionary[count] += 1
    for e in dictionary:
        answer += dictionary[e]*(dictionary[e]-1)//2
    print(answer)


if __name__ == "__main__":
    main()