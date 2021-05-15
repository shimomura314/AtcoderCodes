def main():
    s = list(str(input()))
    K = int(input())
    substrings = []
    for index in range(len(s)):
        for length in range(1, min(len(s)+1, 6)):
            substrings.append("".join(s[index:index+length]))
    substrings = list(set(substrings))
    substrings.sort()
    print(substrings[K-1])


if __name__ == "__main__":
    main()