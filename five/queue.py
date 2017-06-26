class Queue(object):

	def __init__(self):
		self.Queue = []

	def enqueue(self, order):
		self.Queue.append(order)

	def dequeue(self):
		return self.Queue.pop(0)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
print(q.dequeue()) 
print(q.dequeue()) 