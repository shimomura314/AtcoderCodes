class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}


def main():
    n,m = map(int,input().split())
    p = list(map(int,input().split()))
    UF = UnionFind(n)
    for i in range(m):
        x,y = map(int,input().split())
        UF.union(x-1, y-1)
    answer = 0
    for i in range(n):
        if UF.find(p[i]-1) == UF.find(i):
            answer += 1
    print(answer)


if __name__ == "__main__":
    main()