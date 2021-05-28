def main():
    m = int(input())
    if m < 100:
        print("00")
    elif m <= 5000:
        print("%02d" %(m//100))
    elif m <= 30000:
        m = m//1000
        print(m+50)
    elif m <= 70000:
        m = m//1000
        m -= 30
        m /= 5
        m += 80
        print(int(m))
    else:
        print(89)


if __name__ == "__main__":
    main()
