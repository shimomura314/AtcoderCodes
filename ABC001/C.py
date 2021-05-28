def main():
    a,b = map(int,input().split())
    ans = ["",0]
    h = ["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW","N"]
    a = (a*10 + 1125) // 2250
    b /= 60
    ans[0] = h[a]
    if 0 <= b and b < 0.25:
        ans[1] = 0
    elif b < 1.55:
        ans[1] = 1
    elif b < 3.35:
        ans[1] = 2
    elif b < 5.45:
        ans[1] = 3
    elif b < 7.95:
        ans[1] = 4
    elif b < 10.75:
        ans[1] = 5
    elif b < 13.85:
        ans[1] = 6
    elif b < 17.15:
        ans[1] = 7
    elif b < 20.75:
        ans[1] = 8
    elif b < 24.45:
        ans[1] = 9
    elif b < 28.45:
        ans[1] = 10
    elif b < 32.65:
        ans[1] = 11
    else:
        ans[1] = 12
    if ans[1] == 0:
        ans[0] = "C"
    print(*ans)


if __name__ == "__main__":
    main()
