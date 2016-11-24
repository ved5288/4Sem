import scipy as *
import numpy as np
import matplotlib.pyplot as plt
def func(x):
	return float(1)/(1+x*x)
x=np.linspace(0,5,num=51)
print x
y=func(x)
plt.figure(0)
plt.plot(x,y)
plt.ylabel(r'Plot of $1/(1+t^{2})$')
plt.show()
plt.close(0)

from scipy.integrate import quad
w=[quad(func,0,a) for a in x]
l=[w[a][0] for a in range(0,51)]
print l
z=arctan(x)
print z
plt.figure(1)
plt.plot(x,l,'ro',label=r'Plot of $integral$')
plt.plot(x,z,'k',label=r'Plot of $taninverse$')
plt.show()
plt.close(1)

err=abs(l-z)
plt.figure(2)
plt.semilogy(x,err,'ro')
plt.show()
plt.close(2)

h=0.1
print h
i=[h*(np.cumsum(func(a))-(1/2)*(func(a)+func(0))) for a in x]
print i

def ftrap(x,y):
	h=x[1]-x[0]
	h=h/2
	x=np.linspace(0,5,num=(5/h)+1)
	y=func(x)
	i=[h*(np.cumsum(func(a))-(1/2)*(func(a)+func(0))) for a in x]
	return((x,y))
eserr=[]
trerr=[]
H=[]
while h>pow(10,-3):
	h=x[1]-x[0]
	i1=[h*(np.cumsum(func(a))-(1/2)*(func(a)+func(0))) for a in x]	
	(x,y)=ftrap(x,y)
	h=x[1]-x[0]
	H.append(h)
	i2=[h*(np.cumsum(func(a))-(1/2)*(func(a)+func(0))) for a in x]
	z=arctan(x)
	es=max(list(abs(np.array(i2)-np.array(i1))))
	tr=max(list(abs(np.array(i2)-np.array(z))))
	eserr.append(es)
	trerr.append(tr)

plt.figure(3)
plt.plot(H,eserr,'+',label='estimated error')
plt.plot(H,trerr,'ro',label='true error')
plt.show()
plt.close(3)



