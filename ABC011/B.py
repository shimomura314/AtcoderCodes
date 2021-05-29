def main():
    s = list(input())
    s[0] = s[0].upper()
    if len(s) >= 2:
        for i in range(1,len(s)):
            s[i] = s[i].lower()
    print("".join(s))


if __name__ == "__main__":
    main()