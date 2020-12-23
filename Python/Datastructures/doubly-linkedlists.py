class Node:
  
  size = 0
  head = None
  tail = None

  def __init__(self, data):
    self.data = data
    self.back_ref = None
    self.forward_ref = None

class DoublyLinkedList:
  
  def __init__(self):
    self.start_node = None

  def insert_start(self, data):
    new_node = Node(data)
    new_node.back_ref = None
    new_node.forward_ref = self.start_node
    self.start_node = new_node

  def insert_end(self, data):
    new_node = Node(data)
    if self.start_node is None:
      self.start_node = new_node
      return
    n = self.start_node
    while n.forward_ref is not None:
      n = n.forward_ref
    n.forward_ref = new_node
    new_node.backward_ref = n

  def insert_at_a_point(self, data, x):
    node = self.start_node
    while node.forward_ref is not None:
      if node.forward_ref.data == x:
        break
      node = node.forward.ref

    if node.forward.ref is None:
      print('Item not in list')
    else:
      new_node = Node(data)
      new_node.ref = n.


  def traverse(self):
    if self.start_node == None:
      print(f'Empty linked list')
    else:
      node = self.start_node
      while node.forward_ref is not None:
        print(f'{node.data}')
        node = node.forward_ref

new_list = DoublyLinkedList()
#new_list.insert_end(5)
#new_list.insert_end(6)
#new_list.insert_end(10)
new_list.traverse()

