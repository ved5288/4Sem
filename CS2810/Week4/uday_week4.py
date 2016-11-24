def parent(i):
  return i/2
def left_child(i):
  return 2*(i)+1

def right_child(i):
  return 2*(i)+2

def min_heapify(A,i,dist):
  #print 'mh'
  l=left_child(i)
  r=right_child(i)
  if l >= len(A) and r >= len(A):
    #print A
    return 
  if l<= len(A)-1 and dist[A[l]-1]<dist[A[i]-1]:
    smallest= l
  else:
    smallest= i
  if r<= len(A)-1 and dist[A[r]-1]<dist[A[smallest]-1]:
    smallest= r
  if smallest != i:
    temp= A[i]
    A[i]= A[smallest]
    A[smallest]=temp
    min_heapify(A,smallest,dist)
  #print A
  return   
  
def build_min_heap(A,dist):
  n=len(A)/2
  #print n
  i=n
  while i>=0:
    #print 'y'
    min_heapify(A,i,dist)
    i-=1
  return 

def extract_min(A,dist):
  minimum=A[0]
  A[0],A[len(A)-1]=A[len(A)-1],A[0]
  A.pop()
  return minimum

def decrease_priority(A,i,dist):
  while(i>0 and dist[A[(i-1)/2]-1]>dist[A[i]-1]):
    A[i],A[(i-1)/2]=A[(i-1)/2],A[i]
    i = (i-1)/2

def Dj(G,n,source,dest):
  dist=[]
  A=[]
  A.append(source)
  for i in range(1,n+1):
    if (i!= source):
      dist.append(1000)
      A.append(i)
    else:
      dist.append(0)
  #print A
  #print dist
  while len(A)>0:
    minimum=extract_min(A,dist)
    build_min_heap(A,dist)
    #print "nhp", A
    
    for i in range(len(A)):
      if(G[minimum-1][A[i]-1]!=0):
        eff_dist=dist[minimum-1]+G[minimum-1][A[i]-1]
        #print eff_dist
        if(dist[A[i]-1]>eff_dist):
          dist[A[i]-1]=eff_dist
          #print "nd", dist
          decrease_priority(A,i,dist)
  return dist[dest-1]      
  
arr = map(int, raw_input().split())
n=arr[0]
m=arr[1]
G=[[0 for x in range(n)] for x in range(n)]

for i in range(m):
  x,y,z = map(int, raw_input().split())
  #print x,y,z
  G[x-1][y-1]= G[y-1][x-1] = z

#print G

"""for i in range(n):
  G[i][i]= 0"""
k= int(raw_input())
a=[0 for i in range(k)]
b=[0 for i in range(k)]
#print a
#print b
for i in range(k):
  a[i],b[i] = map(int, raw_input().split())
for i in range(k):
  print("%d" %(Dj(G,n,a[i],b[i])))
