def main():
    string = list(input().split())
    number = int(string[0])
    integer_part,fractional_part = list(map(int,string[1].split('.')))
    print(number*integer_part + number*fractional_part//100)


if __name__ == "__main__":
    main()