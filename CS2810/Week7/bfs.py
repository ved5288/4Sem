class Queue:
	def __init__(self, size):
		self.n = size							# Max. no. of elements in queue
		self.curr = 0							# No. of elements currently in queue	
		self.head = 0							# Position of next element to be removed
		self.tail = 0							# Position where next element is to be added
		self.q = ['e' for i in range(self.n)]				# Queue : 'e' for empty

	def enqueue(self,x):
		if self.curr == self.n:						# Error checking
			print "Error. Queue full."

		else:
			self.q[self.tail] = x					# Add element
			self.curr += 1

			if self.tail == (self.n-1):				# Move tail pointer ahead
				self.tail = 0
			else:
				self.tail += 1

	def dequeue(self):
		x = 0
		if self.curr == 0:						# Error checking
			print "Error. Queue empty."

		else:
			x = self.q[self.head]					# Element to remove
			self.curr -= 1
			self.q[self.head] = 'e'					# Remove it
		
			if self.head == (self.n-1):				# Move head pointer ahead
				self.head = 0
			else:
				self.head += 1

		return x							# The removed element



def BFS(G,n,vertex):
  color=[0 for x in range(n)]
  d=[float("inf") for x in range(n)]
  color[vertex]=1
  d[vertex]=0

  Q=Queue(n)			# create the queue
  Q.enqueue(vertex)
  while len(Q.queue)>0:
    u=Q.dequeue()
    for i in range(n):
      if G[i][u]==1:
        if color[i]==0:
	  color[i]=1
	  d[i]=d[u]+1
	  Q.enqueue(v)
    Q.dequeue()
    color[u]=2

  maxi=0
  for i in range(m):
    if d[i]>maxi:
      maxi=d[i]
  return maxi			# returns the maximum length from the vertex to any node
