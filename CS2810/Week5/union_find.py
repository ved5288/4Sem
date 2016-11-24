
class Node:

  def __init__(self, ops):
    self.parent = self
    self.ops = ops


  def get_root(self):
    self.ops.increment()

    # Implement path compression
    if (self.parent == self):
      return self
    else:
      return self.parent.get_root()


  def union(self, other):
    self.ops.increment()

    # Implement rank based union
    p1 = self.root()
    p2 = other.root()
    p1.parent = p2
