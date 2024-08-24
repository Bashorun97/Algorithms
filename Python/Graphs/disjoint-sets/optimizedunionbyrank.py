
class UnionFind:
    
    def __init__(self, size) -> None:
        self.vertices = [i for i in range(size)]
        self.rank = [1] * size
    

    def find(self, x):
        if x == self.vertices[x]:
            return x
        self.vertices[x] = self.find(self.vertices[x])
        return self.vertices[x]
    
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if self.rank[xroot] > self.rank[yroot]:
            self.vertices[yroot] = xroot
        elif self.rank[yroot] > self.rank[xroot]:
            self.vertices[xroot] = yroot
        else:
            self.vertices[xroot] = yroot
            self.rank[yroot] += 1
    

    def connected(self, x, y) -> bool:
        return self.find(x) == self.find(y)


uf = UnionFind(10)
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))
print(uf.connected(5, 7))
print(uf.connected(4, 9))
uf.union(9, 4)
print(uf.connected(4, 9))
print(uf.vertices)