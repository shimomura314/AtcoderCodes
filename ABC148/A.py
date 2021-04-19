def main():
    a = int(input())
    b = int(input())
    for number in range(1,4):
        if number != a and number != b:
            print(number)
            return


if __name__ == "__main__":
    main()