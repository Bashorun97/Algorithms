class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.front_node = None
    self.rear_node = None

  def enqueue(self, data):
    node = Node(data)
    if self.front_node is None:
      self.front_node = node
      self.rear_node = node
    else:
      self.rear_node.next = node
      self.rear_node = node

  def dequeue(self):
    if self.front_node is None:
      print(f'Queue is Empty')
    else:
      p = self.front_node
      self.front_node = self.front_node.next
      x = p.data
      del x

  def display(self):
    if self.front_node is None:
      print(f'No element to display')
    else:
      p = self.front_node
      count = 1
      while (p != None):
        print(f'Node {count}: {p.data}')
        p = p.next
        count += 1

queue = Queue()

queue.enqueue(19)
queue.enqueue(10)
queue.enqueue(9)
queue.enqueue(21)
queue.enqueue(21)
queue.dequeue()
queue.dequeue()

queue.display()
