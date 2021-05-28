def main():
    n,k = map(int,input().split())
    t = sorted([list(map(int, input().split())) for _ in range(n)])

    for i in range(pow(k,n)):
        index = []
        number = 0
        while number != 7:
            index.append(i%k)
            i = i//k
            number += 1
        temp = []
        x = [0 for _ in range(7)]
        for j in range(n):
            temp.append(t[j][index[j]])
        for q in range(n):
            temp_number = 0
            while temp[q] > 0:
                x[temp_number] += temp[q] % 2
                temp_number += 1
                temp[q] = temp[q] //2
        
        flag = True
        for p in range(7):
            if x[p]%2!=0:
                flag = False
        if flag:
            print('Found')
            return
    print('Nothing')        


if __name__ == "__main__":
    main()