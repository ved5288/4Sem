class node:
  def __init__(self,value):
    self.key=value
    self.left=None
    self.right=None
    self.height=1

class Tree:
  def __init__(self):
    self.counter=0
    self.size=0
    self.root=None

  def height(self,node):
    if node is None :
      return 0
    return node.height

  def balance_factor(self,node):
    if node is None :
      return 0
    elif self.height(node.left)<self.height(node.right):
      return self.height(node.right)-self.height(node.left)
    return self.height(node.left)-self.height

  def left_rotate(self, x):
    y = x.right
    temp = y.left
    y.left = x
    x.right = temp
    x.height = max(self.height(x.left), self.height(x.right)) + 1
    y.height = max(self.height(y.left), self.height(y.right)) + 1
    return y
    
  def right_rotate(self, y):
    x = y.left
    temp = x.right
    x.right = y
    y.left = temp
    y.height = max(self.height(y.left), self.height(y.right)) + 1
    x.height = max(self.height(x.left), self.height(x.right)) + 1
    return x

  def query(self,key):
    return self.aux_query(self.root,key)

  def aux_query(self,node,key):
    self.counter+=1
    if node is None:
      return None
    if key < node.key :
      return self.aux_query(node.left,key)
    elif node.key < key :
      return self.aux_query(node.right,key)
    return node

  def insert(self,key):
    self.root=self.aux_insert(self.root,key)

  def aux_insert(self,node,key):
    self.counter+=1
    if(node is None):
      self.size+=1
      new_node=node(key)
      return new_node
    elif(key==node.key):
      return node
    elif(key<node.key):
      node.left=self.aux_insert(node.left,key)
    else :
      node.right=self.aux_insert(node.right,key)

    node.height=max(self.height(node.left),self.height(node.right))+1
    bf = self.balance_factor(node)

    if(bf>=2):
      if(key<node.left.key):
        return self.right_rotate(node)
      elif(key>node.left.key):
        node.left = self.left_rotate(node.left)
        return self.right_rotate(node)
      elif(key<node.right.key):
        node.right = self.right_rotate(node.right)
      	return self.left_rotate(node)
      elif(key>node.right.key):
        return self.left_rotate(node)

    return node

  def successor(self,node):
    if node is None :
      return None
    curr_node=node
    while curr_node.left is not None :
      curr_node=curr_node.left
    return curr_node

  def delete(self,key):
    self.root=self.aux_delete(self.root,key)
    
  def aux_delete(self,node,key):
    self.counter+=1
    if node is None:
      return None

    if(key<node.key) :
      node.left=self.aux_delete(node.left,key)
    elif(key>node.key) :
      node.right=self.aux_delete(node.right,key)
    else :
      self.size-=1
      if node.left is None :
        temp=node.right
        node=None
        return temp
      elif node.right is None :
        temp=node.left
        node=None
        return temp
      else :
        temp=self.successor(node.right)
        node.key=temp.key
        node.right=self.aux_delete(node.right,temp.key)
    if node is None :
      return None

    bf=self.balance_factor(node)
    bf_left=self.balance_factor(node.left)
    bf_right=self.balance_factor(node.right)

    if(bf>=2) :
      if bf_left >=0 :
        return self.right_rotate(node)
      if bf_left <0 :
        node.left=self.left_rotate(node.left)
        return self.right_rotate(node)
      if bf_right <=0:
        return self.left_rotate(node)
      if bf_right>0:
        node.right=self.right_rotate(node.right)
        return self.left_rotate(node)

    return node
