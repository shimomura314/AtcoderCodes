from collections import defaultdict


def main():
    n = int(input())
    common_factor = defaultdict(int)
    s = list(input())
    for e in s:
        common_factor[e] += 1
    for _ in range(n-1):
        s = list(input())
        temp_factor = defaultdict(int)
        for e in s:
            temp_factor[e] += 1
        for key in common_factor.keys():
            common_factor[key] = min(common_factor[key], temp_factor[key])
    answer = []
    for key in common_factor.keys():
        for _ in range(common_factor[key]):
            answer.append(key)
    answer.sort()
    print("".join(answer))


if __name__ == "__main__":
    main()