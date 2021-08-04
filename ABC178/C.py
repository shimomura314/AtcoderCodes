mod = 10**9 + 7
n = int(input())
include_none = 1
include_or = 0
include_and = 0
for _ in range(n):
    include_and = include_and*10 + include_or
    include_or = include_or*9 + include_none*2
    include_none = include_none * 8
    include_and %= mod
    include_or %= mod
    include_none %= mod
print(include_and)
