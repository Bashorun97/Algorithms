"""
Time Complexity
    1. Find: O(1)
    2. Union: O(N)
    3. Connected: O(1)

Space Complexity: O(N)
"""

class QuickFind:

    def __init__(self, size: int):
        self.vertexes = [i for i in range(size)]

    
    def find(self, x) -> int:
        return self.vertexes[x]
    

    def union(self, x, y):
        vertex_x = self.find(x)
        vertex_y = self.find(y)

        if vertex_x != vertex_y:
            for i in range(len(self.vertexes)):
                if self.vertexes[i] == vertex_y:
                    self.vertexes[i] = vertex_x
    
    def connected(self, x, y) -> bool:
        return self.find(x) == self.find(y)


qf = QuickFind(10)
qf.union(1, 2)
qf.union(2, 5)
qf.union(5, 6)
qf.union(6, 7)
qf.union(3, 8)
qf.union(8, 9)
print(qf.connected(1, 5))
print(qf.connected(5, 7))  # true
print(qf.connected(4, 9))  # false
qf.union(9, 4)
print(qf.connected(4, 9))  # true
print(qf.vertexes)