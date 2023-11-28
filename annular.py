import numpy as np
import matplotlib.pyplot as plt

np.random.seed(None)  # different seed in each run

r1 = 9
r2 = 10

n = 1000000

exact_area = np.pi * (r2 ** 2 - r1 ** 2)
square_area = 4 * r2 ** 2

x = np.random.uniform(-r2, r2, n)
y = np.random.uniform(-r2, r2, n)

i = 0

fig, ax = plt.subplots()

inside = (x**2 + y**2 <= r2**2) & (x**2 + y**2 >= r1**2)  
count = np.sum(inside)

ax.scatter(x, y, color='blue')
circle1 = plt.Circle((0, 0), r1, color='red', fill=False)
circle2 = plt.Circle((0, 0), r2, color='green', fill=False)
ax.add_patch(circle1)
ax.add_patch(circle2)
ax.set_xlim([-r2, r2])
ax.set_ylim([-r2, r2])
ax.set_aspect('equal', adjustable='box')

area_estimate = (square_area * count) / n

title_text = 'Area Estimate: {:.2f}\nError: {:.4f}'.format(area_estimate, abs(area_estimate - exact_area))
ax.set_title(title_text)
plt.show()
