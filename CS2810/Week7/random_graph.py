import random
from bfs import *

class random_graph :
  def __init__(self,n):
    self.n=n

  def gnp_model(self,p):
    self.p=p
    if(self.p>1):
      raise ValueError("Probability greater than 1")
    self.G=[[0 for x in range(self.n)]for x in range(self.n)]
    for i in range(0,self.n):
      for j in range(i+1,self.n):
        r=random.random()
        if(r<self.p):
          self.G[i][j]=1
	  self.G[j][i]=1
    return self.G

  def deg_specified(self,deg):
    if(deg>self.n-1):
      raise ValueError("Invalid Degree")
    self.G=[[0 for x in range(self.n)]for x in range(self.n)]
    k=deg
    for i in range(0,self.n):
      for j in range(i+1,self.n):
        while(k>0):
          a=random.randint(0,self.n-1)
          if(a!=i):
   	    self.G[i][j]=1
	    self.G[j][i]=1
	    k=k-1
    return self.G

  def max_degree(self):
    maxi=0
    for i in range(self.n):
      count=0
      for j in range(self.n):
        if G[i][j]==1:
	  count+=1
      if count>maxi:
	maxi=count
    return maxi

  def avg_degree(self):
    avg=0
    count=0
    for i in range(self.n):
      for j in range(self.n):
        if self.G[i][j]==1:
	  count+=1
    avg=count/float(self.n)
    return avg

  def diameter(self):
    diameter=0
    for i in range(self.n):
      a=BFS(self.G,self.n,i)
      if a>diameter:
	diameter=a
    return diameter
