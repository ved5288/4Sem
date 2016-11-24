import sys
n=100
M=5
nk=500
u0=5
p=0.25
Msig=2
Me=10

xx=[0 for a in range(0,n*M)]
u=[0 for a in range(0,n*M)]
dx=[0 for a in range(0,n*M)]

I=[]
X=[]
v=[]

ii=where(xx>0)
X[ii]=0
dx[ii]=u[ii]+0.5
X[ii]=X[ii]+dx[ii]
jj=where(X[ii]>n)
X[jj]=0

u[ii]=u[ii]+1
kk=where(u>u0) #kk is the vector of indices corresponding to energetic electrons
ll=where(rand(len(kk[0]))<=p)
kl=kk[ll]

#for inelastic collision :-
p=0.5
u[kl]=0
x[kl]=x[kl]-dx[kl]*p #p is a random number between 0 and 1. taking it to be 0.5
#change the code here

I.extend(xx[kl].tolist())

m=randn()*Msig+Me


