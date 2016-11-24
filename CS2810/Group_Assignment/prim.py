# Input the number of vertices.
n,m = map(int, raw_input("Enter the number of vertices and edges: ").split())

# Initialize the adjacency matrix for the Graph G
G = [[float("inf") for x in range(n)] for x in range(n)]

vertices=[]			# vertices[i]=0 indicates vertex number 'i+1' is not yet included, 1 signifies the other way round.

for i in range(n):
  vertices.append(0)

arr = [[0 for x in range(4)] for x in range(m)]

mini=float("inf")
for i in range(m):
  #input vertex number and weight of the edge
  u,v,d= map(int, raw_input().split())
  arr[i][0]=u
  arr[i][1]=v
  arr[i][2]=d
  if arr[i][2]<G[arr[i][0]-1][arr[i][1]-1] :
    G[arr[i][0]-1][arr[i][1]-1]=G[arr[i][1]-1][arr[i][0]-1]=arr[i][2]

min_tree=[]
min_tree.append(1)		#start index be 1
vertices[0]=1

while len(min_tree)<n :
  i=0
  index=0
  j=0
  mini=float("inf")
  for j in range(len(min_tree)) :
    for i in range(n):
      if vertices[i]==0 :
          if G[min_tree[j]-1][i] < mini :
            mini=G[min_tree[j]-1][i]
	    index=i
            index_2=min_tree[j]-1
  i=0
  for i in range(m):
    if arr[i][2]==mini:
      if (arr[i][0]==index+1 and arr[i][1]==index_2+1) or (arr[i][0]==index_2+1 and arr[i][1]==index+1) :
  	arr[i][3]=1
  min_tree.append(index+1)
  vertices[index]=1
  i=0
        
print(min_tree)
print(arr)

      

