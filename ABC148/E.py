def main():
    n = int(input())
    if n%2==0:
        n = n//2
        answer = 0
        while n > 0:
            answer += n//5
            n = n//5
        print(answer)
    else:
        print(0)


if __name__ == "__main__":
    main()