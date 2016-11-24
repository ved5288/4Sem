from minheap import *
import numpy

#def min_dist(a,b)
	

n,m=map(int, raw_input().split())

input_matrix=[[float("inf") for x in range(m)]for x in range(m)]
for x in range(m):
	input_matrix[x][x]=0
	a,b,d=map(int, raw_input().split())
	input_matrix[a-1][b-1]=d
	input_matrix[b-1][a-1]=d

print(input_matrix)
test_cases = int(raw_input())

for x in range(test_cases):
	a,b=map(int, raw_input().split())
	#print(min_dist(a,b))

