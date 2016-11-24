from minheap import *

def heap_minimum(A):
	return A[0]

def heap_extract_min(A):
	mini=A[0]
	A[0]=A[A.heapsize-1]
	A.heapsize=A.heapsize-1
	Min_Heapify(A,0)
	return mini



A=[1,2,3,9,7,8,6,10]
Build_Min_Heap(A)
print(A, A.heapsize)
print(heap_extract_min(A))
print(A, A.heapsize)
print(heap_extract_min(A))
print(A, A.heapsize)
print(heap_extract_min(A))
print(A, A.heapsize)

