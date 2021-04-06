def main():
    n = int(input())
    answer = 100 - n%100
    print(answer) if answer != 0 else print(100)


if __name__ == "__main__":
    main()