class QueueCircular:
  def __init__(self):
    self.front = 0
    self.rear = 0
    self.size = 7
    self.queue = []

  def create(self):
    self.queue = [0 for i in range(0, 7)]

  def enqueue(self, x):
    full_rear = self.rear+1
    if full_rear % self.size == self.front:
      print(f'Queue Full')
    else:
      full_rear = self.rear+1
      self.rear = full_rear%self.size
      self.queue[self.rear] = x
      print(f'Enqueued {x}')

  def dequeue(self):
    if self.rear == self.front:
      print(f'Queue is Empty')
    else:
      full_rear = self.front+1
      self.front = full_rear%self.size
      dequeued = self.queue.pop(self.front)
      print(f'Dequeued {dequeued}')
      
      self.queue.insert(self.front, 0)

  def display(self):
    queue = [i for i in self.queue]
    print(queue)

queue = QueueCircular()
queue.create()

queue.enqueue(31)
queue.enqueue(9)
queue.enqueue(3)
queue.enqueue(3)
queue.enqueue(12)
queue.enqueue(6)
queue.enqueue(1)


queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.display()
