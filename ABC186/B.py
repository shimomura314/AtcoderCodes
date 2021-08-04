h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
min_block = 1000
sum_block = 0
for e in a:
    min_block = min(min_block, min(e))
    sum_block += sum(e)
print(sum_block - min_block*h*w)
