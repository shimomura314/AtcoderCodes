def f(x):
    x = str(x)
    x = list(map(int, x))
    return sum(x)


a, b = map(int, input().split())
print(max(f(a), f(b)))