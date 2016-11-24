LEFT = -1
RIGHT = 1
from random import randint as r

class node: # Class for each node of the tree
	def __init__(self, k = None):
		self.key = k
		self.left = None
		self.right = None
		self.parent = None
		self.dir = None
		self.height = 0
		self.balance = 0


class AVL_tree: # Class for the tree itself
	def __init__(self):
		self.root = None
		self.size = 0
		self.ops = 0

	def inc(self):
		self.ops+=1
	
	def _aux_query(self, r, n): # Auxillary query function
		if r is None:
			self.inc()
			return None
		if n<r.key:
			self.inc()
			return self._aux_query(r.left, n)
		elif r.key<n:
			self.inc()
			return self._aux_query(r.right, n)
		else:
			return r

	def _aux_insert(self, r, n): # Auxillary insert function
		if self.root is None:
			self.inc()
			self.root = node(n)
			return self.root
		elif n<r.key:
			self.inc()
			if r.left is None:
				self.inc()
				r.left = node(n)
				r.left.parent = r
				r.left.dir = LEFT
				if r.right is None:
					self.inc()
					r.height = 1 + r.left.height
					r.balance = 1 + r.left.height
				else:
					r.height = 1 + max(r.left.height, r.right.height)
					r.balance = r.left.height - r.right.height
				return r.left
			else:
				ins = self._aux_insert(r.left, n) # Recurses to the left
				if r.right is None:
					self.inc()
					r.height = 1 + r.left.height
					r.balance = 1 + r.left.height
				else:
					r.height = 1 + max(r.left.height, r.right.height)
					r.balance = r.left.height - r.right.height
				return ins

		else:
			if r.right is None:
				self.inc()
				r.right = node(n)
				r.right.parent = r
				r.right.dir = RIGHT
				if r.left is None:
					self.inc()
					r.height = 1 + r.right.height
					r.balance = -(1 + r.right.height)
				else:
					r.height = 1 + max(r.left.height, r.right.height)
					r.balance = r.left.height - r.right.height
				return r.right
			else:
				ins = self._aux_insert(r.right, n) # Recurses to the right
				if r.left is None:
					self.inc()
					r.height = 1 + r.right.height
					r.balance = -(1 + r.right.height)
				else:
					r.height = 1 + max(r.left.height, r.right.height)
					r.balance = r.left.height - r.right.height
				return ins

	def _aux_delete(self, q): # Auxillary delete function
		if q.left is None and q.right is None:
			self.inc()
			if q.parent is not None:
				self.inc()
				if q.dir == RIGHT:
					self.inc()
					q.parent.right = None
					lh = -1 if q.parent.left is None else q.parent.left.height
					q.parent.height = 1 + lh
					q.parent.balance = 1 + lh
				else:				
					q.parent.left = None
					rh = -1 if q.parent.right is None else q.parent.right.height
					q.parent.height = 1 + rh
					q.parent.balance = -(1 + rh)

			temp = q.parent
			q = None
			return temp
		elif q.left is not None:
			self.inc()
			pred = q.left
			while pred.right is not None:
				pred = pred.right
				self.inc()
			q.key = pred.key
			d = self._aux_delete(pred)
			lh = -1 if pred.left is None else pred.left.height
			rh = -1 if pred.right is None else pred.right.height
			pred.height = 1 + max(lh, rh)
			pred.balance = lh - rh
			return d
		else:
			succ = q.right
			while succ.left is not None:
				succ = succ.left
				self.inc()
			q.key = succ.key
			d = self._aux_delete(succ)
			lh = -1 if succ.left is None else succ.left.height
			rh = -1 if succ.right is None else succ.right.height
			succ.height = 1 + max(lh, rh)
			succ.balance = lh - rh
			return d


	def left_rotate(self, r):
		a = r
		b = a.left
		c = b.left
		d = b.right
		e = a.right

		b.right = a
		a.left = d
		b.parent = a.parent
		a.parent = b
		if d is not None:
			self.inc()
			d.parent = a
			d.dir = LEFT
		b.dir = a.dir
		a.dir = RIGHT
		ch = -1 if c is None else c.height
		dh = -1 if d is None else d.height
		eh = -1 if e is None else e.height
		a.height = 1 + max(dh, eh)
		b.height = 1 + max(ch, a.height)
		a.balance = dh - eh
		b.balance = ch - a.height
		if b.parent is not None:
			self.inc()
			if b.dir == LEFT:
				self.inc()
				b.parent.left = b
			else:
				b.parent.right = b
		else:
			self.root = b
		self.height_adjust(b)
		return

	def right_rotate(self, r):
		a = r
		b = a.right
		c = b.right
		d = b.left
		e = a.left

		b.left = a
		a.right = d
		b.parent = a.parent
		a.parent = b
		if d is not None:
			self.inc()
			d.parent = a
			d.dir = RIGHT
		b.dir = a.dir
		a.dir = LEFT
		ch = -1 if c is None else c.height
		dh = -1 if d is None else d.height
		eh = -1 if e is None else e.height
		a.height = 1 + max(dh, eh)
		b.height = 1 + max(ch, a.height)
		a.balance = eh - dh
		b.balance = a.height - ch
		if b.parent is not None:
			self.inc()
			if b.dir == LEFT:
				self.inc()
				b.parent.left = b
			else:
				b.parent.right = b
		else:
			self.root = b
		self.height_adjust(b)
		return

	def height_adjust(self, node):
		lh = -1 if node.left is None else node.left.height
		rh = -1 if node.right is None else node.right.height
		node.height = 1 + max(lh, rh)
		node.balance = lh - rh
		if node.parent is not None:
			self.height_adjust(node.parent)
		return

	def rebalance(self, node):
		while node is not None and node.balance in [-1, 0, 1]:
			node = node.parent
		if node is not None:
			self.inc()
			if node.balance == 2:
				self.inc()
				if node.left.balance < 0:
					self.inc()
					self.right_rotate(node.left)
				self.left_rotate(node)
			elif node.balance == -2:
				if node.right.balance > 0:
					self.inc()
					self.left_rotate(node.right)
				self.right_rotate(node)					

	def query(self, n):  # Query function that calls _aux_query()
		return self._aux_query(self.root, n)

	def insert(self, n): # Insert function calling _aux_insert()
		ins = self._aux_query(self.root, n)
		if ins is not None:
			self.inc()
			return None
		else:
			self.size+=1
			ins = self._aux_insert(self.root, n)
			self.height_adjust(ins)
			self.rebalance(ins)					

	def delete(self, n): # Delete function calling _aux_delete()
		q = self.query(n)
		if q is None:
			self.inc()
			return None
		else:
			self.size-=1
			leaf = self._aux_delete(q)
			if leaf is not None:
				self.inc()
				self.height_adjust(leaf)
				self.rebalance(leaf)

	def _inorder(self, r): # Inorder traversal (for testing)
		if r is None:
			return
		print r.key
		self._inorder(r.left)
		self._inorder(r.right)

	def inorder(self):
		self._inorder(self.root)
