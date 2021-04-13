def main():
    a = str(input())
    if a == 'z':
        print('a')
        return
    x = ord(a) + 1
    print(chr(x))


if __name__ == "__main__":
    main()