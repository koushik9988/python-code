import numpy as np
import matplotlib.pyplot as plt

def f1(x, y, t):
    return y

def f2(x, y, t):
    return -np.sin(x)



def rk_2(f1, f2, x, y, t,tf, h):
    X = []
    Y = []
    T = []
    while t<tf:
        k11 = h * f1(x, y, t)
        k22 = h * f2(x, y, t)
        k12 = h * f1(x + k11 / 2, y + k22 / 2, t + h / 2)
        k21 = h * f2(x + k11 / 2, y + k22 / 2, t + h / 2)
        y = y + k21
        x = x + k12
        t = t + h
        X.append(x)
        Y.append(y)
        T.append(t)
    return np.array(X),np.array(Y),np.array(T)

def rk_1(f1,f2,x,y,t,tf,h):
    X = []
    Y = []
    T = []
    while t<tf:
        x=x+h*f1(x,y,t)
        y=y+h*f2(x,y,t)
        t=t+h
        X.append(x)
        Y.append(y)
        T.append(t)
    return np.array(X),np.array(Y),np.array(T)

def rk_4(f1,f2,x,y,t,tf,h):
    X = []
    Y = []
    T = []
    while t<tf:
        k1x = h*f1(x,y,t)
        k1y = h*f2(x,y,t)
        k2x = h*f1(x+k1x/2, y+k1y/2,t+h)
        k2y = h*f2(x+k1x/2, y+k1y/2,t+h)
        k3x = h*f1(x+k2x/2, y+k2y/2,t+h)
        k3y = h*f2(x+k2x/2, y+k2y/2,t+h)
        k4x = h*f1(x+k3x,y+k3y,t+h)
        k4y = h*f2(x+k3x,y+k3y,t+h)
        x = x + (k1x + 2*k2x + 2*k3x + k4x)/6
        y = y + (k1y + 2*k2y + 2*k3y + k4y)/6
        t = t + h
        X.append(x)
        Y.append(y)
        T.append(t)
    return np.array(X),np.array(Y),np.array(T)

ti = 0
tf = 100
h = 0.1
x0 = 1
y0 = 1

X1,Y1,T1 = rk_1(f1, f2, x0, y0, ti, tf, h)
X2,Y2,T2 = rk_2(f1, f2, x0, y0, ti, tf, h)
X3,Y3,T3 = rk_4(f1, f2, x0, y0, ti, tf, h)

#plt.plot(T, Y)
plt.plot(T1,X1,label ="rk-1")
plt.plot(T2,X2,label ="rk-2")
plt.plot(T3,X3,label ="rk-4")
plt.xlabel('times')
plt.ylabel('position')
plt.title('Runge-Kutta Method 2nd Order')
plt.legend()
plt.show()
