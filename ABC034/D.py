import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


def main():
    # global wp,n,k
    n,k = map(int,input().split())
    wp = []
    for _ in range(n):
        wp.append(list(map(int,input().split())))
    
    ok = 0
    ng = 100
    while abs(ok-ng) > 0.00001:
        mid = (ng+ok)/2
        temp = []
        
        for i in range(n):
            [w,p] = wp[i]
            temp.append(w*(p-mid))
        temp.sort(reverse=True)
        count = 0
        for i in range(k):
            count += temp[i]
        if count >= 0:
            ok = mid
        else:
            ng = mid
    print(ok)


if __name__ == "__main__":
    main()