import numpy
""" This program implements Strassen's algorithm, a divide-and-conquer algorithm for faster matrix multiplication. 
Our textbooks cover a simple version of this algorithm in which we find the product AB of two n X n matrices A, B (where n is a power of 2). 
We extend it for more general cases : matrices of unequal sizes, rectangular matrices, or square matrices where n is not a power of 2. 
The only requirement: number of columns of A = number of rows of B"""

""" We need to divide the matrices into four 'quarters'. 
The two auxiliary functions below help in finding submatrices and copying a matrix into a part of other matrix"""

def submatrix(matrix, rlow, rhigh, clow, chigh):
	sub = matrix[rlow:rhigh, clow:chigh]  		# Pretty easy in Python, simply write the row and column limits
	return sub

def copyToSubmatrix(matrix, rlow, rhigh, clow, chigh, submatrix):
	matrix[rlow:rhigh, clow:chigh] = submatrix 	# Easy again

"""The simple version of Strassen's algorithm is written below. Matrices are implemented as numpy matrix objects. 
These objects have many attributes, like a shape[] array and in-built methods to add and subtract matrices like normal variable addition. """

def mult_mat_aux(m1, m2, p, r):
	size =  m1.shape[0]  				# Size of the modified input matrices (square, equal for both, power of 2)
	m3 = numpy.zeros((size, size), dtype=m1.dtype)  # To store the result of multiplying m1 and m2. Elements initialised to zero.

	if p == 1 and r == 1:				# p, r refer to the actually desired dimensions of the answer. p,r <= size
		m3[0][0] = m1[0][0] * m2[0][0]		# Base case : 1 X 1 matrices. Return the product of m1(11) and m2(11)
		return m3

	# Divide: m1 (i.e., A) and m2 (i.e., B) into smaller quarters
	a11 = submatrix(m1, 0, (size/2), 0, (size/2))
	a12 = submatrix(m1, 0, (size/2), (size/2), size)
	a21 = submatrix(m1, (size/2), size, 0, (size/2))
	a22 = submatrix(m1, (size/2), size, (size/2), size)
	b11 = submatrix(m2, 0, (size/2), 0, (size/2))
	b12 = submatrix(m2, 0, (size/2), (size/2), size)
	b21 = submatrix(m2, (size/2), size, 0, (size/2))
	b22 = submatrix(m2, (size/2), size, (size/2), size)

	# Conquer: Find the smaller sums and products recursively.
	s1 = b12 - b22
	s2 = a11 + a12
	s3 = a21 + a22
	s4 = b21 - b11
	s5 = a11 + a22
	s6 = b11 + b22
	s7 = a12 - a22
	s8 = b21 + b22
	s9 = a11 - a21
	s10 = b11 + b12

	#  Note that we call mult_mat(). This method can deal with general input sizes (may be irregular / not power of 2).
	p1 = mult_mat(a11, s1)
	p2 = mult_mat(s2, b22)
	p3 = mult_mat(s3, b11)
	p4 = mult_mat(a22, s4)
	p5 = mult_mat(s5, s6)
	p6 = mult_mat(s7, s8)
	p7 = mult_mat(s9, s10)

	# Combine: the solutions into the submatrices of m3 (i.e., C) and store them in m3.
	c11 = p5 + p4 + p6 - p2
	c12 = p1 + p2
	c21 = p3 + p4
	c22 = p5 + p1 - p3 - p7		
	copyToSubmatrix(m3, 0, (size/2), 0, (size/2), c11)
	copyToSubmatrix(m3, 0, (size/2), (size/2), size, c12)
	copyToSubmatrix(m3, (size/2), size, 0, (size/2), c21)
	copyToSubmatrix(m3, (size/2), size, (size/2), size, c22)
		 
  # Remove the following line and add your implementation
  # m[i][j] gives the i-j-th element (zero based index)
  # raise NotImplementedError("TODO: Implement this!")

	return submatrix(m3, 0, p, 0, r)			# m3, "truncated" to the required dimensions

""" To extend the simple method to multiply A(p X q) and B (q X r) we convert them to square matrices, whose size is a power of 2, big enough to hold the elements of the original matrices. To ensure that this doesn't give a wrong answer, we fill the extra elements with 0s."""

def mult_mat(m1, m2):  
	p = m1.shape[0]    					# Rows of m1
	q = m1.shape[1]						# Columns of m1
	r = m2.shape[1]						# Columns of m2
	if (q != m2.shape[0]):  				# Basic requirement for multiplication not satisfied.
		raise ValueError("matrix dimensions do not match.")

	# m1 = (p X q);  m2 = (q X r);  m3 should be (p x r)
	m1, m2 = resize(m1, m2)
	return mult_mat_aux(m1, m2, p, r)

def resize(m1, m2):   			# Convert m1, m2 to matrices whose size is the smallest power of 2 >= any dimension of the two matrices
	d = max(m1.shape[0], m1.shape[1], m2.shape[1])		# For multiplying, m1.shape[1] = m2.shape[0] so no need to check it again
	size=1							# Start with 2 ** 0	
	while size<d:
		size *= 2

	padded_m1 = pad(m1, size)
	padded_m2 = pad(m2, size)
	return padded_m1,padded_m2

def pad(m, size):			# Generate a square matrix containing the parameter matrix and padded with zeroes 
	p = m.shape[0]
	q = m.shape[1]	
	if size < p or size < q:				# A small check
		print "New matrix can't hold original matrix. No action taken."
		return m

	padded_m = numpy.zeros((size, size), dtype=int)		# This (size X size) numpy matrix is initially 'filled' with zeros
	for i in range(m.shape[0]):
		for j in range(m.shape[1]):
			padded_m[i][j] = m[i][j]

	return padded_m

