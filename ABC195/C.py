def main():
    n = int(input())
    answer = 0
    for i in range(3, 16, 3):
        if n >= 10**i:
            answer += n-10**i+1
    print(answer)


if __name__ == "__main__":
    main()