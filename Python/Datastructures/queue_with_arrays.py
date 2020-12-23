class Queue:
  def __init__(self):
    self.queue = []
    self.head = 0
    self.tail = 0

  def enqueue(self, data):
    if self.tail == 6: # Queue with length 6
      print(f'Queue Overflow Error')
    else:
      self.queue.append(data)
      self.tail += 1
      print(f'Data enqueued at position {self.tail}')

  def dequeue(self):
    if self.head == self.tail:
      print('Queue underflow Error')
    else:
      popped = self.queue.pop(self.head)
      self.queue.insert(self.head, 0)
      self.head += 1

queue = Queue()
queue.enqueue(43)
queue.enqueue(4)
queue.enqueue(8)
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.enqueue(9)
print(queue.queue)
