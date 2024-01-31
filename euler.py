import numpy as np
import matplotlib.pyplot as plt

mu = 0.5
m = 1

def f1(x,y,t):
	return y  
	
def f2(x,y,t):
	return  -1*x

X=[]
Y=[]
T=[]

def integrate(f1,f2,x,y,t,tf,h):
	while t<tf:
		x=x+h*f1(x,y,t)
		y=y+h*f2(x,y,t)
		t=t+h
		X.append(x)
		Y.append(y)
		T.append(t)
	return np.array(X),np.array(Y),np.array(T)

x0=10000 #initial position
y0=4	 # initial velocity
t0=0
t=300
h=0.01  #step size

X,Y,T=integrate(f1,f2,x0,y0,t0,t,h) 


plt.figure(2)
plt.plot(T,Y,label='$\mu = 0.5 $')
plt.xlabel('time')
plt.ylabel('velocity')
plt.legend()
plt.grid(True)
plt.savefig('velocity vs time.png',dpi=1000)
plt.show()

		
		
		
	
	
	
	
	
	
	
	
