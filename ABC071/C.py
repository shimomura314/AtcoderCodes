from collections import defaultdict


def main():
    n = int(input())
    a = list(map(int,input().split()))
    border = defaultdict(int)
    for e in a:
        border[e] += 1
    candidate = []
    for key in border.keys():
        for _ in range(border[key]//2):
            candidate.append(key)
    if len(candidate) < 2:
        print(0)
        return
    candidate.sort(reverse=True)
    print(candidate[0] * candidate[1])


if __name__ == "__main__":
    main()