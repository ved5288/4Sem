from geometry import Point
from sorting import AngleComparator


def cross_product(v1,v2):
    return v2.y*v1.x-v1.y*v2.x

def graham_scan(points):

  # Step 1:  compute p0, the bottom-most, left-most point.
  # Step 2:  set that as the first point.
  if (min(points) != points[0]):
    points[0].swap(min(points))

  # Step 3:  sort the rest of the points in increasing order of the angle subtended by the vector (p - p0) with the X-axis.  If two points subtend the same angle, then the closer point should appear first.
 # print("points before sort",points)
  points.sort(cmp=AngleComparator(points[0]))
 # print("points after sort",points)

  # Complete the implementation below


  # Step 4:  (corner case):  if there are less than 3 points, just return the original list.
  if len(points)<3:
      return points
  # Step 5:  Maintain a list to contain the convex hull.
  vertices = []
  
  # Step 6:  Push p0, and the point that subtends the smallest angle.
  vertices.append(points[0])
  vertices.append(points[1])

  index = 2 # index which we are going to test

  # Step 7: Loop while there are points to process
  # Loop Invariant:  
  #  (i)  points[0], points[1], ..., points[curr_index-1] have been processed.
  #  (ii) output is the convex hull of the processed points 
  while index<len(points):
      if cross_product(points[index]-vertices[-1], vertices[-1]-vertices[-2]) <= 0:
          vertices.append(points[index])
          index = index + 1
      else:
          vertices.pop()

  return vertices
    # Step 7.1:  check if the penultimate point in the output, the last point in the output, and the current point form a counter-clockwise turn.  If so, add the current point to the convex hull.  Otherwise, pop the last point from the output (and leave the current point unprocessed for the next iteration).  

    # One corner case to handle is when the three points are collinear.  In this case, the above would handle it correctly, UNLEESS, penultimate is p0.  In this case, the output would be left with less than 2 points.  Handle this case alone by adding the current point to the output.

  # Step 8:  return the constructed convex hull.
  
