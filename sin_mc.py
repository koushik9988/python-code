import numpy as np
import matplotlib.pyplot as plt

np.random.seed(None)  # different seed in each run


def f(x):
    return np.sin(x)

def f1(x):
    return -np.cos(x)

a = 0
b = np.pi
c = (3*np.pi)/2
print(f(c))
n_1 = 1000
n_2 = 1000


x = np.random.uniform(a, b, n_1)
y = np.random.uniform(f(a), f(b/2), n_1)
x1 = np.random.uniform(b, c, n_2)
y1 = np.random.uniform(f(b), f(c), n_2)

# between 0 and pi
under_curve_1 = y <= f(x)
count_1 = np.sum(under_curve_1)

#between pi and 3*pi/2
under_curve_2 = abs(y1) <= abs(f(x1))
count_2 = np.sum(under_curve_2)

# integral estimate
int_estimate_1 = (abs((f(b/2)*(b-a)))* count_1) / n_1
int_estimate_2 = (abs((f(c)*(c-b)))* count_2) / n_2
int_estimate = int_estimate_1 - int_estimate_2
print(" in postive region   ",int_estimate_1)
print(" in negative region ",int_estimate_2)
exact = f1(c) - f1(a)
error = abs(int_estimate - exact)

# Plotting
z = np.linspace(a, c, 10000)
fig, ax = plt.subplots()
ax.plot(z, f(z), color='green', label='$f(x) = sin(x)$')
ax.scatter(x, y, color='blue')  
ax.scatter(x1, y1, color='red')
ax.set_xlim([a, c])
ax.set_ylim([f(c), f(b/2)])
ax.set_aspect('equal', adjustable='box')
ax.legend()

# Set title
title_text = 'Integration Value Estimate: {:.2f}\nExact value : {}\nError: {}'.format(int_estimate,exact, error)
ax.set_title(title_text)

plt.show()



