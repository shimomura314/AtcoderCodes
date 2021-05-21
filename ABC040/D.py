import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

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
    def size(self, x):
        return -self.parents[self.find(x)]
    def same(self, x, y):
        return self.find(x) == self.find(y)
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    def group_count(self):
        return len(self.roots())
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def main():
    n,m = map(int,input().split())
    bridge = []
    for _ in range(m):
        a,b,y = map(int,input().split())
        bridge.append([y,a-1,b-1])
    q = int(input())
    query = []
    for i in range(q):
        v,w = map(int,input().split())
        query.append([w,v-1,i])
    bridge.sort(reverse=True)
    query.sort(reverse=True)

    answer = [0 for _ in range(q)]
    uf = UnionFind(n)
    index_b = 0
    index_q = 0
    while index_q < q:
        QUERY = query[index_q]
        while index_b < m and QUERY[0] < bridge[index_b][0]:
            BRIDGE = bridge[index_b]
            uf.union(BRIDGE[1],BRIDGE[2])
            index_b += 1
        answer[QUERY[2]] = uf.size(QUERY[1])
        index_q += 1
    for i in range(q):
        print(answer[i])


if __name__ == "__main__":
    main()