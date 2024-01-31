import numpy as np
import matplotlib.pyplot as plt

N = 100
u = np.zeros(N)
u1 = np.zeros(N)
u2 = np.zeros(N)

x = np.linspace(-2, 2, N)


for i in range(N):
    if x[i] > 1 or x[i] < -1:
        u[i] = 0
    elif -1 <= x[i] <= 1:
        u[i] = 2

for i in range(N):
    if x[i] >= 0:
        u1[i] = 2 - x[i]
    elif x[i] < 0:
        u1[i] = 2 + x[i]
 
for i in range(N):
    u2[i] = 1 - abs(x[i] % 2 - 1)

plt.plot(x, u, label='Rectangular')
plt.plot(x, u1, label=' squre')
plt.plot(x, u2, label='Triangular')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
