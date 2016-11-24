from AVL import AVL_tree
import matplotlib.pyplot as plt
import numpy as np

num_steps = 50 # The value of k (geometric series) 

x = []
y = []

for k in range(num_steps):
	print k
	T = AVL_tree()
	num_ops = int(5*(1.2**k)) # Varying the size of the tree as a geometric series
	for i in range(num_ops):
		op = np.random.randint(0,3) # Choosing an operation
		val = np.random.randint(0,num_ops) # Choosing a key
		if op == 0: # Performing the operation
			T.query(val)
		elif op == 1:
			T.insert(val)
		elif op == 2:
			T.delete(val)
	x.append(np.log2(num_ops))
	y.append(T.ops*1.0/num_ops)

plt.scatter(x, y) # Plotting the result
plt.xlabel('log(#comparisons)')
plt.ylabel('Average time per operation')

par = np.polyfit(x, y, 1, full=True) # Fitting a straight line to the data
slope = par[0][0]
intercept = par[0][1]
w = [slope*i+intercept for i in x]
plt.plot(x, w)

plt.show()			
