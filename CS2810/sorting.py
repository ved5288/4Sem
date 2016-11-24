"""
Sorting module:  defines a point data-type to represent a 2-D point
"""

from geometry import Point
import math

def bottom_left_compare(p, q):
  """
  A simple (lexicographic) ordering of the points based on the y-coordinate, and then by the x-coordinate.  Returns -1 if p < q; 0 if p == q; and 1 if p > q.
  """
  if (p < q):
    return -1
  if (p == q):
    return 0
  return 1


class AngleComparator:
  """
  This class (should) return a comparison function that compares p and q based on the angle it makes with the line parallel to the X-axis, passing through p0.  You may assume that the input points, (p, and q) are above / on-level to p0.  If p0 and the two points are collinear, then the point nearer to p0 is considered to be smaller.
  """

  def __init__(self, p0):
    """
    The constructor takes a point against which the comparisons are to be made.
    """
    self.p0 = p0


  def __call__(self, p, q):
    """
    Implements function calling semantics:  a = AngleComparator(p0); a(p, q) should return -1, 0 or 1.
    """  

    # We want to make sure p0 is always the smallest point.  So whenever one of the arguments is p0, we return a value accordingly.
    if (p == self.p0 and q == self.p0):
      return 0
    if (p == self.p0):
      return -1
    if (q == self.p0):
      return 1
    r=math.atan((p.y-self.p0.y)/(p.x-self.p0.x))
    s=math.atan((q.y-self.p0.y)/(q.x-self.p0.x))

    if r<0: r = r + math.pi
    if s<0: s = s + math.pi

    if r>s:
        return 1
    else if r == s:
        return 0
    else:
        return -1

