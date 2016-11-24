from graph import Distance
from matrix import mult_mat
import numpy

m1 = m2 = m3 = 0
def setup_random(d1, d2, d3):
  global m1, m2
  m1 = numpy.random.randint(0, 2, (d1, d2))
  m2 = numpy.random.randint(0, 2, (d2, d3))

def multiply():
  global m1, m2, m3
  m3 = mult_mat(m1, m2)

def power(matrix, n):
  if (n == 1):
    return matrix
  t = power(matrix, n/2)
  if (n%2 == 0):
    return mult_mat(t, t)
  else
    return mult_mat(matrix, mult_mat(t, t))


N = 8
trials = 1

for t in range(N):
  dim = 2**t
  dim1 = dim2 = dim3 = dim
  for i in range(trials):
    setup_random(dim1, dim2, dim3)
    multiply()
    if (check() != True):
      print("Error!\nDimensions: (%d x %d) X (%d x %d)" % (dim1, dim2, dim2, dim3))
      sys.exit("Program failed!")
