
from numpy import random
import numpy

from random_graph import *

import matplotlib.pyplot as plt


N = 200			# Limit of |V(G)| upto which we want to test and plot
lower = 10		# Lower limit of |V(G)|
d = 3			# Number of neighbours (some value) for randomly choosing those many neighbours for every graph
max_degree = []		# To plot maximum degree
diameters = []		# To plot diameter
connectivity = []	# To describe if graph is connected or not (1 if connected, 0 if not)

""" Generating based on adding 'd' randomly chosen neighbours"""
for i in range(lower,N):
 	G = random_graph(i).deg_specified(d)				
	max_degree.append(G.max_degree())		
	diameters.append(G.diameter())

	if diameters[-1] == float("inf"):
		connectivity.append(0)
	else:
		connectivity.append(1)

""" Generating based on randomly including edges"""
for i in range(10,N):
	p = 10/float(i)
	G=random_graph(i).gnp_model(p)	
  	max_degree.append(G.max_degree())		
  	diameters.append(G.diameter())
	
	if diameters[-1] == float("inf"):
		connectivity.append(0)
	else:
		connectivity.append(1)
  
""" Plotting based on randomly including edges"""
plt.figure(1)
plt.plot(range(lower,N), max_degree, 'ro',label = 'Maximum Degree')				# red	
plt.plot(range(lower,N), diameters, 'bo',label = 'Diameter')					# blue
plt.plot(range(lower,N), connectivity, 'go',label = 'Connectivity (1 if connected, else 0)')	# green
plt.ylabel('Value')
plt.xlabel('Number of vertices(n)')
plt.xscale('log')
plt.legend()
plt.show()

""" Plotting based on adding 'd' randomly chosen neighbours"""
plt.figure(2)
plt.plot(range(lower,N), max_degree, 'ro',label = 'Maximum Degree')				# red	
plt.plot(range(lower,N), diameters, 'bo',label = 'Diameter')					# blue
plt.plot(range(lower,N), connectivity, 'go',label = 'Connectivity (1 if connected, else 0)')	# green
plt.ylabel('Value')
plt.xlabel('Number of vertices(n)')
plt.xscale('log')
plt.legend()
plt.show()
