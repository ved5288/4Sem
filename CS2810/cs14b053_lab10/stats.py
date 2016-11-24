from avl import Tree
import matplotlib.pyplot as plt
import numpy as np

k = 45    #Parameter which controls n, n = 5*(1.2)^k

x_array = [int(5*(1.2 ** i)) for i in range(1, k+1)] # Array containing no of nodes (geometric series)
y_array = []

for n in x_array:
  a = 1      # parameter for insertions
  b = 10     # parameter for deletions
  c = 2      # parameter for queries
  #print n
 
  tree = Tree()
  
  insertions = n/a
  for j in xrange(insertions):
    key = np.random.randint(n) + 1  #random key in 1 to n
    tree.insert(key)
  
  queries = n/c
  for j in xrange(queries):
    key = np.random.randint(n) + 1  #random key in 1 to n
    tree.search(key)
    
  deletions = n/b
  for j in xrange(deletions):
    key = np.random.randint(n) + 1  #random key in 1 to n
    tree.delete(key)
  
  ops = tree.counter              # total number of operations
  avg_ops = float(ops)/n            # avg number of operations
  y_array.append(avg_ops)

#Code for plotting

plt.figure(1)
plt.plot(x_array, y_array, 'ro')    
plt.xscale('log')
plt.xlabel('n (log scale)')
plt.ylabel('Average operations')
plt.show()

