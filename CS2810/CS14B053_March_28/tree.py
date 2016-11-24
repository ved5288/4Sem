LEFT = -1
RIGHT = 1

class node: # Class for each node of the tree
	def __init__(self, k = None):
		self.key = k
		self.left = None
		self.right = None
		self.parent = None
		self.dir = None

class tree: # Class for the tree itself
	def __init__(self):
		self.root = None
		self.size = 0
		self.ops = 0
	
	def _aux_query(self, r, n): # Auxillary query function
		if r is None:
			return None
		if n<r.key:
			self.ops+=1
			return self._aux_query(r.left, n)
		elif r.key<n:
			self.ops+=1
			return self._aux_query(r.right, n)
		else:
			self.ops+=1
			return r

	def _aux_insert(self, r, n): # Auxillary insert function
		if self.root is None:
			self.root = node(n)
			return self.root
		elif n<r.key:
			self.ops+=1
			if r.left is None:
				r.left = node(n)
				r.left.parent = r
				r.left.dir = LEFT
				return r.left
			else:
				return self._aux_insert(r.left, n) # Recurses to the left
		else:
			self.ops+=1
			if r.right is None:
				r.right = node(n)
				r.right.parent = r
				r.right.dir = RIGHT
				return r.right
			else:
				return self._aux_insert(r.right, n) # Recurses to the right

	def _aux_delete(self, q): # Auxillary delete function
		if q.left is None and q.right is None:
			self.ops+=1
			if q.parent is not None:
				if q.dir == RIGHT:
					q.parent.right = None
				else:				
					q.parent.left = None
			q = None
			return self.root
		elif q.left is not None:
				pred = q.left
				while pred.right is not None:
					pred = pred.right
					self.ops+=1
				q.key = pred.key
				return self._aux_delete(pred)
		else:
				succ = q.right
				while succ.left is not None:
					succ = succ.left
					self.ops+=1
				q.key = succ.key
				return self._aux_delete(succ)

	def query(self, n):  # Query function that calls _aux_query()
		return self._aux_query(self.root, n)

	def insert(self, n): # Insert function calling _aux_insert()
		if self._aux_query(self.root, n) is not None:
			return None
		else:
			self.size+=1
		return self._aux_insert(self.root, n)

	def delete(self, n): # Delete function calling _aux_delete()
		q = self.query(n)
		if q is None:
			return None
		else:
			self.size-=1
			return self._aux_delete(q)

	def inorder(self, r): # Inorder traversal (for testing)
		if r is None:
			return
		self.inorder(r.left)
		print r.key
		self.inorder(r.right)


#self.ops is roughly the number of comparisons performed in total
