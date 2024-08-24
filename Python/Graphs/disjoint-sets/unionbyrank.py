
class UnionByRank:

    def __init__(self, size):
        self.vertices = [i for i in range(size)]
        self.rank = [1] * size
    

    def find(self, x):
        while x != self.vertices[x]:
            # Get the root node and assign to x
            x = self.vertices[x]
        return x
    

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot != yroot:
            if self.rank[xroot] > self.rank[yroot]:
                self.vertices[yroot] = xroot
            elif self.rank[yroot] > self.rank[xroot]:
                self.vertices[xroot] = yroot
            else:
                self.vertices[xroot] = yroot
                self.rank[yroot] += 1


    def connected(self, x, y) -> bool:
        return self.find(x) == self.find(y)


ur = UnionByRank(10)
ur.union(1, 2)
ur.union(2, 5)
ur.union(5, 6)
ur.union(6, 7)
ur.union(3, 8)
ur.union(8, 9)
print(ur.connected(1, 5))  # true
print(ur.connected(5, 7))  # true
print(ur.connected(4, 9))  # false

ur.union(9, 4)
print(ur.connected(4, 9))  # true
print(ur.vertices)