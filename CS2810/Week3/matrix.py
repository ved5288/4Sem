import numpy

def expand(m1,m2) :
  p = m1.shape[0]
  q = m1.shape[1]
  r = m2.shape[1]
  maxi=max(p,q,r)

  n=1
  while(n<maxi):
    n*=2

  new_m1=numpy.zeros((n,n),dtype=m1.dtype)
  new_m2=numpy.zeros((n,n),dtype=m2.dtype)

  for i in range(p) :
    for j in range(q):
      new_m1[i][j]=m1[i][j]

  for i in range(q) :
    for j in range(r):
      new_m2[i][j]=m2[i][j]

  return m1,m2

def modified_mult_mat(m1,m2,p,r):
  n=m1.shape[0]
  m3=numpy.zeros((n,n),dtype=m1.dtype)

  if p==1 and r==1 :
    m3[0][0]=m1[0][0]*m2[0][0]
    return m3

  #Divide m1 into sub-matrices
  a11=m1[0:n/2,0:n/2]
  a12=m1[0:n/2,n/2:n]
  a21=m1[n/2:n,0:n/2]
  a22=m1[n/2:n,n/2:n]

  #Divide m2 into sub-matrices
  b11=m2[0:n/2,0:n/2]
  b12=m2[0:n/2,n/2:n]
  b21=m2[n/2:n,0:n/2]
  b22=m2[n/2:n,n/2:n]

  #Tricky matrices
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

  #The product matrices : Note all of them will be n/2 X n/2
  p1 = modified_mult_mat(a11, s1,n/2,n/2)
  p2 = modified_mult_mat(s2, b22,n/2,n/2)
  p3 = modified_mult_mat(s3, b11,n/2,n/2)
  p4 = modified_mult_mat(a22, s4,n/2,n/2)
  p5 = modified_mult_mat(s5, s6,n/2,n/2)
  p6 = modified_mult_mat(s7, s8,n/2,n/2)
  p7 = modified_mult_mat(s9, s10,n/2,n/2)

  #Sub-matrices of final answer
  c11 = p5 + p4 + p6 - p2
  c12 = p1 + p2
  c21 = p3 + p4
  c22 = p5 + p1 - p3 - p7	

  #Store it in m3
  m3[0:n/2,0:n/2]=c11
  m3[0:n/2,n/2:n]=c12
  m3[n/2:n,0:n/2]=c21
  m3[n/2:n,n/2:n]=c22

  return m3[0:p,0:r]

def mult_mat(m1, m2):

  p = m1.shape[0]
  q = m1.shape[1]
  r = m2.shape[1]


  if (q != m2.shape[0]):
    raise ValueError("matrix dimensions do not match.")

  m1,m2=expand(m1,m2)

  # m1 = (p X q);  m2 = (q X r);  m3 should be (p x r)
  m3 = numpy.zeros((p, r), dtype=m1.dtype)
  
  m3 = modified_mult_mat(m1,m2,p,r) 

  # Remove the following line and add your implementation
  # m[i][j] gives the i-j-th element (zero based index)
  raise NotImplementedError("TODO: Implement this!")

  return m3

