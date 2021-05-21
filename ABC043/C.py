import numpy as np

def main():
    n = int(input())
    a = np.array(list(map(int,input().split())))
    cost = float("inf")
    for integer in range(-100, 101):
        to_list = np.ones(n)*integer
        temp = np.sum( (a - to_list) ** 2 )
        cost = min(cost, temp)
    print(int(cost))


if __name__ == "__main__":
    main()