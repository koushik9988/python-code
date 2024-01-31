import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

np.random.seed(None)  # different seed in each run

def f(x):
    return np.sin(x)

a = 0
b = np.pi
z = np.linspace(a,b,1000)

n = 60000
x = np.random.uniform(0,b,n)
y = np.random.uniform(0,f(np.pi/2),n)


under_curve = y <=f(x)
counts = sum(under_curve)
integration_value = counts*(b-a)*f(np.pi/2)/n
print(integration_value)
actual_value = -(np.cos(np.pi)-np.cos(0))
print(actual_value)


plt.scatter(x,y)
plt.plot(z,f(z), color = "r")

plt.show()
