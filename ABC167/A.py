def main():
    s = list(input())
    t = list(input())
    
    for number, element in enumerate(s):
        if t[number] != element:
            print('No')
            return
    print('Yes')


if __name__ == "__main__":
    main()