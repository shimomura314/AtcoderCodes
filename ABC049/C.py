
s = list(input())
s.reverse()
i = 0
while i < len(s):
    if i <= len(s)-5 and "".join(s[i:i+5]) == "maerd":
        i += 5
    elif i <= len(s)-7 and "".join(s[i:i+7]) == "remaerd":
        i += 7
    elif i <= len(s)-5 and "".join(s[i:i+5]) == "esare":
        i += 5
    elif i <= len(s)-6 and "".join(s[i:i+6]) == "resare":
        i += 6
    else:
        print("NO")
        exit()
print("YES")