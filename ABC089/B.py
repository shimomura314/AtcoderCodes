n = int(input())
s = input().split()
bag = {}
for a in s:
    bag[a] = 1
if len(bag.keys()) == 3:
    print("Three")
else:
    print("Four")