def main():
    a,b,c,d,e,f = map(int, input().split())
    max_concentration = -1
    answer = [0,0]
    for number1 in range(f//(a*100) + 1):
        for number2 in range((f-100*a*number1)//(b*100) + 1):
            for number3 in range(f//c + 1):
                if (number1*a + number2*b) * 100 + number3*c > f:
                    break
                for number4 in range(f//d + 1):
                    if (number1*a + number2*b) * 100 + number3*c + number4*d > f:
                        break
                    water = (number1*a + number2*b) * 100
                    if not water:
                        continue
                    sugar = number3*c + number4*d
                    if sugar > water*e/100:
                        break
                    if max_concentration < 100*sugar / (water+sugar):
                        max_concentration = 100*sugar / (water+sugar)
                        answer = [water+sugar, sugar]
    print(*answer)


if __name__ == "__main__":
    main()