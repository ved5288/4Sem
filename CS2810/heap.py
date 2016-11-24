def Parent(i):
	return (i-1)/2

def Left(i):
	return 2*i+1

def Right(i):
	return 2*i+2

class Heap:
	#heapsize=0
	#length=0
	A=[]
	
	def __init__(self,array):
		self.heapsize=len(array)
		self.length = len(array)
		self.A=array

