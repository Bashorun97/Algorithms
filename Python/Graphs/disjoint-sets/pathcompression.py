class PathCompression:

    def __init__(self, size):
        self.vertices = [i for i in range(size)]
    

    def find(self, x) -> int:
        if x == self.vertices[x]:
            return x
        
        self.vertices[x] = self.find(self.vertices[x])
        return self.vertices[x]
    
    
    def union(self, x, y) -> None:
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot != yroot:
            self.vertices[yroot] = xroot
        
    
    def connected(self, x, y) -> bool:
        return self.find(x) == self.find(y)


pc = PathCompression(10)

pc.union(1, 2)
pc.union(2, 5)
pc.union(5, 6)
pc.union(6, 7)
pc.union(3, 8)
pc.union(8, 9)
print(pc.connected(1, 5))
print(pc.connected(5, 7))
print(pc.connected(4, 9))

pc.union(9, 4)
print(pc.connected(4, 9))
print(pc.vertices)