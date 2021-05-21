def main():
    h1,w1 = map(int,input().split())  
    h2,w2 = map(int,input().split())
    if h1!=h2 and h1!=w2 and w1!=h2 and w1!=w2:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    main()
