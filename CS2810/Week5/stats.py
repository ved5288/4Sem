from union_find import Node
from numpy import random
import numpy

import matplotlib.pyplot as plt


class OpsClass:
  def __init__(self):
    self.count = 0

  def increment(self):
    self.count = self.count + 1

  def value(self):
    return self.count

def random_queries(n, m):
  ops = OpsClass()
  elements = []
  for i in range(n):
    elements.append(Node(ops))

  for i in range(m):
    j = random.randint(0, 2)
    u = random.randint(0, n)
    v = random.randint(0, n)
    if (j == 1):
      elements[u].union(elements[v])
    else:
      elements[u].get_root()
      elements[v].get_root()

  return ops.count

n = 1000
m_min = 100
m_max = 5000
m_values = numpy.arange(m_min, m_max, 300)
ops_values = []
for i in range(len(m_values)):
  m = m_values[i]
  print("Obtaining stats: (%d elements, %d operations)" % (n, m))
  ops_count = random_queries(n, m)
  print("Ops time: %d" % (ops_count))
  ops_values.append(ops_count)

plt.plot(m_values, ops_values, linewidth=5.0)
plt.ylabel("Time")
plt.xlabel("Ops Count")
plt.title("Union Find Statistics")
plt.show()
