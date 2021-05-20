import math

def main():
    a,b,weight = map(int,input().split())
    weight *= 1000
    
    if weight < a:
        print('UNSATISFIABLE')
        return
    
    maximam = weight//a
    if weight%a == 0 or weight-maximam*a <= maximam*(b-a):
        pass
    elif (maximam-1)*a > weight:
        print('UNSATISFIABLE')
        return
    else:
        maximam -= 1

    minimam = int(math.ceil(weight/b))
    if weight%b == 0:
        minimam = weight//b
    elif (b*minimam-weight) <= (b-a)*minimam:
        pass
    elif (minimam-1)*b < weight:
        print('UNSATISFIABLE')
        return
    else:
        minimam += 1

    print(minimam, maximam)


if __name__ == "__main__":
    main()