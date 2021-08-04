n = int(input())
a = list(map(int, input().split()))

temp = 0
alter = 0
moving_max = -10**10
answer = 0
for e in a:
    alter += e
    moving_max = max(moving_max, alter)
    # print(temp, alter, moving_max)
    answer = max(answer, temp + alter, temp + moving_max)
    temp += alter
print(answer)
