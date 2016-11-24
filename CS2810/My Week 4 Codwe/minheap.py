from heap import *

def Min_Heapify(A,i):
	l=Left(i)
	r=Right(i)
	smallest = i

	if(r<Heap(A).heapsize):
		if(A[r]<A[i]):
			smallest = r
	if((l<Heap(A).heapsize)):
		if(A[l]<A[smallest]):
			smallest = l
	if(smallest!=i):
		temp=A[i]
		A[i]=A[smallest]
		A[smallest]=temp
		Min_Heapify(A,smallest)

def Build_Min_Heap(A):
	i=(Heap(A).length)/2
	while(i>=0):
		Min_Heapify(A,i)
		i-=1


	
