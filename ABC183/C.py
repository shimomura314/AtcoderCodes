from itertools import permutations

n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]

li = [i for i in range(1, n)]
answer = 0

for pair in permutations(li, len(li)):
    pre = 0
    cost = 0
    for index in range(len(pair)):
        to = pair[index]
        cost += t[pre][to]
        pre = to
        if index == len(pair)-1:
            cost += t[to][0]
    if cost == k:
        answer += 1
print(answer)
