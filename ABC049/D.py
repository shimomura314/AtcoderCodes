from collections import defaultdict

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
    n,k,l = map(int,input().split())
    UF = UnionFind(2*n)
    for _ in range(k):
        p,q = map(int,input().split())
        UF.union(p-1, q-1)
    for _ in range(l):
        r,s = map(int,input().split())
        UF.union(r+n-1 ,s+n-1)

    root_s = defaultdict(int)
    root = []
    for i in range(n):
        root.append(str(UF.find(i)) + " " + str(UF.find(i+n)))
        root_s[root[i]] += 1
    
    ans = [0 for _ in range(n)]
    for i in range(n):
        ans[i] = root_s[root[i]]
    print(*ans) 


if __name__ == "__main__":
    main()
