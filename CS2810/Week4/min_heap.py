#Implement a min heap

def Parent(i):
  return (i-1)/2

def Left(i):
  return 2*i+1

def Right(i):
  return 2*i+2

class heap:

  def __init__(self,array,dist):
    self.heap=array
    self.heap_size = len(array)
    self.Build_Min_Heap(dist)

  def Build_Min_Heap(self,dist):
    i=self.heap_size/2
    while(i>=0):
      self.Min_Heapify(i,dist)
      i=i-1

  def Min_Heapify(self,i):		#Note : self is a heap
    l=Left(i)
    r=Right(i)
    smallest=i
    if(r<self.heap_size and dist[self.heap[r]]<dist[self.heap[i]]):
      smallest=r
    if(l<self.heap_size and dist[self.heap[l]]<dist[self.heap[smallest]]):
      smallest=l
    if smallest != i :
      self.heap[i],self.heap[smallest]=self.heap[smallest],self.heap[i]
      self.Min_Heapify(smallest,dist)

  def extract_min(self,dist)
    self.heap[0],self.heap[self.heap_size-1]=self.heap[self.heap_size-1],self.heap[0]
    mini=self.heap.pop()
    self.heap_size -=1
    self.Min_Heapify(0,dist)
    return mini

  def insert(self,key,dist):
    self.heap.append(key)
    self.heap_size+=1
    i=self.heap_size - 1
    self.decrease_priority(i,dist)

  def decrease_priority(self,i,dist)
    while(i>=0):
      if dist[self.heap[Parent(i)]] > dist[self.heap[i]] :
        self.heap[Parent(i)],self.heap[i]=self.heap[i],self.heap[Parent(i)]
	i=Parent(i)
      else :
	break

  def empty(self):
    return self.heap_size==0	#returs true / '1' if empty

def dijkstra(graph,n,source,dest)
  dist=[]
  A=[]
  A.append(source)
  
  for i in range(1,n+1):
    if i!= source :
      dist.append(10000)
      A.append(i)
    else
      dist.append(0)

  while len(A)>0:
    mini=heap.extract_min(A,dist)
    # build_min_heap(A,dist)
    #print "nhp", A
    
    for i in range(len(A)):
      if graph[mini-1][A[i]-1] != 0:
        eff_dist=dist[mini-1]+graph[mini-1][A[i]-1]
        #print eff_dist
        if(dist[A[i]-1]>eff_dist):
          dist[A[i]-1]=eff_dist
          #print "nd", dist
          heap.decrease_priority(i,dist)
  return dist[dest-1]      
  

def main():
  n, m = map(int, raw_input().split())
  graph=[[0 for x in range(n)] for x in range(n)]
  
  for i in range(m):
    u,v,d=map(int, raw_input().split())
    graph[u-1][v-1]=graph[v-1][u-1]=d

  t = int(raw_input())
  for i in range(t) :
    a,b=map(int,raw_input().split())
    print("%d"%dijkstra(graph,n,a,b))

