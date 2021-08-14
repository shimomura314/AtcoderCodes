a, b, c = map(int, input().split())
if c == 0:
    if a >= b+1:
        print("Takahashi")
    else:
        print("Aoki")
if c == 1:
    if a+1 <= b:
        print("Aoki")
    else:
        print("Takahashi")