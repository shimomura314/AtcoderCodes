import copy
import sys
from itertools import combinations


def main():
    h,w,k = map(int,input().split())
    c = [list(input()) for _ in range(h)]
    answer = 0
    for number_1 in range(h+1):
        for selected_1 in combinations(range(h), number_1):
            for number_2 in range(w+1):
                for selected_2 in combinations(range(w), number_2):
                    copied_c = copy.deepcopy(c)
                    for row in selected_1:
                        for column in range(w):
                            copied_c[row][column] = '.'
                    for column in selected_2:
                        for row in range(h):
                            copied_c[row][column] = '.'
                    count = 0
                    for row in range(h):
                        for column in range(w):
                            if copied_c[row][column] == '#':
                                count += 1
                    if count == k:
                        answer += 1
    print(answer)


if __name__ == "__main__":
    main()