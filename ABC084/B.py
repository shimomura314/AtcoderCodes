a,b = map(int,input().split())
s = list(input())
if s[a] != "-" or "-" in s[:a] or "-" in s[a+1:]:
    print("No")
    exit()
print("Yes")