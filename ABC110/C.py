from collections import defaultdict

s = list(input())
t = list(input())
s.sort()
t.sort()
s1 = defaultdict(int)
t1 = defaultdict(int)
s1_value = []
t1_value = []

for e in s:
    s1[e] += 1
for e in t:
    t1[e] += 1

for value in s1.values():
    s1_value.append(value)
for value in t1.values():
    t1_value.append(value)

s1_value.sort()
t1_value.sort()

if s1_value == t1_value:
    print("Yes")
else:
    print("No")