class Queue:

    def __init__ (self):
        self.queue = []
    
    def queue_empty (self):
        return self.queue == []

    def enqueue (self, data):
        self.queue.append(data)
    
    def dequeue (self):
        data = self.queue[0]
        del self.queue[0]
        return data
    
    def peek (self):
        return self.queue[0]

    def queue_size (self):
        return len(self.queue)

    def show_queue (self):
        return self.queue

#initialize class and methods
init_queue = Queue()

start = init_queue.queue_empty()
print(start)

init_queue.enqueue(12)
init_queue.enqueue(123)
init_queue.enqueue(9)
init_queue.enqueue(33)
init_queue.dequeue()
print(init_queue.show_queue())

print(init_queue.peek())

init_queue.queue_size()
print(init_queue.show_queue())
