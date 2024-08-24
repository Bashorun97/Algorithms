class QuickUnion:

    def __init__(self, size) -> None:
        self.vertices = [i for i in range(size)]

    
    def find(self, x) -> int:
        while x != self.vertices[x]:
            x = self.vertices[x]
        return x


    def union(self, x, y) -> None:
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot != yroot:
            self.vertices[yroot] = xroot
    
    
    def connected(self, x, y) -> bool:
        return self.find(x) == self.find(y)

qu = QuickUnion(10)
qu.union(1, 2)
qu.union(2, 5)
qu.union(5, 6)
qu.union(6, 7)
qu.union(3, 8)
qu.union(8, 9)
print(qu.connected(1, 5))  # true
print(qu.connected(5, 7))  # true
print(qu.connected(4, 9))  # false
qu.union(9, 4)
print(qu.connected(4, 9))  # true
print(qu.vertices)