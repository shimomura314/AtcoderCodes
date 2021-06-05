from collections import defaultdict

n = int(input())
dic = defaultdict(int)
for _ in range(n):
    dic[input()] += 1

print('AC x', dic['AC'])
print('WA x', dic['WA'])
print('TLE x', dic['TLE'])
print('RE x', dic['RE'])