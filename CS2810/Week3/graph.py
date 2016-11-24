class Distance(int):
  def __new__(cls, *args, **kwargs): 
    return  super(Distance, cls).__new__(cls, *args, **kwargs)

  def __add__(self, x):
    return Distance(max(self,x))

  def __mul__(self, x):
    return Distance(int.__add__(self, x))

