import copy

a = []

def g(x):
    for i in range(-1, 2):
        last = int(x[-1]) + i
        if int(''.join(x)) <= 3234566667 and last != -1 and last != 10:
            y = copy.copy(x)
            y.append(str(last))
            f(y)
    return


def f(x):
    a.append(int(''.join(x)))
    g(x)
    return


f(['1'])
f(['2'])
f(['3'])
f(['4'])
f(['5'])
f(['6'])
f(['7'])
f(['8'])
f(['9'])
a.sort()


def main():
    n = int(input())
    print(a[n-1])


if __name__ == "__main__":
    main()